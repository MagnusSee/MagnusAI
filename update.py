import os
import platform

#initalize system variable
system = platform.system()

#Create shortcut for os.system()
def cmd(arg):
    os.system(str(arg))

#Clear console screen
if system == 'Linux' or system == 'Darwin':
    cmd('clear')
else:
    cmd('cls')

#git must be installed for this to work
print('Updater only works if Magnus is installed in the Desktop folder under the folder Magnus\n')
input('This updater requires git\tPress Enter if you wish to continue and you have git')
if system == 'Linux' or system == 'Darwin':
    cmd('cd ~/Desktop && mkdir -p Magnus && cd Magnus && rm -rf MagnusAI && git clone https://github.com/MagnusSee/MagnusAI.git')
    
if system == 'Windows':
    user = os.getlogin()

    cmd('cd C:\\Users\\'+ user +'\\Desktop && if exist Magnus rmdir Magnus /Q /S')
    cmd('cd C:\\Users\\'+ user +'\\Desktop && mkdir Magnus')
    cmd('cd C:\\Users\\'+ user +'\\Desktop\\Magnus && git clone https://github.com/MagnusSee/MagnusAI.git')
