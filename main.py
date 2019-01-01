from flask import Flask, render_template, make_response
import boto3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', card = '3', suite = 'd')

if __name__ == "__main__":
    app.run(debug=True)