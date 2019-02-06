import subprocess
import os

from src.commit import commit
from src.settings import setting
# ============================================ #
language = setting.language
if language == 'zh-cn':
    from src.language import zhcn
# ============================================ #
try:
    Caching_changes = zhcn.Caching_changes
    Caching_changes_finish = zhcn.Caching_changes_finish
    Please_select_the_type_of_changes_to_be_submitted = zhcn.Please_select_the_type_of_changes_to_be_submitted
    Please_enter_the_reasons_for_submission = zhcn.Please_enter_the_reasons_for_submission
except ImportError:
    pass
# ============================================ #
while True:
    print(Caching_changes)
    add = subprocess.Popen(r'src\add\add.sh',shell=True)
    add.wait()
    print(Caching_changes_finish)
    print(Please_select_the_type_of_changes_to_be_submitted)
    print('1.fix bugs')
    choose = input()
    if choose == '1':
        print(Please_enter_the_reasons_for_submission)
        commit.fix_bugs()
    commits = subprocess.Popen(r'src\commit\commit.sh',shell=True)
    commits.wait()
    push = subprocess.Popen(r'src\push\push.sh',shell=True)
    push.wait()
