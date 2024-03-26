def main():
    alunos = []  # Lista para armazenar as médias dos alunos
    alunos_aprovados = 0  # Contador de alunos aprovados
    alunos_reprovados = 0  # Contador de alunos reprovados

    while True:  # Loop para entrada contínua de dados do aluno
        nomealuno = input("Digite o nome do Aluno: ")  # Solicita o nome do aluno
        nota1 = float(input("Digite a sua 1ª nota: "))  # Solicita a primeira nota do aluno
        nota2 = float(input("Digite a sua 2ª nota: "))  # Solicita a segunda nota do aluno
        nota3 = float(input("Digite a sua 3ª nota: "))  # Solicita a terceira nota do aluno
        tipom = str(input("Digite o tipo da sua média (A para média aritmética, P para média ponderada): "))  # Solicita o tipo de média

        if tipom == "A":  # Verifica se é escolhida a média aritmética
            media = calcular_media_aritmetica(nota1, nota2, nota3)  # Calcula a média aritmética
            print(f"A média aritmética é: {media}")  # Exibe a média aritmética calculada
        elif tipom == "P":  # Verifica se é escolhida a média ponderada
            media = calcular_media_ponderada(nota1, nota2, nota3)  # Calcula a média ponderada
            print(f"A média ponderada é: {media}")  # Exibe a média ponderada calculada
        else:
            resultado = "Tipo de média inválido. Use 'A' para média aritmética ou 'P' para média ponderada."
            print(f"O resultado da média é: {resultado}")  # Exibe mensagem de tipo de média inválido
            continue  # Retorna ao início do loop

        if media >= 6:  # Verifica se a média é maior ou igual a 6
            print(f"Parabéns {nomealuno}! Você está aprovado.")  # Exibe mensagem de aprovação
            alunos_aprovados += 1  # Incrementa o contador de alunos aprovados
        else:
            print(f"Infelizmente {nomealuno}, você está reprovado.")  # Exibe mensagem de reprovação
            alunos_reprovados += 1  # Incrementa o contador de alunos reprovados

        alunos.append(media)  # Adiciona a média do aluno à lista de médias
        continua = input("Deseja cadastrar outro aluno? (S/N): ")  # Pergunta se deseja cadastrar outro aluno
        if continua.upper() != 'S':  # Verifica se a resposta não é 'S'
            break  # Encerra o loop se a resposta for diferente de 'S'

    if alunos:  # Verifica se a lista de alunos não está vazia
        media_geral = sum(alunos) / len(alunos)  # Calcula a média geral dos alunos
        print(f"A média geral dos alunos cadastrados é: {media_geral}")  # Exibe a média geral dos alunos

    print(f"Total de alunos aprovados: {alunos_aprovados}")  # Exibe o total de alunos aprovados
    print(f"Total de alunos reprovados: {alunos_reprovados}")  # Exibe o total de alunos reprovados

def calcular_media_aritmetica(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3  # Calcula a média aritmética das notas

def calcular_media_ponderada(nota1, nota2, nota3):
    pesos = [2, 3, 5]  # Pesos para a média ponderada
    return (nota1 * pesos[0] + nota2 * pesos[1] + nota3 * pesos[2]) / sum(pesos)  # Calcula a média ponderada com os pesos            

main()  # Chama a função principal para iniciar o programa
