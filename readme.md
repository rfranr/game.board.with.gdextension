basic tuto
https://docs.godotengine.org/en/4.4/tutorials/scripting/gdextension/gdextension_cpp_example.html#doc-gdextension-cpp-example

compile for the web
https://docs.godotengine.org/en/4.4/contributing/development/compiling/compiling_for_web.html

remember to have emcc

# build extension
scons platform=linux







# view how to optimze for the web
scons help=1
# build for the web
cd godot-cpp
scons platform=web target=template_release -j8 use_exceptions=no use_rtti=no debug_symbols=no lto=yes optimize=size



# view: https://docs.godotengine.org/en/4.4/contributing/development/compiling/compiling_for_web.html
# scons target=template_release build_profile=/path/to/profile.gdbuild
scons platform=web target=template_release  optimize=size lto=full
scons platform=web target=template_release -j8 debug_symbols=no lto=full optimize=size


# copy the compiled extension to the demo folder


# add the godot engine to the path
# https://www.youtube.com/watch?v=TgLxdEA6f04
# https://popcar.bearblog.dev/how-to-minify-godots-build-size/
# https://godot-build-options-generator.github.io/
git submodule add https://github.com/godotengine/godot.git godot-engine-source
git submodule update --init --recursive

copy custom.py
emsdk activate latest
source ~/emsdk/emsdk_env.sh
then 
cd godot-engine-source
scons platform=web target=release_debug tools=no module_gdextension_enabled=yes custom_modules
scons platform=web target=template_release -j8 




# consolidate
# Compile Custom Extension
cd godot-cpp
scons platform=web target=template_release -j8




# consolidate 
- Compile Engine with Custom Options
cd godot-engine-source
# Copy your custom.py configuration file into the godot-engine-source directory
cp ../custom.py .
# Build the Godot engine for Web with your custom options
scons platform=web target=template_release -j8
scons platform=web target=template_debug -j8























# # Generated using https://godot-build-options-generator.github.io
production = "yes"
disable_3d = "yes"
optimize = "size"
disable_advanced_gui = "yes"
deprecated = "no"
minizip = "no"
module_bmp_enabled = "no"
module_camera_enabled = "no"
module_csg_enabled = "no"
module_dds_enabled = "no"
module_gltf_enabled = "no"
module_hdr_enabled = "no"
module_ktx_enabled = "no"
module_meshoptimizer_enabled = "no"
module_mobile_vr_enabled = "no"
module_noise_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_text_server_adv_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_threads_enabled=no