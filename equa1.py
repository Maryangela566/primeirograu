import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="Equação do 1o Grau",
    page_icon="📈",
    layout="centered"
)
# ============================================
# TEMA BTS - ROXO
# ============================================

st.markdown("""
<style>

    /* Fundo da página */
    .stApp {
        background: linear-gradient(135deg, #12001f, #24003d, #3b0066);
        color: white;
    }

    /* Título */
    h1 {
        color: #d8b4fe !important;
        text-align: center;
        font-weight: bold;
    }

    /* Subtítulos */
    h2, h3 {
        color: #c084fc !important;
    }

    /* Textos */
    p, label {
        color: #f3e8ff !important;
    }

    /* Campos de entrada */
    div[data-baseweb="input"] {
        background-color: #1f0b2e !important;
        border: 1px solid #a855f7 !important;
        border-radius: 10px;
    }

    input {
        color: white !important;
    }

    /* Botão */
    .stButton > button {
        background: linear-gradient(90deg, #7e22ce, #a855f7);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #a855f7, #c084fc);
        transform: scale(1.02);
    }

    /* Caixa de sucesso */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* Linha divisória */
    hr {
        border-color: #9333ea;
    }

    /* Rodapé */
    .stCaption {
        color: #c084fc !important;
        text-align: center;
    }

</style>
""")

# ============================================
# CAMINHO DA PASTA DO PROGRAMA
# ============================================

PASTA_APP = Path(__file__).parent


# ============================================
# CAMINHO DA LOGOMARCA
# ============================================

CAMINHO_LOGO = PASTA_APP / "Maryangela.jpg"


# ============================================
# LOGOMARCA
# ============================================

if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("⚠️ A imagem mat.jpeg não foi encontrada.")


# ============================================
# TÍTULO
# ============================================

st.title("📈 Equação do 1o Grau")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


# ============================================
# ENTRADA DOS VALORES
# ============================================

a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)


# ============================================
# BOTÃO CALCULAR
# ============================================

if st.button("Calcular", use_container_width=True):

    # ========================================
    # VERIFICA O VALOR DE A
    # ========================================

    if a == 0:

        if b == 0:
            st.warning(
                "A equação possui infinitas soluções."
            )

        else:
            st.error(
                "A equação não possui solução."
            )

    else:

        # ====================================
        # CALCULA A RAIZ
        # ====================================

        x_raiz = -b / a


        # ====================================
        # RESULTADO
        # ====================================

        st.subheader("✅ Resultado")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"x = {x_raiz:.2f}"
        )


        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================

        st.subheader("Equação")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )


        # ====================================
        # MOSTRA O CÁLCULO
        # ====================================

        st.subheader("Resolução")

        if b >= 0:
            st.latex(
                f"{a}x + {b} = 0"
            )
        else:
            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.latex(
            f"{a}x = {-b}"
        )

        st.latex(
            f"x = \\frac{{{-b}}}{{{a}}}"
        )

        st.latex(
            f"x = {x_raiz:.2f}"
        )


        # ====================================
        # GRÁFICO
        # ====================================

        st.subheader("📊 Gráfico da função")

        # Cria intervalo para o gráfico

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        # Função do primeiro grau

        y = a * x + b

        # Cria gráfico

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Desenha a reta

        ax.plot(
            x,
            y,
            linewidth=2,
            label=f"y = {a}x + {b}"
        )

        # Eixo X

        ax.axhline(
            y=0,
            linewidth=1
        )

        # Eixo Y

        ax.axvline(
            x=0,
            linewidth=1
        )

        # Marca a raiz

        ax.scatter(
            [x_raiz],
            [0],
            s=100,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )


        # ====================================
        # CONFIGURAÇÃO DO GRÁFICO
        # ====================================

        ax.set_xlabel("x")

        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1o Grau"
        )

        ax.grid(True)

        ax.legend()


        # ====================================
        # MOSTRA GRÁFICO
        # ====================================

        st.pyplot(fig)

        plt.close(fig)


# ============================================
# RODAPÉ
# ============================================

st.divider()

st.caption(
    "📚 Calculadora de Equação do 1o Grau"
)
