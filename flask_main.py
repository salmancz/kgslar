from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/output/')
def output():
    return render_template("status.html")

if __name__ =="__main__":
    app.run(debug=False,host='0.0.0.0') 