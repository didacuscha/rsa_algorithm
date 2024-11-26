from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode

def generar_par_claves():
    """Genera y guarda un par de claves RSA."""
    try:
        # Generamos un par de claves de 2048 bits
        key = RSA.generate(2048)
        
        # Guardamos la clave privada
        private_key = key.export_key()
        with open("private.pem", "wb") as f:
            f.write(private_key)
        
        # Guardamos la clave pública
        public_key = key.publickey().export_key()
        with open("public.pem", "wb") as f:
            f.write(public_key)
        
        return "Claves generadas correctamente"
    except Exception as e:
        return f"Error al generar las claves: {str(e)}"

def encriptar_mensaje(mensaje, archivo_clave_publica="public.pem"):
    """Encripta un mensaje usando la clave pública."""
    try:
        # Leemos la clave pública
        with open(archivo_clave_publica, "rb") as f:
            public_key = RSA.import_key(f.read())
        
        # Creamos el cipher RSA
        cipher = PKCS1_OAEP.new(public_key)
        
        # Encriptamos el mensaje
        mensaje_encriptado = cipher.encrypt(mensaje.encode())
        
        # Convertimos a base64 para mejor manejo
        return b64encode(mensaje_encriptado).decode()
    except Exception as e:
        return f"Error al encriptar: {str(e)}"

def desencriptar_mensaje(mensaje_encriptado, archivo_clave_privada="private.pem"):
    """Desencripta un mensaje usando la clave privada."""
    try:
        # Leemos la clave privada
        with open(archivo_clave_privada, "rb") as f:
            private_key = RSA.import_key(f.read())
        
        # Creamos el cipher RSA
        cipher = PKCS1_OAEP.new(private_key)
        
        # Desencriptamos el mensaje
        mensaje_bytes = b64decode(mensaje_encriptado)
        mensaje_desencriptado = cipher.decrypt(mensaje_bytes)
        
        return mensaje_desencriptado.decode()
    except Exception as e:
        return f"Error al desencriptar: {str(e)}"