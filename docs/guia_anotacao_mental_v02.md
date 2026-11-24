# Guia de anotação v0.2 - Risco textual em saúde mental

**Status: MINUTA TÉCNICA PARA REVISÃO DO ORIENTADOR E DE PROFISSIONAL QUALIFICADO EM SAÚDE MENTAL.** Este guia orienta a anotação de **textos sintéticos**, não avalia pessoas nem oferece diagnóstico, prognóstico ou triagem clínica. O nível de risco refere-se apenas aos indícios expressos na consulta. A utilidade científica das categorias ainda precisa de avaliação de consistência interanotadores.

## 1. Unidade de anotação

Anotar uma consulta textual de cada vez. Não presumir história clínica, intenção, idade, confirmação de sintomas ou situação não informada. Registrar a justificativa baseada em elementos observáveis do texto e assinalar incertezas. Campos previstos: `id`, `consulta`, `risco_proposto`, `trecho_sinalizador`, `justificativa`, `revisao_necessaria`, `classe_alternativa`, `informacao_ausente`, `anotador`, `data`, `status_revisao`.

## 2. Classes (proposta operacional)

| Classe | Sinais no texto | Exemplos positivos da v0.2 | Fronteira a discutir |
| --- | --- | --- | --- |
| **Baixo** | Solicitação educativa ou preventiva sem relato de crise, prejuízo ou perigo imediato | Q001 (hábitos de sono), Q003 (manejo cotidiano de estresse), Q010 (limites trabalho-descanso) | Q006 menciona ansiedade em pergunta educativa; Q011 fala de sentimentos sem relatar sofrimento. A presença dessas palavras isoladamente não obriga elevação de risco. |
| **Moderado** | Sofrimento persistente ou prejuízo funcional relatado, sem indício textual explícito de perigo iminente | Q016 (ansiedade afetando sono), Q020 (choro frequente), Q029 (insônia por ansiedade) | Q018 pode descrever hábito comum ou dificuldade clinicamente relevante; Q028 precisa de duração e impacto para contextualizar. |
| **Alto** | Sinais textuais de **possível** ameaça atual à segurança, crise aguda, intenção autolesiva com iminência, ou ameaça grave a terceiros | Q031 (medo de se machucar nas próximas horas), Q032 (ideação e despedidas), Q034 (temor de agredir imediatamente) | Q033 e Q038 indicam insegurança e crise, mas a situação exata não está plenamente descrita: manter orientação de revisão prioritária, sem supor ausência de risco. |

**Não confundir** a classe textual proposta com probabilidade calibrada de dano, diagnóstico ou necessidade clínica efetiva. O conceito de iminência precisa ser definido e validado por especialistas.

## 3. Regras para contexto e linguagem

- **Negação:** distinguir "não penso em me machucar" de "tenho medo de me machucar". Uma negação isolada não descarta outros sinais presentes no texto.
- **Hipóteses e perguntas educativas:** "o que é ideação suicida?" pode ser informativa; não classificar como alto apenas pelo termo. Examinar a pessoa gramatical e o sentido global.
- **Terceira pessoa:** relatos sobre alguém em possível perigo imediato podem requerer classe alta e revisão; não excluir porque o autor não é o paciente.
- **Expressões figuradas:** "estou morrendo de vergonha" não é, por si, indicação literal de morte. Havendo ambiguidade relevante, registrar dúvida.
- **Temporalidade:** "anos atrás" e "hoje/agora" não são equivalentes; verificar se o texto sinaliza urgência atual ou memória passada.
- **Contexto incompleto:** não traduzir silêncio em evidência de segurança. Se houver indícios preocupantes e informação insuficiente, sinalizar `revisao_necessaria=sim` e justificar a abstenção.
- **Palavras-chave não são regras únicas:** ansiedade, pânico, suicídio ou violência isoladamente não determinam automaticamente um nível; interpretação depende do contexto textual.

## 4. Abstenção e revisão humana

A decisão `revisao_necessaria` é **independente** da classe. Definir `sim` quando houver dúvida de classe, menção a possível perigo atual, informação insuficiente, negação/ironia conflitante, referência indireta ou casos de fronteira. Nesta versão conservadora, as 45 consultas oficiais já estão com `revisao_necessaria=sim`. Isso não é prova de que todas são clinicamente problemáticas; indica que nenhuma recebeu revisão registrada.

Na análise futura de erros, falsos negativos da classe alta merecem prioridade, mas a métrica deve ser calculada somente quando houver protocolo de anotação e avaliação aprovado. O sistema de pesquisa não deve produzir orientação individual de emergência a partir deste dataset.

## 5. Protocolo recomendado de anotação

1. Congelar o CSV de trabalho e registrar sua versão e SHA-256.
2. Dois revisores, quando possível, anotam independentemente sem consultar o rótulo original; justificar a decisão com indício textual.
3. Registrar discordâncias e a necessidade de informação adicional, sobretudo moderado/alto.
4. Realizar adjudicação com supervisão qualificada, guardar versões pré e pós-adjudicação e não sobrescrever decisões históricas.
5. Calcular concordância (por exemplo, kappa ponderado) **apenas após haver dois conjuntos reais de anotações independentes**.
6. Documentar regras que foram modificadas por causa das discordâncias; revalidar amostras afetadas.
7. Identificar possíveis paráfrases e registrar `seed_group` confirmado antes de dividir treino/teste.

## 6. Limitações e aprovação

Este documento foi preparado como **minuta operacional** para facilitar a revisão da Tarefa 1B; ainda falta aprovação metodológica pelo orientador e avaliação por profissional de saúde mental, quando disponível. O caráter sintético do dataset, seu equilíbrio artificial e a ausência de pacientes impedem qualquer alegação de validade assistencial.
