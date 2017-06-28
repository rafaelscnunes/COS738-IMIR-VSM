#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Indexador
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Indexador - A função desse módulo é criar o modelo vetorial, dadas as listas invertidas simples.
# TODO: 1) O indexador será configurado por um arquivo INDEX.CFG
# a. O arquivo conterá apenas uma linha LEIA, que terá o formato
#   i. LEIA=<nome de arquivo>
# b. O arquivo conterá apenas uma linha ESCREVA, que terá o formato
#   i. ESCREVA=<nome de arquivo>

# TODO: 2) O Indexador deverá implementar um indexador segundo o Modelo Vetorial
# a. O Indexador deverá utilizar o tf/idf padrão
#   i. O tf pode ser normalizado como proposto na equação 2.1 do Cap. 2 do Modern Information Retrieval
# b. O indexador deverá permitir a alteração dessa medida de maneira simples
# c. O Indexador deverá possuir uma estrutura de memória deve de alguma forma representar a matriz termo documento
# d. O Indexador deverá classificar toda uma base transformando as palavras apenas da seguinte forma:
#   i. Apenas palavras de 2 letras ou mais
#  ii. Apenas palavras com apenas letras
# iii. Todas as letras convertidas para os caracteres ASCII de A até Z, ou seja, só letras maiúsculas e nenhum outro símbolo
# e. A base a ser indexada estará na instrução LEIA do arquivo de configuração

# TODO: 3) O sistema deverá salvar toda essa estrutura do Modelo Vetorial para utilização posterior

# TODO: 4) Todos os módulos devem possuir um LOG que permita pelo menos a um programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.