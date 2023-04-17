import re
import os

#fazer funcao pede pro usuario comando, e ela pega o comando e retorna requisicao

def testando():
    x = input("Insira o comando:")
    print(formatar_msg(x))
    
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
    
def fileReader(PATH, fileName):
    
    if os.path.exists(PATH):
        if os.path.exists(PATH+"/"+fileName):
            file = open(PATH+"/"+fileName, "r")
            body = file.read()
            print(body)
            lenght = len(body)
            if lenght < 999999:
                CODE = 0
                message = "Arquivo lido com sucesso"
            else:
                CODE = 3
                messaage = "Tamanho do arquivo para ser escrito maior que tamanho máximo permitido"
        else:
            message = "Nome de arquivo não existente no servidor"
            CODE = 2
    else:
        message = "Caminho não existente no servidor"
        CODE = 1

testando()