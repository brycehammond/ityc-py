from flask import Flask, render_template, make_response, request, jsonify
import boto3

app = Flask(__name__)

# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('ityc')

@app.route("/")
def home():
    record = db.get_item(Key={'id': 'card'})['Item']
    return jsonify({'card': record['card'].upper(), 'suit': record['suit'].lower()})

@app.route('/update', methods = ['POST'])
def update():
    #get the data from the request
    request_data = request.get_json()
    card = request_data['card'].upper()
    suit = request_data['suit'].lower()

    #update the record
    res = db.update_item(
        Key={'id': 'card'},
        UpdateExpression='set card=:card, suit=:suit',
        ExpressionAttributeValues={':card': card, ':suit': suit},
    )
    return jsonify({'card': card, 'suit': suit})
    
if __name__ == "__main__":
    app.run(debug=True)