print('Seja bem vindo !!!')

print('Vamos falar um pouco sobre investimentos !!!')

print('Você sabia que investir no lugar certo e com pessoas comprometidas sua vida financeira pode dar um UP?')

print('Quital fazermos isso de um jeito divertido?....!!')

score = 0 

jogador = input ('Qual seu nome?  ')

print(jogador, 'Vamos jogar!')

print('Investimento é seguro?\n (A) Sim\n (B) Talvez\n (C) Nem um pouco\n (D) Não sei')

resposta = input('Digite uma resposta:  ')
print(resposta)
if resposta == 'A':
    print('Acertou!! Investir é super seguro !!')
    score = score + 10
else:
    print('Errou :( , a resposta é SIIIM!!')
    
print('Tenho pouco dinheiro para investir , faço mesmo assim?\n (A) Nunca\n (B) Claro que não\n (C) Sim !! Hoje é possível investir com pouco\n (D) Talvez')

resposta = input('Digite uma resposta:  ')
print(resposta)
if resposta == 'C':
    print('Parabéns , você acertou , fale com um de nossos especialistas e comece a investir hoje mesmo !!')
    score = score + 10
else:
    print('Incorreto , vamos conversar mais sobre investimento? Fale hojê mesmo com um de nossos especialistas!!')   

print(f'Nosso quizz acabou , espero que tenha gostado ... Pontuação : {score}/20') 




