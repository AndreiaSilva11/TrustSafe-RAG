# Registro de atividades – Semana 1

## Projeto
TrustSafe-RAG

## Objetivo da etapa
Realizar a auditoria exploratória do conjunto de consultas, verificar sua estrutura, investigar similaridades textuais e preparar os registros candidatos para revisão humana.

## Atividades realizadas

- Análise estrutural do conjunto de dados.
- Verificação da quantidade de registros, identificadores, classes de risco, temas, decisões e status de revisão.
- Investigação exploratória de similaridade textual utilizando TF-IDF e similaridade de cosseno.
- Identificação de pares candidatos para revisão humana.
- Exportação da tabela de pares candidatos.
- Verificação inicial dos campos relacionados à procedência.
- Organização do notebook de auditoria.
- Implementação de testes automatizados iniciais.

## Resultados da auditoria

- 180 registros analisados.
- 60 registros de risco baixo.
- 60 registros de risco moderado.
- 60 registros de risco alto.
- 8 pares candidatos identificados para revisão humana.
- Nenhuma duplicidade exata de identificadores ou consultas foi identificada.

## Testes automatizados

Foi implementado um teste automatizado utilizando pytest para verificar:

- Quantidade de registros.
- Unicidade dos identificadores.
- Distribuição dos níveis de risco.
- Consistência das decisões de inclusão.

Resultado da execução inicial: 1 teste aprovado.

## Arquivos relacionados

- notebooks/03_auditoria_procedencia.ipynb
- tests/test_semana1.py
- docs/auditoria_escopo_v06.csv
- docs/revisao_seed_groups_2a.csv

## Pendências

- Realizar revisão humana dos pares candidatos.
- Confirmar agrupamentos de consultas semelhantes.
- Documentar a procedência individual quando informações adicionais estiverem disponíveis.
- Preparar o split dos dados considerando os grupos confirmados.
- Ampliar os testes automatizados nas próximas etapas.

## Limitações

A análise de similaridade é exploratória e não confirma duplicidade sem revisão humana. A verificação de procedência também depende da disponibilidade de informações de origem e rastreabilidade dos registros.
