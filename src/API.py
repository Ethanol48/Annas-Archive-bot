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

class BookSpecific(Resource):

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument("language", type=str, required=False)
        parser.add_argument("author", type=str, required=False)
        parser.add_argument("book_title", type=str, required=False)
        parser.add_argument("file_type", type=str, required=False)


        file_types = [
            "Content", "Journal article", "Book (any)", "Book (non-fiction)",
            "Book (fiction)", "Book (unknown)", "Comic book", "Magazine",
            "Standards document"
        ]

        languages = [
            'English [en]', 'Russian [ru]', 'German [de]', 'Spanish [es]',
            'French [fr]', 'Italian [it]', 'Ukrainian [uk]', 'Portuguese [pt]',
            'Dutch [nl]', 'Greek [el]', 'Chinese [zh]', 'Hungarian [hu]',
            'Romanian [ro]', 'Polish [pl]', 'Turkish [tr]', 'Latin [la]',
            'Kazakh [kk]', 'Belarusian [be]', 'Lithuanian [lt]',
            'Bashkir [ba]', 'Arabic [ar]', 'Czech [cs]', 'Japanese [ja]',
            'Swedish [sv]', 'Catalan [ca]', 'Latvian [lv]', 'Serbian [sr]',
            'Indonesian [id]', 'Hindi [hi]', 'Austronesian languages [map]',
            'Danish [da]', 'Uzbek [uz]', 'Afrikaans [af]', 'Norwegian [no]',
            'Tatar [tt]', 'Turkmen [tk]', 'Georgian [ka]', 'Croatian [hr]',
            'Mongolian [mn]', 'Sinhala [si]', 'Korean [ko]', 'Hebrew [he]',
            'Ancient Greek [grc]', 'Eastern Tamang [taj]',
            'Central Tarahumara [tar]', 'Flemish [nl-BE]', 'Serili [sve]',
            'Slovak [sk]', 'Pashto [ps]', 'Bulgarian [bg]', 'Kyrgyz [ky]',
            'Persian [fa]', 'Marathi [mr]', 'Azerbaijani [az]',
            'Esperanto [eo]', 'Albanian [sq]', 'Samoan [sm]', 'Malayalam [ml]',
            'Galician [gl]', 'Ndolo [ndl]', 'Uyghur [ug]', 'Gujarati [gu]',
            'Slovenian [sl]', 'Filipino [fil]', 'Quechua [qu]',
            'Armenian [hy]', 'Somali [so]', 'Bosnian [bs]', 'Estonian [et]',
            'Dongxiang [sce]', 'Urdu [ur]', 'Bangla [bn]', 'Tamil [ta]',
            'Vietnamese [vi]', 'Finnish [fi]', 'Thai [th]', 'Kurdish [ku]',
            'Sanskrit [sa]', 'Telugu [te]', 'Nepali [ne]',
            'Serbo-Croatian [sh]', 'Icelandic [is]', 'Basque [eu]',
            'Burmese [my]', 'Tagalog [tl]', 'Malay [ms]', 'Yiddish [yi]',
            'Swahili [sw]', 'Punjabi [pa]', 'Macedonian [mk]',
            'Haitian Creole [ht]', 'Tibetan [bo]', 'Kannada [kn]', 'Lao [lo]',
            'Kara'
        ]
        args = parser.parse_args()

        if args["language"] not in languages:
            return { "message": "the parameter used for language is not correct" }, 400

        elif args["file_type"] not in file_types:
            return { "message": "the parameter used for file_type is not correct" }, 400

        else:
            return args, 200


        # json_response = get_books(get_soup_from_internet("https://annas-archive.org/search?q=Dale+Carnegie"))

        # if json_response is not None or json_response != "No books found":
        #     return json_response[book_id], 200

        # elif json_response == "No books found":
        #     return json_response, 502

        # else:
        #     return {}, 400

api.add_resource(Books, "/books")
api.add_resource(BookSpecific, "/books_specs")


if __name__ == "__main__":
    app.run(debug=False)
