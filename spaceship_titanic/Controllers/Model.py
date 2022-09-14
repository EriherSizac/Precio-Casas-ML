"""

"""
from spaceship_titanic.Classes.Model import Prediction
from flask import request, jsonify, current_app, render_template
from flask_mail import Mail, Message

def getPrediction():
    json = request.json
    # Utilizar el modelo
    prediction = Prediction(json)
    res = {
        'Transported': bool(prediction.transported)
    }
    return res

def howToSurvive():
    import os
    name = request.json["name"]
    email = request.json["email"]
    with current_app.app_context():
        # Obtenemos el sender email para enviar el correo
        MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
        mail = Mail()
        subject = "Tips to survive"
        recipients = [email]
        sender = ('PSK Insurance', MAIL_USERNAME)
        html = render_template("/tips.html", name=name)
        msg = Message(subject=subject, recipients=recipients, sender=sender, html=html)
        mail.send(msg)
    return {
        "msg": "Mail sent to " + email
    }

def getInfo():
