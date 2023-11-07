import socket
import sys
SOCK_BUFFER = 1024

def factorial(n):
    x=1
    for i in range(1,(n+1)):
        x=x*i
    return x

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5010)
    print(f"Iniciando servidor en direccion -> {server_address[0]}, puerto -> {server_address[1]}")
    sock.bind(server_address)
    sock.listen(5)
    contador_data=1
    while True:
        conn, client_address = sock.accept()
        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                resultado=factorial(int(data.decode("utf-8")))
                contador_data=contador_data+1
                if contador_data%50==0:
                    print(f"Recibimos {int(data)} y  enviamos {resultado}")
                conn.sendall(str(resultado).encode("utf-8"))
        except Exception as e:
            print(f"Excepcion: {e}")
        finally:
            conn.close()