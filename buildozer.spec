[app]

# (str) Title of your application
title = Pattern 8: So That's Why

# (str) Package name
package.name = pattern8whythatswhy

# (str) Package domain (needed for android/ios packaging)
package.domain = org.spokenppt

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.3.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #1A1A2E

# (string) Presplash animation using Lottie format
# see https://github.com/airbnb/lottie-android
#android.presplash_lottie = %(source.dir)s/assets/presplash.json

# (str) Adaptive icon of the application (used if Android API level is 26+)
#icon.adaptive_foreground.filename = %(source.dir)s/assets/icon_foreground.png
#icon.adaptive_background.filename = %(source.dir)s/assets/icon_background.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# Use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = %(source.dir)s/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
#android.extra_application_xml = %(source.dir)s/extra_application.xml

# (str) Full name including package path of the Java class that implements Android Service
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, e.g. OUYA-ODK/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the Android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets needs to be a list. It is used by
# python-for-android to copy the files in the assets directory of the apk.
#android.assets =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Kotlin version to use for building (if using Kotlin)
#android.kotlin_version = 1.9.0

# (list) add-apt-repositories needed to add packages for buildozer
# ppa_id format: ppa:user/ppa-name
#android.add_apt_repos =

# (list) List of packages to install via apt
#android.add_apt_packages =

# (str) python-for-android branch to use, if not master
#p4a.branch = master

# (str) OUYA Console category. Should be one of the following: game, app, or other
# If not specified, defaults to 'game'
#android.ouya.category = game

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/assets/ouya_icon.png

# (str) XML to include in AndroidManifest.xml for intent-filter for OUYA
#android.ouya.intent_xml =

# (str) Splash screen filename (deprecated, use presplash.filename)
#android.splash =

# (str) Copy these files to src/main/res/xml/ (used for example with backup rules)
#android.res_xml =

# (bool) Enable proguard (deprecated, use android.gradle_dependencies instead)
#android.proguard = False

# (str) Path to a custom proguard file
#android.proguard_file =

# (str) String xml resource for network security config
#android.network_security_config =

# (list) List of Gradle repositories to add (for mavenCentral() use "mavenCentral")
#android.gradle_repositories =

# (str) Path to a custom gradle.properties file
#android.gradle_properties =

# (str) Path to a custom settings.gradle file
#android.settings_gradle =

# (str) Path to a custom build.gradle file
#android.build_gradle =

# (str) Path to a custom proguard-rules.pro file
#android.proguard_rules =

# (str) Path to a custom gradle wrapper properties file
#android.gradle_wrapper_properties =

# (list) List of additional aapt2 flags
#android.aapt2_flags =

# (list) List of additional adb flags
#android.adb_flags =

# (bool) Enable AAB format instead of APK
android.build_aab = False

# (str) Keystore file for signing (release builds only)
#android.keystore =

# (str) Keystore password (release builds only)
#android.keystore_password =

# (str) Key alias (release builds only)
#android.key_alias =

# (str) Key password (release builds only)
#android.key_password =

#
# iOS specific
#

# (str) Path to a custom xcodebuild file
#ios.xcodebuild =

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = "iPhone Distribution: <lastname> <firstname> (<hexstring>)"

# (str) Path to a custom provisioning profile for debug build
#ios.provisioning.debug =

# (str) Path to a custom provisioning profile for release build
#ios.provisioning.release =

# (str) Path to a custom entitlements file
#ios.entitlements =

# (bool) Enable Bitcode
#ios.enable_bitcode = False

#
# Buildozer specific
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug