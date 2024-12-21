from flask import Flask, render_template, request
from model.recommender import GiftRecommender
import pandas as pd

app = Flask(__name__)
recommender = GiftRecommender(data_path='data/Christmas Sales and Trends.csv')
# recommender.preprocess()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    age = int(request.form['age'])
    gender = request.form['gender']
    recommendations = recommender.get_recommendations(age, gender)
    print("Recommendations passed to the template:", recommendations)
    return render_template('result.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True)
