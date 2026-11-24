# Relatório técnico de consolidação da Tarefa 1B

**Projeto:** TrustSafe-RAG - Artigo 1: risco textual em consultas de saúde mental  
**Versão deste pacote:** correção técnica de 24/11/2026  
**Origem:** ZIP `TrustSafe-RAG-main.zip` fornecido pelo orientador  
**Status:** organização e validação estrutural concluídas; validação clínica e revisão da origem das consultas pendentes.

## 1. Escopo e alterações realizadas

Foi preservado o arquivo inicial de saúde geral `consultas_v01.csv` e mantido **sem alteração de conteúdo** o conjunto v0.2 de saúde mental, com **45 exemplos**, 15 por classe. A versão expandida de **180 registros**, também recebida da aluna, foi disponibilizada no caminho canônico `data/raw/consultas_mental_v04.csv`, com **60 por classe**. A auditoria correspondente de 180 linhas foi colocada em `docs/auditoria_escopo_v06.csv`; os rótulos, textos e estados `PENDENTE` foram preservados.

Os nomes e caminhos incongruentes foram eliminados do fluxo oficial. Agora os três notebooks oficiais são: `gerador_consultas.ipynb`, `01_exploracao_consultas.ipynb` e `02_exploracao_180_com_auditoria.ipynb`. Nenhum exige upload manual por célula ou substitui silenciosamente dados ausentes. Um arquivo fonte mestre específico permite reproduzir de modo determinístico a v0.2, com validação posterior.

## 2. Correspondência e auditoria

Por comparação de **textos exatos e rótulos**, as 45 consultas v0.2 aparecem na base ampliada. **30 receberam um ID diferente** ao serem incorporadas à organização por blocos de risco da base de 180. Foi produzido `correspondencia_ids_v02_v04.csv`, com 45 pares comprovados; a integração por ID isoladamente não é permitida.

A auditoria original de escopo v0.2 foi preservada com 45 linhas. Na auditoria v06 há 180 justificativas preenchidas e **180 registros com revisão humana PENDENTE**. Foi criado um formulário em branco para a revisão humana da v0.2 e da v0.4, sem marcar aprovações inexistentes. A procedência e os grupos de consulta têm identificadores provisórios, todos assinalados como **PENDENTE_REVISAO**; é necessário validar paráfrases antes da partição treino/teste.

## 3. Documentação e gráficos

Foram escritos o **guia de anotação (minuta)** e a discussão de **cinco casos ambíguos**, incluindo quatro exemplos de risco moderado e um limite alto/moderado. As justificativas individualizadas existentes na auditoria de 180 foram transportadas como **propostas de revisão** para os 45 casos correspondentes, sem alterar o CSV oficial ou declarar validação clínica.

O projeto gera três figuras em `figures/v02_45/` e quatro em `figures/v04_180/`, evitando sobreposição de resultados de bases diferentes. Os READMEs conflitantes foram retirados do fluxo principal e preservados apenas em `historico_entrega_original/`; um único README atualizado descreve a execução.

## 4. Testes executados

- CSV oficial v0.2: **45 registros, 45 IDs únicos, 15/15/15, sem textos duplicados nem campos vazios**.
- CSV ampliado v0.4: **180 registros, 180 IDs únicos, 60/60/60, sem textos duplicados nem campos vazios**.
- Auditorias: cobertura de **45** IDs (escopo) e **180** IDs (expansão), sem divergência de texto ou rótulo após junção.
- Linhagem: **45** correspondências textuais, das quais **30** exigem conversão de ID.
- Revisão: **180/180** pendentes, **180/180** grupos provisórios pendentes.
- Automação: **6 testes com pytest passaram**; **3 notebooks executados com nbclient sem células com erro**, em ambiente local.
- Gráficos: **7 imagens** geradas em pastas por versão; relatório JSON com versões do ambiente e hashes oficiais foi gravado em `docs/relatorio_validacao_automatica.json`.

Esses resultados medem a **consistência computacional do repositório** e não demonstram qualidade clínica, desempenho de RAG ou validade dos rótulos.

## 5. Pendências e decisão de aprovação

Faltam: (i) aprovação do guia pelo orientador, idealmente com consultoria profissional na área; (ii) revisão e adjudicação de rótulos/justificativas, com foco em alto risco e casos ambíguos; (iii) verificação da procedência das consultas de 180, identificação de paráfrases e aprovação de `seed_group`; (iv) registro do commit Git publicado. O ZIP fornecido não inclui `.git`; por isso **nenhum hash de commit foi inventado**. Os arquivos originais foram preservados em `historico_entrega_original/`.

**Parecer:** a Tarefa 1B encontra-se **tecnicamente consolidada, mas cientificamente pendente de validação humana**. A expansão para 180 pode ser aproveitada após a revisão; não iniciar treinamento nem reportar desempenho comparativo antes da conclusão das pendências.
