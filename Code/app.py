from flask import Flask, render_template
from histogram import list_of_words, hist_dictionary
from random_hist import sample_by_frequency
import os
from markov import markov

import cleanup
import tokenize_word
import word_count
import sample
import sentence


app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    """Desc: Home page for tweet bot"""
    """Displays random sentence based on weighed sample"""
    # words_list = list_of_words('words.txt')
    # words_list = tokenize_word.tokens('words.txt')
    # histogram  = hist_dictionary(words_list)
    histogram = word_count.hist_dictionary('words.txt')
    return render_template('index.html', sentence = sentence.sentence(histogram, 5))
    # sample_by_frequency(histogram))

@app.route('/markov')
def markov_sentence():
  """ Displays a markov chain sentence based on weighed sample for each word """
  sentence = markov()
  return render_template('markov.html', sentence = sentence)
  # return "hello world"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))