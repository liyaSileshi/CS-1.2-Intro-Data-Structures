from flask import Flask
from dictionary_words import rand_dict
from histogram import list_of_words
import os
app = Flask(__name__)

@app.route('/')
def index():
    # dict_words = rand_dict(6)
    #print(' '.join(dict_words)+'.')
    # return rand_dict(5);
    # return (' '.join(dict_words)+'.')
    return (' '.join(list_of_words())+'.')
    


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))