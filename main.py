import subprocess
import platform
import os
from src.push import push
print(Caching_changes)
add = subprocess.Popen(r'src\add\add.sh',shell=True)
add.wait()
print(Caching_changes_finish)
if platform.system() == 'Windows':
    choose = input()
    if choose == '1':
        push.fix_bugs()
        push = subprocess.Popen(r'src\push\push.sh',shell=True)
        push.wait()