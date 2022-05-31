from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def entry_point():
    return render_template("index.html")

@app.route('/replace', methods=["GET","POST"])
def replace():
    replacetext=request.form['replacetext']
    thetext=request.form['thetext']
    thepara=request.form["thepara"]

    resulttext=re.sub(replacetext,thetext,thepara)

    return render_template("index.html", resulttext=resulttext)

if __name__ == '__main__':
    app.run(debug=True)
