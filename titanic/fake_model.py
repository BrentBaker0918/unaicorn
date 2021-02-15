def fake_predict(user_age):
    if user_age < 10:
        prediction = 'survive(under 10)'
    else:
        prediction = 'died like hell(over 10)'
    return prediction
