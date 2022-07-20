#!/usr/bin/python
import os
import sys
import time
from sys import argv


def getnoncommand():
    non_commands = []
    times = 0
    for i in argv:
        if times > 1:
            non_commands.append(i)
        times = times + 1
    return non_commands


def add():
    if len(getnoncommand()) == 0:
        print('已缓存所有文件')
        os.popen('cd "' + os.getcwd() + '" && git add .')
    else:
        print('已缓存以下文件')
        for i in getnoncommand():
            print(i)
            os.popen('cd "' + os.getcwd() + '" && git add ' + i)


def commit(command):
    os.popen('cd "' + os.getcwd() + '" && git commit -am "' + str(command) + '"')


def push(additional_item):
    os.popen('git config --global http.sslVerify "false"')
    os.popen('cd "' + os.getcwd() + '" && git push ' + additional_item)


def tag(version_):
    os.popen('cd "' + os.getcwd() + '" && git tag ' + version_)


def main():
    if argv[1] == 'commit':
        commit_ = []
        commit_text = ''
        type_ = input(
            ' feat：新功能（feature） \n fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG \n fix：产生diff并自动修复此问题。适合于一次提交直接修复问题 \n '
            'to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix \n docs：文档（documentation） \n style：格式（不影响代码运行的变动） \n '
            'refactor：重构（即不是新增功能，也不是修改bug的代码变动） \n perf：优化相关，比如提升性能、体验 \n test：增加测试 \n chore：构建过程或辅助工具的变动 \n '
            'revert：回滚到上一个版本 \n merge：代码合并 \n sync：同步主线或分支的Bug \ntype: ')
        if type_ == '':
            print('error: 未输入git commit的类别')
            sys.exit()
        commit_.append(type_)
        scope = input('scope: ')
        if scope != '':
            commit_.append('(' + scope + ')')
        elif scope == '':
            commit_.append(': ')
        commit_.append(': ')
        subject_ = input('subject: ')
        if subject_ == '':
            print('error: 未输入git commit目的的简短描述')
            sys.exit()
        commit_.append(subject_)
        task = input('task: ')
        if task != '':
            commit_.append(' '+task)
        for i in commit_:
            commit_text = str(commit_text) + str(i)
        commit(commit_text)
    if argv[1] == 'acp':
        commit_ = []
        commit_text = ''
        type_ = input(
            ' feat：新功能（feature） \n fix/to：修复bug，可以是QA发现的BUG，也可以是研发自己发现的BUG \n fix：产生diff并自动修复此问题。适合于一次提交直接修复问题 \n '
            'to：只产生diff不自动修复此问题。适合于多次提交。最终修复问题提交时使用fix \n docs：文档（documentation） \n style：格式（不影响代码运行的变动） \n '
            'refactor：重构（即不是新增功能，也不是修改bug的代码变动） \n perf：优化相关，比如提升性能、体验 \n test：增加测试 \n chore：构建过程或辅助工具的变动 \n '
            'revert：回滚到上一个版本 \n merge：代码合并 \n sync：同步主线或分支的Bug \n type: ')
        if type_ == '':
            print('error: 未输入git commit的类别')
            sys.exit()
        commit_.append(type_)
        scope = input('scope: ')
        if scope != '':
            commit_.append('(' + scope + '): ')
        if scope == '':
            commit_.append(': ')
        subject_ = input('subject: ')
        if subject_ == '':
            print('error: 未输入git commit目的的简短描述')
            sys.exit()
        commit_.append(subject_)
        for i in commit_:
            commit_text = str(commit_text) + str(i)
        commit(commit_text)
        for i in commit_:
            commit_text = str(commit_text) + str(i)
        add()
        time.sleep(0.3)
        commit(commit_text)
        time.sleep(0.3)
        push('')
    if argv[1] == 'push':
        if argv[2] == 'branch':
            push('--set-upstream origin ' + argv[3])
        else:
            push('')
    if argv[1] == 'test':
        add()
        time.sleep(0.5)
        commit('test')
        time.sleep(0.5)
        print('good')
    if argv[1] == 'tag':
        tag(input('version: '))
        time.sleep(0.5)
        push('--tags')
    if argv[1] == 'add':
        add()
'''
#    if argv[1] == '':
#        if argv[2] == 'cr':
            print('Real name填GitHub Username \n'
                  'Email address填GitHub email address private')
            print('当你完成gpg key创建之后，请输入"gt gpg deploy"')
            os.popen('gpg --gen-key')
            os.popen('gpg --list-keys --keyid-format SHORT')
        if argv[2] == 'd':
            key = input("请输入pub  rsa2048/D609DBC4 中的pub  rsaxxx/后的内容")
            os.popen('gpg --send-key ' + key)
            os.popen('gpg --armor --export ' + key)
            print('请你将其添加到代码GitHub的gpg key中就可以了')
            os.popen('start https://github.com/settings/keys')
            print('正在配置你的Git')
            os.popen('git config --global user.signingkey ' + key)
            os.popen('git config commit.gpgsign true')
            os.popen('git config --global commit.gpgsign true')
'''