reason = input()
command = 'git commit -m fix bugs: '
sh = open("push.sh", "w+")
sh.write(command)
sh.write(reason)
sh.close()