# **TrustSafe-RAG — Tarefa 2**

## **Descrição**

Este projeto apresenta a validação, a exploração e a análise de um conjunto de consultas sintéticas relacionadas à saúde mental para o TrustSafe-RAG.

Nesta segunda etapa, o conjunto de dados foi ampliado de 45 para **60 consultas**, permitindo aprofundar a análise exploratória e a avaliação da organização das informações utilizadas no processo de auditoria.

O projeto também contempla a análise das classificações de risco, a organização dos registros de auditoria e a identificação de consultas que necessitam de revisão humana.

As classificações são provisórias e exigem revisão humana. O dataset não deve ser utilizado isoladamente para diagnóstico ou decisões clínicas.

## **Estrutura do dataset**

O conjunto de dados utilizado nesta etapa contém 60 consultas.

As informações são organizadas em arquivos CSV, contemplando os registros das consultas e os dados relacionados ao processo de auditoria.

Principais informações analisadas:

* `id_consulta`: identificador da consulta;  
* `consulta`: texto da consulta;  
* `risco`: nível de risco atribuído;  
* `tema`: assunto relacionado à consulta;  
* `pertence_saude_mental`: indicação de relação com saúde mental;  
* `decisao`: decisão atribuída durante a auditoria;  
* `justificativa`: justificativa da classificação;  
* `status_revisao`: situação da revisão humana.

## **Estrutura do projeto**

* `data/raw/`: datasets e arquivos de dados;  
* `notebooks/`: notebooks de validação e exploração;  
* `docs/`: documentação, auditoria e arquivos de revisão;  
* `figures/`: gráficos produzidos durante a análise;  
* `README.md`: documentação do projeto.

## **Ordem de execução**

### **1\. Conferir o dataset**

Verifique se os arquivos CSV utilizados na Tarefa 2 estão disponíveis nos diretórios correspondentes.

Confirme a quantidade de registros, a organização das colunas e a integridade dos dados antes de iniciar a exploração.

### **2\. Executar a exploração**

O notebook principal desta etapa é:

`notebooks/01_exploracao_consultas_180_com_auditoria_v06.ipynb`

O notebook realiza a leitura dos dados, validações, análise exploratória, cálculos estatísticos e geração de gráficos.

A execução deve ser realizada no Google Colab, com o Google Drive montado e os arquivos disponíveis nos caminhos utilizados pelo notebook.

## **Validação do dataset**

Nesta etapa, o conjunto de dados foi ampliado para 60 consultas.

A validação deve contemplar:

* Conferência da quantidade total de registros;  
* Verificação de identificadores únicos;  
* Identificação de valores ausentes;  
* Verificação da distribuição dos níveis de risco;  
* Conferência das colunas utilizadas na auditoria;  
* Verificação dos campos de decisão e status de revisão.

A distribuição das consultas deve ser analisada a partir dos resultados efetivamente encontrados no dataset.

As verificações estruturais não comprovam, isoladamente, a precisão clínica das classificações.

## **Auditoria das consultas**

A auditoria tem como objetivo organizar e acompanhar o processo de avaliação das consultas.

São considerados os campos de risco, tema, justificativa, decisão e situação da revisão.

Os registros pendentes representam consultas que ainda necessitam de avaliação. A classificação automática ou inicial não substitui a revisão humana.

## **Figuras**

Os gráficos produzidos durante a análise exploratória são armazenados no diretório `figures/`.

Entre as visualizações previstas estão:

* comprimento\_consultas (1)  
* comprimento\_consultas  
* distribuicao\_classes&nbsp;  
* distribuicao\_classes  
* graficos\_analise\_dataset  
* tipos\_fontes\_desejaveis (1)  
* tipos\_fontes\_desejaveis

Os gráficos devem ser regenerados por meio da execução do notebook principal, garantindo que representem os dados atualizados desta etapa.

## **Limitações**

O conjunto de dados é sintético e a análise possui caráter exploratório e descritivo.

As classificações de risco são provisórias e necessitam de revisão humana.

A análise não comprova a precisão de um sistema RAG, não substitui avaliação especializada e não deve ser utilizada isoladamente para orientar diagnósticos ou decisões clínicas.

A reprodutibilidade depende da disponibilidade dos arquivos de dados, das dependências necessárias e da execução correta do notebook principal.

&nbsp;