import re
import os
import socket


class PTATCLiente:
        def enviar_requisicao(self, requisicao):
            global x
            global endereco_servidor
            for i in requisicao:
                x.sendto(i.encode(), endereco_servidor) 

        def receber_resposta(self):
            global endereco_cliente
            global x
            resposta = []
            for i in range(7):
                mensagem, endereco_servidor = x.recvfrom(4000000)
                mensagem = mensagem.decode()
                print(mensagem) 
                resposta.append(mensagem)

        def _init_(self):
            self.y = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            endereco_servidor = "localhost", 200
            self.y.bind(endereco_servidor)
            mensagem, endereco_cliente = self.y.recvfrom(1024)
            mensagem = mensagem.decode()
            print(mensagem)
            self.y.sendto("oi".encode(), endereco_cliente)
            lista = []
            for i in range(3):
                mensagem, endereco_cliente = self.y.recvfrom(1024)
                mensagem = mensagem.decode()
                print(mensagem) 
                lista.append(mensagem)   
            for i in lista:
                self.y.sendto(i.encode(), endereco_cliente)

#fazer funcao pede pro usuario comando, e ela pega o comando e retorna requisicao


    
def formatar_msg(msg):
    # Separa a mensagem em partes utilizando o espaço como separador
    msg_separada = re.split(r'[/\s]+', msg)

    # Verifica qual operação deve ser realizada
    if msg_separada[0] == 'read': #adicionar "or del"
        op = '0'
        caminho_remote = msg_separada[1]       
        filename_remote = msg_separada[2]      
        file = open(caminho_remote+"/"+filename_remote, "r")
        body = file.read()  
        length = len(body)
    elif msg_separada[0] == 'write':
        op = '1'
        caminho_local = msg_separada[1]
        filename_local = msg_separada[2]    
        caminho_remote = msg_separada[3]    
        filename_remote = msg_separada[4]       
        file = open(caminho_local+"/"+filename_local, "r")
        body = file.read()                  
        length = len(body)                  
    elif msg_separada[0] == 'del':
        op = '2'
        caminho_local = msg_separada[1]
        filename_remote = msg_separada[2]  
        
    elif msg_separada[0] == 'list':
        op = '3'
        caminho_remoto = msg_separada[1]
    return formatar_lista(op, length, filename_remote, caminho_remote, body)
            
def formatar_lista(op, length, filename, PATH, body):
        requisicao = [
            op,
            f"{length:0>6}",
            filename.ljust(64),
            PATH.ljust(128),
            body
        ]
        return requisicao 
    


def Principal():
    cliente = PTATCLiente()
    while True:
        comando = input("Insira o comando: ")
        requisicao = formatar_msg(comando)
        #cliente.enviar_requisicao(requisicao)
        print("Enviei a requisicao")
        resposta = cliente.receber_resposta()
        print("Enviei a resposta")
        print(resposta)
        
Principal()