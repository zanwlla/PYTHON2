#1 10/04 imoport lib os (operational system)
import os


def chamar_nome_do_app():
    print ("Restaurante Expresso\n")
    
def escolher_opcoes():
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")

#2 declarando a função finalizar_app
def finalizar_app():
    os.system('cls')
    print ('Finalizando o app\n')

#8 declarando a função opcao_digitada1
def opcao_digitada1():
    opcao_digitada = (int(input("Escolha uma opção")))
    print ("Você selecionou:",opcao_digitada, "\n")
    if(opcao_digitada==1):
        print("Você escolheu Cadastrar Restayrante\n")
    elif(opcao_digitada==2):
        print("Você escolheu Listar Restaurante\n") 
    elif(opcao_digitada==3):
         print ("Voce escolheu Ativar Restaurante\n")
    #3 chamando a função finalizar_app
    else:
        finalizar_app()     
  
  #5 escrever a funçaõ main
def main():
    #6 chamar o nome do app
    chamar_nome_do_app()
    #7 chamar a escolha de opções
    escolher_opcoes()
    #9 chamar a opção digitada
    opcao_digitada1()

#4 criando a entrada através da variável main
if(__name__=='__main__'):
    main()