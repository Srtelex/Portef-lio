import os
import shutil

def organizar_arquivos(caminho_pasta):
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao_arquivo = nome_arquivo.split('.')[-1]
            pasta_destino = os.path.join(caminho_pasta, extensao_arquivo)
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))

organizar_arquivos('/caminho/para/sua/pasta')
