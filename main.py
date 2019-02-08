import subprocess
import os
import time
from src.commit import commit
from src.settings import setting
def main():
    print(Please_select_the_type_of_changes_to_be_submitted)
    print('1.fix bugs')
    print('2.update')
    print('3.exit')
    choose = input()
    if choose == '1':
        print(Please_enter_the_reasons_for_submission)
        commit.fix_bugs()
        update()
    elif choose == '2':
        print(Please_enter_the_reasons_for_submission)
        commit.update()
        update()
    elif choose == '3':
        print(Please_enter_the_reasons_for_submission)
        commit.delete()
        update()
    elif choose == '4':
        os._exit(0)
    else:
        main()
# ============================================ #
def update():
    print(in_commit)
    commits = subprocess.Popen(r'src\commit\commit.sh',shell=True)
    commits.wait()
    print(commit_finish)
    time.sleep(1)
    print(in_push)
    push = subprocess.Popen(r'src\push\push.sh',shell=True)
    push.wait()
    print(push_finish)
    os.remove(r'src\commit\commit.sh')
    time.sleep(3)
    main()
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
    commit_finish = zhcn.commit_finish
    in_commit = zhcn.in_commit
    in_push = zhcn.in_push
    push_finish = zhcn.push_finish
except ImportError:
    pass
# ============================================ #
print(Caching_changes)
add = subprocess.Popen(r'src\add\add.sh',shell=True)
add.wait()
print(Caching_changes_finish)
main()