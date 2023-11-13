from flask import Flask, request
import json
import csv


with open('imdb-movie-data.csv', newline='') as csvfile:
    respond = []
    context = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
    columns = context[0]

    for row in context[1:]:
        movie = {}
        for index in range(len(columns)):
            movie[columns[index]] = row[index]
        respond.append(movie)


app = Flask(__name__)
data = []
        
@app.route("/")
def get_genre_param():
    genre = request.args.get('genre', default=None, type=str)
    
    answer  = []
    for row in respond:
        gens = [g.lower() for g in row['Genre'].split(',')]
        if genre in gens:
            answer.append(row)

    return json.dumps(answer)

@app.route("/<genre>")
def get_genre(genre):
    answer  = []
    for row in respond:
        gens = [g.lower() for g in row['Genre'].split(',')]
        if genre in gens:
            answer.append(row)

    return json.dumps(answer)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)