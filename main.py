import subprocess
import os
import time
from src.commit import commit
from src.version import version
from src.settings import setting
from src.InspectionCenter import InspectionCenter
def menu():
    print(hi_I_am_noder)
    time.sleep(0.5)
    print(Can_I_help_you)
    time.sleep(0.5)
    print(please_tell_me_How_to_do_it)
    print('1.push the codes to Web')
    print('2.update')
    print('3.version')
    print('4.exit')
    choose_2 = input()
    if choose_2 == '1':
        print(Caching_changes)
        add = subprocess.Popen(r'src\add\add.sh',shell=True)
        add.wait()
        print(Caching_changes_finish)
        update_loding()
    elif choose_2 == '2':
        print('')
    elif choose_2 == '3':
        print('EasyGitTool-cil:',EasyGitTool_cil)
        
        time.sleep(1)
        menu()
    elif choose_2 == '4':
        while True:
            print(Are_you_sure,'|yes or no|')
            choose = input()
            if choose == 'yes':
                print('good bye')
                time.sleep(1)
                os._exit(0)
            elif choose == 'no':
                menu()
            elif choose == 'YES':
                print('good bye')
                time.sleep(1)
                os._exit(0)
            elif choose == 'NO':
                menu()
            else:
                print(paramete_error)
                pass
                time.sleep(1)
    else:
        menu()
def update_loding():
    print(Please_select_the_type_of_changes_to_be_submitted)
    print('1.fix bugs')
    print('2.update')
    print('3.delete')
    print('4.go back')
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
        while True:
            print(Are_you_sure,'|yes or no|')
            choose = input()
            if choose == 'yes':
                menu()
            elif choose == 'no':
                update_loding()
            elif choose == 'YES':
                menu()
            elif choose == 'NO':
                update_loding()
            else:
                print(paramete_error)
                pass
                time.sleep(1)
    else:
        update_loding()
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
    update_loding()
# ============================================ #
EasyGitTool_cil = version.EasyGitTool_cil
language = setting.language
if language == 'zh-hans':
    from src.language import zh_hans
# ============================================ #
try:
    Caching_changes = zh_hans.Caching_changes
    Caching_changes_finish = zh_hans.Caching_changes_finish
    Please_select_the_type_of_changes_to_be_submitted = zh_hans.Please_select_the_type_of_changes_to_be_submitted
    Please_enter_the_reasons_for_submission = zh_hans.Please_enter_the_reasons_for_submission
    commit_finish = zh_hans.commit_finish
    in_commit = zh_hans.in_commit
    in_push = zh_hans.in_push
    push_finish = zh_hans.push_finish
    hi_I_am_noder = zh_hans.hi_I_am_noder
    Can_I_help_you = zh_hans.Can_I_help_you
    please_tell_me_How_to_do_it = zh_hans.please_tell_me_How_to_do_it
    Are_you_sure = zh_hans.Are_you_sure
    paramete_error = zh_hans.paramete_error
except ImportError:
    pass
# ============================================ #
menu()