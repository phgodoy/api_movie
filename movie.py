#importa bibliotecas 
import requests
import json

class Movie:

    #inicia objetos 
    def __init__(self, title, dictionary ):
        self.title = title
        self.dic = dictionary 
        #faz a requisicao na api
        req =  requests.get('http://www.omdbapi.com/?apikey=5bca5fcb&t=' + self.title)
       
        #organiza os dados da requisicao
        self.dictionary = json.loads(req.text)
      
        

    #printa em forma de lista 
    def printDetails(self,dictionary):
        if self.dictionary['Response'] == False:
            print('filme nao encontrado')
        else:
            print('Title:', self.dictionary['Title'])
            print('Year:', self.dictionary['Year'])
            print('Rated:', self.dictionary['Rated'])
            print('Released:', self.dictionary['Released'])
            print('Genre:', self.dictionary['Genre'])
            print('Poster:', self.dictionary['Poster'])
            print()          
