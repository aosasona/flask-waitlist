from flask import Flask, render_template, request, redirect, url_for
from services.db import insert, show

# Flask initialisation
app = Flask(__name__)


# Index route
@app.route("/")
@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        email = request.form["email"]
        join_list = insert(email)
        if join_list:
            return render_template("index.html", success=True)
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
