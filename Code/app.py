from flask import Flask, render_template
import os
from markov import markov

import cleanup
import tokenize_word
import word_count
import sample
import sentence


app = Flask(__name__)


@app.route('/')
def index():
    """Desc: Home page for tweet bot"""
    """Displays random sentence based on weighed sample"""
    histogram = word_count.hist_dictionary('words.txt')
    return render_template('index.html', sentence = sentence.sentence(histogram, 5))
    

@app.route('/markov')
def markov_sentence():
  """ Displays a markov chain sentence based on weighed sample for each word """
  sentence = markov()
  return render_template('markov.html', sentence = sentence)
  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
  