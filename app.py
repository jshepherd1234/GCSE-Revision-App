from flask import Flask, render_template #Importing the flask library which will handle requests and brininging in the HTML file

app = Flask(__name__) #Creates the flask application

@app.route("/") #Sets the route for the homepage

def homepage(): #Creates function for the homepage

    return render_template("home.html")

@app.route("/jekyll-hyde") #Sets route for Jekyll and hyde page

def jekyll_hyde(): #Creating Jekyll and Hyde function

    return render_template("jekyll_hyde.html") #Return correct page to user

@app.route("/macbeth") #Sets the route for the "Macbeth" quiz

def Macbeth(): #Creating Macbeth function

    return render_template("macbeth.html") #Return correct page to user

@app.route("/an-inspector-calls") #Sets the route for "An inspector calls" quiz

def an_inspector_calls(): #Creating "An inspector calls function"

    return render_template("an_inspector_calls.html") #Return correct page to user 

@app.route("/war-conflict-poetry") #Sets route for poetry quiz

def war_conflict_poetry(): #Creating poetry function

    return render_template("war_conflict_poetry.html") #Return correct page to user
app.run()