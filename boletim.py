
import streamlit as st
import pandas as pd
import plotly.express as px

# Título da aplicação
st.title("Boletim Automatizado 2025")

# Disciplinas
disciplinas = ["Português", "Matemática", "Ciências", "História", "Geografia", "Inglês", "Artes", "Ed Física"]

# Entrada de notas
st.subheader("Insira as notas por disciplina e bimestre")

notas = {}
for disc in disciplinas:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        n1 = st.number_input(f"{disc} - 1º Bim", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
    with col2:
        n2 = st.number_input(f"{disc} - 2º Bim", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
    with col3:
        n3 = st.number_input(f"{disc} - 3º Bim", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
    with col4:
        n4 = st.number_input(f"{disc} - 4º Bim", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
    notas[disc] = [n1, n2, n3, n4]

# Botão para calcular médias
if st.button("Calcular Médias e Situação"):
    medias = {}
    situacoes = {}
    for disc, valores in notas.items():
        media = sum(valores) / len(valores)
        medias[disc] = round(media, 2)
        situacoes[disc] = "Aprovado" if media >= 6 else "Reprovado"

    # Mostrar tabela
    df = pd.DataFrame({"Disciplina": disciplinas, "Média Final": [medias[d] for d in disciplinas], "Situação": [situacoes[d] for d in disciplinas]})
    st.write("### Resultado Final")
    st.dataframe(df)

    # Botão para gerar gráfico
    if st.button("Gerar Gráfico de Médias"):
        fig = px.bar(df, x="Disciplina", y="Média Final", color="Situação", title="Médias por Disciplina", text="Média Final")
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig)

st.write("
Para publicar, salve este código como boletim.py e rode com: streamlit run boletim.py")
