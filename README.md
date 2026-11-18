# Citizen Assist AI
## Global Solution FIAP — 2º Semestre de 2026

### 1. Objetivo
Desenvolver um assistente digital que facilite
o acesso a orientações sobre serviços ao cidadão.

### 2. Tecnologias utilizadas
- Python
- Google Colab
- JSON
- CSV

### 3. Base de conhecimento
15 orientações organizadas em três temas:
- Documentos pessoais
- Trabalho e emprego
- Serviços digitais do governo

Cada orientação contém uma fonte de referência.

### 4. Funcionamento
O assistente permite:
- Consultar orientações por tema.
- Digitar perguntas livremente.
- Visualizar respostas e fontes.
- Receber avisos quando não há resposta confiável.

### 5. Algoritmo
A busca utiliza normalização de textos,
comparação de palavras-chave e regras de prioridade.

### 6. Modelos de resposta
Modelo 1: orientação e fonte.
Modelo 2: orientação, fonte e aviso de limitação.

O Modelo 2 foi selecionado por oferecer
mais informações de transparência.

### 7. Testes realizados
Total: 14 perguntas.
Acertos: 14.
Taxa de acerto: 100%.

Tempo médio medido: 0,2002 ms.

Teste de usabilidade:
3 tarefas concluídas por 1 participante.

Os resultados representam apenas os testes realizados.

### 8. Como executar
Na pasta principal do projeto, execute:

python src/sistema.py

### 9. Privacidade e responsabilidade
O sistema não solicita dados pessoais.
Não possui integração com órgãos públicos.
As orientações devem ser confirmadas nas fontes oficiais.

### 10. Limitações e melhorias
- Melhorar a identificação de perguntas ambíguas.
- Ampliar a base de conhecimento.
- Realizar testes com mais usuários.

### 11. Equipe
Nome da equipe: Citizen Assist AI
Integrante: Hugo Camisotti Junior - RM 570978

### 12. Vídeo de apresentação
Link do YouTube: PREENCHER


### Organização e navegação entre assuntos

O sistema utiliza um grafo simples, representado
por um dicionário Python.

Os três temas são:
- Documentos pessoais
- Trabalho e emprego
- Serviços digitais do governo

Cada tema está conectado aos outros dois.

Após consultar uma orientação, o usuário pode
escolher um assunto relacionado e acessar
diretamente suas perguntas.

Essa organização facilita a navegação
e permite ampliar os temas futuramente.


### Exemplos de funcionamento

**Exemplo 1 — Pergunta reconhecida**

Pergunta: Como recuperar minha senha gov.br?

Resultado: O assistente apresenta a orientação
cadastrada para recuperação de senha, acompanhada
da fonte oficial e do aviso de limitação.

**Exemplo 2 — Pergunta fora da base**

Pergunta: Como comprar um carro?

Resultado: O assistente informa que não encontrou
uma orientação confiável e solicita que o usuário
reformule sua pergunta.

**Exemplo 3 — Entrada vazia**

Quando nenhuma pergunta é digitada, o assistente
informa que não encontrou orientação suficiente,
sem inventar uma resposta.
