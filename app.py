from flask import Flask, render_template #Importing the flask library which will handle requests and brininging in the HTML file

app = Flask(__name__) #Creates the flask application

macbeth_data = {

    "name": "Macbeth",

    "overview": """

    Macbeth is the tragic hero of Shakespeare's play.
    He begins as a respected and courageous soldier, but his ambition 
    and desire for power lead him towards violence and his downfall.
    """,

    "development": [

        {

            "title": "Beginning of the play",

            "text": """
            
            Macbeth is presented as a brave and loyal soldier who is praised for his actions in battle.
            """
        },

        {

            "title": "Middle of the play",

            "text": """

            Macbeth becomes increasingly controlled by ambition and commits 
            murder to secure his position as king.
            """

        },

        {

            "title": "End of the play",

            "text": """

            Macbeth becomes a rutheless tyrant and loses respect of those 
            around him before being defeated.
            """

        }

    ],

    "relationships": [

        {

            "name": "Lady Macbeth",

            "description": """

            Lady MAcbeth initially encourages Macbeth to pursue power. However,
            Macbeth later becomes more independent and increasinly ruthless.

            """

        },

        {

            "name": "Banquo",

            "description": """

            Banquo acts as a moral contrast to Macbeth. Both recieve prophecies,
            but Banquo refuses to pursue them through violence.

            """
        },

        {

            "name": "The Witches",

            "description": """

            The Witches awaken Macbeth's ambition through their prophecies, but
            Macbeth remains responsible for the decisions he makes.
            """

        }

    ],

    "themes": [

        "Ambition",

        "Power",

        "Guilt",

        "Supernatural"

    ],

    "quotes": [

        {

            "text": "Vaulting ambition",

            "theme": "Ambition",

            "explanation": """

            Shows Macbeth recognising thathis ambition is pushing him towards destructive actions.
            """

        },

        {

            "text": "Is this a dagger which I see before me?",

            "theme": "Supernatural / Guilt",

            "explanation": """

            Shows Macbeth's uncertainty before murdering Duncan and highlights
            his internal conflict.
            """

        }

    ],

    "exam_tips": [

        {

            "tip": "Link Macbeth to ambition",

            "reasoning": """

            When writing about Macbeth, connect his actions to his overwhelming ambition and desire for power, and he allows his ambition to dictate his actions.
            """ 

        },

        {

            "tip": "Discuss change through the play",

            "reasoning": """
            
            To achieve top marks, you need to speak about the play as a whole, this means comparing the noble warrior fighting for king and country at the beginning to the malicious tyrant at the end of the play and what causes this change.
            """

        },

        {

            "tip": "Context",

            "reasoning": """

            Link Macbeth's downfall to Jacobean beliefs about kingship, the supernatural and the consequences of disrupting the natural order. Again to acheive top marks, showing you know and understand the context of the play is crucial to achieveing the top bands/marks on the mark scheme.
            """

        }

    ],

}


lady_macbeth_data = {

    "name": "lady Macbeth",

    "overview": """

    Lady Macbeth is one of Shakespeare's most ambitious characters.
    She encourages Macbeth to pursue power, but later becomes overwhelmed
    by guilt and the consequences of their actions.

    """,

    "development": [

        {

            "title": "Beginning of the play",

            "text": """

            Lady Macbeth is presented as powerful, determined and willing to
            manipulate Macbeth to achieve their ambitions.

            """
        },

        {

            "title": "Middle of the play",

            "text": """

            As Macbeth becomes more independent and ruthless, Lady Macbeth 
            begins to lose control.

            """

        },

        {

            "title": "End of the play",

            "text": """

            Lady Macbeth is consumed by guilt and her mental decline shows the
            consequences of their actions.

            """
        }

    ],

    "themes": [

        "Ambition",

        "Guilt",

        "Power",

        "Gender"

    ],

    "relationships": [

        {

            "name": "Macbeth",

            "description": """

            Lady Macbeth intially appears more dominant than Macbeth and encourages
            him to murder Duncan. Their relationship weakens as Macbeth beginsacting
            without consulting her.

            """
        }
    ]

    "quotes": [

        {

            "text": "Unsex me here",

            "theme": "Gender / Power",

            "explanation": """

            Shows Lady Macbeth rejecting traditional expectations of women
            because she wants more power.

            """

        },

        {

            "text": "Out, damned spot!",

            "theme": "Guilt",

            "explanation": """

            Shows Lady Macbeth's guilt becoming impossible to hide.

            """

        }

    ],

    "exam_tips": [

        {

            "tip": "Compare Lady Macbeth and Macbeth",

            "reasoning": """

            Explore how their relationship changes throughout the play and
            how Macbeth eventually becomes more powerful than Lady Macbeth.

            """

        }

    ]
}

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

#Macbeth character route
#-----------------------
@app.route("/macbeth/characters/macbeth")

def macbeth_character():

    return render_template(
        "character.html",
        character=macbeth_data
    )


#Lady Macbeth character route
#----------------------------
@app.route("/macbeth/characters/lady-macbeth")

def lady_macbeth_character():

    return render_template(
        "character.html",
        character=lady_macbeth_data
    )

#Banquo character route
#----------------------
@app.route("/macbeth/characters/banquo")

def banquo_character():

    return render_template("banquo_character.html")

#Macduff character route
#-----------------------
@app.route("/macbeth/characters/macduff")

def macduff_character():

    return render_template("macduff_character.html")

#Witches character route
#----------------------
@app.route("/macbeth/characters/witches")

def witches_character():

    return render_template("witches_character.html")

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