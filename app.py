from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

ChattyBot = ChatBot("Chatterbot", storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(ChattyBot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(ChattyBot.get_response(userText))


if __name__ == '__main__':
    app.run()

