# Leitura da dissertação e preparação para a reunião

Documento lido: Ariadne de Andrade Costa, *Quasi-criticalidade auto-organizada em avalanches neuronais*, versão corrigida, USP, Ribeirão Preto, 2011. A folha de rosto identifica uma dissertação de mestrado em Ciências, na área de Física Aplicada à Medicina e à Biologia, orientada por Osame Kinouchi Filho. Não é um resumo de doutorado. Você informou que Ariadne é sua orientadora.

O PDF tem 115 páginas físicas. Nas referências abaixo, “p.” significa a página impressa no trabalho. A página impressa 24, por exemplo, é a página 45 do PDF: no corpo principal e no apêndice, some 21. A ficha catalográfica informa 113 páginas, mas isso não corresponde à contagem física do arquivo.

Este guia cobre todos os capítulos, as sete seções de resultados, as perspectivas e o apêndice. As páginas iniciais contêm identificação, agradecimentos, epígrafe, resumos e listas. A bibliografia tem 98 entradas. Li o texto integral extraído, examinei visualmente as 29 figuras e conferi as equações centrais e os números utilizados aqui. Isso é uma conferência documental e matemática delimitada: não reproduzi as simulações da dissertação nem li integralmente os 98 trabalhos citados. As divergências encontradas estão em VALIDACAO_E_DUVIDAS.md.

## 1. A pergunta da pesquisa

A pergunta é como uma rede de elementos excitáveis pode ajustar suas próprias conexões e permanecer perto da fronteira entre uma atividade que desaparece depressa e uma atividade que se amplifica. O trabalho testa se a depressão e a recuperação das sinapses produzem essa aproximação sem escolher uma configuração inicial especial. O objetivo aparece nas pp. 19–20.

O modelo combina os elementos excitáveis de Kinouchi e Copelli com uma dinâmica de sinapses inspirada em Levina, Herrmann e Geisel. A vantagem procurada é reduzir a complexidade do modelo para permitir cálculos e simulações de redes maiores, com variação dos parâmetros.

A conclusão de 2011 é que o sistema apresenta quasi-criticalidade auto-organizada: aproxima-se da região crítica em uma faixa de parâmetros, mas suas propriedades continuam dependendo desses parâmetros e do tamanho da rede. A conclusão não afirma que qualquer rede neural, em qualquer condição, se torne crítica.

## 2. Os conceitos necessários para acompanhar o texto

### Neurônio, disparo e sinapse (pp. 4–8)

O capítulo inicial apresenta a estrutura dos neurônios e a comunicação por sinapses elétricas e químicas. O ponto que entra diretamente no modelo é o uso de recursos sinápticos: após um disparo, a eficácia da transmissão pode diminuir temporariamente e depois se recuperar.

“Depressão sináptica” significa redução da eficácia da sinapse. Não é o nome de um transtorno de humor. “Recuperação sináptica” é o retorno gradual dessa eficácia. O modelo representa esse mecanismo de forma simplificada, sem simular individualmente moléculas ou vesículas.

Uma sinapse dinâmica muda durante a simulação. Isso também não equivale, por si só, a um treinamento supervisionado: não há uma resposta correta apresentada à rede para calcular um erro e ajustar os pesos. A mudança depende da própria atividade.

### Avalanche neuronal (pp. 10–13 e 71–75)

Uma avalanche é uma sequência de atividade desencadeada por uma ativação, que continua enquanto existem disparos e termina quando não há elementos ativos. No protocolo da dissertação, um estímulo externo inicia uma nova avalanche quando a atividade anterior acaba.

Exemplo didático: se os números de disparos em passos sucessivos forem 1, 3, 2, 1 e 0, o episódio tem sete eventos de disparo e quatro passos ativos. Não se deve confundir a contagem de eventos com a contagem de neurônios distintos: um mesmo elemento pode voltar a participar após a recuperação. Para reproduzir exatamente o programa original, convém confirmar com a orientadora a convenção de contagem utilizada.

A Figura 1.3, p. 12, explica a identificação experimental de episódios por registros de eletrodos, separados por intervalos sem atividade. Um eletrodo mede um sinal coletivo; não é automaticamente uma observação de um único neurônio.

### Subcrítico, crítico e supercrítico (pp. 11–13)

Em um processo de ramificação ideal, a taxa de ramificação indica quantas ativações descendentes uma ativação produz, em média. Se essa média é menor que um, a propagação tende a diminuir. Se é maior que um, tende a aumentar inicialmente. O valor um marca a fronteira crítica desse processo ideal. Um episódio crítico ainda pode terminar: “crítico” não significa disparo eterno nem atividade constante em todos os passos.

Há duas medidas relacionadas, mas não idênticas: a razão entre atividades de passos consecutivos e uma medida calculada a partir das probabilidades das conexões. A introdução usa a primeira para explicar experimentos; o modelo trabalha com a segunda. Na aproximação homogênea, a taxa nominal é σ = K × probabilidade sináptica média. Correlações e indisponibilidade de neurônios refratários limitam a interpretação direta como número efetivo de descendentes.

### Lei de potência e corte (pp. 9–10 e 73–75)

Uma distribuição P(s) proporcional a s elevado a −3/2 significa que eventos pequenos são mais frequentes e eventos grandes ficam progressivamente mais raros. Por exemplo, antes de considerar o corte, aumentar s por um fator quatro reduz o valor da distribuição por um fator oito. Isso é uma ilustração matemática, não um dado medido na dissertação.

Em uma rede finita, o comportamento não se prolonga indefinidamente. O trabalho usa a forma P(s) proporcional a s^(−3/2) exp(−s/s_c), em que s_c caracteriza o corte. A proporcionalidade deixa explícito que falta uma constante de normalização. Alguns gráficos usam P(s) para frequências com valores maiores que um; não leia seus eixos como probabilidades normalizadas.

### Auto-organização e quasi-criticalidade (pp. 17–20)

Auto-organização significa que as regras internas conduzem o sistema a um regime, em vez de alguém impor continuamente o valor final de cada conexão. Na dissertação, a recuperação aumenta a capacidade de transmissão e os disparos provocam depressão. Essa realimentação pode conter tanto o enfraquecimento excessivo quanto o crescimento da atividade.

O texto distingue isso da obtenção de criticalidade exata sem ajuste de parâmetros. Observar uma faixa aproximadamente reta em um gráfico log–log não resolve a questão. Também se examina o que acontece quando N cresce e se as distribuições de redes diferentes podem ser reescaladas para uma mesma curva. Esse procedimento é o escalonamento de tamanho finito.

A discussão de conservação e separação de escalas temporais é apresentada dentro do debate da época, especialmente com Bonachela e colaboradores. Não transforme a formulação histórica em uma regra universal já encerrada: trabalhos posteriores da própria autora retomam essa classificação.

## 3. Como o modelo funciona

### O modelo de comparação: Levina, Herrmann e Geisel (pp. 21–24)

O modelo descrito usa neurônios integra-dispara com potencial de membrana contínuo. Um estímulo externo aumenta o potencial; ao atingir um limiar, o neurônio dispara e seu potencial é reduzido. O disparo transmite contribuições aos outros neurônios.

As sinapses possuem uma variável J_ij, associada à disponibilidade de recursos, que se recupera em direção a um valor de referência e diminui quando o neurônio pré-sináptico dispara. A dissertação escolhe a versão com fração de utilização u constante. Na versão descrita, a rede é totalmente conectada e a propagação da avalanche é determinística, dadas as condições iniciais e os estímulos. A aleatoriedade aparece na preparação e na aplicação de estímulos externos.

### O modelo estudado por Ariadne (pp. 24–28)

A rede tem N elementos e conexões direcionadas. Cada elemento possui exatamente K conexões de saída, totalizando NK conexões. O número de conexões de entrada varia entre elementos e tem média K. Não se deve afirmar que cada elemento possui exatamente K entradas e K saídas.

Cada elemento assume um estado s_i entre 0 e n−1. O estado 0 é suscetível: pode ser excitado. O estado 1 é ativo: pode transmitir atividade. Os estados de 2 a n−1 são refratários: o elemento percorre uma recuperação antes de voltar a ser suscetível. Para n = 3, a sequência após a ativação é 1 → 2 → 0.

Um elemento suscetível pode ser ativado probabilisticamente por vizinhos que estejam ativos. Após a ativação, a passagem pelos estados refratários é determinística. Logo, o modelo mistura transmissão probabilística com recuperação de estados determinística.

Quando a rede fica sem elementos ativos, um elemento escolhido aleatoriamente é excitado para iniciar outro episódio. Isso é diferente de manter uma corrente externa contínua em vários neurônios.

A probabilidade de transmissão de j para i é P_ij. A equação central, Eq. 2.4 na p. 26, é:

P_ij(t+1) = P_ij(t) + [ε/(KN)] [A − P_ij(t)] − u P_ij(t) δ(t−t_j).

O primeiro termo conserva o valor anterior. O segundo recupera a conexão em direção a A. O último reduz sua eficácia quando o neurônio pré-sináptico dispara, pois o indicador δ vale um nesse evento e zero fora dele. No caso annealed, a escolha das conexões deprimidas é modificada, como explicado adiante.

A é o valor de referência da recuperação; ε controla a rapidez da recuperação; u é a fração de depressão por disparo. A escala de recuperação definida no texto é KN/ε. N é o número de elementos, K o número de conexões de saída e n o número de estados possíveis. σ_0 define a ramificação média inicial e a inicialização uniforme das probabilidades, com P_max = 2σ_0/K.

Exemplo didático com valores usados em parte do estudo: N = 10.000, K = 10, A = 1, ε = 2, u = 0,1 e P_ij = 0,1. A recuperação em um passo acrescenta 0,000018. Se a conexão sofre depressão nesse passo, subtrai-se 0,01. Sem depressão, o novo valor é 0,100018; com depressão, 0,090018. A recuperação lenta compete com quedas associadas aos disparos.

O modelo usa probabilidades entre zero e um, não pesos positivos e negativos como o MUX. A p. 27 propõe interpretar os elementos como grupos de neurônios, com efeito líquido das interações. Essa interpretação não introduz conexões inibitórias negativas explícitas na equação.

### Quenched e annealed (p. 29)

Na versão quenched, a vizinhança é sorteada no início e permanece fixa. A depressão acompanha as sinapses associadas aos neurônios que disparam. Isso permite formar correlações entre atividade e enfraquecimento das conexões.

Na versão annealed descrita no documento, a vizinhança também é inicialmente sorteada e mantida. A diferença é que cada disparo provoca a atualização depressiva de K sinapses escolhidas aleatoriamente pela rede. A intenção é retirar a associação espacial entre o caminho percorrido pela atividade e as sinapses que são deprimidas. Seria incorreto resumir esse procedimento como “todos os vizinhos são ressorteados a cada passo”.

O texto menciona uma implementação intermediária, mais econômica, que escolhe um neurônio e atualiza um conjunto de suas sinapses. Foram feitas algumas medidas, mas a autora ressalva que seria necessário estudar melhor as correlações dessa alternativa.

As simulações foram programadas em Fortran 90. O estudo varia σ_0, N, ε, u, A, n e K. Não há no PDF o código-fonte nem os dados brutos necessários para uma reprodução completa.

## 4. O que a aproximação de campo médio faz (pp. 30–36)

Campo médio substitui a diversidade das interações por uma descrição média. Em vez de acompanhar toda correlação entre neurônios e sinapses, descreve a rede por poucas grandezas, como a fração ativa ρ e a ramificação média σ. É uma aproximação, particularmente limitada quando há correlações espaciais.

Sob essa aproximação, a probabilidade de um elemento suscetível receber ao menos uma ativação é π = 1 − (1 − σρ/K)^K. A expressão calcula primeiro a probabilidade de nenhuma tentativa ativar o elemento e subtrai esse valor de um.

No estado estacionário, as equações centrais são:

ρ* = [1 − (n−1)ρ*] [1 − (1 − σ*ρ*/K)^K].

σ* = AKε / (uKNρ* + ε).

A primeira relaciona a fração ativa com a fração disponível para receber excitação e com a transmissão. A segunda vem do balanço médio entre recuperação e depressão sináptica. Um asterisco indica o regime estacionário, não uma multiplicação.

“Estacionário” significa que as propriedades estatísticas se estabilizam após um transiente. As trajetórias ainda podem oscilar. A condição ρ_0 = 1 − (n−1)ρ é justificada no estado estacionário; durante transientes, as populações dos estados refratários guardam a história dos passos anteriores.

O capítulo obtém, por expansão para atividade pequena, ρ* ≈ ε(AK−1)/[uKN + (n−1)AKε]. Quando o termo uKN domina o denominador e os demais parâmetros ficam fixos, isso sugere ρ* proporcional a 1/N. Essa expressão não deve produzir uma “densidade negativa”: sua aplicação ao ramo ativo exige respeitar as hipóteses da derivação.

Também se obtém a expressão aproximada σ* ≈ [1 + (n−1)Aε/(uN)]/[1 + (n−1)ε/(uKN)] e o expoente β = 1 na análise de campo médio perto da transição. O ponto para a leitura é que tamanho de rede e parâmetros afetam a distância ao regime crítico. Há problemas nas expansões seguintes e na Figura 3.1; por isso não trate todas as fórmulas aproximadas como identidades válidas em qualquer regime. A conferência está no arquivo de validação.

O Apêndice A, pp. 92–94, refaz o balanço diretamente pela média da atualização sináptica. Ele recupera a mesma relação σ* = AKε/(uKNρ*+ε). Não é um novo experimento nem um modelo adicional.

## 5. Todos os blocos de resultados

### Condição inicial e distribuição das conexões (pp. 37–41; Figuras 4.1–4.2)

Redes iniciadas com diferentes σ_0 aproximam-se de valores estacionários semelhantes dentro de cada configuração. Na Figura 4.1, com n = 3, u = 0,1, A = 1, K = 10, N = 30.000 e ε = 2, o texto informa 1,000 ± 0,012 para annealed e 1,104 ± 0,012 para quenched. Esses números pertencem a esse conjunto de parâmetros; não definem constantes universais.

As conexões começam com distribuição uniforme. Depois formam distribuições concentradas, aproximadamente gaussianas ou assimétricas, dependendo da versão. As distribuições de pesos sinápticos não são a mesma coisa que distribuições de tamanhos de avalanches. Uma pode ser aproximadamente gaussiana enquanto a outra tem trecho de lei de potência.

### Tamanho da rede N (pp. 41–44; Figuras 4.3–4.5)

Nas condições estudadas, aumentar N reduz as flutuações e altera o valor estacionário. A extrapolação da Figura 4.4 informa 0,9999 ± 0,0003 para annealed e 1,1001 ± 0,0004 para quenched, com n = 3, u = 0,1, A = 1, K = 10 e ε = 2. São extrapolações do estudo, não medições de uma rede infinita.

A autora atribui a diferença entre versões às correlações geradas pela depressão. O trabalho de 2011 ainda apresenta a localização do ponto crítico quenched como uma estimativa a ser refinada.

### Recuperação ε (pp. 45–51; Figuras 4.6–4.10 e Tabela 4.1)

Valores pequenos de ε deixam a recuperação lenta; valores elevados favorecem uma transmissão mais forte. As curvas mostram uma região subcrítica, uma faixa próxima da criticalidade e uma região supercrítica. A faixa aproximadamente plana se estende quando N aumenta.

O texto compara simulações annealed com campo médio e usa ε/N para reescalar a região supercrítica. Isso é diferente do ajuste ε_c proporcional a N^(1/3), usado mais adiante para localizar as distribuições de avalanches próximas do ponto crítico. Não confunda as duas relações: elas respondem a perguntas diferentes.

A Tabela 4.1 apresenta médias e desvios de cinco simulações. Há uma linha aparentemente duplicada e divergências que impedem tratar toda a tabela como uma base de reprodução já validada.

### Depressão u (pp. 52–57; Figuras 4.11–4.13 e Tabela 4.2)

Aumentar u intensifica a queda sináptica associada aos disparos e, nas varreduras apresentadas, reduz σ*. O resultado depende de ε e N. Com ε = 0,25, as configurações mostradas são classificadas como subcríticas; com ε = 2, parte dos valores fica próxima da região crítica; com ε = 128, a recuperação forte mantém valores maiores em boa parte das curvas.

A versão quenched mostra maior sensibilidade a certas variações. O texto usa intervalos próximos dos valores de referência para argumentar que não é necessário escolher um único valor exato de u. Isso não demonstra independência completa em relação a u.

A discussão biológica da p. 53 não estabelece uma calibração experimental para u. A autora informa que não encontrou uma referência para a fração adequada e relata uma estimativa discutida com pesquisadores. Essa estimativa não deve ser apresentada como resultado experimental comprovado.

### Valor de recuperação A (pp. 58–63; Figuras 4.14–4.16 e Tabela 4.3)

Aumentar A eleva o nível para o qual as probabilidades tendem durante a recuperação. Com ε = 0,25, as curvas mostradas ficam subcríticas. Com ε = 2, valores baixos de A ficam subcríticos e uma faixa de valores maiores aproxima a rede da região crítica. Com ε = 128, aparece dependência mais forte de N e crescimento aproximadamente linear de σ* com A nas curvas apresentadas.

O texto não define uma faixa biologicamente comprovada de A. O efeito depende também de ε. A identidade AK = 1 discutida em uma aproximação não garante, sozinha, criticalidade nas simulações finitas: a própria Tabela 4.3 mostra resultados que exigem essa distinção.

### Número de estados n (pp. 64–65; Figura 4.17 e Tabela 4.4)

Foram comparados n = 2, 3, 6, 11 e 21. A dependência de σ* foi pequena, mas mensurável, nas condições testadas. A comparação foi feita com ε = 0,5, em regime identificado no texto como subcrítico. Não é evidência de que o período refratário nunca importe.

### Número de vizinhos K (pp. 66–70; Figuras 4.18–4.20 e Tabela 4.5)

Este parâmetro produz a diferença qualitativa mais clara entre as versões. Nas condições apresentadas, σ* cresce lentamente com K em annealed e diminui com K em quenched. A interpretação é que aumentar a vizinhança reduz as correlações que afetam a segunda versão.

O ajuste com soma de duas exponenciais descreve os pontos quenched estudados. Não é uma lei teórica universal. A autora propõe estudar K/N para distinguir conectividade absoluta de conectividade relativa. Por exemplo, K = 99 corresponde ao grafo completo se N = 100, mas a uma rede esparsa se N = 15.000. O grafo completo não foi simulado nesse estudo.

### Avalanches (pp. 71–75; Figuras 4.21–4.23)

As distribuições subcríticas apresentam queda rápida; as próximas do regime crítico exibem um trecho compatível com potência de expoente 3/2 e corte; as supercríticas mostram excesso de eventos grandes, descrito como uma saliência na cauda.

Para comparar tamanhos de rede, foi ajustada empiricamente a relação ε_c(N) = ε′ N^(1/3), com ε′ = 0,066 ± 0,006, mantendo n = 3, u = 0,1, A = 1 e K = 10. A autora afirma que não verificou como ε′ muda quando esses outros parâmetros variam. Para N = 8.000, a expressão central fornece ε_c = 1,32; este valor é um cálculo a partir da fórmula, não uma simulação nova nem o parâmetro confirmado da Figura 4.21.

As avalanches da Figura 4.22 foram observadas entre os passos 1.000.000 e 3.000.000. O estudo relata expoente 3/2 e sugere um corte s_c proporcional a N^(3/4), a partir do colapso da Figura 4.23. O expoente 3/4 é um resultado empírico sugerido pelo ajuste e pela comparação visual, não uma demonstração analítica exata.

O uso de uma representação monotônica baseada em ordenação/Zipf suaviza a apresentação das distribuições. Não substitui a necessidade de definir normalização, método de ajuste e incerteza. Há também divergência no valor supercrítico de ε entre a prosa, a legenda e os painéis da Figura 4.21; não repita um deles como valor confirmado.

## 6. O que o trabalho conclui e o que deixa em aberto (pp. 76–81)

A conclusão é que a dinâmica de recuperação e depressão consegue conduzir a rede para perto de um regime crítico em uma faixa de parâmetros. A memória das condições iniciais se reduz nos exemplos, mas σ* continua dependendo dos demais parâmetros. O modelo oferece um mecanismo suficiente dentro das condições estudadas; não prova que seja o único mecanismo biológico ou que todo cérebro opere assim.

O estudo combina uma aproximação analítica com resultados numéricos, enfatiza as diferenças de correlação entre versões e identifica distribuições de avalanches compatíveis com os expoentes discutidos. A classificação adotada ao fim da dissertação é SOqC.

As perspectivas incluem refinar ε′ e sua dependência dos outros parâmetros; simular o grafo completo; adicionar um campo externo persistente e estudar adaptação; testar outras topologias; e permitir parâmetros diferentes entre elementos, sorteados de distribuições.

O texto propõe ainda interpretações alternativas: um sistema epidemiológico do tipo suscetível–infectado–refratário–suscetível, com interações sociais que diminuem durante a doença, e uma reformulação por rede dual, com outra interpretação das variáveis e possível relação com circuitos olfatórios. Essas propostas não foram resultados demonstrados nas simulações apresentadas.

As sugestões experimentais incluem estudar a mudança dos expoentes ao alterar conexões de longo alcance e investigar relações entre dinâmica coletiva, drogas e condições neuropsiquiátricas. São perspectivas históricas de pesquisa, não evidências clínicas produzidas pela dissertação nem recomendações de tratamento.

## 7. Como isso se relaciona com o seu MUX

O arquivo codigo_final_mux.py simula seis neurônios com potenciais contínuos e disparos probabilísticos, usando a dinâmica identificada no código como Galves–Löcherbach. As nove conexões têm pesos fixos, com valores positivos e negativos. A tarefa é avaliar se a saída seleciona J0 ou J1 de acordo com A.

A dissertação usa autômatos com estados discretos, conexões probabilísticas dinâmicas e redes muito maiores para estudar atividade coletiva. O arquivo enviado não é a descrição direta do algoritmo do seu multiplexador.

Algumas letras mudam de significado. σ na dissertação é a taxa de ramificação; sigma = 0,25 no MUX controla a largura da função de probabilidade de disparo. A na dissertação é o valor assintótico sináptico; A no MUX é o controle de seleção. ρ na dissertação é a fração ativa na população; Rho[5,t] no seu script é a média de disparos de N5 entre execuções naquele instante. Trocar essas interpretações leva a conclusões erradas.

O MUX tem entradas persistentes em intervalos, e não o protocolo de iniciar uma avalanche apenas quando a atividade cessa. Também não calcula distribuição de tamanhos de avalanches, escalonamento com N ou adaptação sináptica. Uma acurácia digital alta no MUX não demonstra criticalidade. A relação científica entre os dois trabalhos precisa ser definida com a orientadora; ainda não consta como objetivo formal nos arquivos do projeto.

## 8. Trabalhos posteriores que mudam a leitura histórica

No artigo de 2015 *Can dynamical synapses produce true self-organized criticality?*, Costa, Copelli e Kinouchi apresentam um comportamento que aproximam de SOC conservativa, apesar da dissipação microscópica, e discutem o desaparecimento de flutuações no limite de redes grandes. Isso torna inadequado apresentar a conclusão de 2011 como a última posição dos autores. A consulta feita aqui cobriu o registro e o resumo do artigo, não sua validação integral. [Registro e resumo](https://arxiv.org/abs/1405.7740).

No artigo de 2017 *Correlations Induced by Depressing Synapses in Critically Self-Organized Networks with Quenched Dynamics*, Campos, Costa, Copelli e Kinouchi relatam que as correlações podem deslocar a ramificação nominal de um, enquanto o maior autovalor da matriz sináptica se aproxima de um. Essa é uma resposta posterior diretamente relacionada à dúvida da dissertação sobre quenched. Foram conferidos o registro e o resumo; não foi refeita a análise. [Registro e resumo](https://arxiv.org/abs/1604.05779).

## 9. Perguntas para a reunião das 18h

1. “Qual é a pergunta central da minha iniciação científica: demonstrar a função do MUX, estudar sua precisão, acrescentar plasticidade ou investigar regimes coletivos?”
2. “Que parte desta dissertação devo usar como base conceitual para o MUX, já que o modelo de neurônio e a dinâmica dos pesos são diferentes?”
3. “De onde vieram os nove pesos do código? Foram obtidos por otimização, ajuste manual ou algum trabalho anterior? Existe o programa que os gerou?”
4. “Nossa saída precisa acertar somente HIGH/LOW ou também reproduzir a amplitude da entrada selecionada? Qual erro é aceitável?”
5. “Quais resultados da dissertação de 2011 devo atualizar com os artigos de 2015 e 2017? Quando devo usar σ e quando devo olhar o maior autovalor?”
6. “Se formos estudar avalanches, qual será o protocolo de estímulo, a definição de tamanho e duração e o método de ajuste das distribuições?”
7. “Qual primeiro resultado você espera que eu reproduza e quais parâmetros devo manter fixos nessa etapa?”
8. “Há códigos e dados originais que eu possa consultar para conferir as figuras e as diferenças de valores entre texto e legenda?”

Se o tempo da reunião for curto, priorize as perguntas 1, 2, 3 e 7. Elas delimitam o trabalho que você realmente fará.

## 10. Roteiro para reler o original antes da reunião

Comece pelo resumo, p. vii (PDF 8), e pelos objetivos, pp. 19–20 (PDF 40–41). Leia depois as pp. 24–29 (PDF 45–50), que definem o modelo e as versões quenched e annealed. Observe a Figura 2.1 na p. 27: ela mostra a recuperação interrompida por quedas sinápticas.

Passe à Figura 4.1, p. 38 (PDF 59), para entender a convergência a partir de condições iniciais diferentes. Compare com as Figuras 4.19–4.20, pp. 68–69 (PDF 89–90), que mostram o efeito diferente de K nas duas versões. Termine com as pp. 71–79 (PDF 92–100), incluindo as distribuições de avalanches e as conclusões.

As referências que sustentam a sequência histórica estão na própria bibliografia: Beggs e Plenz, 2003, referência 12; Kinouchi e Copelli, 2006, referência 49; Levina, Herrmann e Geisel, 2007, referência 55; Bonachela e Muñoz, 2009, referência 17; Bonachela e colaboradores, 2010, referência 16. São referências identificadas no documento, não cinco artigos lidos integralmente nesta preparação.
