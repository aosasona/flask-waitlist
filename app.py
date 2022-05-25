from flask import Flask, render_template, request, redirect, url_for
from services.db import insert, show, find_email


# Flask initialisation
app = Flask(__name__)


# Index route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Submit Email
@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"].lower()
    verify = find_email(email)
    if verify < 1:
        if insert(email):
            return render_template("index.html", success=True)
        else:
            return render_template("index.html", error=True)
    else:
        return render_template("index.html", error=True)


# Show All E-mails
@app.route("/show")
def display():
    mails = show()
    if mails is not False:
        return render_template("list.html", data=mails, error=False)
    else:
        return render_template("list.html", error=True)




#
# if __name__ == '__main__':
#     app.run()
