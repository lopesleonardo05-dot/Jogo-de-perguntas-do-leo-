print ("Carregando...")
print("Jogo daora carregado.")
print("Após uma longa viajem você sofre um acidente (uma galinha lhê picou) e você está condenado(a) a responder perguntas de matemática (e outros não importantes) por motivos de roteiro, você respondera a seguinte questão:")
import random

print("Qual o animal mais pesado do planeta?")
resposta1 = input("Qual a resposta?")
if resposta1 == ("baleia azul"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo.")
a = random.randint (10,100)
b = random.randint (10,100)
print(a, "+", b)
resposta2 = int(input("Qual a resposta?"))
if resposta2 == a + b:
    print("Acertou, não fez mais do que era seu dever, com uma pergunta facil dessas eu também conseguiria.")
else:
    print("ERROU KKKKKKK NUMA PERGUNTA FACIL DESSA? KKKKKKKK, a resposta era", a + b)
