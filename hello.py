import random
import os
from flask import Flask

app = Flask(__name__)

FANNY_FACTS = [
	'Did you know? The average Fanny survives off a diet of pistachios and milk tea.',
	'Fanny is either on her period, or not on her period. There is a 50% chance Fanny is on her period.',
	'The average Fanny hates you.',
	'Fanny has 3-starred every puzzle in Hungry Cat Picross! Me-wow!',
	'It is estimated that Fanny can make over 60 different dubstep sounds.',
	'The average Fanny can sleep for over 8 hours a day, split between her bed, her car, and random couches.',
	'The average Fanny is estimated to have over 500 unique dance moves... and counting!',
	'',
]

@app.route('/')
def hello():
    return random.choice(FANNY_FACTS)
