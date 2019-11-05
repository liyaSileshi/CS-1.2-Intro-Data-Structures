from flask import Flask, render_template
from histogram import list_of_words, hist_dictionary
from random_hist import sample_by_frequency
import os

import cleanup
import tokenize
import word_count
import sample
import sentence


app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    """Desc: Home page for tweet bot"""
    words_list = list_of_words()
    histogram  = hist_dictionary(words_list)
    return render_template('index.html', rand_word = sample_by_frequency(histogram))


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))