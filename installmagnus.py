import os
import platform

#initalize system variable
system = platform.system()

#Create shortcut for os.system()
def cmd(arg):
    os.system(str(arg))

print('Magnus is installed in the Documents folder under Magnus')
if system == 'Linux' or system == 'Darwin':
    cmd('cd ~/Documents && mkdir Magnus && cd Magnus &&')
    

