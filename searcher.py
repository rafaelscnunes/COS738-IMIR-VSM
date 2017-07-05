#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Buscador
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Buscador - O objetivo desse módulo é obter os resultados de um conjunto de
#            buscas em um modelo salvo.
# TODO: 1) O Buscador deverá ler o arquivo de consultas e o arquivo do modelo
#          vetorial e realizar cada consulta, escrevendo outro arquivo com a
#          resposta encontrada para cada consulta.

# DONE: 2) Para isso, usará o arquivo de configuração BUSCA.CFG, que possuirá
#          duas instruções
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

# from nltk.corpus import stopwords
# if not stopwords: nltk.download('stopwords')


# os.chdir('/Users/rafaenune/Documents/PESC-EDC/COS738 - Busca e Recuperação '
#          'da Informação/GitHub/')
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s|%(levelname)s|%(name)s|%(funcName)s'
                       '|%(message)s',
                filename=__file__.split('.')[0]+'.log',
                filemode='w')
logger = log.getLogger(__file__.split('/')[-1])


CONFIG_FILE = 'BUSCA.CFG'
SEP = ';'
count = 0


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
    w_ij_documents = pickle.load(pickle_in)
    # print(w_ij_documents)
    # print(len(w_ij_documents))
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
    queries_vsm = vsm.tfn_table(queries)
    queries_vsm = vsm.w_ij(queries_vsm)
    print(queries_vsm)
    # print(len(queries_vsm))
    logger.info('Queries VSM all w_ij for the queries were created.')

    logger.info('Running queries...')
    logger.info('%d queries run!' % count)


    logger.info('Finished %s' % __file__)
else:
    logger.error(CONFIG_FILE + ' not found!')
    print(CONFIG_FILE + ' not found! Execution aborted.')
    logger.error('Execution aborted.')
