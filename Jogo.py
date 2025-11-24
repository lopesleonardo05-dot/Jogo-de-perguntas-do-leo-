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
    print("errou... Era uma pergunta dificil mesmo, era a baleia azul.")
print("Qual é o animal mais rápido do planeta?")
resposta2 = input("2. Qual a resposta?")
if resposta2 == ("falcao peregrino"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo, era o falcao peregrino.")
a = random.randint (10,100)
b = random.randint (10,100)
print(a, "+", b)
resposta3 = int(input("3. Qual a resposta?"))
if resposta3 == a + b:
    print("Acertou...")
else:
    print("ERROU era", a + b)
    print("Qual é a resposta da questão: 15 + 90 = ?")
resposta4 = input("4. Qual a resposta?")
if resposta4 == ("105"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo, era 105.")
    print("Qual o animal mais forte?")
resposta5 = input("5. Qual a resposta?")
if resposta5 == ("besouro rinocerounte"):
    print("Acertou")
else:
    print("errou... Era uma pergunta dificil mesmo, era o besouro rinocerounte.")
    
