#www.atozknowledge.com

import ...

bot= chatbot('test')
conv = open('home.py', 'r').readlines()

bot.set_trainer (ListTrainer)
bot.train(conv)

while True:
         request = input('you: ')
         response = bot.get_response(request)
         print('Bot: ',response)
