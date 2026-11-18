import re
import unicodedata


import json
import os

print("=== CITIZEN ASSIST AI ===")

# Localizar a base de conhecimento
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(
    pasta_atual, "..", "data", "base_conhecimento.json"
)

try:
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        base_conhecimento = json.load(arquivo)

    if not isinstance(base_conhecimento, list) or not base_conhecimento:
        raise ValueError("A base está vazia ou possui formato inválido.")

    campos = {"id", "tema", "pergunta",
              "palavras_chave", "orientacao",
              "fonte", "data_verificacao"}

    for registro in base_conhecimento:
        if not isinstance(registro, dict) or not campos.issubset(registro):
            raise ValueError("Registro com campos obrigatórios ausentes.")

    for registro in base_conhecimento:
        for campo in campos - {"palavras_chave"}:
            if not isinstance(registro[campo], str) or not registro[campo].strip():
                raise ValueError(f"Campo inválido: {campo}")

        palavras = registro["palavras_chave"]

        if (
            not isinstance(palavras, list)
            or not palavras
            or any(not isinstance(p, str) or not p.strip() for p in palavras)
        ):
            raise ValueError("Campo inválido: palavras_chave")

    print("Base carregada com sucesso!")
    print("Total de orientações:", len(base_conhecimento))

except (FileNotFoundError, json.JSONDecodeError, ValueError) as erro:
    print("Erro ao carregar a base:", erro)
    print("O sistema será encerrado por segurança.")
    raise SystemExit(1)



def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Consultar por tema")
    print("2 - Digitar uma pergunta")
    print("0 - Sair")


temas = {
    "1": "Documentos pessoais",
    "2": "Trabalho e emprego",
    "3": "Serviços digitais do governo"
}



assuntos_relacionados = {
    "Documentos pessoais": [
        "Trabalho e emprego",
        "Serviços digitais do governo"
    ],
    "Trabalho e emprego": [
        "Documentos pessoais",
        "Serviços digitais do governo"
    ],
    "Serviços digitais do governo": [
        "Documentos pessoais",
        "Trabalho e emprego"
    ]
}

def mostrar_relacionados(tema):
    print("\nVocê também pode consultar:")

    for assunto in assuntos_relacionados.get(tema, []):
        print("-", assunto)

def escolher_tema(opcao_inicial=None):

    opcao = opcao_inicial if opcao_inicial is not None else input("\nEscolha uma opção: ").strip()

    if opcao == "0":
        print("Obrigado por utilizar o Citizen Assist AI!")
        return

    if opcao not in temas:
        print("Opção inválida.")
        return

    tema_escolhido = temas[opcao]

    registros = [
        r for r in base_conhecimento
        if r["tema"] == tema_escolhido
    ]

    print("\nPerguntas disponíveis:")

    for numero, registro in enumerate(registros, 1):
        print(f"{numero} - {registro['pergunta']}")

    escolha = input("\nEscolha uma pergunta: ").strip()

    if not escolha.isdigit() or not 1 <= int(escolha) <= len(registros):
        print("Opção inválida.")
        return

    registro = registros[int(escolha) - 1]

    print("\nORIENTAÇÃO:")
    print(registro["orientacao"])

    print("\nFONTE:")
    print(registro["fonte"])

    print("\nAviso: confirme as informações no site oficial.")
    mostrar_relacionados(tema_escolhido)

    print("\nDeseja consultar outro assunto?")
    print("1 - Sim")
    print("0 - Voltar ao menu principal")

    continuar = input("Escolha: ").strip()

    if continuar == "1":
        relacionados = assuntos_relacionados.get(tema_escolhido, [])

        for numero, assunto in enumerate(relacionados, 1):
            print(f"{numero} - {assunto}")

        escolha = input("Escolha o assunto relacionado: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(relacionados):
            assunto = relacionados[int(escolha) - 1]
            print("\nAssunto escolhido:", assunto)

            numero_tema = next(
                numero for numero, nome in temas.items()
                if nome == assunto
            )

            escolher_tema(numero_tema)
        else:
            print("Assunto inválido.")

    elif continuar != "0":
        print("Opção inválida. Voltando ao menu principal.")


def normalizar_texto(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

    texto = re.sub(r"[^a-z0-9\s]", " ", texto)

    return " ".join(texto.split())

def buscar_orientacao(pergunta):
    pergunta = normalizar_texto(pergunta)

    if not pergunta:
        return None

    palavras_ignoradas = {
        "como", "meu", "minha", "de", "do", "da",
        "o", "a", "um", "uma", "no", "na",
        "para", "quero", "posso", "consultar"
    }

    palavras_pergunta = set(pergunta.split()) - palavras_ignoradas

    melhor_registro = None
    maior_pontuacao = 0

    for registro in base_conhecimento:
        pontuacao = 0

        for chave in registro["palavras_chave"]:
            palavras_chave = set(
                normalizar_texto(chave).split()
            ) - palavras_ignoradas

            if palavras_chave:
                correspondencias = palavras_pergunta & palavras_chave

                if correspondencias:
                    pontuacao += len(correspondencias) / len(palavras_chave)

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_registro = registro

    return melhor_registro if maior_pontuacao >= 1 else None

busca_anterior = buscar_orientacao

def buscar_orientacao(pergunta):
    texto = normalizar_texto(pergunta)

    if not texto:
        return None


    # Evitar resposta incorreta sobre acesso à conta
    if "nao consigo entrar" in texto:
        return None

    # Priorizar expressões específicas
    prioridades = {
        "DOC002": ["comprovante de inscricao", "segunda via cpf"],
        "DOC003": ["titulo de eleitor"],
        "DOC004": ["solicitar cin", "carteira de identidade"],
        "TRA004": ["abono salarial"]
    }

    for identificador, expressoes in prioridades.items():
        for expressao in expressoes:
            if expressao in texto:
                for registro in base_conhecimento:
                    if registro["id"] == identificador:
                        return registro

    # Usar a busca anterior para os demais casos
    return busca_anterior(pergunta)


def iniciar_assistente():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            print("\nTemas disponíveis:")
            for numero, tema in temas.items():
                print(f"{numero} - {tema}")
            escolher_tema()

        elif opcao == "2":
            pergunta = input("\nDigite sua pergunta: ").strip()
            resultado = buscar_orientacao(pergunta)

            if resultado:
                print("\nORIENTAÇÃO:")
                print(resultado["orientacao"])
                print("\nFONTE:")
                print(resultado["fonte"])
                print("\nAviso: confirme as informações na fonte oficial.")
            else:
                print("\nNão encontrei uma orientação confiável.")
                print("Tente reformular sua pergunta.")

        elif opcao == "0":
            print("\nObrigado por utilizar o Citizen Assist AI!")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    iniciar_assistente()
