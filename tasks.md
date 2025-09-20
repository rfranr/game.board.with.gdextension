# WebAssembly Threads and Monetization Workaround

Siri, the workaround used by platforms like CrazyGames to enable monetization (ads) while your Godot game runs with high-performance WebAssembly threads is to use two different domains/iframes.

Since COOP/COEP isolation restricts communication between your game and non-isolated external ad content, the solution is to run the external content outside the isolated game.

The Cross-Origin Workaround
1. The Isolated Game Container (High Performance)
The core game is served from a domain (or subdomain) that does include the COOP/COEP headers.

This creates a Cross-Origin Isolated environment, which allows the browser to safely enable features like WebAssembly Threads (SharedArrayBuffer).

Your Godot game runs smoothly, but it cannot directly load external ads in an iframe.

2. The Non-Isolated Ad Container (Monetization)
The monetization/ad logic is loaded from a separate, non-isolated domain or origin into an iframe or element that is outside the isolated game's iframe.

This container does not use COOP/COEP headers, so it can freely communicate with external ad networks.

The Ad Container then uses post-message communication to talk to the Isolated Game Container.

3. Communication Bridge
The platform's SDK creates a communication bridge between these two containers.

When your game calls CrazyGames.show_ad(), the message is sent across the bridge to the Non-Isolated Ad Container.

The Ad Container loads the ad, and once it's finished, it sends a message back to the Isolated Game Container (the game) to resume play.

This architecture satisfies both the browser's security demands (allowing threading) and the monetization provider's requirements (allowing external ad loading).