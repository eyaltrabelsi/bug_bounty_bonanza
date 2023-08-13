import random

import pygame.mixer  
import requests

from flask import Flask,request
from gtts import gTTS

app = Flask(__name__)


sentences = [
    "Every time Shlomi writes a line of code, he earns his title of 'bug-yoo-nehr'.",
    "Shlomi, our resident bug-yoo-nehr, struck again with a new unexpected feature.",
    "They say Rome wasn't built in a day, and neither was Shlomi's reputation as a bug-yoo-nehr.",
    "If bugs were currency, Shlomi the bug-yoo-nehr would be a millionaire.",
    "Some people search for bugs; Shlomi just naturally creates them as a bug-yoo-nehr.",
    "When things go awry in the code, the first question is always: 'Did Shlomi the bug-yoo-nehr have a hand in this?'",
    "Bugs are just Shlomi's way of adding a personal touch to every project, earning him the title of bug-yoo-nehr.",
    "They say practice makes perfect, but in Shlomi's case, practice makes him a better bug-yoo-nehr.",
    "If there were a Bug-yoo-nehr Hall of Fame, Shlomi would be its first inductee."
]


@app.route("/", methods=['GET', 'POST'])
def hello():
    sentence = random.choice(sentences)
    tts = gTTS(text=sentence, lang='en')
    tts.save("temp_robotic_voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('temp_robotic_voice.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # wait for the music to finish playing
        pygame.time.Clock().tick(10)

    return sentence

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
