#importa bibliotecas 
import requests
import json

class Movie:

    #inicia objetos 
    def __init__(self, title, dic ):
        self.title = title
        self.dic = dic  

        req =  requests.get('http://www.omdbapi.com/?apikey=5bca5fcb&t=' + self.title)
        self.dic = json.loads(req.text)
        print(self.dic)
        

    #printa em forma de lista 
    def printDetails(self,dic):
        if self.dic['Response'] == False:
            print('filme nao encontrado')
        else:
            print('Title:', self.dic['Title'])
            print('Year:', self.dic['Year'])
            print('Rated:', self.dic['Rated'])
            print('Released:', self.dic['Released'])
            print('Genre:', self.dic['Genre'])
            print('Poster:', self.dic['Poster'])
            print()          