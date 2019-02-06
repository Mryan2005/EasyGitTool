def fix_bugs():
    reason = input()
    command = "git commit -m 'fix bugs: "
    sh = open(r"src\commit\commit.sh", "w+")
    sh.write(command)
    sh.write(reason)
    sh.write("'")
    sh.close()
