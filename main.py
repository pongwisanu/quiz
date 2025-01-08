from flask import Flask, render_template , request
import os
import pathlib

app = Flask(__name__)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def Index():
    return render_template("index.html")

# List
@app.route("/list")
def ListPage():
    list_path = os.path.join(CURRENT_PATH, "list")
    dir_list = os.listdir(list_path)
    return render_template("list/list_page.html", file_list=dir_list)

@app.route("/list/quiz")
def ListQuiz():
    quiz = request.args.get("name")
    list_path = os.path.join(CURRENT_PATH, "list")
    list = os.path.join(list_path, quiz)
    return render_template("list/quiz.html", full_path=list)

# Image
@app.route("/image")
def ImagePage():
    image_path = os.path.join(CURRENT_PATH, "image")
    dir_list = os.listdir(image_path)
    return render_template("image/image_page.html", file_list=dir_list)

@app.route("/image/quiz")
def ImageQuiz():
    quiz = request.args.get("name")
    return render_template("image/quiz.html", image_name=quiz)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000 , True)