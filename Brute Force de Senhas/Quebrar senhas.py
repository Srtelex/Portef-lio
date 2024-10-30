import string as st
import secrets
from google.colab import files

def confirmar_criacao_arquivo():
    resposta = input("Você permite a criação do arquivo de senhas? (s/n): ").strip().lower()
    return resposta == 's'

def obter_caminho_arquivo():
    return "senhas.txt"

def escolher_senha_para_adivinhar(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        senhas = arquivo.readlines()
    senha_selecionada = secrets.choice(senhas).strip().split(": ")[1]
    return senha_selecionada

def iniciar_desafio(senha_para_adivinhar):
    tentativas = 3
    while tentativas > 0:
        tentativa = input("Tente adivinhar a senha: ").strip()
        if tentativa == senha_para_adivinhar:
            print("Parabéns! Você adivinhou a senha corretamente!")
            return True
        else:
            tentativas -= 1
            print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
    print("Você usou todas as tentativas.")
    return False

def brute_force(caminho_arquivo, senha_para_adivinhar):
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            senha_arquivo = linha.strip().split(": ")[1]
            print(f"Tentando: {senha_arquivo}")
            if senha_arquivo == senha_para_adivinhar:
                print(f"A senha foi encontrada pelo brute force: {senha_arquivo}")
                return

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algarismos = letras + numeros + especial

quantidade_de_senhas = 200
caminho_arquivo = obter_caminho_arquivo()

if confirmar_criacao_arquivo():
    with open(caminho_arquivo, "w") as arquivo:
        for i in range(quantidade_de_senhas):
            senha = ''.join(secrets.choice(algarismos) for _ in range(12))
            arquivo.write(f"Senha {i + 1}: {senha}\n")

    print(f"{quantidade_de_senhas} senhas geradas e salvas em '{caminho_arquivo}'.")
    files.download(caminho_arquivo)

    senha_para_adivinhar = escolher_senha_para_adivinhar(caminho_arquivo)
    print("Uma senha foi selecionada aleatoriamente para você tentar adivinhar!")
    
    sucesso = iniciar_desafio(senha_para_adivinhar)
    
    if not sucesso:
        print("Iniciando brute force para encontrar a senha...")
        brute_force(caminho_arquivo, senha_para_adivinhar)
else:
    print("A criação do arquivo foi cancelada pelo usuário.")
