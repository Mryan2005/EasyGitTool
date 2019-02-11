import os
def settings():
    if os.path.exists(r'src\settings\setting.py'):
        pass
    else:
        setting = open(r'src\settings\setting.py', "w+")
        setting.write("language = 'zh-hans'\n")
        #setting.write()
        setting.close()