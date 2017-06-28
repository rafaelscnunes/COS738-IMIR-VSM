#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Gerador de Lista Invertida
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Gerador de Lista Invertida - A função desse módulo é criar as listas invertidas simples.
# TODO: 1) O Gerador Lista Invertida deverá ler um arquivo de configuração
# a. O nome do arquivo é GLI.CFG
# b. Ele contém dois tipos de instruções
#   i. LEIA=<nome de arquivo>
#  ii. ESCREVA=<nome de arquivo>
# iii. Podem ser uma ou mais instruções LEIA
#  iv. Deve haver uma e apenas uma instrução ESCREVA
#   v. A instrução ESCREVA aparece depois de todas as instruções LEIA

# TODO: 2) O Gerador Lista Invertida deverá ler um conjunto de arquivos em formato XML
# a. Os arquivos a serem lidos serão indicados pela instrução LEIA no arquivo de configuração
# b. O formato é descrito pelo arquivo cfc2.dtd.
# c. O conjunto de arquivos será definido por um arquivo de configuração
# d. Os arquivos a serem lidos são os fornecidos na coleção

# TODO: 3) Só serão usados os campos RECORDNUM, que contém identificador do texto e ABSTRACT, que contém o texto a ser classificado
# a. Atenção: Se o registro não contiver o campo ABSTRACT deverá ser usado o campo EXTRACT

# TODO: 4) O Gerador Lista Invertida deverá gerar um arquivo
# a. O arquivo a ser gerado será indicado na instrução ESCREVA do arquivo de configuração
# b. O arquivo deverá ser no formato cvs
#   i. O caractere de separação será o “;”, ponto e vírgula
# c. Cada linha representará uma palavra
# d. O primeiro campo de cada linha conterá a palavra em letras maiúsculas, sem acento
# e. O segundo campo de cada linha apresentará uma lista (Python) de identificadores de documentos onde a palavra aparece
# f. Se uma palavra aparece mais de uma vez em um documento, o número do documento aparecerá o mesmo número de vezes na lista
# g. Exemplo de uma linha:
#   i. FIBROSIS ; [1,2,2,3,4,5,10,15,21,21,21]

# TODO: 5) Todos os módulos devem possuir um LOG que permita pelo menos a um programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.