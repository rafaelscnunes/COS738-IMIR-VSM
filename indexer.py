#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Indexador
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Indexador - A função desse módulo é criar o modelo vetorial, dadas as listas
#             invertidas simples.
# DONE: 1) O indexador será configurado por um arquivo INDEX.CFG
# a. O arquivo conterá apenas uma linha LEIA, que terá o formato
#   i. LEIA=<nome de arquivo>
# b. O arquivo conterá apenas uma linha ESCREVA, que terá o formato
#   i. ESCREVA=<nome de arquivo>

# DONE: 2) O Indexador deverá implementar um indexador segundo o Modelo
#          Vetorial [A MAIOR PARTE FOI IMPLEMENTADA NO inverted.py]
# a. O Indexador deverá utilizar o tf/idf padrão
#   i. O tf pode ser normalizado como proposto na equação 2.1 do Cap. 2 do
#      Modern Information Retrieval
# b. O indexador deverá permitir a alteração dessa medida de maneira simples
# c. O Indexador deverá possuir uma estrutura de memória deve de alguma forma
#    representar a matriz termo documento
# d. O Indexador deverá classificar toda uma base transformando as palavras
#    apenas da seguinte forma:
#   i. Apenas palavras de 2 letras ou mais
#  ii. Apenas palavras com apenas letras
# iii. Todas as letras convertidas para os caracteres ASCII de A até Z,
#      ou seja, só letras maiúsculas e nenhum outro símbolo
# e. A base a ser indexada estará na instrução LEIA do arquivo de configuração

# DONE: 3) O sistema deverá salvar toda essa estrutura do Modelo Vetorial para
# utilização posterior

# DONE: 4) Todos os módulos devem possuir um LOG que permita pelo menos a um
# programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e
#    palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.

import os
import logging as log
import math
import pickle

# from nltk.corpus import stopwords
# if not stopwords: nltk.download('stopwords')


os.chdir('/Users/rafaenune/Documents/PESC-EDC/COS738 - Busca e Recuperação '
         'da Informação/GitHub/')
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s|%(levelname)s|%(name)s|%(funcName)s'
                       '|%(message)s',
                filename=__file__.split('.')[0]+'.log',
                filemode='w')
CONFIG_FILE = 'INDEX.CFG'
SEP = ';'
logger = log.getLogger(__file__.split('/')[-1])


logger.info('Started %s' % __file__)
if os.path.isfile(CONFIG_FILE):
    logger.info('Accessing ' + CONFIG_FILE + '...')
    for line in open(CONFIG_FILE, 'r'):
        if line.rstrip('\n').split('=')[0] == 'LEIA':
            f_leia = line.rstrip('\n').split('=')[1]
        elif line.rstrip('\n').split('=')[0] == 'ESCREVA':
            f_escreva = line.rstrip('\n').split('=')[1]
            logger.info('Gracefully stopped reading configuration file ' +
                        CONFIG_FILE + ', ESCREVA parameter found.')
            break
        else:
            logger.error('Invalid parameter found reading configuration. ')
    if f_leia and f_escreva:
        logger.info('All set! Successfully read configuration!')
    else:
        logger.error('Error reading configuration files!')

    logger.info('Creating Vector Space Model...')
    """ Using dense matrix, no zero value stored """

    logger.info('Reading inverted list...')
    inverted_list = {}
    for line in open(f_leia, 'r'):
        if line != 'Word;Documents\n':
            inverted_list[line.rstrip('\n').split(';')[0]] \
            = line.rstrip('\n').split(';')[1].lstrip('[').rstrip(']')\
                .replace(' ', '').split(',')
    logger.info('Inverted list read.')

    logger.info('Building TF...')
    """ Term Frequency table
        The number of times a term appears in a particular document """
    tf = {}
    count = 0
    for word, docs in inverted_list.items():
        count += 1
        qtde = {}
        for doc in docs:
            if doc in qtde:
                qtde[doc] += 1
            else:
                qtde[doc] = 1
        for doc in qtde.keys():
            if word in tf:
                if doc in tf[word]:
                    tf[word][doc] = qtde[doc]
                else:
                    tf[word][doc] = {}
                    tf[word][doc] = qtde[doc]
            else:
                tf[word] = {}
                tf[word][doc] = {}
                tf[word][doc] = qtde[doc]
    # print(tf)
    # print('%d words imported from inverted index.' % count)
    logger.info('TF built with %d words imported from inverted index.' % count)

    logger.info(('Evaluating max_freq of index terms...'))
    """ Evaluate the maximum number of times each one of the terms appears
        across all documents where the given term appears """
    max_freq = {}
    count = 0
    for word, docs in tf.items():
        count += 1
        for doc in docs:
            if word in max_freq:
                if tf[word][doc] > max_freq[word]:
                    max_freq[word] = tf[word][doc]
            else:
                max_freq[word] = tf[word][doc]
    # print(max_freq)
    # print('%d terms had the max_freq evaluated.' % count)
    # print(len(max_freq))
    logger.info('max_freq evaluated for %d words had the max_freq evaluated.'
                % count)

    logger.info(('Normalizing TF...'))
    """ Evaluate a real number between 0 and 1 to represent the relevance of 
        a term in a document """
    tf_norm = {}
    for word, docs in tf.items():
        for doc in docs:
            if word not in tf_norm:
                tf_norm[word] = {}
            if doc not in tf_norm[word]:
                tf_norm[word][doc] = {}
            tf_norm[word][doc] = tf[word][doc]/max_freq[word]
    # print(tf_norm)
    # print(len(tf_norm))
    logger.info('TF normalized for %d terms.' % len(tf_norm))

    logger.info('Evaluating ni_docs...')
    """ ni_docs is the number of documents in which the index term appears """
    ni_docs = {}
    for word in tf:
        ni_docs[word] = len(set(tf[word]))
    # print(ni_docs)
    # print(len(ni_docs))
    logger.info(('Evaluated ni_docs for %d terms' % len(ni_docs)))

    logger.info('Evaluating N_docs...')
    """ N is the total number of documents """
    N_docs = {}
    for word, docs in tf.items():
        for doc in docs:
            if doc not in N_docs:
                N_docs[doc] = tf[word][doc]
            else:
                N_docs[doc] += tf[word][doc]
    N = len(N_docs)
    # print(N_docs)
    # print(N)
    logger.info(('Evaluated N = %d. And also the total number os terms in '
                 'each doc.' % N))

    logger.info('Evaluating idf...')
    idf = {}
    for word in ni_docs:
        idf[word] = math.log10(N/ni_docs[word])
    # print(idf)
    logger.info('Evaluated idf.')

    logger.info('Evaluating w_ij...')
    w_ij = {}
    for word, docs in tf_norm.items():
        for doc in docs:
            if word not in w_ij:
                w_ij[word] = {}
            if doc not in w_ij[word]:
                w_ij[word][doc] = {}
            w_ij[word][doc] = tf_norm[word][doc]*idf[word]
    # print(w_ij)
    # print(len(w_ij))
    logger.info('w_ij evaluated for %d terms.' % len(w_ij))

    logger.info('Saving Vector Space Model...')
    pickle_out = open(f_escreva,'wb')
    pickle.dump(w_ij, pickle_out)
    pickle_out.close()
    logger.info(('VSM saved at %s.' % f_escreva))

    logger.info('Finished %s' % __file__)
else:
    logger.error(CONFIG_FILE + ' not found!')
    print(CONFIG_FILE + ' not found! Execution aborted.')
    logger.error('Execution aborted.')
