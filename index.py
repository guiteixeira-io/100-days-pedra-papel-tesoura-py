import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
opcoes = [pedra, papel, tesoura]
print("Vamos jogar pedra, papel, tesoura?")
print("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura")
escolha_p1 = int(input("Qual você escolhe?\n"))
print(opcoes[escolha_p1])
print("Eu escolho:\n")
escolha_p2 = random.randint(0, 2)
print(opcoes[escolha_p2])

if escolha_p1 == escolha_p2:
    print("Empate!")
elif (escolha_p1 == 0 and escolha_p2 == 2) or \
     (escolha_p1 == 1 and escolha_p2 == 0) or \
     (escolha_p1 == 2 and escolha_p2 == 1):
    print("Você ganhou!")
else:
    print("Você perdeu!")