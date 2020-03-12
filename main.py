#importa arquivo movie
import movie as mv

#declaracao das variaveis
esc = False
dictionary = False

#menu
while not esc:
    op = input('Escreva o nome de um filme ou exit para fechar: ')
    
    if op == 'exit':
        esc = True
    else:
        movie1 = mv.Movie(op,dictionary)    
        print(movie1.printDetails(op))
