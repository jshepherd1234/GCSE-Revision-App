from flask import (Flask, render_template, request, session, redirect, url_for, flash)

import os

import random

import sqlite3

from questions.macbeth_quiz import macbeth_quiz_questions

from jinja2 import TemplateNotFound

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__) #Creates the flask application

DATABASE = "database.db"

def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection

def create_tables():

    connection = get_db_connection()

    connection.execute("""
    
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        role TEXT NOT NULL,

        is_frozen INTEGER NOT NULL DEFAULT 0

    )

    """)

    columns = connection.execute(

        "PRAGMA table_info(users)"

    ).fetchall()

    column_names = [

        column["name"]

        for column in columns

    ]

    if "is_frozen" not in column_names:

        connection.execute(

            """

            ALTER TABLE users

            ADD COLUMN is_frozen INTEGER NOT NULL DEFAULT 0

            """

        )

    connection.execute("""
    
    CREATE TABLE IF NOT EXISTS reports (
    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        
        user_id INTEGER NOT NULL,
        
        page TEXT NOT NULL,
        
        category TEXT NOT NULL,
        
        message TEXT NOT NULL,
        
        status TEXT NOT NULL DEFAULT 'Open',
        
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        
        FOREIGN KEY(user_id) REFERENCES users(id)
        
    )
    
    """)
    
    connection.execute("""

    CREATE TABLE IF NOT EXISTS app_settings(
    
        setting_name TEXT PRIMARY KEY,
        
        setting_value TEXT NOT NULL
        
    )

    """)

    connection.commit()

    connection.close()
    
app.secret_key = os.environ.get(

    "SECRET_KEY",

    "temporary-development-secret-key"

)

def get_setting(setting_name):

    connection = get_db_connection()

    setting = connection.execute(

        """

        SELECT setting_value

        FROM app_settings

        WHERE setting_name = ?

        """,

        (setting_name,)

    ).fetchone()

    connection.close()

    if setting is None:

        return None

    return setting["setting_value"]

def save_setting(setting_name, setting_value):

    connection = get_db_connection()

    connection.execute(

        """

        INSERT INTO app_settings(
        
            setting_name,
            
            setting_value
            
        )

        VALUES (?, ?)

        ON CONFLICT(setting_name)

        DO UPDATE SET

            setting_value = excluded.setting_value

        """,

        (

            setting_name,

            setting_value

        )

    )

    connection.commit()

    connection.close()

page_status = {

    "jekyll_hyde.html": False,

    "an_inspector_calls.html": False,

    "war_conflict_poetry.html": False,

    "macbeth.html": True,

    "character.html": True,

    "macbeth_overview.html": True,

    "macbeth_characters.html": True,

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
    "quiz.html": True,

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

#Register page
#=============
@app.route("/register", methods=["GET", "POST"])

def register():

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"]

        requested_role = request.form.get("role", "student")

        tester_code = request.form.get("tester_code", "").strip()

        if requested_role == "tester":

                stored_tester_code = get_setting("tester_code")

                if(

                    stored_tester_code is None

                    or not check_password_hash(

                        stored_tester_code,

                        tester_code
                    )

                ):

                    flash("Invalid tester code", "error")

                    return redirect(url_for("register"))

                

                role = "tester"

        else:

            role = "student"

        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        try:

            connection.execute(

                """

                INSERT INTO users
                
                (username, password, role)

                VALUES (?, ?, ?)

                """,

                (

                    username,

                    hashed_password,

                    role
                )

            )

            connection.commit()

        except sqlite3.IntegrityError:

            flash("That username already exists.", "error")

            return redirect(url_for("register"))

        finally:

            connection.close()

        return redirect(url_for("login"))

    return render_template("register.html")

#Login page
#==========
@app.route("/login", methods=["GET", "POST"])

def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(

            "SELECT * FROM users WHERE username = ?",

            (username,)

        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password"], password):

            if user["is_frozen"]:

                flash(

                    "This account has been frozen. Contact the administrator.",
                    "error"

                )

                return redirect(url_for("login"))

            session.clear()

            session["user_id"] = user["id"]

            session["username"] = user["username"]

            session["role"] = user["role"]

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid username or password", "error")

            return redirect(url_for("login"))

    return render_template("login.html")

#Dashboard
#=========
@app.route("/dashboard")

def dashboard():

    if "username" not in session:

        return redirect(url_for("login"))

    return render_template(

        "dashboard.html",

        username = session["username"],

        role = session.get("view_role", session["role"])

    )

#Logout
#======
@app.route("/logout")

def logout():

    session.clear()

    return redirect(url_for("homepage"))

#Switch role
#===========
@app.route("/switch-role/<role>")

def switch_role(role):

    if session.get("role") != "main":

        return "Access Denied", 403

    if role not in ["main", "tester", "student"]:

        return "Invalid role", 400

    session["view_role"] = role

    return redirect(url_for("dashboard"))

#Create tester
#=============
@app.route("/create-tester", methods=["GET", "POST"])

def create_tester():

    if session.get("role") != "main":

        return "Access denied", 403

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        try:

            connection.execute(

                """

                INSERT INTO users

                (username, password, role)

                VALUES (?, ?, ?)

                """,

                (

                    username,

                    hashed_password,

                    "tester"

                )

            )

            connection.commit()

        except sqlite3.IntegrityError:

            return "Username already exists"

        finally:

            connection.close()

        return redirect(url_for("dashboard"))

    return render_template("create_tester.html")

#Changing tester registration code
#=================================
@app.route("/change-tester-code", methods=["POST"])

def change_tester_code():

    if session.get("role") != "main":

        return "Access denied", 403

    new_code = request.form.get(

        "new_tester_code",

        ""

    ).strip()

    if len(new_code) < 8:

        flash(

            "Tester code must be at least 8 characters.",

            "error"

        )

        return redirect(url_for("manage_accounts"))

    hashed_code = generate_password_hash(new_code)

    save_setting(

        "tester_code",

        hashed_code

    )

    flash(

        "Tester registration code changed successfully.",

        "success"

    )

    return redirect(url_for("manage_accounts"))

#Freeze and unfreeze account
#===========================
@app.route("/set-account-frozen/<int:user_id>", methods=["POST"])

def set_account_frozen(user_id):

    if session.get("role") != "main":

        return "Access denied", 403

    if user_id == session.get("user_id"):

        flash("You cannot freeze your own account.", "error")

        return redirect(url_for("manage_accounts"))

    action = request.form.get("action", "")

    if action not in ["freeze", "unfreeze"]:

        flash("Invalid account action.", "error")

        return redirect(url_for("manage_accounts"))

    connection = get_db_connection()

    user=connection.execute(

        """

        SELECT id, username, role, is_frozen

        FROM users

        WHERE id = ?

        """,

        (user_id,)

    ).fetchone()

    if user is None:

        connection.close()

        flash("Account not found.", "error")

        return redirect(url_for("manage_accounts"))

    if user["role"] == "main":

        connection.close()

        flash("Main accounts cannot be frozen.", "error")

        return redirect(url_for("manage_accounts"))

    new_status = 1 if action == "freeze" else 0

    username = user["username"]

    connection.execute(

        """

        UPDATE users

         SET is_frozen = ?

        WHERE id = ?

        """,

        (

            new_status,

            user_id

        )

    )

    connection.commit()

    connection.close()

    if new_status == 1:

        flash(

            f"{username} has been frozen.",
            "success"

        )

    else:

        flash(

            f"{username} has been unfrozen.",
            "success"

        )

    return redirect(url_for("manage_accounts"))



#Managing accounts
#=================
@app.route("/manage-accounts")

def manage_accounts():

    if session.get("role") != "main":

        return "Access denied", 403

    username = request.args.get("username", "").strip()

    role = request.args.get("role", "").strip()

    user_id = request.args.get("user_id", "").strip()

    query = """

        SELECT id, username, role, is_frozen

        FROM users

        WHERE 1 = 1

    """

    parameters = []

    if username:

        query += " AND username LIKE ?"

        parameters.append(f"%{username}%")

    if role:

        query += " AND role = ?"

        parameters.append(role)

    if user_id:

        if user_id.isdigit():

            query += " AND id = ?"

            parameters.append(int(user_id))

    query += " ORDER BY username"

    connection = get_db_connection()

    users = connection.execute(

        query,

        parameters

    ).fetchall()

    connection.close()

    return render_template(

        "manage_accounts.html",

        users=users,

        selected_username=username,

        selected_role=role,

        selected_user_id=user_id

    )

#Temp password reset
#===================
@app.route("/reset-password/<int:user_id>", methods=["POST"])

def reset_password(user_id):

    if session.get("role") != "main":

        return "Access denied", 403

    new_password = request.form.get("new_password", "").strip()

    if len(new_password) < 6:

        flash("Password must be at least 6 characters.", "error")

        return redirect(url_for("manage_accounts"))

    connection = get_db_connection()

    user = connection.execute(

        """

        SELECT id, role

        FROM users

        WHERE id = ?

        """,

        (user_id,)

    ).fetchone()

    if user is None:

        connection.close()

        flash("Account not found", "error")

        return redirect(url_for("manage_accounts"))

    if user["role"] == "main":

        connection.close()

        flash("Main-account passwords cannot be reset here.", "error")

        return redirect (url_for("manage_accounts"))

    hashed_password = generate_password_hash(new_password)

    connection.execute(

        """

        UPDATE users

        SET password = ?

        WHERE id = ?

        """,

        (

            hashed_password,

            user_id

        )

    )

    connection.commit()

    connection.close()

    flash("Password reset successfully.", "success")

    return redirect(url_for("manage_accounts"))

#Deleting accounts ability
#=========================
@app.route("/delete-account/<int:user_id>", methods=["POST"])

def delete_account(user_id):

    if session.get("role") != "main":

        return "Access denied", 403

    if user_id == session.get("user_id"):

        return ("You cannot delete your own account (yet)"), 400

    connection = get_db_connection()

    user = connection.execute(

        """

        SELECT id, role

        FROM users

        WHERE id = ?

        """,

        (user_id,)

    ).fetchone()

    if user is None:

        connection.close()

        return "Account not found", 404

    if user["role"] == "main":

        connection.close()

        return "Main accounts cannot be deleted here", 403

    connection.execute(

        """

        DELETE FROM reports

        WHERE user_id = ?

        """,

        (user_id,)

    )

    connection.execute(

        """

        DELETE FROM users

        WHERE id = ?

        """,

        (user_id,)

    )

    connection.commit()

    connection.close()

    flash("Account deleted successfully.", "success")

    return redirect(url_for("manage_accounts"))

#Report issue ability
#====================
@app.route("/report-issue", methods=["GET", "POST"])

def report_issue():

    if session.get("role") != "tester":

        return "Access denied", 403

    if request.method == "POST":

        page = request.form["page"]

        category = request.form["category"]

        message = request.form["message"]

        connection = get_db_connection()

        connection.execute(

            """

            INSERT INTO reports

            (user_id, page, category, message)

            VALUES (?, ?, ?, ?)

            """,

            (

                session["user_id"],

                page,

                category,

                message

                )

        )

        connection.commit()

        connection.close()

        return redirect(url_for("dashboard"))

    return render_template("report_issue.html")

@app.route("/reports")

def reports():

    if session.get("role") != "main":

        return "Access denied", 403

    connection = get_db_connection()

    reports = connection.execute(

        """

        SELECT

            reports.*,

            users.username

        FROM reports

        JOIN users

        ON reports.user_id = users.id

        ORDER BY reports.created_at DESC

        """

    ).fetchall()

    connection.close()

    return render_template(

        "reports.html",

        reports=reports
        
    )

@app.route("/update-report/<int:report_id>/<status>")

def update_report(report_id, status):

    if session.get("role") != "main":

        return "Access denied", 403

    allowed_statuses = [

        "Open",

        "In Progress",

        "Fixed"

    ]

    if status not in allowed_statuses:

        return "Invalid Status", 400

    connection = get_db_connection()

    connection.execute(

        """

        UPDATE reports

        SET status = ?

        WHERE id = ?

        """,

        (

            status,

            report_id

        )

    )

    connection.commit()

    connection.close()

    return redirect(url_for("reports"))

@app.route("/my-reports")

def my_reports():

    if session.get("role")!= "tester":

        return "Access denied!", 403

    connection = get_db_connection()

    reports = connection.execute(

        """

        SELECT *

        FROM reports 

        WHERE user_id = ?

        ORDER BY created_at DESC

        """,

        (session["user_id"],)

    ).fetchall()

    connection.close()

    return render_template(

        "my_reports.html",

        reports=reports

    )


@app.route("/english") #Sets route for the general english page 

def english(): #Creates function for english page

    return render_page_or_coming_soon("english.html") #Return correct page to user

@app.route("/english-literature")

def english_literture():

    return render_page_or_coming_soon("english_literature.html")

@app.route("/english-language")

def english_language():

    return render_page_or_coming_soon("english_langauge.html")


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

#Quiz route
#==========
@app.route("/quiz/macbeth/start", methods=["POST"])

def start_macbeth_quiz():

    quiz_length = request.form.get(

        "quiz_length",

        type=int

    )    

    total_questions = len(macbeth_quiz_questions)

    if quiz_length is None:

        return redirect(url_for("macbeth_quiz_setup"))

    if quiz_length < 1 or quiz_length > total_questions:

        return redirect(url_for("macbeth_quiz_setup"))

    selected_questions = random.sample(

        macbeth_quiz_questions,

        quiz_length

    )

    session["macbeth_quiz_ids"] = [

        question["id"]

        for question in selected_questions

    ]

    return redirect(url_for("macbeth_quiz"))

@app.route("/quiz/macbeth/questions", methods=["GET", "POST"])

def macbeth_quiz():

    selected_ids = session.get("macbeth_quiz_ids")

    if not selected_ids:

        return redirect(url_for("macbeth_quiz_setup"))

    questions_by_id = {

        question["id"]: question

        for question in macbeth_quiz_questions

    }

    questions = [

        questions_by_id[question_id]

        for question_id in selected_ids
        if question_id in questions_by_id

    ]

    score = None

    results = []

    if request.method == "POST":

        score = 0

        for question_number, question in enumerate(questions):

            user_answer = request.form.get(

                f"question_{question_number}"

            )

            is_correct = user_answer == question["answer"]

            if is_correct:

                score += 1

            results.append({

                "user_answer": user_answer,

                "correct_answer": question["answer"],

                "is_correct": is_correct

            })

    return render_template(

        "macbeth_quiz.html",

        questions = questions,

        score = score,

        results = results

    )

@app.route("/quiz/macbeth")

def macbeth_quiz_setup():

    return render_template(

        "macbeth_quiz_setup.html",

        total_questions = len(macbeth_quiz_questions)

    )

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

    create_tables()

    app.run(host="0.0.0.0", port=5000, debug=True)