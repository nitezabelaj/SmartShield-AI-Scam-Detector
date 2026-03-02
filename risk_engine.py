def calculate_risk(probability):
    risk_score = int(probability * 100)

    if risk_score < 40:
        classification = "Safe"
    elif risk_score < 70:
        classification = "Suspicious"
    else:
        classification = "High Risk"

    return risk_score, classification