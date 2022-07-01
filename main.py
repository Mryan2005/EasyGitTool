from cgi import test
import os
import subprocess
from sys import argv
import sys
import time
def add():
    os.popen('cd "'+ os.getcwd() + '" && git add .')
def commit(command):
    os.popen('cd "'+ os.getcwd() + '" && git commit -am "' + str(command) + '"')
def push():
    os.popen('cd "'+ os.getcwd() + '" && git push')
if argv[1] == 'commit':
    commit_ = []
    commit_text = ''
    type_ = input(' feat：新功能（feature） \n fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG \n fix：产生diff并自动修复此问题。适合于一次提交直接修复问题 \n to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix \n docs：文档（documentation） \n style：格式（不影响代码运行的变动） \n refactor：重构（即不是新增功能，也不是修改bug的代码变动） \n perf：优化相关，比如提升性能、体验 \n test：增加测试 \n chore：构建过程或辅助工具的变动 \n revert：回滚到上一个版本 \n merge：代码合并 \n sync：同步主线或分支的Bug \n type: ')
    if type_ == '':
        print('error: 未输入git commit的类别')
        sys.exit()
    commit_.append(type_)
    scope = input('scope: ')
    if scope != '':
        commit.append(scope)
    subject_ = input('subject: ')
    if subject_ == '':
        print('error: 未输入git commit目的的简短描述')
        sys.exit()
    commit_.append(subject_)
    for i in commit_:
        commit_text = str(commit_text) + str(i)
        commit_text = str(commit_text) + ' '
    commit(commit_text)
if argv[1] == 'acp':
    commit_ = []
    commit_text = ''
    type_ = input(' feat：新功能（feature） \n fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG \n fix：产生diff并自动修复此问题。适合于一次提交直接修复问题 \n to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix \n docs：文档（documentation） \n style：格式（不影响代码运行的变动） \n refactor：重构（即不是新增功能，也不是修改bug的代码变动） \n perf：优化相关，比如提升性能、体验 \n test：增加测试 \n chore：构建过程或辅助工具的变动 \n revert：回滚到上一个版本 \n merge：代码合并 \n sync：同步主线或分支的Bug \n type: ')
    if type_ == '':
        print('error: 未输入git commit的类别')
        sys.exit()
    commit_.append(type_)
    scope = input('scope: ')
    if scope != '':
       commit_.append('('+scope+')')
    subject_ = input('subject: ')
    if subject_ == '':
        print('error: 未输入git commit目的的简短描述')
        sys.exit()
    commit_.append(subject_)
    for i in commit_:
        commit_text = str(commit_text) + str(i)
        commit_text = str(commit_text) + ' '
    add()
    time.sleep(0.5)
    commit(commit_text)
    time.sleep(0.5)
    push()
if argv[1] == 'push':
    push()
if argv[1] == 'test':
    add()
    time.sleep(0.5)
    commit('test')
    time.sleep(0.5)