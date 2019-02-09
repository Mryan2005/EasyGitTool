import os
def settings():
    if os.path.exists(r'src\settings\setting.py'):
        print('setting.py存在')
    else:
        setting = open(r'src\settings\setting.py', "w+")
        setting.write("language = 'zh-cn'")
        setting.close()