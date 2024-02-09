#!/usr/bin/env python3
import os
import time
import json
import requests

Blue_azul = '\33[94m'
Yellow_amarelo = '\33[93m'
neutro = '\33[0m'
Red_vermelho = '\33[91m'

time.sleep(3)
print(Yellow_amarelo, "[+] Carregando...")
time.sleep(6)
print(Blue_azul, "[✔] Concluído !")
time.sleep(3)

os.system("clear")
time.sleep(3)

def banner_main():
    print("______________________________________________________________")
    print("| Olá mundo! meu nome é Wesley, sou um Programador Full Stack|")
    print("| use e tenha controle sobre meus Scripts e seus atos pois eu|")
    print("| não me responsabilizo pelo seus atos. _____________________|")
    print("|_______________________________________|")
    print()
    time.sleep(12)
    os.system("clear")
    
    print("_____________________")
    print("|IP Script em Python|")
    print("|___________________|")
    print()
    
    ip = input(neutro + "Digite um Endereço de IP: ")
    if len(ip) == "":
        print(Red_vermelho, "Não foi possivel achar o Endereço de IP!")
        exit()
    
    r = requests.get(f"https://ipinfo.io/{ip}/json".format(ip))    
        
    ip = r.json()
      
    for ip in r.json():
        print("\nIP HACKEADO ✔")
        print()
        print(Blue_azul, "IP: ", r.json()['ip'])
        print(Yellow_amarelo, "Localização: ", r.json()['loc'])
        print(Blue_azul, "País: ", r.json()['country'])
        print(Yellow_amarelo, "Cidade: ", r.json()['city'])
        print(Blue_azul, "Org: ", r.json()['org'])
        print(Yellow_amarelo, "Timezone: ", r.json()['timezone'])
        print(Blue_azul, "Postal: ", r.json()['postal'])
        print()

        try:
            opção = input(Blue_azul + "Vc deseja limpar a tela (sim ou não)?: ")
            if opção == "Sim" or opção == "sim" or opção == "SIM":
                print(opção, "Okay Então")
                time.sleep(3)
                os.system("clear")
            elif opção == "Não" or opção == "não" or opção == "NÂO":
                print(opção, "Okay Então")
                time.sleep(3)
                exit()
            else:
                print("Digite certo aí okay !")
                exit()
        except 123:
            print(Red_vermelho, "Digite apenas letras por enquanto ")
            exit()
                  
        print(Blue_azul, "Olá mundo, meu nome é Wesley, sou um PROGRAMADOR FULL STACK,")
        print(Blue_azul, "caso queira entrar em contato comigo só ir no GITHUB")
        print(Blue_azul, "e pedir meu instagram")
        print(Blue_azul, "- qualquer problemas nas minhas Ferramentas e Scripts de Programação")
        print(Blue_azul, "Entra em contato comigo que vou te ajuda a resolver qualquer problema!")
        exit()
          
banner_main()