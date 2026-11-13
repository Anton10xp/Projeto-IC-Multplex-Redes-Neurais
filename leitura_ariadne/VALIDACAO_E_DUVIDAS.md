# Conferência da leitura e dúvidas técnicas

Fonte: Dissertacao_Corrigida.pdf, de Ariadne de Andrade Costa. As páginas citadas são as impressas; para localizar no PDF, some 21 às páginas do corpo principal e do apêndice.

## O que foi conferido

Foram extraídas 115 páginas, sem páginas de texto vazias, totalizando 197.009 caracteres na extração. A leitura cobriu os elementos iniciais, os cinco capítulos, as 98 entradas da bibliografia e o Apêndice A. Foram examinadas visualmente as páginas com as 29 figuras. A folha de rosto foi conferida: mestrado, USP, 2011, orientação de Osame Kinouchi Filho.

As referências de página do guia foram confrontadas com os títulos, legendas e texto. Foram recalculados o exemplo de atualização sináptica e valores da Eq. 3.16. O balanço da Eq. 3.9 foi comparado à derivação do Apêndice A. Os parâmetros e a interpretação do MUX foram confrontados com codigo_final_mux.py e biblioteca_GLmodel.py.

A extração de texto perde algumas ligaturas e desorganiza frações e índices. Por isso, a leitura de fórmulas ambíguas foi confrontada com imagens das páginas. Não foram executadas as simulações da dissertação nem do MUX. Os resultados numéricos da dissertação continuam sendo resultados relatados pela autora, não resultados reproduzidos nesta sessão.

## 1. Figura 4.21: três valores para o caso supercrítico

Na p. 71, a prosa menciona ε = 128 para o caso supercrítico. Na p. 72, a legenda da Figura 4.21 informa ε = 2,00. Os dois painéis inferiores mostram ε = 4. Essa divergência foi confirmada visualmente no PDF.

É possível descrever o excesso de grandes avalanches mostrado nos painéis, mas não determinar com segurança qual ε gerou os dados. A pergunta adequada é qual conjunto de parâmetros está correto e se há código ou dados da figura. Nenhum dos três valores foi escolhido por suposição no guia.

## 2. Figura 3.1 e Eq. 3.16 não coincidem como apresentadas

Na p. 34, a Eq. 3.16 é σ* = [1 + (n−1)Aε/(uN)]/[1 + (n−1)ε/(uKN)]. Com os parâmetros da legenda, n = 3, u = 0,1, A = 0,9, K = 10 e N = 16.000, essa expressão é maior que um para todo ε positivo, pois A > 1/K.

Substituindo diretamente, ε = 0,01 dá aproximadamente 1,000010; ε = 1 dá 1,001000; ε = 100 dá 1,098765; e ε = 1.000 dá 1,888889. A figura mostra pontos inferiores a um para ε pequeno, inclusive na série rotulada como Eq. 3.16. Isso não pode ser obtido da expressão impressa com os parâmetros informados.

O que foi confirmado é a incompatibilidade entre fórmula, parâmetros declarados e desenho. Não foi identificada a rotina que gerou o gráfico. Não cabe concluir, apenas com o PDF, se o problema está na legenda, na numeração da equação, nos parâmetros ou na curva.

## 3. Expansão de primeira ordem nas pp. 34–35

Expandindo a expressão racional da Eq. 3.16 para N grande, com K e os outros parâmetros fixos, obtém-se:

σ* = 1 + [(n−1)ε/u] (A − 1/K)/N + O(N^(−2)).

A Eq. 3.17 omite a contribuição −(n−1)ε/(uKN), embora ela também seja de ordem 1/N. Uma aproximação adicional de K grande poderia justificar desprezá-la em certas condições, mas essa hipótese precisa ser explicitada; ela não é um termo de ordem 1/N². A própria Eq. 4.5, p. 51, contém o fator A − 1/K.

Este reparo se refere à expansão da expressão aproximada, não a uma validação de todas as hipóteses usadas para chegar à Eq. 3.16.

## 4. Segunda ordem e o caso AK = 1 (pp. 50–51)

Para (1 + ax)/(1 + bx), a expansão correta até segunda ordem é 1 + (a−b)x + (b²−ab)x² + O(x³). Na Eq. 4.4 aparece o termo −abx², mas falta b²x².

Quando AK = 1, os coeficientes a e b definidos ali coincidem. A expressão racional vale exatamente um, dentro daquela aproximação. Não surge a correção quadrática negativa apresentada na Eq. 4.6 a partir dessa expressão. A conclusão σ* < 1 para esse caso não pode ser sustentada por essa expansão incompleta.

Isso não prova que todas as simulações finitas com AK = 1 devam dar σ* = 1. A Tabela 4.3, p. 63, mostra valores diferentes, e as aproximações de campo médio têm limites. É necessário separar a identidade algébrica de uma aproximação e o comportamento do sistema simulado.

## 5. Tabelas e legendas que merecem confirmação

A Tabela 4.1, p. 49, repete a média annealed 0,43801 e o desvio 1,5496 × 10^−4 nas linhas ε = 0,03125 e ε = 0,0625. A repetição é suspeita, mas não basta para inferir o valor correto.

Há resultados diferentes para conjuntos declarados iguais. Para N = 4.000, n = 3, K = 10, A = 1, u = 0,1 e ε = 128, a Tabela 4.1 informa média annealed 1,52987 e quenched 1,58209; a Tabela 4.2 informa 1,65193 e 1,66627; a Tabela 4.3 informa 1,6525 e 1,66573. É uma diferença que exige esclarecer parâmetros efetivamente usados, janelas de medição ou transcrição. Os dados brutos não estão disponíveis para resolver a divergência.

Algumas legendas de varreduras em N incluem N = 10.000 como se fosse fixo, embora as curvas mostrem N = 500 a 16.000. A legenda da Figura 4.20, p. 69, lista K = 10, embora o eixo horizontal varie K. O guia descreve as varreduras conforme os eixos, as séries e a seção, e não reproduz esses valores como condições simultaneamente fixas.

Na p. 62, a remissão à tabela de A usa o número 4.4, mas a tabela correspondente é a 4.3. No apêndice, algumas remissões às equações estão deslocadas: a fórmula de σ* corresponde à Eq. 3.9 e a relação autoconsistente de ρ* à Eq. 3.10. Esses problemas de remissão não mudam o conteúdo das fórmulas.

## 6. Cuidados de interpretação

No estado estacionário, as densidades dos estados refratários podem ser igualadas para obter ρ_0* = 1 − (n−1)ρ*. Durante transientes, cada estado acompanha atividades de passos anteriores. O Apêndice A explicita a aproximação perto do estado estacionário. Não use a relação simplificada como identidade exata de toda a evolução temporal.

A taxa nominal calculada por probabilidades das conexões e a razão entre números de disparos não são medidas universalmente intercambiáveis. O σ ≈ 1,1 associado a quenched em parte da dissertação não é um novo limiar universal que substitui um para qualquer rede.

A estimação ε′ = 0,066 ± 0,006 foi feita para n = 3, u = 0,1, A = 1 e K = 10. A autora informa que não verificou a dependência de ε′ dos outros parâmetros. O expoente de corte 3/4 é sugerido pelos resultados e pelo colapso, sem prova analítica apresentada.

O texto não fornece uma caracterização completa de incerteza estatística para todos os expoentes nem dados brutos para refazer ajustes ou comparar distribuições alternativas. O guia os apresenta como resultados relatados, não como estimativas revalidadas independentemente.

As seções biológicas iniciais contêm descrições históricas e simplificadas. O guia preserva o mecanismo necessário à modelagem, sem adotar como fatos atuais números históricos de células, detalhes bioquímicos não conferidos ou generalizações clínicas. As perspectivas médicas foram identificadas como propostas, sem transformar hipóteses em eficácia terapêutica.

## 7. Conferência externa delimitada

O registro e o resumo de Bonachela e colaboradores, 2010, confirmam que a crítica à criticalidade genérica em modelos dissipativos com carregamento é parte do debate que embasa a dissertação. [Artigo](https://arxiv.org/abs/1001.3256).

O registro e o resumo de Costa, Copelli e Kinouchi, 2015, mostram uma discussão posterior sobre comportamento semelhante a SOC conservativa e flutuações que desaparecem no limite termodinâmico. Isso não deve ser misturado ao que a dissertação concluiu em 2011. [Artigo](https://arxiv.org/abs/1405.7740).

O registro e o resumo de Campos, Costa, Copelli e Kinouchi, 2017, relacionam os desvios de σ em quenched às correlações e usam a aproximação do maior autovalor a um como critério. [Artigo](https://arxiv.org/abs/1604.05779).

Essas consultas não equivalem a uma revisão integral da literatura até 2026. Para a reunião, a formulação útil é: “Li a conclusão de 2011 e encontrei estes desdobramentos. Qual versão teórica devo adotar no meu projeto?”
