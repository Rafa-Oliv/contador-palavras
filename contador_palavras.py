import string
from collections import defaultdict
from pprint import pprint

# Dicionário para armazenar a contagem de palavras
words = defaultdict(int)

# Caracteres que devem ser ignorados
caracters_ignore = string.digits + string.punctuation

# Solicita o texto ao usuário
text = input('Cole seu texto: ')

# Remove caracteres indesejados do texto
for c in caracters_ignore:
    text = text.replace(c, ' ')

# Transforma todo o texto em minúsculas e separa em palavras
word_list = text.lower().split()

# Conta as palavras
for word in word_list:
    words[word] += 1

sorted_words = sorted(words.items(), key=lambda x: (x[1], x[0]))


total = sum(words.values())

print(f'Total de palavras: {total}\n\nPalavras mais frequentes:\n')

# Exibe as palavras e suas contagens

print(40*'-')
for word, frequency in sorted_words:
    if frequency >= 2:
        print(f'{word}: {frequency}')
print(40*'-')


