#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on Wednesday, june 28th, 2017
@title:  IMIR - In Memory Information Retrieval - Processador de Consultas
@author: Rafael Nunes - rnunes@cos.ufrj.br
"""
# Processador de Consultas - O objetivo desse módulo é transformar o arquivo de consultas fornecido no padrão de palavras que estamos utilizando.
# DONE: 1) O Processador de Consultas deverá ler um arquivo de configuração
# a. O arquivo é criado por vocês
# b. O nome do arquivo é PC.CFG
# c. Ele contém dois tipos de instruções:
#   i. LEIA=<nome de arquivo>
#  ii. CONSULTAS=<nome de arquivo>
# iii. ESPERADOS=<nome de arquivo>
#  iv. As instruções são obrigatórias, aparecem uma única vez e nessa ordem.

# DONE: 2) O Processador de Consultas deverá ler um arquivo em formato XML
# a. O arquivo a ser lido será indicado pela instrução LEIA no arquivo de configuração
#   i. O formato é descrito pelo arquivo “cfcquery-2.dtd”.
#  ii. O arquivo a ser lido é “cfquery.xml”.

# TODO: 3) O Processador de Consultas deverá gerar dois arquivos
# a. Os arquivos deverão ser no formato cvs
#   i. O caractere de separação será o “;”, ponto e vírgula
#       1. Todos os caracteres “;” que aparecerem no arquivo original devem ser eliminados
#  ii. A primeira linha do arquivo cvs deve ser o cabeçalho com o nome dos campos
#
# b. O primeiro arquivo a ser gerado será indicado na instrução CONSULTAS do arquivo de configuração
#   i. Cada linha representará uma consulta
#       1. O primeiro campo de cada linha conterá o número da consulta
#           a. Campo QueryNumber
#       2. O segundo campo de cada linha conterá uma consulta processada em letras maiúsculas, sem acento
#           a. A partir do campo QueryText
#       3. Cada aluno poderá escolher como criar sua consulta
#
# c. O segundo arquivo a ser gerado será indicado na instrução ESPERADOS
#   i. Cada linha representará uma consulta
#       1. O primeiro campo de cada linha conterá o número da consulta
#           a. Campo QueryNumber
#       2. O segundo campo conterá um documento
#           a. Campo DocNumber
#       3. O terceiro campo conterá o número de votos do documento
#           a. Campo DocVotes
#       4. Uma consulta poderá aparecer em várias linhas, pois podem possuir vários documentos como resposta
#       5. As linhas de uma consulta devem ser consecutivas no arquivo
#       6. Essas contas devem ser feitas a partir dos campos Records, Item e do atributo Score de Item
#           a. Considerar qualquer coisa diferente de zero como um voto

# TODO: 4) Todos os módulos devem possuir um LOG que permita pelo menos a um programador posterior, usando o módulo logging de Python:
# 1. Identificar quando iniciaram suas operações
# 2. Identificar quando iniciam cada parte de seu processamento
# a. Ler arquivo de configuração
# b. Ler arquivo de dados
# 3. Identificar quantos dados foram lidos
# 4. Identificar quando terminaram os processamentos
# 5. Calcular os tempos médios de processamento de consultas, documento e palavras, de acordocom o programa sendo usado
# 6. Identificar erros no processamento, caso aconteçam.

import os
import xml.etree.cElementTree as ET


os.chdir('/Users/rafaenune/Documents/PESC-EDC/COS738 - Busca e Recuperação da Informação/GitHub/')


f_config = open('PC.CFG', 'r')
f_leia = './data/' + f_config.readline().split('=')[1][:-1]
f_consultas = './data/' + f_config.readline().split('=')[1][:-1]
f_esperados = './data/' + f_config.readline().split('=')[1][:-1]
f_config.close()


# Parse a xml file (specify the path)
try:
    tree = ET.parse(f_leia)
    root = tree.getroot()
except:
    exit_err("Unable to open and parse input definition file: " + f_leia)


# for child in root:
#     print(child.tag, child.iter('QueryNumber'))

for elem in tree.iter():
    print(elem.tag, elem.attrib, elem.text)

# for elem in tree.iter(tag='QueryNumber'):
#     print(elem.tag, elem.attrib)