{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "15bd97bf-390d-47a6-96a9-0f7748b8c7e4",
   "metadata": {},
   "source": [
    "# 📊 Dashboard SAPRE (TJBA)\n",
    "\n",
    "Este projeto é um **dashboard interativo em Streamlit** desenvolvido para facilitar o monitoramento de **precatórios, documentos anexados e honorários advocatícios** vinculados ao **SAPRE (Sistema de Administração de Precatórios) do Tribunal de Justiça da Bahia – TJBA**.  \n",
    "\n",
    "O objetivo é permitir que advogados, servidores e interessados acompanhem informações relevantes **sem precisar acessar diretamente o sistema SAPRE**, tornando a análise mais ágil, clara e acessível.\n",
    "\n",
    "---\n",
    "\n",
    "## 🏛️ O que é o SAPRE?\n",
    "\n",
    "O **SAPRE (Sistema de Administração de Precatórios)** é a plataforma do **TJBA (Tribunal de Justiça do Estado da Bahia)** utilizada para **gerenciar precatórios e RPVs (Requisições de Pequeno Valor)**.  \n",
    "\n",
    "No sistema, é possível acompanhar:\n",
    "- Cadastro e tramitação dos precatórios;  \n",
    "- Situações processuais (cadastrado, publicado, deferido, pago, suspenso etc.);  \n",
    "- Controle de documentos obrigatórios anexados;  \n",
    "- Honorários advocatícios e pagamentos.  \n",
    "\n",
    "Este dashboard foi criado para **espelhar essas informações** em uma interface amigável, oferecendo **gráficos, filtros e relatórios automáticos** sem necessidade de navegar pelo SAPRE.\n",
    "\n",
    "---\n",
    "\n",
    "## ⚡  Funcionalidades\n",
    "\n",
    "- **📊 Dashboard Principal**  \n",
    "  - Indicadores gerais: total de precatórios, soma dos valores, total de honorários e percentual médio de documentos anexados.  \n",
    "  - Alertas automáticos para precatórios com documentos incompletos.  \n",
    "  - Gráficos interativos de distribuição por situação, honorários por advogado e anexos por precatório.  \n",
    "\n",
    "- **📈 Análises Avançadas**  \n",
    "  - Distribuição estatística dos valores.  \n",
    "  - Correlação entre valor e percentual de documentos anexados.  \n",
    "  - Agrupamento por Núcleo de Precatórios.  \n",
    "\n",
    "- **📋 Relatórios**  \n",
    "  - Estatísticas descritivas.  \n",
    "  - Relatórios agregados por situação.  \n",
    "  - Exportação para Excel.\n",
    "\n",
    "- **⚙️ Configurações**  \n",
    "  - Ajuste da taxa de honorários (%).  \n",
    "  - Ativação de alertas e limites para notificações de documentos.  \n",
    "\n",
    "---"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
