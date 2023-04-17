
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
    