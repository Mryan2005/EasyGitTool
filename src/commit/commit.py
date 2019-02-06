def fix_bugs():
    reason = input()
    if reason == '':
        command = "git commit -m 'fix bugs"
    else:
        command = "git commit -m 'fix bugs: "
    sh = open(r"src\commit\commit.sh", "w+")
    sh.write(command)
    sh.write(reason)
    sh.write("'")
    sh.close()
def update():
    reason = input()
    if reason == '':
        command = "git commit -m 'update"
    else:
        command = "git commit -m 'update: "
    sh = open(r"src\commit\commit.sh", "w+")
    sh.write(command)
    sh.write(reason)
    sh.write("'")
    sh.close()

if __name__ == "__main__":
    fix_bugs()