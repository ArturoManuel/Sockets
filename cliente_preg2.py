import socket
import time
import sys
import statistics
import numpy as np
SOCK_BUFFER = 1024

def numero_aleatorio():
    data_list = np.random.randint(10,30,size=10)
    data_list = data_list.tolist()
    return data_list

def factorial_local(n):
    x=1
    for i in range(1,(n+1)):
        x= x*i
    return x
    
def factorial_remoto(n):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 5010)
    sock.connect(server_address)
    try:
        sock.sendall(str(n).encode("utf-8"))
        data = sock.recv(SOCK_BUFFER) 
    except KeyboardInterrupt:
        print("Usuario cerró abruptamente el programa")
        sock.close()
    except Exception as e:
        print(f"Exepción: {e}")
    finally:
        sock.close()
    return int(data.decode('utf-8'))

if __name__ == "__main__":
    lista = numero_aleatorio()
    remoto = []
    local = []
    #Remota
    for n in lista:
        for i in range(50):
            inicio= time.perf_counter()
            resultado=factorial_remoto(n)
            fin = time.perf_counter()
            remoto.append(fin-inicio)
        print(f"Resultado remoto de {n} es {resultado}")

    #Local
    for k in lista:
        for i in range(50):
            inicio = time.perf_counter()
            resultado2 = factorial_local(k)
            fin = time.perf_counter()
            local.append(fin-inicio)
        print(f"Resultado local de {k} es {resultado2} ")
    
    #Mediana de la ejecución remota:
    mediana_remoto = statistics.mean(remoto)
    print("La mediana de la remota es",round((mediana_remoto*1000000),2),"us")

    #Mediana de la ejecución local:
    mediana_local = statistics.mean(local)
    print("La mediana de la  local es",round((mediana_local*1000000),2),"us")
    #La salida es la resta de la remota menos la local
    salida= mediana_remoto-mediana_local
    print("El tiempo de entrada-salida es",round((salida*1000000),2),"us")