import smtplib
import email.message
from flask import Flask, request, jsonify
from configApi import app

def RouteEmail():
    @app.route('/', methods=['POST'])
    def enviar_email():
        # Variaveis do json
        data = request.get_json()
        name = data.get('nameEnterprise')
        emailContato = data.get('emailContato')

        corpo_email = f"""
            Email enviado por {name}.
        """
        msg = email.message.Message()
        msg['Subject'] = f"Contato feito por {name}"
        msg['From'] = 'emailsenderaqui'
        msg['To'] = f'{emailContato}'
        password = 'senhaaqui'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        try:
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            return jsonify({'message': f'Email Enviado com sucesso'}), 200
        except Exception as e:
            return f"Houve um erro {e}", 500
        print('Email enviado')
