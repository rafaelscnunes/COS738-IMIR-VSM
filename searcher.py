#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created: 2017-07-05
@title:  IMIR-VSM (In Memory Information Retrieval - Vector Space Model)
@module: searcher.py
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Buscador - O objetivo desse módulo é obter os resultados de um conjunto de
#            buscas em um modelo salvo.
# DONE: 1) O Buscador deverá ler o arquivo de consultas e o arquivo do modelo
#          vetorial e realizar cada consulta, escrevendo outro arquivo com a
#          resposta encontrada para cada consulta.

# DONE: 2) Para isso, usará o arquivo de configuração BUSCA.CFG, que possuirá
#          duas instruções
# a. MODELO=<nome de arquivo>
# b. CONSULTAS=<nome de arquivo>
# c. RESULTADOS=<nome de arquivo>

# DONE: 3) A busca deverá ser feita usando modelo vetorial

# DONE: 4) Cada palavra na consulta terá o peso 1

# DONE: 5) O arquivo de resultados deverá
# a. Ser no formato .csv
# b. Separar os campos por “;”, ponto e vírgula
# c. Cada uma de suas linhas terá dois campos:
#   i. O primeiro contendo o identificador da consulta
#  ii. O segundo contendo uma lista Python de ternos ordenados:
#       1. O primeiro elemento é a posição do documento no ranking
#       2. O segundo elemento é o número do documento
#       3. O terceiro elemento é a distância do elemento para a consulta

# DONE: 6) Os alunos devem entregar em um arquivo ZIP com o nome do aluno (
#          formato <nomedoaluno>.zip):
# 1. Todo o código fonte
# 2. Um arquivo README.TXT com qualquer instrução adicional para uso do código entregue
# 3. Um arquivo MODELO.(DOC ou TXT) com a descrição do formato do modelo.
# 4. Todos os arquivos criados por sua execução.
# 5. O arquivo RESULTADOS.cvs

# DONE: 7) Todos os módulos devem possuir um LOG que permita pelo menos
#          a um programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.


import vsm
import os
import re
import logging as log
import math
import pickle
from pprint import pprint
import heapq


logger = log.getLogger(__file__.split('/')[-1])
CONFIG_FILE = 'BUSCA.CFG'
SEP = ';'
MIN_SIM = 0.25


logger.info('Started %s' % __file__)
if os.path.isfile(CONFIG_FILE):
    logger.info('Reading configuration from ' + CONFIG_FILE + '...')
    for line in open(CONFIG_FILE, 'r'):
        if line.rstrip('\n').split('=')[0] == 'MODELO':
            f_vsm = line.rstrip('\n').split('=')[1]
        elif line.rstrip('\n').split('=')[0] == 'CONSULTAS':
            f_consultas = line.rstrip('\n').split('=')[1]
        elif line.rstrip('\n').split('=')[0] == 'RESULTADOS':
            f_resultados = line.rstrip('\n').split('=')[1]
            logger.info('Gracefully stopped reading configuration file ' +
                        CONFIG_FILE + ', RESULTADOS parameter found.')
            break
        else:
            logger.error('Invalid parameter found reading configuration.')
    if f_vsm and f_consultas and f_resultados:
        logger.info('All set! Configuration successfully read!')
    else:
        logger.error('Error reading configuration files!')

    logger.info('Reading Vector Space Model form %s...' % f_vsm)
    pickle_in = open(f_vsm, 'rb')
    w_ij_inverse_index, tf_idf_corpora = pickle.load(pickle_in)
    # print(w_ij_inverse_index)
    # print(tf_idf_corpora)
    # print(w_ij_inverse_index['1236']['WITH'])
    # aux = w_ij_inverse_index['1236']['WITH']
    # if w_ij_inverse_index == tf_idf_corpora:
    #     print('The dictionaries are identical')
    # else:
    #     print('The dictionaries are different!')
    # w_ij_inverse_index['1236']['WITH'] = aux - 0.0000000004
    # print(w_ij_inverse_index['1236']['WITH'])
    # if w_ij_inverse_index == tf_idf_corpora:
    #     print('The dictionaries are identical')
    # else:
    #     print('The dictionaries are different!')
    # w_ij_inverse_index['1236']['WITH'] = aux
    # print(w_ij_inverse_index['1236']['WITH'])
    # if w_ij_inverse_index == tf_idf_corpora:
    #     print('The dictionaries are identical')
    # else:
    #     print('The dictionaries are different!')
    logger.info('Vector Space Model read successfully!')

    logger.info('Reading queries form %s...' % f_consultas)
    queries = {}
    for line in open(f_consultas, 'r'):
        if line != 'QueryNumber;QueryText\n':
            QueryNumber = line.strip('\n').split(SEP)[0]
            QueryText   = line.strip('\n').split(SEP)[1]
            queries[QueryNumber] = QueryText
    # print(queries)
    # print(len(queries))
    logger.info('Queries read successfully!')

    logger.info('Creating vector space model for the queries...')
    tf_idf_queries = vsm.tf_idf(queries, weight1 = 0.5, weight2 = 0.5)
    # print(tf_idf_queries)
    # print(len(tf_idf_queries))
    logger.info('Queries VSM all w_ij for the queries were created.')

    logger.info('Running queries...')
    searchs = {}
    for query in tf_idf_queries:
        for corpus in tf_idf_corpora:
            if query not in searchs:
                searchs[query] = {}
            if corpus not in searchs[query]:
                searchs[query][corpus] = vsm.cos_similarity(
                                         tf_idf_queries[query],
                                         tf_idf_corpora[corpus])
    # print(searchs)

    logger.info('Finding all documents with a cosine similarity to the '
                'corresponding query greater than %f.' % MIN_SIM)
    results = []
    for query, documents in searchs.items():
        for doc in documents:
            if searchs[query][doc] > MIN_SIM:
                results.append([query, doc, searchs[query][doc]])
    logger.info('Queries returned %d documents.' % len(results))

    # qtde_buscas = len(tf_idf_queries)
    # qtde_documentos = len(tf_idf_corpora)
    # limite_de_resultados = qtde_buscas*qtde_documentos
    # qtde_resultados = len(results)
    #
    # print('%d consultas em %d documentos = %d resultados esperados.'
    #       % (qtde_buscas, qtde_documentos, limite_de_resultados))
    # print('O total de resultados encontrados foi %d' % qtde_resultados)
    #
    # if qtde_resultados <= limite_de_resultados:
    #     print('Esse resultado está dentro da quantidade limite esperada!')
    #
    # print(results[0:25])

    logger.info('Ranking results...')
    def getKey1(item):
        return(int(item[0]))
    def getKey2(item):
        return(item[2])
    results = sorted(sorted(results,
                     key = getKey2, reverse = True),
                     key = getKey1, reverse = False)
    logger.info('Ranking finished!')

    # print(results[0:25])

    logger.info('Saving %d results to %s file' % (len(results),f_resultados))
    f_out = open(f_resultados, 'w')
    f_out.write('QueryNumber' + SEP + '[Rank, Document, Similarity]\n')
    rank = 0
    for i in range(0, len(results)-1):
        f_out.write(results[i][0] + SEP +
                    str([rank,int(results[i][1]),results[i][2]]) + '\n')
        if results[i][0] == results[i+1][0]:
            rank += 1
        else:
            rank = 0
    f_out.close()
    logger.info('Queries results successfully saved to %s.' % f_resultados)
    logger.info('Finished %s' % __file__)
else:
    logger.error(CONFIG_FILE + ' not found!')
    print(CONFIG_FILE + ' not found! Execution aborted.')
    logger.error('Execution aborted.')
