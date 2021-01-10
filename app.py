from flask import Flask, redirect, url_for
from store.answers import *

app = Flask("PhilosophyStore")


@app.route("/", methods=['GET'])
def redirect_page():
    return redirect(url_for('main'))


@app.route("/main", methods=["GET"])
def main():
    page = open("front/index.html", encoding="UTF-8").read()
    return page


@app.route("/pages/<num>/", methods=["GET"])
def page_menu(num: str):
    path = "front/mines/"+str(num)+".html"
    page = open(path, encoding="UTF-8").read()
    return page


@app.route("/q/<num>/", methods=["GET"])
def get_question(num: str):
    html = make_question(num)
    return html


def make_question(num):
    ans = get_ans(num)
    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Question {num}</title>
</head>
<body>
<p>{ans}</p>
</body>
</html>
    '''
    return html


if __name__ == "__main__":
    app.run()
