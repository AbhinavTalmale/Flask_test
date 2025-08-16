from flask import Flask,request
import pickle
import sklearn

app = Flask(__name__)

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/",methods = ["GET"])

def hello():
    return "<h1> Loan Approval Application</h1>"

@app.route("/predict", methods=["GET"])
def predict():
    return {
    "API": "Loan Prediction",
    "Welcome": "Thank you for using our Loan Approval Prediction service.",
    "Instructions": "To get a prediction, send a POST request to this endpoint with your loan details in JSON format.",
    "Required Fields": [
        "Gender (Male/Female)",
        "Married (Yes/No)",
        "ApplicantIncome (numeric)",
        "LoanAmount (numeric)",
        "CreditHistory (0 or 1)"
    ],
    "Sample Request": {
        "Gender": "Male",
        "Married": "Yes",
        "ApplicantIncome": 5000,
        "LoanAmount": 200,
        "CreditHistory": 1
    }
}

@app.route("/predict",methods = ['POST'])
def predict_post():
    loan_req = request.get_json()
    
    if loan_req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == 'Yes':
        Married = 1
    else:
        Married = 0
        
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    CreditHistory = loan_req['CreditHistory']
    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]
    
    res = model.predict([input_data])
    # Assuming the model returns 1 for approval and 0 for rejection
    # Adjust the logic based on your model's output
    
    
    if res[0] == 1:
        pred = "Loan Approved"
    else:
        pred = "Loan Rejected"

    return {"Loan Approval Status": pred, "Details": loan_req}
