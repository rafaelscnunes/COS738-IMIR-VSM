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

import os
import logging as log
import xml.etree.cElementTree as ET

os.chdir('/Users/rafaenune/Documents/PESC-EDC/COS738 - Busca e Recuperação '
         'da Informação/GitHub/')
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s|%(levelname)s|%(name)s|%(funcName)s'
                       '|%(message)s',
                filename=__file__.split('.')[0]+'.log',
                filemode='w')
CONFIG_FILE = 'GLI.CFG'
SEP = ';'
logger = log.getLogger(__file__.split('/')[-1])
papers = []


class paperRecords:
    """ Classe para armazenar os registros lidos do .xml """

    def __init__(self):
        self.PaperNum = ''
        self.Citations = []
        self.RecordNum = 0
        self.MedlineNum = 0
        self.Authors = []
        self.Title = ''
        self.Source = ''
        self.MajorSubJ_Topics = []
        self.MinorSubJ_Topics = []
        self.Abstract = ''
        self.References = []

    def __repr__(self):
        return '{}: {} {} {} {} {} {}' \
               '    {} {} {} {} {}'.format(self.__class__.__name__,
                                           self.PaperNum,
                                           self.Citations,
                                           self.RecordNum,
                                           self.MedlineNum,
                                           self.Authors,
                                           self.Title,
                                           self.Source,
                                           self.MajorSubJ_Topics,
                                           self.MinorSubJ_Topics,
                                           self.Abstract,
                                           self.References)


def computeVotes(votes):
    evaluation = 0
    for i in range(0, len(votes)):
        evaluation = evaluation + int(votes[i])
    return(str(evaluation))


logger.info('Started %s' % __file__)
files = []
if os.path.isfile(CONFIG_FILE):
    logger.info('Acessando ' + CONFIG_FILE + '...')
    for line in open(CONFIG_FILE, 'r'):
        if line.rstrip('\n').split('=')[0] == 'LEIA':
            files.append(line.rstrip('\n').split('=')[1])
        elif line.rstrip('\n').split('=')[0] == 'ESCREVA':
            file_out = line.rstrip('\n').split('=')[1]
            break
        else:
            logger.error('Detectado parâmetro inválido no arquivo de '
                         'configuração')

    if files and file_out:
        logger.info('Parâmetros lidos com sucesso!')
    else:
        logger.error('Falha na carga dos parâmetros de configuração!')

    logger.info('Processando os .xmls...')
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        if root:
            for RECORD in root.findall('RECORD'):
                paper = paperRecords()
                paper.PaperNum = RECORD.find('PAPERNUM').text
                try:
                    for cite in RECORD.find('CITATIONS'):
                        paper.Citations.append(cite.attrib)
                except:
                    logger.warning('O paper número: ' + paper.PaperNum +
                                   ' no arquivo: ' + file + ' não tem'
                                   ' nenhuma citação.')
                    pass
                paper.RecordNum = int(RECORD.find('RECORDNUM').text)
                paper.MedlineNum = int(RECORD.find('MEDLINENUM').text)
                for item in RECORD.find('AUTHORS'):
                    paper.Authors.append(item.text)
                paper.Title = RECORD.find('TITLE').text
                words = paper.Title.split()
                paper.Title = ' '.join(words).upper()
                paper.Source = RECORD.find('SOURCE').text
                for topic in RECORD.find('MAJORSUBJ'):
                    paper.MajorSubJ_Topics.append(topic.text)
                for topic in RECORD.find('MINORSUBJ'):
                    paper.MinorSubJ_Topics.append((topic.text))
                try:
                    paper.Abstract = RECORD.find('ABSTRACT').text
                except:
                    logger.warning('O paper número: ' + paper.PaperNum +
                                   ' no arquivo: ' + file + ' não tem'
                                   ' ABSTRACT.')
                    pass
                try:
                    paper.Abstract = RECORD.find('EXTRACT').text
                except:
                    logger.info('O paper número: ' + paper.PaperNum +
                                   ' no arquivo: ' + file + ' não tem'
                                   ' EXTRACT.')
                    pass
                words = paper.Abstract.split()
                paper.Abstract = ' '.join(words).upper()
                try:
                    for cite in RECORD.find('REFERENCES'):
                        paper.References.append(cite.attrib)
                except:
                    pass
                papers.append(paper)
                print(papers[len(papers)-1])
            logger.info('O processamento leu ' + str(len(papers)) +
                        ' papers no arquivo ' + file)
        else:
            logger.error('Houve falha no processamento do arquivo ' + file)

    # logger.info('Exportando todas as queries para .csv')
    # f_out = open(f_consultas, 'w', encoding = 'utf-8')
    # f_out.write('QueryNumber' + SEP + 'QueryText\n')
    # count = 0
    # for i in range(0, len(queries)):
    #     f_out.write(str(queries[i].Number) + SEP + queries[i].Text + '\n')
    #     count += 1
    # logger.info('Foram exportados ' + str(count) + ' registros para ' +
    #             f_consultas)
    #
    # logger.info('Exportando os votos de cada documento para .csv')
    # f_out = open(f_esperados, 'w', encoding = 'utf-8')
    # f_out.write('QueryNumber' + SEP + 'DocNumber' + SEP + 'DocVotes\n')
    # count = 0
    # for i in range(0, len(queries)):
    #     for docs, votes in queries[i].Records.items():
    #         f_out.write(str(queries[i].Number) + SEP + docs + SEP +
    #                     computeVotes(votes) + '\n')
    #         count += 1
    # logger.info('Foram exportados ' + str(count) + ' registros para ' +
    #             f_esperados)
else:
    logger.error('O arquivo ' + CONFIG_FILE + ' não foi localizado!')
    print('O arquivo ' + CONFIG_FILE + ' não foi localizado. Execução '
                                       'abortada!')
logger.info('Finished %s' % __file__)