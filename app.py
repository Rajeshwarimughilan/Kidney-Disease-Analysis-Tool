from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function for kidney disease prediction
def kidney_disease_prediction(age, blood_pressure, blood_sugar, creatinine, urea, hemoglobin, wbc,
                              diabetes_status, hypertension_status, appetite, swelling, anemia, cholesterol):
    risk_factors = 0

    # Blood Pressure (Normal: 120/80 mmHg)
    if blood_pressure > 140:
        risk_factors += 2

    # Blood Sugar (Normal fasting: 70-99 mg/dL)
    if blood_sugar > 125:
        risk_factors += 1

    # Creatinine (Normal: 0.6-1.2 mg/dL)
    if creatinine > 1.2:
        risk_factors += 1

    # Urea (Normal: 7-20 mg/dL)
    if urea > 20:
        risk_factors += 1

    # Hemoglobin (Normal: 13.8-17.2 g/dL for men, 12.1-15.1 g/dL for women)
    if hemoglobin < 12.0:
        risk_factors += 1

    # WBC (White Blood Cell) Level (Normal: 4,500-11,000 cells/mcL)
    if wbc > 11000:
        risk_factors += 1

    # Diabetes Status (Yes = Diabetic)
    if diabetes_status:
        risk_factors += 1

    # Hypertension Status (Yes = Hypertension)
    if hypertension_status:
        risk_factors += 1

    # Appetite Changes (Reduced can indicate illness)
    if appetite == "Reduced":
        risk_factors += 1

    # Swelling in Legs or Feet (Yes = Possible kidney issue)
    if swelling:
        risk_factors += 1

    # Anemia (Yes = Anemia)
    if anemia:
        risk_factors += 1

    # Cholesterol (Normal: Less than 200 mg/dL)
    if cholesterol > 200:
        risk_factors += 1

    # Decision Logic for Prediction
    if risk_factors >= 5:
        prediction = "High likelihood of kidney disease. Consult a doctor."
    elif 2 <= risk_factors < 5:
        prediction = "Moderate risk of kidney disease. Consider medical advice."
    else:
        prediction = "Low likelihood of kidney disease."

    # Health Tips based on input
    health_tips = []
    
    if blood_pressure > 140:
        health_tips.append("Monitor your blood pressure regularly. A balanced diet and reducing salt intake can help.")
    if blood_sugar > 125:
        health_tips.append("Maintain a healthy blood sugar level by exercising regularly and avoiding high-sugar foods.")
    if creatinine > 1.2:
        health_tips.append("Keep an eye on your creatinine levels and drink enough water.")
    if hemoglobin < 12.0:
        health_tips.append("Iron-rich foods can help boost your hemoglobin levels.")

    if not health_tips:
        health_tips.append("Maintain a balanced diet and regular check-ups to ensure ongoing kidney health.")

    return prediction, health_tips

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    # Extracting data from the request
    age = int(data.get('age'))
    blood_pressure = float(data.get('bloodPressure'))
    blood_sugar = float(data.get('bloodSugar'))
    creatinine = float(data.get('creatinine'))
    urea = float(data.get('urea'))
    hemoglobin = float(data.get('hemoglobin'))
    wbc = float(data.get('wbc'))
    diabetes_status = data.get('diabetes') == 'yes'
    hypertension_status = data.get('hypertension') == 'yes'
    appetite = data.get('appetite')
    swelling = data.get('swelling') == 'yes'
    anemia = data.get('anemia') == 'yes'
    cholesterol = float(data.get('cholesterol'))

    # Predicting kidney disease risk
    result, health_tips = kidney_disease_prediction(age, blood_pressure, blood_sugar, creatinine, urea, hemoglobin, wbc,
                                                    diabetes_status, hypertension_status, appetite, swelling, anemia, cholesterol)

    # Preparing the response
    response = {
        'name': data.get('name'),
        'email': data.get('email'),
        'phone': data.get('phone'),
        'age': age,
        'sex': data.get('sex'),
        'bloodPressure': blood_pressure,
        'bloodSugar': blood_sugar,
        'creatinine': creatinine,
        'urea': urea,
        'hemoglobin': hemoglobin,
        'wbc': wbc,
        'diabetes': data.get('diabetes'),
        'hypertension': data.get('hypertension'),
        'appetite': appetite,
        'swelling': data.get('swelling'),
        'anemia': data.get('anemia'),
        'cholesterol': cholesterol,
        'result': result,
        'health_tips': health_tips
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
