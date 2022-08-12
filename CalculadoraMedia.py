print('Calculadora de aprovados e reprovados UVV')
index = 0
alunos = 50
aprovado = 0
reprovado = 0
while index < alunos:
    while True:
        aop1 = float(input(f'\nDigite a nota[0, 1] da aop1 do aluno {index + 1}:'))
        if aop1 < 0.0 or aop1 > 1.0:
            print('Erro na digitação da nota da aop1, digite novamente:')
        else:
            break
    while True:
        aop2 = float(input(f'\nDigite a nota[0, 2] da aop2 do aluno {index + 1}:'))
        if aop2 < 0.0 or aop2 > 2.0:
            print('Erro na digitação da nota da aop2, digite novamente:')
        else:
            break
    while True:
        aop3 = float(input(f'\nDigite a nota[0, 1] da aop3 do aluno {index + 1}:'))
        if aop3 < 0.0 or aop3 > 1.0:
            print('Erro na digitação da nota da aop3, digite novamente:')
        else:
            break
    while True:
        prov_reg = float(input(f'\nDigite a nota[0, 6] da prova regular do aluno {index + 1}:'))
        if prov_reg < 0.0 or prov_reg > 6.0:
            print('Erro na digitação da nota da prova regular, digite novamente:')
        else:
            break
    soma = aop1 + aop2 + aop3 + prov_reg
    if soma >= 7.0:
        print('\nMédia do módulo {}, aluno {} aprovado.'.format(soma,index + 1))
        aprovado += 1
    else:
        while True:
            prov_recup = float(input(f'\nDigite a nota da prova de recuperação do aluno {index + 1}:'))
            if prov_recup < 0 or prov_recup > 10:
                print('Erro da digitação da nota da prova de recuperação. Digite novamente:')
            elif (soma + prov_recup) / 2 < 5:
                print('\nMédia do módulo {}, média após recuperação {}, aluno {} reprovado.'.format(soma,(soma + prov_recup) / 2,index + 1))
                reprovado += 1
                break
            else:
                print('\nMédia do módulo {}, média após recuperação {}, aluno {} aprovado.'.format(soma,(soma + prov_recup) / 2,index + 1))
                aprovado += 1
                break
    index +=1
print(f'\nPorcentagem dos aprovados {aprovado / (aprovado + reprovado) * 100: .1f}%.')
print(f'Porcentagem dos reprovados {reprovado / (aprovado + reprovado) * 100: .1f}%.')
