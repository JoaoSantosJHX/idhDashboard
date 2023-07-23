# IdhDashboard
**Dashbord criado em Python mostrando histórico do IDH brasileiro**

## Tecnologias usadas:
- A biblioteca **Pandas** para a manipulação do arquivo,
- O framework **Flask** para criar um servidor web que serve como o backend do dashboard. Ele é responsável por receber as solicitações do navegador, processar os dados (obtidos do Pandas) e enviar as respostas com as visualizações geradas para o frontend.
- E por fim o **Plotly** que é uma biblioteca Python para criação de gráficos interativos. Neste projeto, o Plotly é usado para criar visualizações gráficas a partir dos dados do Pandas. No caso específico, usei o Plotly para criar gráficos de linha e de barras que mostram a comparação da expectativa de vida masculina e feminina e a comparação da expectativa de anos de escolaridade masculina e feminina, respectivamente.
