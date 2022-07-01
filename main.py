import os
import subprocess
def order(command):
    subprocess.run(command,shell=True,stdout=None,stderr=None,encoding="utf-8",cwd=os.getcwd())
