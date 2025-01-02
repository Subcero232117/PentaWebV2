from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'santosramonsteven@gmail.com'  # Tu correo
app.config['MAIL_PASSWORD'] = 'steven06062323'  # Contraseña de aplicación de Gmail

mail = Mail(app)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.json
        
        # Crear el mensaje de correo
        msg = Message(
            'Nuevo registro de evento Penta Games',
            sender='santosramonsteven@gmail.com',
            recipients=['santosramonsteven@gmail.com']
        )
        
        # Construir el contenido del correo
        msg.body = f"""
        Nuevo registro recibido:
        
        Nametag: {data['nametag']}
        Usuario de Discord: {data['discord']}
        Razón: {data['reason']}
        Dispositivo: {data['device']}
        """
        
        # Enviar el correo
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Registro enviado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
