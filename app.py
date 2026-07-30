from flask import Flask, render_template #Importing the flask library which will handle requests and brininging in the HTML file

app = Flask(__name__) #Creates the flask application

@app.route("/") #Sets the route for the homepage
@app.route("/jekyll-hyde")
@app.route("/poetry")

def homepage(): #Creates function for the homepage

    return render_template("home.html")



@app.route("/macbeth") #Sets the route for the "Macbeth" quiz

def Macbeth():

    return("This is the Macbeth quiz!")

app.run()