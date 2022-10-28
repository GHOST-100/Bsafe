from flask import Flask,render_template,request

app = Flask(__name__)


# prediction function 
# def ValuePredictor(to_predict_list): 
#     to_predict = np.array(to_predict_list).reshape(1, 7) 
#     loaded_model = pickle.load(open("model.pkl", "rb")) 
#     result = loaded_model.predict(to_predict) 
#     return result[0]  


@app.route('/')
def home():
    return render_template("front.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route('/welcome',methods=["GET","POST"])
def welcome():
    return render_template("welcome.html")



@app.route('/contact',methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route('/about',methods=["GET","POST"])
def about():
    return render_template("about.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list))
        # result = ValuePredictor(to_predict_list)
    # if int(result)== 1:
        prediction ='Given transaction is fradulent'
    else:
        prediction ='Given transaction is NOT fradulent'            
    return render_template("result.html", prediction = prediction) 
    

if __name__ == "__main__":
    app.run(debug=True,port=5000)
