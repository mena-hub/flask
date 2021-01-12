from initialize import app
from flask import Response, request
from mongodb.interactor import MongoAPI
import json

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
# Terminal
# python app.py