import os
import subprocess
def settings():
    if os.path.exists(r'src\settings\setting.py'):
        pass
    else:
        setting = open(r'src\settings\setting.py', "w+")
        setting.write("language = 'zh-hans'\n")
        setting.write("path = ''\n")
        #setting.write
        settings = subprocess.Popen(r'src\settings\setting.py',shell=True)
        settings.wait()
        setting.close()