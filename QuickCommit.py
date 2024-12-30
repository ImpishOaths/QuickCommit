import subprocess
from easygui import *
msg = enterbox("Commit Message")
subprocess.call(["git","add","."])
subprocess.call(["git","commit","-m",msg])
subprocess.call(["git","push"])
msgbox("done!")
