import os
import platform

#initalize system variable
system = platform.system()

#Create shortcut for os.system()
def cmd(arg):
    os.system(str(arg))

#git must be installed for this to work
print('Magnus is installed in the Documents folder under Magnus')
if system == 'Linux' or system == 'Darwin':
    cmd('cd ~/Documents && mkdir Magnus && cd Magnus && git clone https://github.com/MagnusSee/MagnusAI.git')
    
if system == 'Windows':
    cmd('cd C:\Users\%UserProfile%\Documents && mkdir Magnus && cd Magnus && git clone https://github.com/MagnusSee/MagnusAI.git')
