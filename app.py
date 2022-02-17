from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("index.html")

#@app.route("/ebc")
#def HolaEBC():
#    return "<a href>Hola ebc</a>"

#@app.route("/ebc/random")
#def UnGetRandom():
#    return "Hola EBC Random"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
