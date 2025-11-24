print ("Carregando...")
print("Jogo daora carregado.")
print("Após uma longa viajem você sofre um acidente (uma galinha lhê picou) e você está condenado(a) a responder perguntas de matemática (e outros não importantes) por motivos de roteiro, você respondera a seguinte questão:")
import random
print ("(respostas com letras maiusculas, sem ife e sem acento)")
print("Qual o animal mais pesado do planeta?")
resposta1 = input(" 1. Qual a resposta?")
if resposta1 == ("baleia azul"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo.")
print("Qual é o animal mais rápido do planeta?")
resposta2 = input("2. Qual a resposta?")
if resposta2 == ("falcao peregrino"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo.")






a = random.randint (10,100)
b = random.randint (10,100)
print(a, "+", b)
resposta3 = int(input("3. Qual a resposta?"))
if resposta3 == a + b:
    print("Acertou, não fez mais do que era seu dever, com uma pergunta facil dessas eu também conseguiria.")
else:
    print("ERROU KKKKKKK NUMA PERGUNTA FACIL DESSA? KKKKKKKK, a resposta era", a + b)
