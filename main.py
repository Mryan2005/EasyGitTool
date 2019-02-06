import subprocess
import platform
import os
from src.language import zhcn
from src.push import push
# ============================================ #
Caching_changes = zhcn.Caching_changes
Caching_changes_finish = zhcn.Caching_changes_finish
# ============================================ #
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