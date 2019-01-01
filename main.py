from flask import Flask, render_template, make_response
import boto3

app = Flask(__name__)

# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('ityc')

@app.route("/")
def home():
    record = db.get_item(Key={'id': 'card'})['Item']
    return render_template('home.html', card = record['value'], suit = record['suit'])

if __name__ == "__main__":
    app.run(debug=True)