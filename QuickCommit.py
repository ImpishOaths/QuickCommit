import subprocess
from datetime import datetime
from easygui import *
msg = enterbox("Commit message:")
if(msg == ""):
    date = datetime.today().strftime('%Y-%m-%d')
    msg = enterbox("Explain no commit:")
    with open("noCommit.log", "a") as noCommit:
        noCommit.write(msg)
        noCommit.write(" - " + date + "\n")
subprocess.call(["git","add","."])
subprocess.call(["git","commit","-m",msg])
subprocess.call(["git","push"])
msgbox("Commit complete!\n"+msg)
