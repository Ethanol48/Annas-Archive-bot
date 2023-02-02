from scrapper import get_soup_from_internet
from scrapper import get_books

from flask import Flask
from flask_restful import Resource, Api, reqparse
# import ast


app = Flask(__name__)
api = Api(app)


class Books(Resource):
    
    def get(self):
    
        # TODO: Add a parser to get the search query from the user
        # and when taking the parameters create the the corresponding url

        # https://annas-archive.org/search? lang= &content= &ext= &sort= &q=how+to+win+friends
        # lang, content = {Book, Magazine, ..}, ext -> filetype, sort -> sortear, q -> query

        json_response = get_books(get_soup_from_internet("https://annas-archive.org/search?q=Dale+Carnegie"))

        if json_response is not None or json_response != "No books found":
            return json_response, 200

        elif json_response == "No books found":
            return json_response, 502

        else:
            return {}, 400

api.add_resource(Books, "/books")


if __name__ == "__main__":
    app.run()


