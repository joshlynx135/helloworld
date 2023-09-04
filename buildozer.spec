[app]

# (str) Title of your application
title = HelloWorld

# (str) Package name
package.name = helloworld

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source code entry point (relative to source.dir)
source.include_exts = py,png,jpg,kv,atlas

[buildozer]

# (str) Path to the main.py file
main.filename = main.py

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = kivy

# (str) Custom source folders for requirements
source.custom_data = %(source.dir)s/data/*.png:data

# (list) Garden requirements (Kivy addons)
#garden_requirements = 

# (list) List of all the modules to package with the application
#p4a.source_dir = /home/kivy/Desktop/helloworld/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/hostpython3/desktop/src
#p4a.source_dir = %(source.dir)s
#(list) List of all the modules to package with the application
p4a.modules_dir = %(source.dir)s/modules
