import hashlib

def cadastrar_senha():
    senha = input("Crie sua senha: ")
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    with open("senha.txt", "w") as f:
        f.write(senha_hash)
    return senha_hash

def testar_senha(senha_hash, senha_usuario):
    return hashlib.sha256(senha_usuario.encode()).hexdigest() == senha_hash

if __name__ == "__main__":
    senha_hash = cadastrar_senha()
    senha_usuario = input("Digite sua senha para teste interno: ")
    resultado = testar_senha(senha_hash, senha_usuario)
    if resultado:
        print("Senha correta! Acesso permitido.")
    else:
        print("Senha incorreta. Acesso negado.")
