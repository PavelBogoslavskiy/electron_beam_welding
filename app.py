from flask import Flask, render_template, request
import sklearn
import pickle
from numpy import round

kneighbors_model = pickle.load(open('models/kneighbors_model.pkl', 'rb'))
decision_tree_model = pickle.load(open('models/decision_tree_model.pkl', 'rb'))
random_forest_model = pickle.load(open('models/random_forest_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=["get", "post"])  # http://127.0.0.1:5000/
def index():
    message = ""
    depth = 0
    width = 0
    model_id = 0
    if request.method == "POST":
        model_id = int(request.form.get("rg_model"))
        iw = float(request.form.get("iw"))
        if_ = float(request.form.get("if"))
        vw = float(request.form.get("vw"))
        fp = float(request.form.get("fp"))
        params = [[iw, if_, vw, fp]]
        match model_id:
            case 0: # kneighbors_model
                prediction = kneighbors_model.predict(params)
                depth = round(prediction[0][0], 2)
                width = round(prediction[0][1], 2)
            case 1: # decision_tree_model
                prediction = decision_tree_model.predict(params)
                depth = round(prediction[0][0], 2)
                width = round(prediction[0][1], 2)
            case 2: # random_forest_model
                prediction = random_forest_model.predict(params)
                depth = round(prediction[0][0], 2)
                width = round(prediction[0][1], 2)
            case _:
                print("Что-то пошло не так!")
        message = f"Глубина сварного соединения составляет {depth} мм, ширина {width} мм."

    return render_template("index.html", message=message)

#app.run()
