# TrustSafe-RAG — Tarefa 1

## Descrição

Este projeto apresenta a geração e a exploração de um dataset de consultas para o TrustSafe-RAG.

O dataset oficial possui 45 consultas, distribuídas igualmente entre três níveis de risco:

- 15 consultas de risco baixo
- 15 consultas de risco moderado
- 15 consultas de risco alto

## Estrutura do dataset

O arquivo oficial utilizado na exploração é:

`data/raw/consultas_v01.csv`

As principais colunas são:

- `id`
- `consulta`
- `risco`
- `justificativa`
- `comportamento_esperado`
- `tipo_fonte_desejavel`

## Ordem de execução

### 1. Notebook gerador

Primeiro, executar o notebook responsável pela geração do dataset.

Ele deve criar o arquivo:

`data/raw/consultas_v01.csv`

### 2. Notebook de exploração

Depois, executar o notebook de exploração.

O notebook realiza:

- carregamento do dataset oficial;
- validação dos registros;
- estatísticas descritivas;
- análise das palavras mais frequentes;
- análise gráfica;
- análise de cinco casos ambíguos;
- conclusão dos resultados.

## Validação

O dataset deve apresentar:

- 45 registros;
- 45 IDs únicos;
- nenhuma consulta duplicada;
- nenhum valor nulo;
- 15 consultas de risco baixo;
- 15 consultas de risco moderado;
- 15 consultas de risco alto.

## Figuras

Os gráficos da análise são salvos em:

`figures/graficos_analise_dataset.png`

## Observação

A exploração deve utilizar somente o dataset oficial. Não deve ser utilizado um dataset alternativo ou reduzido para substituir o arquivo oficial.
