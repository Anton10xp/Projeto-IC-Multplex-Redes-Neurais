import sys
import numpy as np
import matplotlib.pyplot as plt


# Localização da biblioteca do modelo GL
sys.path.insert(
    0,
    "C:/Users/erick/Desktop/IC 2025/codigo_origin"
)

import biblioteca_GLmodel as bGL


# 2. PARÂMETROS DO MODELO GL

mu = 0.90
sigma = 0.25
theta_graus = 80

# Sem ruído adicional nas entradas
Jdev = 0


# 3. PARÂMETROS DA SIMULAÇÃO

Execucoes = 50'

Tfinal = 10000

Nintervals = 10

interval = Tfinal // Nintervals

# 4. ESTRUTURA DA REDE

Ncontrols = 1
Ninputs = 2
Nneurons = 6


# 5. TOPOLOGIA DO MUX

Links = [

    [1, 0],   # W0: N0 -> N1
    [5, 1],   # W1: N1 -> N5
    [4, 2],   # W2: N2 -> N4
    [4, 3],   # W3: N3 -> N4
    [5, 4],   # W4: N4 -> N5
    [4, 0],   # W5: N0 -> N4
    [1, 2],   # W6: N2 -> N1
    [5, 3],   # W7: N3 -> N5
    [3, 0]    # W8: N0 -> N3

]


# 6. PESOS FINAIS

Weights = np.array([

    -0.29307238,    # W0: N0 -> N1
     2.79447068,    # W1: N1 -> N5
     2.84167436,    # W2: N2 -> N4
    -5.00000000,    # W3: N3 -> N4
    -3.64830746,    # W4: N4 -> N5
    -0.09830224,    # W5: N0 -> N4
    -3.57436193,    # W6: N2 -> N1
     1.82615225,    # W7: N3 -> N5
    -0.49504811     # W8: N0 -> N3

])


# 7. ENTRADAS

Control = [
    []
]

Javg = [
    [],
    []
]


# ------------------------------------------------------------
# Sinal de controle A
# ------------------------------------------------------------

Control[0] = [

    x * 2

    for x in [

        0.99,
        0.89,
        0.20,
        0.10,
        0.03,
        0.26,
        0.96,
        0.11,
        0.05,
        0.91

    ]

]


# ------------------------------------------------------------
# Entrada J0
# ------------------------------------------------------------

Javg[0] = [

    x * 2

    for x in [

        0.97,
        0.08,
        0.25,
        0.86,
        0.15,
        0.10,
        0.10,
        0.88,
        0.20,
        0.95

    ]

]


# ------------------------------------------------------------
# Entrada J1
# ------------------------------------------------------------

Javg[1] = [

    x * 2

    for x in [

        0.08,
        0.20,
        0.25,
        0.09,
        0.25,
        0.92,
        0.14,
        0.12,
        0.92,
        0.90

    ]

]


# ============================================================
# 8. POTENCIAIS NORMALIZADOS
# ============================================================

Vb, Vr, Vm = bGL.CalculateNormalizedPotentials(
    theta_graus
)


# 9. ESTADOS DA REDE

S = np.zeros(
    Nneurons
)

V = np.zeros(
    Nneurons
)


# Armazena os potenciais ao longo do tempo
V_all = np.zeros(
    (Nneurons, Tfinal)
)


# Armazena os disparos dos neurônios
Rho = np.zeros(
    (Nneurons, Tfinal)
)


# 10. INFORMAÇÕES DOS PESOS

nomes_pesos = [

    "N0 -> N1",
    "N1 -> N5",
    "N2 -> N4",
    "N3 -> N4",
    "N4 -> N5",
    "N0 -> N4",
    "N2 -> N1",
    "N3 -> N5",
    "N0 -> N3"

]


print()
print("=" * 75)
print("MUX NEURAL 2:1 - MODELO DE GALVES-LÖCHERBACH")
print("=" * 75)

print()
print("Parâmetros:")
print(
    f"mu = {mu}"
)

print(
    f"sigma = {sigma}"
)

print(
    f"theta = {theta_graus} graus"
)

print(
    f"Execuções = {Execucoes}"
)

print(
    f"Tempo total = {Tfinal}"
)

print()

print("Pesos utilizados:")
print("-" * 75)


for i in range(
    len(Weights)
):

    print(
        f"W{i} ({nomes_pesos[i]:8s}) = "
        f"{Weights[i]: .8f}"
    )


# 11. SIMULAÇÃO PRINCIPAL

for exe in range(
    Execucoes
):

    # --------------------------------------------------------
    # Estado inicial
    # --------------------------------------------------------

    V[:] = 0


    # --------------------------------------------------------
    # Evolução temporal
    # --------------------------------------------------------

    for t in range(
        Tfinal
    ):


        # ====================================================
        # 11.1 DISPAROS
        # ====================================================

        for i in range(
            Nneurons
        ):

            Phi = bGL.CalculatePhiERF(

                V[i],
                Vm,
                sigma

            )


            x = np.random.uniform()


            S[i] = (

                1

                if x <= Phi

                else 0

            )


            # Acumula atividade
            Rho[i, t] += S[i]


        
        # 11.2 SOMAS SINÁPTICAS
      

        coming = np.zeros(
            Nneurons
        )


        for k, (
            i,
            j
        ) in enumerate(
            Links
        ):

            coming[i] += (

                Weights[k]
                *
                S[j]

            )


        
        # 11.3 INTERVALO ATUAL
       

        y = t // interval


       
        # 11.4 ATUALIZAÇÃO DOS POTENCIAIS
    

        for i in range(
            Nneurons
        ):


            # ------------------------------------------------
            # N0 = controle A
            #
            # Quando A é HIGH, N0 é favorecido.
            # ------------------------------------------------

            if i == 0:

                J = (

                    Control[0][y]
                    +
                    Jdev * np.random.normal()

                )


            # ------------------------------------------------
            # N2 = controle invertido
            #
            # Quando A é LOW, N2 é favorecido.
            #
            # Essa é a INIBIÇÃO CRUZADA.
            # ------------------------------------------------

            elif i == 2:

                J = (

                    2.0
                    -
                    Control[0][y]
                    +
                    Jdev * np.random.normal()

                )


            # ------------------------------------------------
            # N1 = entrada J0
            # ------------------------------------------------

            elif i == 1:

                J = (

                    Javg[0][y]
                    +
                    Jdev * np.random.normal()

                )


            # ------------------------------------------------
            # N3 = entrada J1
            # ------------------------------------------------

            elif i == 3:

                J = (

                    Javg[1][y]
                    +
                    Jdev * np.random.normal()

                )


            # ------------------------------------------------
            # N4 e N5 não recebem entrada externa
            # ------------------------------------------------

            else:

                J = 0


            # =================================================
            # DINÂMICA DE GALVES-LÖCHERBACH
            # =================================================

            if S[i] == 0:

                V[i] = (

                    Vb
                    +
                    mu * (V[i] - Vb)
                    +
                    coming[i]
                    +
                    J

                )

            else:

                V[i] = (

                    Vr
                    +
                    coming[i]
                    +
                    J

                )


            # ------------------------------------------------
            # Limitação do potencial
            # ------------------------------------------------

            V[i] = np.clip(

                V[i],
                Vr,
                2.0

            )


            # Acumula potencial
            V_all[i, t] += V[i]


# 12. NORMALIZAÇÃO DAS EXECUÇÕES

Rho /= Execucoes

V_all /= Execucoes


# 13. RESULTADOS POR INTERVALO

rho5_medias = []

selecionados = []

alvos = []


print()
print("=" * 75)
print("RESULTADOS POR INTERVALO")
print("=" * 75)


for k in range(
    Nintervals
):


    inicio = (
        k * interval
    )

    fim = (
        (k + 1) * interval
    )


    # --------------------------------------------------------
    # Média de rho5
    # --------------------------------------------------------

    rho5 = np.mean(

        Rho[
            5,
            inicio:fim
        ]

    )


    rho5_medias.append(
        rho5
    )


    # --------------------------------------------------------
    # Entradas do intervalo
    # --------------------------------------------------------

    A = Control[0][k]

    J0 = Javg[0][k]

    J1 = Javg[1][k]


    # --------------------------------------------------------
    # Seleção do MUX
    # --------------------------------------------------------

    if A >= 1.0:

        selecionado = J0

        canal = "J0"

    else:

        selecionado = J1

        canal = "J1"


    selecionados.append(
        selecionado
    )


    # --------------------------------------------------------
    # Saída esperada
    # --------------------------------------------------------

    esperado = (
        selecionado / 2.0
    )


    alvos.append(
        esperado
    )


    # --------------------------------------------------------
    # Classificação
    # --------------------------------------------------------

    if rho5 >= 0.5:

        saida = "HIGH"

    else:

        saida = "LOW"


    print(

        f"Intervalo {k}: "
        f"A={A:.2f} | "
        f"J0={J0:.2f} | "
        f"J1={J1:.2f} | "
        f"Selecionado={canal} | "
        f"Esperado={esperado:.2f} | "
        f"rho5={rho5:.4f} | "
        f"Saída={saida}"

    )


# 14. MÉTRICAS

acertos = 0


for k in range(
    Nintervals
):

    esperado = alvos[k]

    rho = rho5_medias[k]


    esperado_digital = (

        1

        if esperado >= 0.5

        else 0

    )


    obtido_digital = (

        1

        if rho >= 0.5

        else 0

    )


    if (
        esperado_digital
        ==
        obtido_digital
    ):

        acertos += 1


acuracia = (

    100
    *
    acertos
    /
    Nintervals

)


# Distância média entre saída e entrada selecionada
distancia_media = np.mean(

    [

        abs(
            rho5_medias[k]
            -
            alvos[k]
        )

        for k in range(
            Nintervals
        )

    ]

)


print()
print("=" * 75)
print("MÉTRICAS")
print("=" * 75)

print(
    f"Acurácia digital: "
    f"{acuracia:.1f}%"
)

print(
    f"Distância média entre "
    f"rho5 e entrada selecionada: "
    f"{distancia_media:.4f}"
)


# 15. PREPARAÇÃO DOS DADOS PARA OS GRÁFICOS

Tempo = np.arange(
    0,
    Tfinal,
    20
)


Rho_input = [

    [],
    [],
    []

]


for t in Tempo:

    y = t // interval


    Rho_input[0].append(
        Javg[0][y]
    )

    Rho_input[1].append(
        Javg[1][y]
    )

    Rho_input[2].append(
        Control[0][y]
    )


# 16. GRÁFICO CONSOLIDADO
#
# 1 - Entradas
# 2 - Potenciais dos neurônios
# 3 - Saída rho5
#

fig, (
    ax1,
    ax2,
    ax3
) = plt.subplots(

    3,
    1,

    figsize=(
        17,
        20
    ),

    sharex=True

)


# 16.1 ENTRADAS

ax1.scatter(

    Tempo,
    Rho_input[0],

    label=r"$J_0$",

    color="cyan",

    s=20

)


ax1.scatter(

    Tempo,
    Rho_input[1],

    label=r"$J_1$",

    color="blue",

    s=20

)


ax1.scatter(

    Tempo,
    Rho_input[2],

    label=r"$A$",

    color="red",

    s=25

)


ax1.set_ylabel(

    "Input",

    fontsize=30

)


ax1.set_ylim(

    0,
    2.0

)


ax1.tick_params(

    axis="both",
    labelsize=25

)


ax1.legend(

    loc="center left",
    fontsize=25

)


ax1.grid(

    True,
    alpha=0.3

)


# 16.2 POTENCIAIS

for i in range(
    Nneurons
):

    ax2.plot(

        Tempo,

        V_all[
            i,
            ::20
        ],

        label=f"$V_{i}$"

    )


ax2.set_ylabel(

    "Potencial $V$",

    fontsize=30

)


ax2.tick_params(

    axis="both",
    labelsize=25

)


ax2.legend(

    ncol=3,

    loc="upper center",

    fontsize=18

)


ax2.grid(

    True,
    alpha=0.3

)


# 16.3 SAÍDA rho5

ax3.plot(

    Tempo,

    Rho[
        5,
        ::20
    ],

    label=r"$\rho_5$",

    color="steelblue"

)


# ------------------------------------------------------------
# Linha de referência
#
# Apenas para demonstrar a separação digital:
#
#   rho5 >= 0.5 -> HIGH
#   rho5 <  0.5 -> LOW
# ------------------------------------------------------------

ax3.axhline(

    0.5,

    linestyle="--",

    linewidth=2,

    color="black",

    label="Referência = 0.5"

)


ax3.set_xlabel(

    "Tempo",

    fontsize=30

)


ax3.set_ylabel(

    r"$\rho_5$",

    fontsize=30

)


ax3.set_ylim(

    0,
    1.0

)


ax3.tick_params(

    axis="both",

    labelsize=25

)


ax3.legend(

    loc="upper center",

    fontsize=18

)


ax3.grid(

    True,
    alpha=0.3

)


# ============================================================
# 17. AJUSTE E SALVAMENTO
# ============================================================

plt.tight_layout()


plt.savefig(

    "MUX_neural_resultados.png",

    dpi=300,

    bbox_inches="tight"

)


plt.show()


# 18. GRÁFICO DA FUNÇÃO DE DISPARO

fig_phi = plt.figure(

    figsize=(
        8,
        6
    )

)


V_values = np.linspace(

    -1.0,
    2.0,
    500

)


Phi_values = [

    bGL.CalculatePhiERF(

        Vi,
        Vm,
        sigma

    )

    for Vi in V_values

]


plt.plot(

    V_values,

    Phi_values,

    color="purple",

    linewidth=2

)


plt.xlabel(

    "V",

    fontsize=20

)


plt.ylabel(

    r"$\phi(V)$",

    fontsize=20

)


plt.title(

    r"Função de Disparo $\phi(V)$",

    fontsize=22

)


plt.grid(
    True
)


plt.ylim(

    0,
    1.05

)


plt.xlim(

    -1,
    2

)


plt.tick_params(

    axis="both",

    labelsize=14

)


plt.tight_layout()


plt.savefig(

    "MUX_funcao_disparo.png",

    dpi=300,

    bbox_inches="tight"

)


plt.show()


# ============================================================
# 19. GRÁFICO PRINCIPAL - rho5 POR INTERVALO
# ============================================================
#
# Este gráfico é útil para o relatório porque mostra
# diretamente a resposta do MUX em cada intervalo.
#
# ============================================================

fig, ax = plt.subplots(

    figsize=(
        14,
        7

    )

)


intervalos_plot = np.arange(
    Nintervals
)


ax.plot(

    intervalos_plot,

    rho5_medias,

    marker="o",

    linewidth=2.5,

    markersize=8,

    label=r"$\rho_5$ médio"

)


# Linha de referência digital

ax.axhline(

    0.5,

    linestyle="--",

    linewidth=2,

    color="black",

    label="Referência = 0.5"

)


# Valores dos pontos

for k, rho in enumerate(
    rho5_medias
):

    ax.annotate(

        f"{rho:.3f}",

        (
            k,
            rho
        ),

        xytext=(
            0,
            10
        ),

        textcoords="offset points",

        ha="center",

        fontsize=12

    )


ax.set_xticks(
    intervalos_plot
)


ax.set_xticklabels(

    [
        str(k)

        for k in range(
            Nintervals
        )

    ]

)


ax.set_ylim(

    0,
    1.05

)


ax.set_xlabel(

    "Intervalo",

    fontsize=22

)


ax.set_ylabel(

    r"$\rho_5$ médio",

    fontsize=22

)


ax.set_title(

    r"Resposta do MUX Neural — $\rho_5$ por intervalo",

    fontsize=24

)


ax.tick_params(

    axis="both",

    labelsize=16

)


ax.grid(

    True,

    alpha=0.3

)


ax.legend(

    fontsize=14

)


plt.tight_layout()


plt.savefig(

    "MUX_rho5_por_intervalo.png",

    dpi=300,

    bbox_inches="tight"

)


plt.show()


# 20. RESUMO FINAL

print()
print("=" * 75)
print("SIMULAÇÃO CONCLUÍDA")
print("=" * 75)

print()

print(
    f"Acurácia digital: "
    f"{acuracia:.1f}%"
)

print(

    f"Distância média: "
    f"{distancia_media:.4f}"

)

print()

print(
    "Arquivos gerados:"
)

print(
    " - MUX_neural_resultados.png"
)

print(
    " - MUX_funcao_disparo.png"
)

print(
    " - MUX_rho5_por_intervalo.png"
)

print()

print("=" * 75)