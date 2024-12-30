import subprocess
from datetime import datetime
from easygui import *
date = datetime.today().strftime('%Y-%m-%d')
msg = enterbox("Commit Message")
if(msg != ""):
    msg += "\n"
msg += date
subprocess.call(["git","add","."])
subprocess.call(["git","commit","-m",msg])
subprocess.call(["git","push"])
msgbox("Done!")
