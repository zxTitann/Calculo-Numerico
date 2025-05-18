import os

# Configurações básicas do Manim
MANIM_DIR = os.path.dirname(__file__) #definindo o diretório do Manim, o __file__ é o arquivo atual
OUTPUT_DIR = os.path.join(MANIM_DIR, "output") #definindo o diretório de saída, o join é para juntar os diretórios