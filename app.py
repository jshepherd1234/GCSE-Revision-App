from flask import Flask, render_template #Importing the flask library which will handle requests and brininging in the HTML file

app = Flask(__name__) #Creates the flask application

@app.route("/") #Sets the route for the homepage

def homepage(): #Creates function for the homepage

    return render_template("home.html")

@app.route("/english") #Sets route for the general english page 

def english(): #Creates function for english page

    return render_template("english.html") #Return correct page to user

@app.route("/english-literature")

def english_literture():

    return render_template("english_literature.html")

@app.route("/english-language")

def english_language():

    return render_template("english)_langauge.html")


@app.route("/jekyll-hyde") #Sets route for Jekyll and hyde page

def jekyll_hyde(): #Creating Jekyll and Hyde function

    return render_template("jekyll_hyde.html") #Return correct page to user

@app.route("/macbeth") #Sets the route for the "Macbeth" page

def macbeth(): #Creating Macbeth function

    return render_template("macbeth.html") #Return correct page to user

#Setting up the overview system for Macbeth
#----------------------------------------
@app.route("/macbeth/overview")

def macbeth_overview():

    return render_template("macbeth_overview.html")

@app.route("/macbeth/characters")

def macbeth_characters():

    return render_template("macbeth_characters.html")

@app.route("/macbeth/themes")

def macbeth_themes():

    return render_template("macbeth_themes.html")

@app.route("/an-inspector-calls") #Sets the route for "An inspector calls" page

def an_inspector_calls(): #Creating "An inspector calls function"

    return render_template("an_inspector_calls.html") #Return correct page to user 

@app.route("/war-conflict-poetry") #Sets route for poetry page

def war_conflict_poetry(): #Creating poetry function

    return render_template("war_conflict_poetry.html") #Return correct page to user

@app.route("/flashcards") #Sets route for flashcards

def flashcards(): #Creating flashcards function

    return render_template("flashcards.html") #Return correct page to user

@app.route("/quiz") #Sets route for quiz

def quiz(): #Creating quiz function

    return render_template("quiz.html") #Return correct page to user

@app.route("/planner") #Sets route for planner 

def planner(): #Creating planner function

    return render_template("planner.html") #Return correct page to user

@app.route("/progress") #Sets route for progress 

def progress(): #Creating progress function

    return render_template("progress.html") #Return correct page to user


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)