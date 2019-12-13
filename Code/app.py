from flask import Flask, render_template, request, jsonify
import os
# from markov import markov
from markov_higher import Markov
from pymongo import MongoClient
import cleanup
from tokenize_word import tokens
import word_count
import sample
import sentence

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet')
client = MongoClient(host=host)
db = client.Tweet
favorites = db.favorites
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    """Desc: Home page for tweet bot"""
    """Displays random sentence based on weighed sample"""
    if request.args.get('favorite') is not None:
      print('favorite button')
      # print(request.args.get('sentence'))
      
    return render_template('index.html')

@app.route('/favorites', methods = ['GET'])
def favorite():
  fav_sentence = request.args.get('sentence')
  # { "sentence": "Hello world", "word_count": 10 }
  # TODO: Save d to database... 
  print(fav_sentence)
  favorites.insert_one({'sentence': fav_sentence})
  return
  # return render_template('favorite.html', favorites = favorites)

@app.route('/show_favorite')
def show():
  return render_template('favorite.html', favorites=favorites.find())

@app.route("/data")
def data():
  words = tokens('alice.txt')
  q = int(request.args.get('q'))
  # book = request.args.get('book')
  # if book == 'a':
  #   words = tokens('alice.txt')
  # elif book == 'b':
  #   words = tokens('bob.txt')
  markov = Markov(words, 3)
  sentence = markov.get_str(q).capitalize()
  sentence += '.'
  # histogram = word_count.hist_dictionary('words.txt')
  # sent = sentence.sentence(histogram, 5)
  # define some data
  s = {
    'sentence' : sentence,
    'num': q
  }
  return jsonify(s)  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))