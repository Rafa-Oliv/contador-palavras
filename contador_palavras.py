import string
from collections import defaultdict
from pprint import pprint

class WordCounter:
    def __init__(self):
        self.caracters_ignore = string.digits + string.punctuation
        self.words = defaultdict(int)

    def clean_text(self, text):
    
        #Remove os caracteres indesejados do texto.
        
        for c in self.caracters_ignore:
            text = text.replace(c, ' ')
        return text.lower()

    def count_words(self, text):
        
        #Conta a ocorrência de cada palavra no texto.
        
        self.words.clear()  # Limpa o dicionário para evitar dados antigos
        word_list = text.split()
        for word in word_list:
            self.words[word] += 1

    def get_sorted_words(self):
        
        #Retorna uma lista de palavras ordenadas pela frequência e pelo nome.
        
        return sorted(self.words.items(), key=lambda x: (x[1], x[0]))

    def display_results(self):
        
        #Exibe o total de palavras e as palavras mais frequentes.
        
        total = sum(self.words.values())
        sorted_words = self.get_sorted_words()

        print(f'Total de palavras: {total}\n\nPalavras mais frequentes:\n')
        print(40*'-')

        for word, frequency in sorted_words:
            if frequency >= 2:
                print(f'{word}: {frequency}')
        print(40*'-')

class WordCounterApp:
    def __init__(self):
        self.word_counter = WordCounter()

    def run(self):
        
        #Método principal que controla o fluxo da aplicação.
        
        print('CONTADOR DE PALAVRAS\n')

        while True:
            # Solicita o texto ao usuário
            text = input('Cole seu texto: ')

            # Limpa o texto e conta as palavras
            clean_text = self.word_counter.clean_text(text)
            self.word_counter.count_words(clean_text)

            # Exibe os resultados
            self.word_counter.display_results()

            # Pergunta ao usuário se deseja continuar
            stop = input('Deseja continuar?\nSim(digite "s" e aperte ENTER)\nNão(Pressione ENTER)\n')
            if stop.lower() != 's':
                break

# Executa o aplicativo
if __name__ == '__main__':
    app = WordCounterApp()
    app.run()

    



