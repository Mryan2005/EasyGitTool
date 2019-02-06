def fix_bugs():
    reason = input()
    command = "git commit -m 'fix bugs: "
    sh = open(r"src\push\push.sh", "w+")
    sh.write(command)
    sh.write(reason)
    sh.write("'")
    sh.close()
