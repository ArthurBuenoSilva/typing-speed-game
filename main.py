import requests
import random
import time

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

response = requests.get(url)
words = response.content.splitlines()

words = [word.decode('utf-8') for word in words]

random_words = random.sample(words, 10)

print('---------------------- COMO JOGAR -----------------------')
print('| Digite a palavra que aparecer o mais rápido que puder |')
print('---------------------------------------------------------\n\n')

input('PRESSIONE <ENTER> PARA INICIAR\n')

score = 0
tic = time.perf_counter()

for word in random_words:
  print(word)
  input_word = input()
  print('')
  
  if input_word == word:
    score += 1

toc = time.perf_counter()

print('Pontuação: ', score)
print('Tempo: ', round(toc - tic, 2), 'segundos')

