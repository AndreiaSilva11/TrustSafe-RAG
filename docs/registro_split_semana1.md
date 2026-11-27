# Registro da Divisão de Dados — Semana 1

## Objetivo
Organizar as 180 consultas em conjuntos de treino e teste,
evitando vazamento de dados entre consultas relacionadas.

## Base utilizada
Arquivo: `auditoria_escopo_v06.csv`
Total: 180 consultas.

## Revisão de similaridade
Foram identificados 8 pares candidatos por similaridade textual.
Após revisão humana, 3 pares foram classificados como SIM
e 5 pares como NAO.

Os pares classificados como SIM foram utilizados para manter
consultas relacionadas no mesmo grupo durante a divisão.

## Estratégia de divisão
Foi utilizado o método StratifiedGroupKFold, com:
- 5 divisões (n_splits=5);
- embaralhamento (shuffle=True);
- semente aleatória 42;
- variável de estratificação: risco;
- variável de agrupamento: grupo_split.

## Resultado
- Treino: 146 consultas.
- Teste: 34 consultas.
- Total: 180 consultas.

## Distribuição de risco

### Treino
- Alto: 49.
- Baixo: 49.
- Moderado: 48.

### Teste
- Alto: 11.
- Baixo: 11.
- Moderado: 12.

## Verificação de vazamento
A interseção entre os grupos de treino e teste foi verificada.
Resultado: zero grupos compartilhados.

## Arquivos gerados
- `data/processed/train_semana1.csv`
- `data/processed/test_semana1.csv`
- `data/processed/split_registro_semana1.csv`

## Observação metodológica
A divisão respeitou os grupos definidos pela revisão humana
e buscou manter a distribuição dos níveis de risco equilibrada.

A similaridade textual não representa equivalência clínica,
semântica ou de segurança entre consultas.
