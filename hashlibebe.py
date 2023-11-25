import hashlib

def cadastrar_senha():
    senha = input("Crie sua senha: ")
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    with open("senha.txt", "w") as f:
        f.write(senha_hash)
    return senha_hash

def testar_senha(senha_hash):
    senha_usuario = input("Digite sua senha para acessar 'Testando sua senha': ")
    if hashlib.sha256(senha_usuario.encode()).hexdigest() == senha_hash:
        print("Senha correta! Acesso permitido.")
    else:
        print("Senha incorreta. Acesso negado.")

if __name__ == "__main__":
    senha_hash = cadastrar_senha()
    testar_senha(senha_hash)
