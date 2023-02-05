from scrapper import get_soup_from_internet
from scrapper import get_books

from flask import Flask
from flask_restful import Resource, Api, reqparse
# import ast

import urllib.parse

app = Flask(__name__)
api = Api(app)


# class Books(Resource):
#
#    def get(self):
#
#        # TODO: Add a parser to get the search query from the user
#        # and when taking the parameters create the the corresponding url
#
#        # https://annas-archive.org/search? lang= &content= &ext= &sort= &q=how+to+win+friends
#        # lang, content = {Book, Magazine, ..}, ext -> filetype, sort -> sortear, q -> query
#
#        json_response = get_books(get_soup_from_internet("https://annas-archive.org/search?q=Dale+Carnegie"))
#
#        if json_response is not None or json_response != "No books found":
#            return json_response, 200
#
#        elif json_response == "No books found":
#            return json_response, 502
#
#        else:
#            return {}, 400


def check_if_null(value):
    if value is None:
        return True

    elif value == "":
        return True

    else:
        return False


class BookSpecific(Resource):

    def get(self):

        parser = reqparse.RequestParser()
        # annas-archive
        parser.add_argument("lang", type=str, required=False)
        parser.add_argument("content", type=str, required=False)
        parser.add_argument("ext", type=str, required=False)
        parser.add_argument("sort", type=str, required=False)

        # para el query
        parser.add_argument("author", type=str, required=False)
        parser.add_argument("title", type=str, required=False)

        contents = [
            "Journal article", "Book (any)", "Book (non-fiction)",
            "Book (fiction)", "Book (unknown)", "Comic book", "Magazine",
            "Standards document"
        ]

        # eliminate all the brackets from the list below

        langs = [
            'en','ru','de','es','fr','it',
            'uk','pt','nl','el','zh','hu',
            'ro','pl','tr','la','kk','be',
            'lt','ba','ar','cs','ja','sv',
            'ca','lv','sr','id','hi','da',
            'uz','af','no','tt','tk','ka',
            'hr','mn','si','ko','he','grc',
            'taj','tar','nl-BE','sve','sk',
            'ps','bg','ky','fa','mr','az',
            'eo','sq','sm','ml','gl','ndl',
            'ug','gu','sl','fil','qu','hy',
            'so','bs','et','sce','ur','bn',
            'ta','vi','fi','th','ku','sa',
            'te','ne','sh','is','eu','my',
            'tl','ms','yi','sw','pa','mk',
            'ht','bo','kn','lo',
        ]

        exts = [
            'pdf', 'epub', 'djvu', 'cbr', 'mobi', 'doc', 'cbz', 'azw3', 'rar',
            'fb2', 'rtf', 'zip', 'lit', 'txt', 'docx', 'htm', 'html', 'lrf',
            'fb2.zip', 'mht'
        ]

        sorts = [ 'newest', 'oldest', 'largest', 'smallest']

        args = parser.parse_args()

        if args["lang"] not in langs and check_if_null(args["lang"]) == False:

            return {
                "message": "the parameter used for lang is not correct",
                "lang": args["lang"],
                "help": "the correct values are the following: ",
                "options": langs
            }, 400

        elif args["content"] not in contents and check_if_null(args["content"]) == False:
            return {
                "message": "the parameter used for content is not correct",
                "content": args["content"],
                "help": "the correct values are the following: ",
                "options": contents
            }, 400

        elif args["ext"] not in exts and check_if_null(args["ext"]) == False:
            return {
                "message": "the parameter used for ext is not correct",
                "ext": args["ext"],
                "help": "the correct values are the following: ",
                "options": exts
            }, 400

        elif args["sort"] not in sorts and check_if_null(args["sort"]) == False:
            return {
                "message": "the parameter used for sort is not correct",
                "sort": args["sort"],
                "help": "the correct values are the following: ",
                "options": sorts
            }, 400


        else:
            # ?lang= &content= &ext= &sort= &q

            args["q"] = args["author"] + ", " + args["title"]

            del args["author"]
            del args["title"]

            url = urllib.parse.urlencode(args)

            url_base = "https://annas-archive.org/search?"

            final_url = url_base + url

            # return {
            #     "lang": args["lang"],
            #     "content": args["content"],
            #     "ext": args["ext"],
            #     "sort": args["sort"],
            #     "url": url_base + url
            # }


            json_response = get_books(get_soup_from_internet(final_url))
            return json_response, 200

            # if json_response is not None or json_response != "No books found":
            #     return json_response, 200

            # elif json_response == "No books found":
            #     return json_response, 502

            # else:
            #     return {}, 400

# api.add_resource(Books, "/books")
api.add_resource(BookSpecific, "/books_specs")

if __name__ == "__main__":
    app.run(debug=True)
