import pandas as pd
from flask import Flask, render_template
import plotly.graph_objs as go

app = Flask(__name__)

# Carregar o arquivo CSV
df = pd.read_csv('idh.csv')

@app.route('/')
def dashboard():
    # Filtrar os dados para o intervalo de anos de 1991 a 2021
    df_filtered = df[(df['ano_referencia'] >= 1991) & (df['ano_referencia'] <= 2021)]

    # Lógica para preparar os dados para o gráfico de linha (Expectativa de Vida)
    data_line = [
        go.Scatter(x=df_filtered['ano_referencia'], y=df_filtered['expectativa_de_vida_masculina'], mode='lines+markers', name='Expectativa de Vida Masculina'),
        go.Scatter(x=df_filtered['ano_referencia'], y=df_filtered['expectativa_de_vida_feminina'], mode='lines+markers', name='Expectativa de Vida Feminina')
    ]

    # Layout do gráfico de linha (Expectativa de Vida)
    layout_line = go.Layout(title='Comparação da Expectativa de Vida Masculina e Feminina', xaxis=dict(title='Ano de Referência'), yaxis=dict(title='Expectativa de Vida'))

    # Criação do gráfico de linha (Expectativa de Vida)
    fig_line = go.Figure(data=data_line, layout=layout_line)

    # Lógica para preparar os dados para o gráfico de barras (Expectativa de Anos de Escolaridade)
    data_bar = [
        go.Bar(x=df_filtered['ano_referencia'], y=df_filtered['expectativa_de_anos_escola_masculina'], name='Expectativa de Anos de Escolaridade Masculina'),
        go.Bar(x=df_filtered['ano_referencia'], y=df_filtered['expectativa_de_anos_escola_feminina'], name='Expectativa de Anos de Escolaridade Feminina')
    ]

    # Layout do gráfico de barras (Expectativa de Anos de Escolaridade)
    layout_bar = go.Layout(title='Comparação da Expectativa de Anos de Escolaridade Masculina e Feminina', xaxis=dict(title='Ano de Referência'), yaxis=dict(title='Expectativa de Anos de Escolaridade'), barmode='group')

    # Criação do gráfico de barras (Expectativa de Anos de Escolaridade)
    fig_bar = go.Figure(data=data_bar, layout=layout_bar)

    # Renderizar os dois gráficos no template HTML do dashboard
    return render_template('dashboard.html', plot_line=fig_line.to_html(), plot_bar=fig_bar.to_html())

if __name__ == '__main__':
    app.run(debug=True)
