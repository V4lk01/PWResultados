import os
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_sqlalchemy import SQLAlchemy


from random import seed
from random import randint

from flask_security import (
    current_user,
    Security,
    SQLAlchemyUserDatastore,
    login_required,
    logout_user,
)
from flask_security.decorators import roles_required, roles_accepted

from models import (Candidature, User, Role, roles_users_table, Result, Question, Contest, Answer)

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
        
 # Flask views
@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/utilizadores") 
@login_required
def users():
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/concursos")  
def contests():
    return render_template("contests.html")

@app.route("/candidaturas")  
def candidatures():
    return render_template("candidatures.html")

@app.route("/resultados")  
def results():
    users = User.query.all()
    results = Result.query.all()
    return render_template("results.html", users=users, results=results)

@app.route("/forms")  
def forms():
    questions = Question.query.all()
    contests = Contest.query.all()
    return render_template("forms.html", contests=contests, questions=questions)

@app.route("/test/<contest_id>")  
def test(contest_id):
    questions = Question.query.all()
    contests = Contest.query.all()
    answers = Answer.query.all()
    randomNumber = 0
    seed(1)
    randomNumber = randint(0,9999)



    return render_template("test.html", contests=contests, questions=questions, contest_id=contest_id, answers = answers, randomNumber = randomNumber)

@app.route("/createContest")
def createContest():
    questions = Question.query.all()
    contests = Contest.query.all()
    answers = Answer.query.all()
    randomNumber = 0
    
    randomNumber = randint(0,9999)



    return render_template("createContest.html", contests=contests, questions=questions,answers = answers, randomNumber = randomNumber)

@app.route("/questions", methods=["GET","POST"])
def questions():
    
   


    
    if(request.method == "POST"):
        contest_id = request.form.get("contest_id")
        contestCode = request.form.get("contestCode")
        contestName = request.form.get("contestName")
        contestArea = request.form.get("contestArea")
        contestDateStart = request.form.get("contestDateStart")
        contestDateEnd = request.form.get("contestDateEnd")
        question = request.form.get("question")
        for key, val in request.form.items():
            if(key.startswith("mulchoice")):
                print(key)
                print(val)
        #print(question)
        
        return "Success"
    
    return "ERRO"
   


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("security.login")) 

'''
@app.errorhandler(403)
def access_forbidden(error):
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500
'''
    
if __name__ == "__main__":
    app.run(debug=True)