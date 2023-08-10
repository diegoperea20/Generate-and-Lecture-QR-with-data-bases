import requests
import qrcode

# Ingresa la URL que deseas codificar en el QR
url = 'http://127.0.0.1:5000/qr'

response = requests.get(url)

if response.status_code == 200:
    user_names = response.json()
    for user in user_names:
        print(user)
    
        # Crea un objeto QRCode
        qr = qrcode.QRCode(
            version=1,  # Controla el tamaño del código QR (1 a 40)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
            box_size=10,  # Tamaño de cada "celda" del código QR
            border=4,  # Tamaño del borde
        )

        # Agrega la URL al objeto QRCode
        qr.add_data(user)
        qr.make(fit=True)

        # Crea una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guarda la imagen en un archivo
        img.save(f'{user}.png')

        print("Código QR generado y guardado como 'codigo_qr.png'")

else:
    print('Error:', response.status_code)

