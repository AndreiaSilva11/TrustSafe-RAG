# TrustSafe-RAG — Tarefa 1

## Descrição

Este projeto apresenta a validação e a exploração de um conjunto de consultas sintéticas relacionadas à saúde mental para o TrustSafe-RAG.

O dataset oficial v0.2 contém 45 consultas, distribuídas igualmente entre três níveis de risco: 15 de risco baixo, 15 moderado e 15 alto.

As classificações são provisórias e exigem revisão humana. O dataset não deve ser utilizado isoladamente para diagnóstico ou decisões clínicas.

## Estrutura do dataset

Arquivo oficial utilizado na exploração:

`data/raw/consultas_mental_v02.csv`

Principais colunas:
- `id`: identificador da consulta;
- `consulta`: texto da consulta;
- `risco`: nível de risco atribuído;
- `justificativa`: justificativa original da classificação;
- `comportamento_esperado`: comportamento esperado original do sistema;
- `tipo_fonte_desejavel`: tipo de fonte recomendado;
- `revisao_necessaria`: indicação de necessidade de revisão humana.

## Estrutura do projeto

- `data/raw/`: datasets e arquivos de dados;
- `notebooks/`: notebooks de validação e exploração;
- `docs/`: auditoria, guia de anotação, casos ambíguos e arquivos de revisão;
- `figures/`: gráficos da análise;
- `README.md`: documentação do projeto.

## Ordem de execução

### 1. Conferir o dataset oficial

Confirme que `data/raw/consultas_mental_v02.csv` está disponível.

O notebook `notebooks/gerador_consultas_v02.ipynb` carrega e valida o dataset existente; atualmente, não gera novas consultas automaticamente.

### 2. Executar a exploração

Execute `notebooks/01_exploracao_consultas.ipynb`.

O notebook carrega o dataset oficial, realiza validações, calcula estatísticas descritivas e gera os gráficos. O Google Drive deve estar montado no Colab e os arquivos devem estar nos caminhos esperados.

## Validação do dataset oficial

As verificações registradas confirmaram:
- 45 registros;
- 15 consultas por nível de risco;
- 45 identificadores únicos;
- ausência de valores ausentes;
- correspondência dos IDs com o arquivo de auditoria;
- indicação de revisão humana nos 45 registros.

A distribuição equilibrada descreve a composição do dataset, mas não demonstra precisão clínica das classificações.

## Revisão de qualidade

O arquivo `docs/revisao_qualidade_consultas_v02.csv` contém uma cópia de trabalho com propostas individualizadas para justificativas e comportamentos esperados.

Foram verificadas:
- 45 consultas;
- IDs únicos correspondentes ao dataset oficial;
- 15 consultas por nível de risco;
- ausência de campos vazios nas novas colunas;
- preservação das colunas originais da cópia de revisão.

As propostas estão marcadas como pendentes de revisão humana. A validação realizada é estrutural e não comprova a correção clínica das propostas. O dataset oficial não foi alterado por esse procedimento.

## Figuras

Os gráficos da análise exploratória são salvos em `figures/`:
- `figures/distribuicao_classes.png`: distribuição das classes de risco;
- `figures/comprimento_consultas.png`: distribuição do comprimento das consultas;
- `figures/tipos_fontes_desejaveis.png`: distribuição dos tipos de fontes desejáveis.

Os três arquivos foram verificados anteriormente como presentes e não vazios. Recomenda-se regenerá-los executando o notebook completo para confirmar a reprodutibilidade.

## Casos ambíguos

O documento `docs/casos_ambiguos_v02.md` apresenta cinco casos do dataset oficial:
- Q016;
- Q018;
- Q019;
- Q022;
- Q028.

O arquivo `docs/revisao_casos_ambiguos_v03.csv` contém os dados de revisão desses cinco casos. A verificação confirmou que os cinco IDs existem no dataset oficial e que o arquivo contém exatamente os cinco IDs esperados.

Os casos discutem classificações alternativas plausíveis, informações contextuais ausentes, impactos potenciais de erros de classificação e comportamentos esperados. A revisão documental não equivale a validação clínica.

## Limitações

O conjunto de dados é sintético e a análise é descritiva. As classificações de risco são provisórias e requerem revisão humana.

A análise não comprova a precisão de um sistema RAG, não substitui avaliação especializada e não deve ser utilizada isoladamente para orientar diagnósticos ou decisões clínicas.

A reprodutibilidade depende da disponibilidade do dataset oficial, das dependências necessárias e da execução correta dos notebooks.
