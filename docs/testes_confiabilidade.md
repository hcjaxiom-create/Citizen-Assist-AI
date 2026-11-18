
# Testes de Confiabilidade
Projeto: Citizen Assist AI

## Teste 1 - Arquivo JSON ausente
Resultado: APROVADO
O programa identificou a ausência do arquivo,
informou o erro e encerrou com código 1.

## Teste 2 - Arquivo JSON vazio
Resultado: APROVADO
O programa identificou a base vazia,
informou o erro e encerrou com código 1.

## Teste 3 - Registro incompleto
Resultado: APROVADO
O programa identificou campos obrigatórios ausentes,
informou o erro e encerrou com código 1.

## Conclusão
O assistente passou nos três testes realizados.

Os testes utilizaram arquivos temporários,
preservando a base original de 15 orientações.

Esses resultados não garantem a detecção
de todos os tipos possíveis de dados inválidos.


## Teste 4 - Tipo de dado incorreto

Resultado: APROVADO

Foi inserido um número no campo palavras_chave,
que deveria conter uma lista de textos.

O sistema identificou o erro, apresentou
uma mensagem explicativa e encerrou
com código de saída 1.

## Resultado atualizado

Total de testes de confiabilidade: 4
Testes aprovados: 4
Taxa de aprovação: 100%

A avaliação contempla apenas os cenários testados.
