from loan import app 
import pytest 

#client -> act as a live server

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.text == "<h1> Loan Approval Application</h1>" 
    
def test_perdict(client):
    test_data = {
        "ApplicantIncome": 50,
        "CreditHistory": 1,
        "Gender": "Male",
        "LoanAmount": 20000,
        "Married": "Yes",
    }
    resp = client.post('/predict',json = test_data)
    assert resp.status_code == 200
    assert resp.json == {'Loan Approval Status': "Loan Rejected","Details": test_data}
    