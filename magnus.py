#Made by MagnusSEE
import os
from neuralintents import GenericAssistant
import platform

#Create system variable which has the name of the OS
system = platform.system()

#Initalize the AI
magnus = GenericAssistant('intents.json')
magnus.train_model()
magnus.save_model()

#Darwin is MacOS
if system == 'Windows':
    os.system('cls')
elif system == 'Darwin' or system == 'Linux':
    os.system('clear')

print("Magnus Alpha")

#Command listening loop
while True:
    msg = input(' >>>')
    print('\n')
    responseMsg = magnus.request(msg)
    print('Response:',responseMsg)