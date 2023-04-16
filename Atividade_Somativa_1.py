# Philip Francisco Alves.
# Analise e Desenvolvimento de Sistemas. (11100010563_20231_02)


import json
lista_aluno = []
lista_professores = []
lista_matriculas = []
lista_turmas = []
lista_disciplina = []


# MENU PRINCIPAL -----------------------------------------------------------------------
def menu():
    print('\33[34m\n\n====== MENU PRINCIPAL ======\33[m\n\n'
          '[1] GERENCIAR PROFESSORES.\n'
          '[2] GERENCIAR ESTUDANTES.\n'
          '[3] GERENCIAR TURMAS.\n'
          '[4] GERENCIAR MATRÍCULAS.\n'
          '[5] GERENCIAR DISCIPLINAS.\n'
          '\033[31m[9] ----SAIR----\33[m\n')
    opcao_menu1 = int(input('Selecione a opção desejada: '))
    sub_menu(opcao_menu1)


def carregar_dados_professores():
    try:
        with open('dados_professores.json', 'r') as f:
            lista_professor = json.load(f)
    except FileNotFoundError:
        lista_professor = []

    return lista_professor


def salvar_dados_professores(lista_professor):
    with open('dados_professores.json', 'w') as f:
        json.dump(lista_professor, f)


def incluir_professor():
    print('\n\n===INCLUIR PROFESSOR===\n\n')
    lista_professor = carregar_dados_professores()
    codigo = str(input('Código: '))
    nome = str(input('Nome: ')).upper().strip()
    CPF = str(input('CPF: '))
    # PARA ARMAZENAR OS DADOS DOS PROFESSORES.
    professores = {
        'codigo': codigo,
        'nome': nome,
        'CPF': CPF
    }
    lista_professor.append(professores)
    salvar_dados_professores(lista_professor)


def listar_professor():
    print('\n\n===LISTAR PROFESSORES===\n\n')
    lista_professor = carregar_dados_professores()
    for dic in lista_professor:
        print(
            "* Código: {} - Nome: {} - CPF: {}".format(dic['codigo'], dic['nome'], dic['CPF']))
        print()
    if len(lista_professor) == 0:
        print('Não há professores cadastrados!')


def atualizar_professor():
    print('\n\n===ATUALIZAR PROFESSOR===\n\n')
    lista_professor = carregar_dados_professores()
    codigo = input('Digite o código do professor: ')
    for professor in lista_professor:
        if professor['codigo'] == codigo:
            novo_nome = input('Digite o novo nome do professor: ').upper()
            professor['nome'] = novo_nome
            salvar_dados_professores(lista_professor)
            print(
                f'O nome do professor com código {codigo} foi atualizado para {novo_nome}.')
            break
    else:
        print('O professor não foi encontrado na lista.')


def excluir_professor():
    print('\n\n===EXCLUIR PROFESSOR===\n\n')
    lista_professor = carregar_dados_professores()
    codigo = input('Digite o código do professor que deseja excluir: ')
    for i, professor in enumerate(lista_professor):
        if professor['codigo'] == codigo:
            del lista_professor[i]
            print(f'O professor com código {codigo} foi excluído da lista.')

            salvar_dados_professores(lista_professor)
            break
    else:
        print('O professor não foi encontrado na lista.')


def carregar_dados_alunos():
    try:  # TENTA EXECURTAR O ARQUIVO
        with open('dados.json', 'r') as f:
            lista_aluno = json.load(f)
    except FileNotFoundError:
        lista_aluno = []

    return lista_aluno


def salvar_dados_alunos(lista_aluno):
    # ABRE UM ARQUIVO PARA ESCRITA
    with open('dados.json', 'w') as f:
        json.dump(lista_aluno, f)  # LISTA EM JSON PARA DENTRO DO ARQUIVO


def incluir_aluno():
    print('\n\n===INCLUIR ALUNO===\n\n')
    lista_aluno = carregar_dados_alunos()
    codigo = str(input('codigo: '))
    nome = str(input('Nome: ')).upper().strip()
    CPF = str(input('CPF: '))
#  PARA ARMAZENAR OS DADOS DOS ALUNOS.
    alunos = {
        'codigo': codigo,
        'nome': nome,
        'CPF': CPF
    }
    lista_aluno.append(alunos)
    salvar_dados_alunos(lista_aluno)


def listar_aluno():
    print('\n\n===LISTAR ALUNOS===\n\n')
    lista_aluno = carregar_dados_alunos()
    for dic in lista_aluno:
        print(
            "* Código: {} - Nome: {} - CPF: {}".format(dic['codigo'], dic['nome'], dic['CPF']))
        print()
    if len(lista_aluno) == 0:  # MOSTRA QUANDO NÃO HOUVER ALUNOS LISTADOS
        print('Não há alunos cadastrados!')


def atualizar_aluno():
    print('\n\n===ATUALIZAR===\n\n')
    lista_aluno = carregar_dados_alunos()
    codigo = input('Digite o código do aluno: ')
    for aluno in lista_aluno:
        if aluno['codigo'] == codigo:
            novo_nome = input('Digite o novo nome do aluno: ').upper()
            aluno['nome'] = novo_nome
            salvar_dados_alunos(lista_aluno)
            print(
                f'O nome do aluno com código {codigo} foi atualizado para {novo_nome}.')
            break
    else:
        print('O aluno não foi encontrado na lista.')


def excluir_aluno():
    print('\n\n===EXCLUIR===\n\n')
    lista_aluno = carregar_dados_alunos()
    codigo = input('Digite o código do aluno que deseja excluir: ')
    for i, aluno in enumerate(lista_aluno):
        if aluno['codigo'] == codigo:
            del lista_aluno[i]
            print(f'O aluno com código {codigo} foi excluído da lista.')

            salvar_dados_alunos(lista_aluno)
            break
    else:
        print('O aluno não foi encontrado na lista.')


def carregar_dados_turmas():
    try:
        with open('dados_turmas.json', 'r') as f:
            lista_turmas = json.load(f)
    except FileNotFoundError:
        lista_turmas = []

    return lista_turmas


def salvar_dados_turmas(lista_turmas):
    with open('dados_turmas.json', 'w') as f:
        json.dump(lista_turmas, f)


def incluir_turma():
    print('\n\n=== INCLUIR TURMA ===\n\n')
    lista_turmas = carregar_dados_turmas()
    codigo = input('Código da turma: ')
    disciplina = input('Código da disciplina: ')
    professor = input('Código do professor: ')
    turma = {
        'codigo': codigo,
        'disciplina': disciplina,
        'professor': professor
    }
    lista_turmas.append(turma)
    salvar_dados_turmas(lista_turmas)


def listar_turmas():
    print('\n\n=== LISTAR TURMAS ===\n\n')
    lista_turmas = carregar_dados_turmas()
    for turma in lista_turmas:
        print(
            f"* Código da turma: {turma['codigo']} - Código da disciplina: {turma['disciplina']} - Código do professor: {turma['professor']}\n")
    if len(lista_turmas) == 0:
        print('Não há turmas cadastradas!')


def atualizar_turma():
    print('\n\n=== ATUALIZAR TURMA ===\n\n')
    lista_turmas = carregar_dados_turmas()
    codigo = input('Digite o código da turma: ')
    for turma in lista_turmas:
        if turma['codigo'] == codigo:
            novo_codigo_disciplina = input(
                'Digite o novo código da disciplina: ')
            novo_codigo_professor = input(
                'Digite o novo código do professor: ')
            turma['disciplina'] = novo_codigo_disciplina
            turma['professor'] = novo_codigo_professor
            salvar_dados_turmas(lista_turmas)
            print(f'A turma com código {codigo} foi atualizada.\n')
            break
    else:
        print('A turma não foi encontrada na lista.\n')


def excluir_turma():
    print('\n\n=== EXCLUIR TURMA ===\n\n')
    lista_turmas = carregar_dados_turmas()
    codigo = input('Digite o código da turma que deseja excluir: ')
    for i, turma in enumerate(lista_turmas):
        if turma['codigo'] == codigo:
            del lista_turmas[i]
            salvar_dados_turmas(lista_turmas)
            print(f'A turma com código {codigo} foi excluída da lista.\n')
            break
    else:
        print('A turma não foi encontrada na lista.\n')


def carregar_dados_matriculas():
    try:
        with open('dados_matriculas.json', 'r') as f:
            lista_matriculas = json.load(f)
    except FileNotFoundError:
        lista_matriculas = []

    return lista_matriculas


def salvar_dados_matriculas(lista_matriculas):
    with open('dados_matriculas.json', 'w') as f:
        json.dump(lista_matriculas, f)


def incluir_matricula():
    print('\n\n===INCLUIR MATRÍCULA===\n\n')
    lista_matriculas = carregar_dados_matriculas()
    codigo_turma = int(input('Código da turma: '))
    codigo_estudante = int(input('Código do estudante: '))
    turmas = carregar_dados_turmas()
    alunos = carregar_dados_alunos()

    # Verifica se o código da turma e do estudante existem
    if not any(turma['codigo'] == codigo_turma for turma in turmas):
        print('Turma não encontrada!')
        return
    if not any(aluno['codigo'] == codigo_estudante for aluno in alunos):
        print('Estudante não encontrado!')
        return

    matricula = {
        'codigo_turma': codigo_turma,
        'codigo_estudante': codigo_estudante
    }
    lista_matriculas.append(matricula)
    salvar_dados_matriculas(lista_matriculas)


def listar_matriculas():
    print('\n\n===LISTAR MATRÍCULAS===\n\n')
    lista_matriculas = carregar_dados_matriculas()
    lista_turmas = carregar_dados_turmas()
    lista_alunos = carregar_dados_alunos()

    for matricula in lista_matriculas:
        codigo_turma = matricula['codigo_turma']
        codigo_estudante = matricula['codigo_estudante']
        turma = next(
            (turma for turma in lista_turmas if turma['codigo'] == codigo_turma), None)
        aluno = next(
            (aluno for aluno in lista_alunos if aluno['codigo'] == codigo_estudante), None)

        if turma and aluno:
            print(
                f"* Código da turma: {turma['codigo']} - Disciplina: {turma['disciplina']} - Professor: {turma['professor']}")
            print(
                f"  Código do estudante: {aluno['codigo']} - Nome: {aluno['nome']}")
            print()
        else:
            print('Erro: matrícula inválida!')
            print()

    if len(lista_matriculas) == 0:
        print('Não há matrículas cadastradas!')


def excluir_matricula():
    print('\n\n===EXCLUIR MATRÍCULA===\n\n')
    lista_matriculas = carregar_dados_matriculas()
    codigo_turma = int(input('Código da turma: '))
    codigo_estudante = int(input('Código do estudante: '))

    # Verifica se a matrícula existe
    if not any(matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo_estudante for matricula in lista_matriculas):
        print('Matrícula não encontrada!')
        return


def carregar_dados_disciplinas():
    try:
        with open('disciplinas.json', 'r') as f:
            lista_disciplina = json.load(f)
    except FileNotFoundError:
        lista_disciplina = []

    return lista_disciplina


def salvar_dados_disciplinas(lista_disciplina):
    with open('disciplinas.json', 'w') as f:
        json.dump(lista_disciplina, f)


def incluir_disciplina():
    print('\n\n===INCLUIR DISCIPLINA===\n\n')
    lista_disciplina = carregar_dados_disciplinas()
    codigo = str(input('Código: '))
    nome = str(input('Nome: ')).upper().strip()

    disciplina = {
        'codigo': codigo,
        'nome': nome
    }
    lista_disciplina.append(disciplina)
    salvar_dados_disciplinas(lista_disciplina)


def listar_disciplinas():
    print('\n\n===LISTAR DISCIPLINAS===\n\n')
    lista_disciplina = carregar_dados_disciplinas()
    for dic in lista_disciplina:
        print("* Código: {} - Nome: {}".format(dic['codigo'], dic['nome']))
        print()
    if len(lista_disciplina) == 0:
        print('Não há disciplinas cadastradas!')


def atualizar_disciplina():
    print('\n\n===ATUALIZAR DISCIPLINA===\n\n')
    lista_disciplina = carregar_dados_disciplinas()
    codigo = input('Digite o código da disciplina: ')
    for disciplina in lista_disciplina:
        if disciplina['codigo'] == codigo:
            novo_nome = input('Digite o novo nome da disciplina: ').upper()
            disciplina['nome'] = novo_nome
            salvar_dados_disciplinas(lista_disciplina)
            print(
                f'O nome da disciplina com código {codigo} foi atualizado para {novo_nome}.')
            break
    else:
        print('A disciplina não foi encontrada na lista.')


def excluir_disciplina():
    print('\n\n===EXCLUIR DISCIPLINA===\n\n')
    lista_disciplina = carregar_dados_disciplinas()
    codigo = input('Digite o código da disciplina que deseja excluir: ')
    for i, disciplina in enumerate(lista_disciplina):
        if disciplina['codigo'] == codigo:
            del lista_disciplina[i]
            print(f'A disciplina com código {codigo} foi excluída da lista.')
            salvar_dados_disciplinas(lista_disciplina)
            break
    else:
        print('A disciplina não foi encontrada na lista.')


# SUBMENU -----------------------------------------------------------------------
def sub_menu(opcao_menu1):
    if opcao_menu1 == 1:
        while True:
            print('\33[32m\n\n-----GERENCIAR PROFESSORES-----\33[m\n\n'

                  '[1]. INCLUIR\n'

                  '[2]. LISTAR\n'

                  '[3]. ATUALIZAR\n'

                  '[4]. EXCLUIR\n'

                  '[5]. RETORNAR COM MENU PRINCIPAL\n')

            op_professor = int(input('Qual opção: '))

            if op_professor == 1:
                incluir_professor()

            elif op_professor == 2:
                listar_professor()

            elif op_professor == 3:
                atualizar_professor()

            elif op_professor == 4:
                excluir_professor()

            elif op_professor == 5:
                menu()
            else:
                print('\n\033[31mOPÇÃO INVÁLIDA!\33[m\n')

    elif opcao_menu1 == 2:
        while True:

            print('\33[32m\n\n-----GERENCIAR ESTUDANTES-----\33[m\n\n'

                  '[1]. INCLUIR\n'

                  '[2]. LISTAR\n'

                  '[3]. ATUALIZAR\n'

                  '[4]. EXCLUIR\n'

                  '[5]. RETORNAR AO MENU PRINCIPAL\n')

            op_estudante = int(input('Qual opção: '))

            if op_estudante == 1:
                incluir_aluno()

            elif op_estudante == 2:
                listar_aluno()

            elif op_estudante == 3:
                atualizar_aluno()

            elif op_estudante == 4:
                excluir_aluno()

            elif op_estudante == 5:
                menu()

            else:
                print('\n\033[31mOPÇÃO INVÁLIDA!\33[m\n')

    elif opcao_menu1 == 3:  # EM DESENVOLVIMENTO... FUNCIONALIDADE SERÁ IMPLEMENTADA AO DECORRER DO CURSO

        while True:

            print('\33[32m\n\n----- GERENCIAR TURMAS-----\33[m\n\n'

                  '[1]. Incluir\n'

                  '[2]. Listar\n'

                  '[3]. Atualizar\n'

                  '[4]. Excluir\n'

                  '[5]. Voltar ao menu principal\n')

            op_turma = int(input('Qual opção: '))

            if op_turma == 1:

                incluir_turma()

            elif op_turma == 2:

                listar_turmas()

            elif op_turma == 3:

                atualizar_turma()

            elif op_turma == 4:

                excluir_turma()

            elif op_turma == 5:

                menu()

                break

            else:

                print('\033[31mOPÇÃO INVÁLIDA!\33[m')

    elif opcao_menu1 == 4:  # OPERAÇAÕ PARA MATRÍCULAS

        while True:

            print('\33[32m\n\n----- GERENCIAR MATRÍCULAS-----\33[m\n\n'

                  '[1]. Incluir\n'

                  '[2]. Listar\n'

                  '[3]. Atualizar\n'

                  '[4]. Excluir\n'

                  '[5]. Voltar ao menu principal\n')

            op_matricula = int(input('Qual opção: '))

            if op_matricula == 1:

                incluir_matricula()

            elif op_matricula == 2:

                listar_matriculas()

            elif op_matricula == 3:

                atualizar_matricula()

            elif op_matricula == 4:

                excluir_matricula()

            elif op_matricula == 5:

                menu()

                break

            else:

                print('\033[31mOPÇÃO INVÁLIDA!\33[m')

    elif opcao_menu1 == 5:  # EM DESENVOLVIMENTO... FUNCIONALIDADE SERÁ IMPLEMENTADA AO DECORRER DO CURSO

        while True:

            print('\33[32m\n\n----- GERENCIAR DICISPLINAS-----\33[m\n\n'

                  '[1]. Incluir\n'

                  '[2]. Listar\n'

                  '[3]. Atualizar\n'

                  '[4]. Excluir\n'

                  '[5]. Voltar ao menu principal\n')

            op_disciplina = int(input('Qual opção: '))

            if op_disciplina == 1:

                incluir_disciplina()

            elif op_disciplina == 2:

                listar_disciplinas()

            elif op_disciplina == 3:

                atualizar_disciplina()

            elif op_disciplina == 4:

                excluir_disciplina()

            elif op_disciplina == 5:

                menu()

                break

            else:

                print('\033[31mOPÇÃO INVÁLIDA!\33[m')

    else:  # FINAZALIÇÃO DA OPERAÇÃO OU RETORNO AO MENU PRINCIPAL.

        print('\033[31mOPERAÇÃO FINALIZADA.\33[m')

        R = input('\nDeseja tentar novamente? (S/N) \n').upper()

        if R == 'S':

            menu()

        else:

            print('\033[31mOPERAÇÃO FINALIZADA.\33[m')

            quit()


menu()
