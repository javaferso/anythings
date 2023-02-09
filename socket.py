import socket
import time

def improve_connection(host, port, buffer_size = 4096, timeout = 5):
    # Crea un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establece un timeout para evitar bloquearse en caso de una conexión fallida
    s.settimeout(timeout)

    # Conecta al host y puerto especificados
    s.connect((host, port))

    # Envía una solicitud para iniciar la conexión
    s.sendall(b'Start Connection')

    # Recibe la respuesta del servidor
    data = s.recv(buffer_size)

    # Verifica si la respuesta es correcta
    if data == b'Connection established':
        print('La conexión se ha establecido con éxito')
    else:
        print('Error al establecer la conexión')

    # Cierra la conexión
    s.close()

# Llama a la función para mejorar la conexión
improve_connection('www.google.com', 80)
