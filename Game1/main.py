#!/usr/bin/env python3

#importando repositórios
import requests
import random
import time
from os import system

#Setando o site para fazer a busca de palavras
url = "https://www.mit.edu/~ecprice/wordlist.10000"

#buscando as informações no site informado
resposta = requests.get(url)

#formando lista com as palavras
palavras = resposta.content.splitlines()

#convertendo as palavras para utf-8
palavras = [palavra.decode("utf-8") for palavra in palavras]

print('Informe a quantidade de palavras que você deseja:')
qtd_palavras = int(input())

#gerar palavras aleatórias para o jogador
random_palavras = random.sample(palavras, qtd_palavras)


print('Digite as palavras a seguir o mais rápido possivel:\n')

pontos = 0

tic = time.perf_counter()

for palavra in random_palavras:
    print(palavra)
    entrada = input()
    if entrada == palavra:
        pontos = pontos + 1
    system('clear')

tac = time.perf_counter()



print('Pontuação: ',pontos)
print('\nTempo gasto: ',tac-tic)