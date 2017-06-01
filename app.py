from flask import Flask #importing the flask library
from flask import render_template #allows for rendering of html files (with jinja)
from flask import session, flash, request, redirect, abort #needed for creating user sessions (log ins)
from wtforms import Form, TextField, validators, StringField, SubmitField #form security
from sqlalchemy.orm import sessionmaker #needed in order to interact with database
from tabledef import * #also needed in order to interact with database
import os #used to generate secret key

app = Flask(__name__) #initializes flask application
app.config.from_object(__name__)

engine = create_engine('sqlite:///tutorial.db', echo=True) #needed to interact with the database tutorial.db



class UserForm(Form): #general form class for logins and registration
    username = StringField('Username', validators=[validators.required()])
    email = StringField('Email')
    password = TextField('Password', validators=[validators.required(), validators.Length(min=3, max=35)])

    def reset(self): #resets back to blank data and reinitializes the security
        blankData = MultiDict([ ('csrf', self.reset_csrf()) ])
        self.process(blankData)



@app.route("/")
@app.route("/index")
def index(): #tells what flask should return/do when user accesses above routes
    return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm(request.form) #gets the data from the form submitted by the user
    print form.errors

    if request.method == 'POST':
        Session = sessionmaker(bind=engine) #starts session in order to insert things into a database
        s = Session()

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print username, " ", email, " ", password

        if form.validate(): #if the form is validated then we want to add a new user to the database
            user = User(username, email, password) #adding to the database User the following data
            s.add(user)
            s.commit()

            flash('Hello ' + username + '! Thanks for registering')
        else:
            flash('Error: All fields of the form are required')

    return render_template("signup.html",
                            form=form) #so it will recognize that the form on the page is the same as the form defined in the signup

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)

    if request.method == 'POST':
        Session = sessionmaker(bind=engine)
        s = Session() #start a session in order to interact with db

        username = request.form['username']
        password = request.form['password']
        print username, " ", password

        #query to see if there is a matching value in the
        query = s.query(User).filter(User.username.in_([username]), User.password.in_([password]))
        result = query.first()

        if result:
            session['logged_in'] = True
            session['username'] = username
            flash('Welcome back, ' + username + '!')
        else:
            flash('Sorry, invalid credentials. Try again')

    return render_template("login.html",
                            form=form)

app.secret_key = os.urandom(12) #essential to creating a session
app.run(debug=True) #tells python to run the application with debugging on
