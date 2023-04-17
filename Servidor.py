import os
import socket

class PTATServidor:
     def __init__(self):
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
            
     def receber_requisicao():
          requisicao = []
          for i in range(7):
               mensagem, endereco_cliente = y.recvfrom(4000000)
               mensagem = mensagem.decode()
               print(mensagem) 
               requisicao.append(mensagem)
        
     def enviar_resposta(resposta):
          global y
          global endereco_cliente
          for i in resposta:
               y.sendto(i.encode(), endereco_cliente)
               
               

def formatar_lista(op, length, filename, PATH, code, message, body):
    requisicao = [
         op,
        f"{length:0>6}",
         filename.ljust(64),
         PATH.ljust(128),
         str(code),
         message.ljust(128),
         body
    ]
    return requisicao

def fileReader(PATH, fileName):
    if os.path.exists(PATH):
        if os.path.exists(PATH+"/"+fileName):
            file = open(PATH+"/"+fileName, "r")
            BODY = file.read()
            print(BODY)
            lenght = len(BODY)
            if lenght < 999999:
                CODE = 0
                message = "Arquivo lido com sucesso"
            else:
                CODE = 3
                message = "Tamanho do arquivo para ser escrito maior que tamanho máximo permitido"
            file.close()
        else:
            message = "Nome de arquivo não existente no servidor"
            CODE = 2    
    else:
        message = "Caminho não existente no servidor"
        CODE = 1
    return formatar_lista("r", lenght, fileName, PATH, CODE, message, BODY)

def fileList(PATH):
    if os.path.exists(PATH):
        if not os.listdir(PATH):
            print("Não há arquivos neste diretório")
        else:
            for arquivo in os.listdir(PATH):
                print(arquivo)
            BODY = str(os.listdir(PATH))
            length = len(BODY)
            if length < 999999:
                CODE = 0
                message = "Arquivo lido com sucesso"
            else: 
                CODE = 3
                message = "Arquivos demais para serem listados."
    else:
        message = "Caminho não existente no servidor"
        CODE = 1
    return formatar_lista("l", length, "", PATH, CODE, message, BODY)

def fileDelet(PATH, fileName):
    if os.path.exists(PATH):
        if os.path.exists(PATH+"/"+fileName):
            os.remove(PATH+"/"+fileName)
            CODE = 0
            message = "Arquivo deletado com sucesso!"
        else:
            message = "Nome de arquivo não existente no servidor"
            CODE = 2   
    else:
        message = "Caminho não existente no servidor."
        CODE = 1
    return formatar_lista("d", 0, fileName, PATH, CODE, message, "")

def fileWrite(PATH, fileName, BODY):
    if os.path.exists(PATH):
        if os.path.exists(PATH+"/"+fileName):
            message = "Nome de arquivo já existente no servidor."
            CODE = 5 #Caso especial, arquivo já existente.
        else:
            with open("arquivo.txt", "w") as file:
                file.write(BODY)
            CODE = 0
            message = "Arquivo escrito com sucesso."   
    else:
        message = "Caminho não existente no servidor."
        CODE = 1
    
    

