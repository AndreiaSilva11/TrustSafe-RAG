# Registro de Procedência dos Dados — TrustSafe-RAG

## 1. Identificação
Projeto: TrustSafe-RAG
Etapa: Semana 1 — Auditoria e organização dos dados

## 2. Base utilizada
Arquivo de referência: `auditoria_escopo_v06.csv`
Quantidade de registros: 180 consultas

A base foi utilizada como conjunto de dados de referência para as
atividades iniciais de auditoria, análise de similaridade e revisão humana.

## 3. Organização dos dados
Os registros possuem identificadores de consulta, textos, classificação
de risco, tema e campos relacionados à auditoria e revisão.

## 4. Verificações realizadas
- Verificação dos identificadores dos registros.
- Verificação de duplicidade exata de consultas.
- Conferência da distribuição das classificações de risco.
- Análise de similaridade textual usando TF-IDF e similaridade de cosseno.
- Identificação de pares candidatos para revisão humana.

## 5. Análise de similaridade
Foi utilizado o limiar de similaridade 0.35 para identificar pares
candidatos à revisão.

Foram identificados 8 pares candidatos, posteriormente submetidos
à revisão humana.

## 6. Revisão humana
A revisão dos 8 pares foi registrada no arquivo:

`revisao_seed_groups_2a.csv`

Resultado:
- 3 pares classificados como SIM.
- 5 pares classificados como NAO.

A decisão humana não substitui a avaliação individual do risco ou
a análise contextual das consultas.

## 7. Limitações
A similaridade textual não representa equivalência semântica,
clínica ou de segurança entre consultas.

Os agrupamentos devem ser utilizados com cautela, principalmente
quando envolvem consultas classificadas como alto risco.

## 8. Reprodutibilidade
Os arquivos e registros das atividades foram organizados no
repositório GitHub TrustSafe-RAG para permitir rastreabilidade
das etapas realizadas.

## 9. Informações ainda a confirmar
- Fonte original e método de coleta da base.
- Data e condições de obtenção dos dados.
- Procedimentos de anonimização, quando aplicáveis.
- Licença ou autorização de uso dos dados.
