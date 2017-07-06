UFRJ-COPPE-PESC - Engenharia de Dados e Conhecimento
COS738 - Busca e Recuperação da Informação
Projeto: IMIR-VSM (In Memory Information Retrieval - Vector Space Model)
Autor..: Rafael Nunes - rnunes@cos.ufrj.br
Data...: 2017/07/05

Detalhes de funcionamento:
==========================
1. o log foi implementado de maneira centralizada, com num único arquivo
   registrando o log de todos os módulos. O sistema de log exige que o
   módulo vsm.py seja importa em todo módulo que utilizar o sistema de log e
   cada módulo deve atualizar o objeto logger com seus dados antes de
   registrar informação no log.
2. O modelo tf-idf é armazenado utilizando-se o tipo dictionary do Python.
   Valores nulos (zero) não são armazenados.
   Foi utilizada a função pickle para gravar e ler o modelo da memória para o
   disco e vice-versa.
   
Módulos:
--------
1. vsm.py      - métodos diversos relativos ao VSM preparados para reuso.
2. query.py    - processador de consultas desenvolvido conforme documentação
3. inverted.py - gerador de lista invertida conforme documentação e incluída
                 a geração de um conjunto de documentos para geração futura
                 da tf_idf.
4. indexer.py  - módulo responsável pela criação do modelo vetorial.
5. searcher.py - buscador desenvolvido conforme especificação na documentação.

Arquivos de configuração:
-------------------------
1. LOG.CFG   - informa o nome do arquivo de log a ser utilizado pelo sistema
2. PC.CFG    - configuração do módulo query.py
3. GLI.CFG   - configuração do módulo inverted.py
4. INDEX.CFG - configuração do módulo indexer.py
5. BUSCA.CFG - configuração do módulo searcher.py

Arquivos gerados pelo sistema
-----------------------------
1. consultas.csv      - criado pelo módulo query.py com base nas informações do 
                        arquivo PC.CFG
2. corpora.csv        - criado pelo módulo indexer.py contendo o conjunto de
                        documentos importados dos .xml indicados no arquivo de
                        configuração GLI.CFG
3. esperados.csv      - criado pelo módulo query.py com base nas informações do
                        arquivo PC.CFG
4. inverted_index.csv - índice invertido criado pelo módulo indexer.py
                        conforme informações obtidas no arquivo INDEX.CFG
5. resultados.csv     - criado pelo módulo searcher.py com o resultados das buscas
6. vsm.pickle         - dump de memória com o modelo vetorial dos documentos
7. imir_vsm.log       - arquivo contendo o registro da execução de todos os
                        módulos do sistema IMIR_VSM
O carectere de separação dos campos nos arquivos .csv é sempre ';'

Anexo:
------
1. IMIR-VSM.pdf - enunciado do exercício.
