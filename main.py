import subprocess
import platform
import os
from src.language import zhcn
from src.commit import commit
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
        commit.fix_bugs()
        push = subprocess.Popen(r'src\commit\commit.sh',shell=True)
        push.wait()
