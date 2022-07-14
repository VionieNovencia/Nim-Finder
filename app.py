from cgitb import reset
from logging import exception
from flask import Flask,render_template,redirect,request, session
import src.main as main

app = Flask(__name__)
app.secret_key = 'super secret key'

def getResult(Page):
    db = []
    if request.method == 'POST':
        try:
            user_input = request.form["user_input"]
            session['page'] = Page
            db = main.Search(user_input)
        except Exception as e:
            print(e)
        if db != []:
            result = db[session['page']*10: session['page']*10+10]
            print(len(result))
            return render_template("search.html", result = result, next = len(db)-Page*10, prev = Page*10,user=user_input)
    return render_template("search.html", result = None ,user="",  next = 0, prev = 0)

@app.route('/', methods=['GET', 'POST'])
def search():
    return getResult(0)

@app.route('/next', methods=['GET', 'POST'])
def nextPage():
    session['page'] += 1
    return getResult(session['page'])

@app.route('/prev', methods=['GET', 'POST'])
def prevPage():
    session['page'] -= 1
    return getResult(session['page'])

if __name__ == "__main__":
    app.run(debug=True)