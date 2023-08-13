import random
import os

import pygame.mixer  
import requests

from flask import Flask,request,render_template_string
from gtts import gTTS
import time
import tempfile

app = Flask(__name__)


sentences = [
    "Every time {} writes a line of code, he earns his title of 'bug-yoo-nehr'.",
    "{}, our resident bug-yoo-nehr, struck again with a new unexpected feature.",
    "They say Rome wasn't built in a day, and neither was {}'s reputation as a bug-yoo-nehr.",
    "If bugs were currency, {} the bug-yoo-nehr would be a millionaire.",
    "Some people search for bugs; {} just naturally creates them as a bug-yoo-nehr.",
    "When things go awry in the code, the first question is always: 'Did {} the bug-yoo-nehr have a hand in this?",
    "Bugs are just {}'s way of adding a personal touch to every project, earning him the title of bug-yoo-nehr.",
    "They say practice makes perfect, but in {}'s case, practice makes him a better bug-yoo-nehr.",
    "If there were a Bug-yoo-nehr Hall of Fame, {} would be its first inductee."
]


@app.route("/", methods=['GET', 'POST'])
def hello():
    template = random.choice(sentences)
    user = os.env.get("BUG_GURU")
    if user:
        user = request.get_json().get('sender', {}).get('login')
    sentence = template.format(user)
    with tempfile.TemporaryDirectory() as temp_dir:
        tts = gTTS(text=sentence, lang='en')
        tts.save(f"{temp_dir}/sentence.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(f"{temp_dir}/sentence.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # wait for the music to finish playing
            pygame.time.Clock().tick(10)
   
    return sentence

if __name__ == '__main__':
    app.run(debug=True)
