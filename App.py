from flask import flask, jsonify,request

app= Flask(__name__)

@app.route("/")
def index():
    if 'query' not in request.args:
        return jsonify({"prediction": None,"mensage": "send me a text"})
    query = request.agrs.get("query")
    modelo = load("modelo_RanomForest.joblib")
    labels=['Não','Sim']
    
    predict = modelo.predict([query])
    prediction = labels[predict[0]]
    
    return jsonify({"prediction": prediction})