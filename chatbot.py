from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
bot = ChatBot(
    'Yalu',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'],
    database_uri='sqlite:///database.db'
)

print('hello')
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
story = [
    "Can you tell me a story",
    "Sure! I am going to read you a story",
    "Can you tell me a bedtime story",
    "Get ready! i am going to read you a bedtime story"
]
trainer = ListTrainer(bot)
trainer.train(story)

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")
print("hello hello")
while True:
    request = input('user :')
    if request == 'bye':
        print("Bot: bye!ave a good day!")
        break
    else:
        response = bot.get_response(request)
        print("Bot: ", response)
