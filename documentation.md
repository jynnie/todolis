# Making a Multi-User Todo List with Flask

Show them what we're going to make;
explain basic structure of how web apps work
explain python, html, css, and jinja used

Setup folders:
todo
todo > templates

make app.py in todo

1. import the flask library
2. initialization
3. setup index route
4. setup app.run (then test)

default will port to 5000
okay we now have a basic page
lets setup our first html page

5. templates > base.html
	- explain tags with the html tag (explain what html is)
	- setup header (explain what a header is)
	- setup body
	- block content (explain)
6. templates > index.html
	- show extend
	- put something basic in
7. import render_template + edit index route
	- show and explain
8. add bootstrap and wow them
	- show the immediate change
9. use style to stick footer to the bottom
	- just to show them a sample of how styling can happen;
	  more to come in the future, this is just a taste
	  let's finish giving the app functionality

(^ the above took approx. 15 minutes)

10. start setting up signup routes
	- need to add get and post methods (must explain)
	- should also explain how a login system 
	  will work with databases before actually just doing it
11. create signup.html
	- need to explain how forms work
	- need to explain id's v. class's
	- now we have the front end we need to make this actually do things
	- also add this to the navbar
12. import wtforms
13. Make UserForm class
14. add functionality to sign up
	- remember to add back form.csrf
	- remember to add form=form to render_template
	- remember to add secret_key
15. make database with tabledef.py
	- well now we need to actually post these things into a database
	- need to explain how __init__ works
	- need to explain the difference between User() and users
	- need to explain columns (draw for this)
16. create database by running tabledef.py
17. test sign up
18. add flash prompts

*possible improvements to sign up: better flash prompts; no double users; limit character count for username*

---

19. add todos table and link to user table
	- gotta explain backref, and foreign keys
	- a one to many relationship
