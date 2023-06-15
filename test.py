import os
import platform 
print(os.name)
print(os.getcwd())
print(os.listdir(path=os.getcwd()))

print("=========================") 
print(platform.system())
print(platform.node())
print(platform.platform())
print(platform.processor())
print(platform.python_version())
print(platform.version())
print(platform.uname())


for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
