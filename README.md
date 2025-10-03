# 📊 Dashboard SAPRE (TJBA)

Este projeto é um dashboard interativo em Streamlit desenvolvido para facilitar o monitoramento de precatórios, documentos anexados e honorários advocatícios vinculados ao SAPRE (Sistema de Administração de Precatórios) do Tribunal de Justiça da Bahia – TJBA. 

O objetivo é permitir que advogados, servidores e interessados acompanhem informações relevantes sem precisar acessar diretamente o sistema SAPRE, tornando a análise mais ágil, clara e acessível.

---

## 🏛️ O que é o SAPRE?

O SAPRE (Sistema de Administração de Precatórios) é a plataforma do TJBA (Tribunal de Justiça do Estado da Bahia) utilizada para gerenciar precatórios e RPVs (Requisições de Pequeno Valor). 

No sistema, é possível acompanhar:
- Cadastro e tramitação dos precatórios; 
- Situações processuais (cadastrado, publicado, deferido, pago, suspenso etc.); 
- Controle de documentos obrigatórios anexados; 
- Honorários advocatícios e pagamentos. 

Este dashboard foi criado para espelhar essas informações em uma interface amigável, oferecendo gráficos, filtros e relatórios automáticos sem necessidade de navegar pelo SAPRE.

---

## ⚡ Funcionalidades

- 📊 **Dashboard Principal**  
  - Indicadores gerais: total de precatórios, soma dos valores, total de honorários e percentual médio de documentos anexados.  
  - Alertas automáticos para precatórios com documentos incompletos.  
  - Gráficos interativos de distribuição por situação, honorários por advogado e anexos por precatório.  

- 📈 **Análises Avançadas**  
  - Distribuição estatística dos valores.  
  - Correlação entre valor e percentual de documentos anexados.  
  - Agrupamento por Núcleo de Precatórios.  

- 📋 **Relatórios**  
  - Estatísticas descritivas.  
  - Relatórios agregados por situação.  
  - Exportação para Excel.  

- ⚙️ **Configurações**  
  - Ajuste da taxa de honorários (%).  
  - Ativação de alertas e limites para notificações de documentos.  

---

## 🛠️ Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**  
  Biblioteca para criação de interfaces web interativas de forma simples e rápida.  
  Permite construir dashboards e aplicativos de dados sem precisar de frameworks complexos de front-end.

- **[Pandas](https://pandas.pydata.org/)**  
  Utilizada para manipulação e análise de dados tabulares.  
  No projeto, organiza os precatórios em DataFrames, permitindo aplicar filtros e cálculos de forma eficiente.

- **[NumPy](https://numpy.org/)**  
  Biblioteca para computação numérica.  
  Foi usada para **gerar dados simulados** (números aleatórios, amostragens) e auxiliar em cálculos matemáticos.

- **[Plotly](https://plotly.com/python/)**  
  Ferramenta para construção de **gráficos interativos** em Python.  
  No dashboard, é usada para criar histogramas, gráficos de barras e visualizações dinâmicas que facilitam a análise.

  ---
