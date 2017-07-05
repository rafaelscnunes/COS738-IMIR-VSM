#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on 04/Jul/2017 with PyCharm Community Edition
@title:  IMIR - vsm
@author: rafaenune - Rafael Nunes - rnunes@cos.ufrj.br

"""
import vsm
from pprint import pprint
import logging as log


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s|%(levelname)s|%(name)s|%(funcName)s'
                       '|%(message)s',
                filename=__file__.split('.')[0]+'.log',
                filemode='w')
logger = log.getLogger(__file__.split('/')[-1])


SEP = ';'

corpora = vsm.get_corpora('../consultas.csv', SEP)
vsm_corpora_dense = vsm.tf_idf(corpora, mode = 'dense')
vsm_corpora_sparse = vsm.tf_idf(corpora, mode = 'sparse')
