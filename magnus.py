#Made by MagnusSEE
import os
from neuralintents import GenericAssistant

magnus = GenericAssistant('intents.json')
magnus.train_model()
magnus.save_model()

print("Magnus Alpha")
while True:
    msg = input('>>>')
    print('\n')
    responseMsg = magnus.request(msg)
    print('Response:',responseMsg)