from flask import Flask, render_template #Importing the flask library which will handle requests and brininging in the HTML file
from jinja2 import TemplateNotFound

app = Flask(__name__) #Creates the flask application

page_status = {

    "jekyll_hyde.html": False,

    "an_inspector_calls.html": False,

    "war_conflict_poetry.html": False,

    "macbeth.html": True,

    "character.html": True,

    "macbeth_overview.html": True,

    "macbeth)_characters.html": True,

    "macbeth_themes.html": True,

    #Other subjects
    #==============
    "biology.html": False,

    "chemistry.html": False,

    "physics.html": False,

    "maths.html": False,

    "geography.html": False,

    "cscience.html": False,

    #Features
    #========
    "quiz.html": False,

    "flashcards.html": False,

    "planner.html": False,

    "progress.html": False

}

def render_page_or_coming_soon(template, **kwargs):

    if page_status.get(template) == False: 

        return render_template(
            "coming_soon.html",
            page_name = template
        )

    try:

        return render_template(
            template,
            **kwargs
        )

    except TemplateNotFound:

        return render_template(
            "coming_soon.html",
            page_name = template
        )

    
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
        },

        {

            "name": "Duncan",

            "description": """

            Lady macbeth welcomes Duncan into her home while secretly helping to plan
            his murder, connecting her to deception and the theme of appearance versus reality.

            """

        }


    ],

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

        },

        {

            "tip": "Compare the change",

            "reasoning": """

            Explore how Lady Macbeth changes throughout the play, does she become stronger or more powerful,
            or is she overwhelmed by guilt and paranoia?

            """
        }

    ],

}

banquo_data = {

    "name": "Banquo",

    "overview": """

    Banquo is Macbeth's friend and fellow soldier.
    He acts as a moral contrast to Macbeth because, despite hearing the witches'
    prophecies, he does not allow ambition to control his actions.

    """,

    "development": [

        {

            "title": "Beginning of the play",

            "text": """

            Banquo is presented as a brave and loyal soldier who fights alongside Macbeth.

            """

        },

        {

            "title": "Middle of the play",

            "text": """

            Banquo becomes suspicious of Macbeth after Duncan's murder and begins to
            question how Macbeth gained the throne.

            """

        },

        {

            "title": "End of the play",

            "text": """

            Banquo is murdered because Macbeth sees him as a threat, especially because
            of the witches' prophecy about Banquo's descendants becoming kings.
            
            """
        }

    ],

    "relationships": [

        {

            "name": "Macbeth",

            "description": """

            Banquo and Macbeth begin as friends and equals, but they become opposites.
            Macbeth follows his ambition, while Banquo remains honourable.

            """

        }

    ],

    "themes": [

        "Loyalty",

        "Morality",

        "Ambition",

        "Supernatural"

    ],

    "quotes": [

        {

            "text": "What, can the devil speak true?",

            "theme": "Supernatural",

            "explanation": """

            Shows Banquo's suspicion of the witchesand contrasts with Macbeth's willingness 
            to trust their prophecies.
        
            """

        },

        {

            "text": "Thou hast it now: King, Cawdor, Glamis as the weird women promised",

            "theme": "Ambition",

            "explanation": """

            Banquo recognises that Macbeth has gained eveything the witches predicted,
            suggesting he suspects something is wrong.

            """

        }

    ],

    "exam_tips": [

        {

            "tip": "Use Banquo as a contrast to Macbeth",

            "reasoning": """

            Shakespeare uses Banquo to show what Macbeth could have been if he had resisted
            temptation and ambition.

            """

        }

    ]

}

macduff_data = {

    "name": "Macduff",

    "overview": """

    Macduff is a noble warrior who opposes Macbeth's role as king and his tyranical reign.
    he represents justice and loyalty to Scotland

    """,

    "development": [

        {

            "title": "Beginning of the play",

            "text": """

            Starts loyal and noble to the king, Duncan. 

            """

        },

        {

            "title": "Middle of the play",

            "text": """

            Begins to become suspicous of Macbeth, refuses to go to his corronation

            """

        },

        {

            "title": "End of the play",

            "text": """

            Macduff leads the revolt against Macbeth at the end of the play.
            
            """
        }

    ],

    "relationships": [

        {

            "name": "Macbeth",

            "description": """

            Macbeth and Macduff become enemies towards the end of the play, Macbeth has Macduff's family murdered causing Macduff to seek
            revenge. Macduff is the one who delivers Macbeth's anagnorisis.

            """

        },

        {

            "name": "Malcolm",

            "description": """

            Malcolm is the rightful king of Scotland after Duncan and is restored to the throne after Macbeth is defeated.

            """

        }

    ],

    "themes": [

        "Justice",

        "Loyalty",

        "Kingship",

        "Revenge"

    ],

    "quotes": [

        {

            "text": "Bleed, bleed, poor country!",

            "theme": "Justice",

            "explanation": """

            Shows Macbeth's effect on Scotland due to his tyrannical reign.

            """

        },

        {

            "text": "Turn, hell-hound, turn!",

            "theme": "Revenge",

            "explanation": """

            Macduff insults Macbeth and wishes to challnge him to return Scotland to it's rightful state, and to bring justice for his family.

            """

        }

    ],

    "exam_tips": [

        {

            "tip": "Compare Macduff's morality with Macbeth's corruption",

            "reasoning": """

            Compare how Macduff refuses to swear loyalty to Macbeth and how he seeks jusctice and to put Malcolm,
            the rightful king, to the throne.

            """

        }

    ]

}

@app.route("/") #Sets the route for the homepage

def homepage(): #Creates function for the homepage

    return render_page_or_coming_soon("home.html")

@app.route("/english") #Sets route for the general english page 

def english(): #Creates function for english page

    return render_page_or_coming_soon("english.html") #Return correct page to user

@app.route("/english-literature")

def english_literture():

    return render_page_or_coming_soon("english_literature.html")

@app.route("/english-language")

def english_language():

    return render_page_or_coming_soon("english)_langauge.html")


@app.route("/jekyll-hyde") #Sets route for Jekyll and hyde page

def jekyll_hyde(): #Creating Jekyll and Hyde function

    return render_page_or_coming_soon("jekyll_hyde.html") #Return correct page to user

@app.route("/macbeth") #Sets the route for the "Macbeth" page

def macbeth(): #Creating Macbeth function

    return render_page_or_coming_soon("macbeth.html") #Return correct page to user

#Setting up the overview system for Macbeth
#----------------------------------------
@app.route("/macbeth/overview")

def macbeth_overview():

    return render_page_or_coming_soon("macbeth_overview.html")

@app.route("/macbeth/characters")

def macbeth_characters():

    return render_page_or_coming_soon("macbeth_characters.html")

@app.route("/macbeth/themes")

def macbeth_themes():

    return render_page_or_coming_soon("macbeth_themes.html")

#Macbeth character route
#-----------------------
@app.route("/macbeth/characters/macbeth")

def macbeth_character():

    return render_page_or_coming_soon(
        "character.html",
        character=macbeth_data
    )


#Lady Macbeth character route
#----------------------------
@app.route("/macbeth/characters/lady-macbeth")

def lady_macbeth_character():

    return render_page_or_coming_soon(
        "character.html",
        character=lady_macbeth_data
    )

#Banquo character route
#----------------------
@app.route("/macbeth/characters/banquo")

def banquo_character():

    return render_page_or_coming_soon(
        "character.html",
        character=banquo_data
    )

#Macduff character route
#-----------------------
@app.route("/macbeth/characters/macduff")

def macduff_character():

    return render_page_or_coming_soon(
        "character.html",
        character=macduff_data
    )

#Witches character route
#----------------------
@app.route("/macbeth/characters/witches")

def witches_character():

    return render_page_or_coming_soon("witches_character.html")
        

@app.route("/an-inspector-calls") #Sets the route for "An inspector calls" page

def an_inspector_calls(): #Creating "An inspector calls function"

    return render_page_or_coming_soon("an_inspector_calls.html") #Return correct page to user 

@app.route("/war-conflict-poetry") #Sets route for poetry page

def war_conflict_poetry(): #Creating poetry function

    return render_page_or_coming_soon("war_conflict_poetry.html") #Return correct page to user

@app.route("/flashcards") #Sets route for flashcards

def flashcards(): #Creating flashcards function

    return render_page_or_coming_soon("flashcards.html") #Return correct page to user

@app.route("/quiz") #Sets route for quiz

def quiz(): #Creating quiz function

    return render_page_or_coming_soon("quiz.html") #Return correct page to user

@app.route("/planner") #Sets route for planner 

def planner(): #Creating planner function

    return render_page_or_coming_soon("planner.html") #Return correct page to user

@app.route("/progress") #Sets route for progress 

def progress(): #Creating progress function

    return render_page_or_coming_soon("progress.html") #Return correct page to user

@app.errorhandler(404)

def page_not_found(error):

    return render_template("404.html"), 404

@app.errorhandler(TemplateNotFound)

def template_not_found(error):

    return render_template("coming_soon.html"), 200

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)