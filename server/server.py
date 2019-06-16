import socket
import time
import os
import sys

HOST,PORT = '127.0.0.1',8888

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)

print('Serving on port ',PORT)



while True:
    connection,address = my_socket.accept() #aguardando a conexao

    request = connection.recv(150000).decode('utf-8') #aguardando a mensagem


    print('Client request ',request) #request é a mensagem recebida pelo cliente



    try:

        file = open(request,'rb') # open file , r => read , b => byte format
        response = file.read()
        file.seek(0,2)
        lenght = file.tell()
        file.close()
        header = 'HTTP/1.1 200 OK'

        if(request.endswith(".jpg")):
          mimetype = 'image/jpg'
		#Abrir arquivo
          fyle = open(request, 'rb')
          kar = fyle.read(15000)
          connection.send(kar)
        elif(request.endswith(".txt")):
          mimetype = 'text/txt'
		#Abrir arquivo
          fyle = open(request, 'rb')
          kar = fyle.read(15000)
          connection.send(kar)
        elif(request.endswith(".gif")):
          mimetype = 'image/gif'
		#Abrir arquivo
          fyle = open(request, 'rb')
          kar = fyle.read(15000)
          connection.send(kar)
        elif(request.endswith(".html")):
          mimetype = 'text/html'
		#Abrir arquivo
          fyle = open(request, 'rb')
          kar = fyle.read(15000)
          connection.send(kar)

        time = time.strftime("%Y-%m-%d %H:%M:%S")
        header += '\nContent-Type: '+str(mimetype)+'\nDate: '+str(time)+'\nServer: Apache/2(Ubuntu)\nLenght:'+str(lenght)+'\nHeader-Number-Fields: 5\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found'
        response = '404: File not found'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response_error = response
    print(header)
    connection.send(final_response)
    connection.send(final_response_error)
    connection.close()
    sys.exit()

