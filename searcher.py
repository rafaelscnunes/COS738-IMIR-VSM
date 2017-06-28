#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Buscador
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Buscador - O objetivo desse módulo é obter os resultados de um conjunto de buscas em um modelo salvo.
# TODO: 1) O Buscador deverá ler o arquivo de consultas e o arquivo do modelo vetorial e realizar cada consulta,
#  escrevendo outro arquivo com a resposta encontrada para cada consulta.

# TODO: 2) Para isso, usará o arquivo de configuração BUSCA.CFG, que possuirá duas instruções
# a. MODELO=<nome de arquivo>
# b. CONSULTAS=<nome de arquivo>
# c. RESULTADOS=<nome de arquivo>

# TODO: 3) A busca deverá ser feita usando modelo vetorial

# TODO: 4) Cada palavra na consulta terá o peso 1

# TODO: 5) O arquivo de resultados deverá
# a. Ser no formato .csv
# b. Separar os campos por “;”, ponto e vírgula
# c. Cada uma de suas linhas terá dois campos:
#   i. O primeiro contendo o identificador da consulta
#  ii. O segundo contendo uma lista Python de ternos ordenados:
#       1. O primeiro elemento é a posição do documento no ranking
#       2. O segundo elemento é o número do documento
#       3. O terceiro elemento é a distância do elemento para a consulta

# TODO: 6) Os alunos devem entregar em um arquivo ZIP com o nome do aluno (formato <nomedoaluno>.zip):
# 1. Todo o código fonte
# 2. Um arquivo README.TXT com qualquer instrução adicional para uso do código entregue
# 3. Um arquivo MODELO.(DOC ou TXT) com a descrição do formato do modelo.
# 4. Todos os arquivos criados por sua execução.
# 5. O arquivo RESULTADOS.cvs

# TODO: 7) Todos os módulos devem possuir um LOG que permita pelo menos a um programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.