from flask import Flask, render_template, request, jsonify
import os
from markov import markov

import cleanup
from tokenize_word import tokens
import word_count
import sample
import sentence


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    """Desc: Home page for tweet bot"""
    """Displays random sentence based on weighed sample"""
    histogram = word_count.hist_dictionary('words.txt')
    sent = sentence.sentence(histogram, 5)
    return render_template('index.html')

@app.route("/data")
def data():
  histogram = word_count.hist_dictionary('words.txt')
  sent = sentence.sentence(histogram, 5)
  # define some data
  s = {
    'sentence' : sent
  }
  return jsonify(s)  

@app.route('/markov')
def markov_sentence():
  """ Displays a markov chain sentence based on weighed sample for each word """
  words = tokens('alice.txt')
  # print(words)
  sentence = markov(words)
  return render_template('markov.html', sentence = sentence)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
  