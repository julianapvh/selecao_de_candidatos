# Função para buscar candidatos
def busca_candidatos(candidatos, minimo_entrevista, minimo_teste_teorico, minimo_teste_pratico, minimo_soft_skills):
    candidatos_encontrados = []
    for candidato in candidatos:
        if (candidato['entrevista'] >= minimo_entrevista
            and candidato['teste teórico'] >= minimo_teste_teorico
            and candidato['teste prático'] >= minimo_teste_pratico
            and candidato['soft skills'] >= minimo_soft_skills):
            candidatos_encontrados.append(candidato['Candidato'])
    return candidatos_encontrados

# Lista de candidatos
candidatos = [
    {'Candidato': 'Pedro', 'entrevista': 5, 'teste teórico': 10, 'teste prático': 8, 'soft skills': 8},
    {'Candidato': 'João', 'entrevista': 10, 'teste teórico': 7, 'teste prático': 7, 'soft skills': 8},
    {'Candidato': 'Maria', 'entrevista': 8, 'teste teórico': 5, 'teste prático': 4, 'soft skills': 9},
    {'Candidato': 'José', 'entrevista': 2, 'teste teórico': 2, 'teste prático': 2, 'soft skills': 1},
    {'Candidato': 'Joaquim', 'entrevista': 10, 'teste teórico': 10, 'teste prático': 8, 'soft skills': 9}
]

while True:
    try:
        # Entrada do usuário - notas mínimas
        minimo_entrevista = int(input("Digite a nota mínima para a entrevista: "))
        minimo_teste_teorico = int(input("Digite a nota mínima para o teste teórico: "))
        minimo_teste_pratico = int(input("Digite a nota mínima para o teste prático: "))
        minimo_soft_skills = int(input("Digite a nota mínima para a avaliação de soft skills: "))
        
        # Busca por candidatos que satisfazem os requisitos
        candidatos_encontrados = busca_candidatos(candidatos, minimo_entrevista, minimo_teste_teorico, minimo_teste_pratico, minimo_soft_skills)
        
        # Exibição dos candidatos encontrados
        if len(candidatos_encontrados) > 0:
            print('Os seguintes candidatos foram encontrados na busca:', candidatos_encontrados)
        else:
            print('Não foi localizado nenhum candidato na busca.')
        
        opcao = input("Deseja realizar outra consulta? (s/n): ")
        if opcao.lower() != 's':
            break
    
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número válido para as notas mínimas.\n")