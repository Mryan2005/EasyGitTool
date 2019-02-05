import subprocess
import platform
import os
if platform.system() == 'Windows':
    choose = input()
    if choose == '1':
        update_type = 'fix bugs: '
        reason = input('reason: ')
        