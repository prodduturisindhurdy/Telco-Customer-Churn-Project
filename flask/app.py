from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    # Numeric inputs
    senior = int(request.form.get('SeniorCitizen', 0))
    tenure = float(request.form.get('tenure', 0))
    monthly = float(request.form.get('MonthlyCharges', 0))
    total = float(request.form.get('TotalCharges', 0))

    # Gender, Partner, Dependents
    gender = request.form.get('Gender', 'Female')
    partner = request.form.get('Partner', 'No')
    dependents = request.form.get('Dependents', 'No')
    gender_male = 1 if gender == "Male" else 0
    partner_yes = 1 if partner == "Yes" else 0
    dependents_yes = 1 if dependents == "Yes" else 0

    # Phone Service
    phone = request.form.get('PhoneService', 'No')
    phone_yes = 1 if phone == "Yes" else 0

    # Multiple Lines (2 dummies)
    multiple = request.form.get('MultipleLines', 'No')
    multiple_no_phone = 1 if multiple == "No phone service" else 0
    multiple_yes = 1 if multiple == "Yes" else 0

    # Internet Service (2 dummies)
    internet = request.form.get('InternetService', 'No')
    internet_fiber = 1 if internet == "Fiber optic" else 0
    internet_no = 1 if internet == "No" else 0

    # Online Security (2 dummies)
    online_sec = request.form.get('OnlineSecurity', 'No')
    online_sec_no_internet = 1 if online_sec == "No internet service" else 0
    online_sec_yes = 1 if online_sec == "Yes" else 0

    # Online Backup (2 dummies)
    online_backup = request.form.get('OnlineBackup', 'No')
    online_backup_no_internet = 1 if online_backup == "No internet service" else 0
    online_backup_yes = 1 if online_backup == "Yes" else 0

    # Device Protection (2 dummies)
    device = request.form.get('DeviceProtection', 'No')
    device_no_internet = 1 if device == "No internet service" else 0
    device_yes = 1 if device == "Yes" else 0

    # Tech Support (2 dummies)
    tech = request.form.get('TechSupport', 'No')
    tech_no_internet = 1 if tech == "No internet service" else 0
    tech_yes = 1 if tech == "Yes" else 0

    # Streaming TV (2 dummies)
    streamtv = request.form.get('StreamingTV', 'No')
    streamtv_no_internet = 1 if streamtv == "No internet service" else 0
    streamtv_yes = 1 if streamtv == "Yes" else 0

    # Streaming Movies (2 dummies)
    streammovies = request.form.get('StreamingMovies', 'No')
    streammovies_no_internet = 1 if streammovies == "No internet service" else 0
    streammovies_yes = 1 if streammovies == "Yes" else 0

    # Contract (2 dummies)
    contract = request.form.get('Contract', 'Month-to-month')
    contract_one = 1 if contract == "One year" else 0
    contract_two = 1 if contract == "Two year" else 0

    # Paperless Billing (1 dummy)
    paperless = request.form.get('PaperlessBilling', 'No')
    paperless_yes = 1 if paperless == "Yes" else 0

    # Payment Method (3 dummies)
    payment = request.form.get('PaymentMethod', 'Bank transfer')
    pay_credit = 1 if payment == "Credit card (automatic)" else 0
    pay_echeck = 1 if payment == "Electronic check" else 0
    pay_mail = 1 if payment == "Mailed check" else 0

    # Build feature vector in training order (30 features)
    features = [
        senior, tenure, monthly, total,
        gender_male, partner_yes, dependents_yes, phone_yes,
        multiple_no_phone, multiple_yes,
        internet_fiber, internet_no,
        online_sec_no_internet, online_sec_yes,
        online_backup_no_internet, online_backup_yes,
        device_no_internet, device_yes,
        tech_no_internet, tech_yes,
        streamtv_no_internet, streamtv_yes,
        streammovies_no_internet, streammovies_yes,
        contract_one, contract_two,
        paperless_yes,
        pay_credit, pay_echeck, pay_mail
    ]

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return render_template(
        "index.html",
        churn_prediction=int(prediction),
        churn_probability=float(probability)
    )

if __name__ == '__main__':
    app.run(debug=True)