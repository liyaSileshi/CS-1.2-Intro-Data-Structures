from flask import Flask
from dictionary_words import rand_dict
app = Flask(__name__)

@app.route('/')
def index():
    dict_words = rand_dict(6)
    #print(' '.join(dict_words)+'.')
    # return rand_dict(5);
    return (' '.join(dict_words)+'.')