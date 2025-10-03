import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard SAPRE",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# Simulação de dados do SAPRE
# -------------------------------------------------
@st.cache_data
def carregar_dados():
    np.random.seed(42)
    n_precatorios = 50
    situacoes = ["Cadastrado", "Em Análise", "Aguardando assinatura / homologação", "Publicado", "Deferido",
                 "Indeferido",
                 "Aguardando pagamento", "Em acordo / conciliação", "Pago parcialmente", "Pago integralmente / Quitado",
                 "Suspenso", "Cancelado", "Arquivado"]
    nucleos = ["Núcleo NACP", "Núcleo de Precatórios"]

    # DataFrame fictício
    df = pd.DataFrame({
        "Número": [f"{1000 + i}" for i in range(n_precatorios)],
        "Credor": [f"Advogado {i % 10 + 1}" for i in range(n_precatorios)],
        "Valor": np.random.randint(50_000, 200_000, size=n_precatorios),
        "Situação": np.random.choice(situacoes, size=n_precatorios),
        "Documentos Anexados (%)": np.random.randint(70, 101, size=n_precatorios)
    })

    # Cálculo automático de honorários (5%)
    df["Honorário (5%)"] = df["Valor"] * 0.05

    return df


# -------------------------------------------------
# Menu Lateral (Sidebar)
# -------------------------------------------------
def criar_menu_lateral():
    with st.sidebar:
        st.title("🏛️ SAPRE Dashboard")
        st.markdown("---")

        # Seção de Navegação
        st.subheader("📋 Navegação")
        pagina_selecionada = st.radio(
            "Selecione uma seção:",
            ["📊 Dashboard Principal", "📈 Análises Avançadas", "📋 Relatórios", "⚙️ Configurações"],
            index=0
        )

        st.markdown("---")

        # Seção de Filtros
        st.subheader("🔍 Filtros")

        df = carregar_dados()

        filtro_situacao = st.multiselect(
            "Situação:",
            options=df["Situação"].unique(),
            default=df["Situação"].unique()
        )

        filtro_credor = st.multiselect(
            "Credor:",
            options=df["Credor"].unique(),
            default=df["Credor"].unique()
        )

        # Filtros adicionais
        st.markdown("**Filtros Especiais:**")
        filtro_valor_min = st.number_input("Valor mínimo (R$):", min_value=0, value=0, step=1000)
        filtro_valor_max = st.number_input("Valor máximo (R$):", min_value=0, value=200000, step=1000)
        filtro_docs_min = st.slider("Documentos anexados (% mín.):", 0, 100, 70)

        st.markdown("---")

        # Seção de Ações Rápidas
        st.subheader("⚡ Ações Rápidas")
        if st.button("🔄 Atualizar Dados", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

        if st.button("📥 Exportar Excel", use_container_width=True):
            st.session_state.exportar = True

        st.markdown("---")

        # Informações do Sistema
        st.subheader("ℹ️ Informações")
        st.info("Sistema SAPRE v2.0\nÚltima atualização: Hoje")

        return pagina_selecionada, {
            "situacao": filtro_situacao,
            "credor": filtro_credor,
            "valor_min": filtro_valor_min,
            "valor_max": filtro_valor_max,
            "docs_min": filtro_docs_min
        }


# -------------------------------------------------
# Função para aplicar filtros
# -------------------------------------------------
def aplicar_filtros(df, filtros):
    df_filtrado = df[
        (df["Situação"].isin(filtros["situacao"])) &
        (df["Credor"].isin(filtros["credor"])) &
        (df["Valor"] >= filtros["valor_min"]) &
        (df["Valor"] <= filtros["valor_max"]) &
        (df["Documentos Anexados (%)"] >= filtros["docs_min"])
        ]
    return df_filtrado


# -------------------------------------------------
# Página Principal do Dashboard
# -------------------------------------------------
def dashboard_principal(df_filtrado):
    st.title("📊 Dashboard de Monitoramento SAPRE")
    st.markdown("Monitoramento de precatórios, documentos e honorários sem precisar entrar no sistema.")

    # Indicadores gerais
    st.subheader("📈 Resumo Geral")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Precatórios", len(df_filtrado))
    with col2:
        media_docs = df_filtrado["Documentos Anexados (%)"].mean() if len(df_filtrado) > 0 else 0
        st.metric("Média Documentos (%)", f"{media_docs:.1f}%")
    with col3:
        total_valor = df_filtrado["Valor"].sum() if len(df_filtrado) > 0 else 0
        st.metric("Total Valor (R$)", f"R$ {total_valor:,.2f}")
    with col4:
        total_honorarios = df_filtrado["Honorário (5%)"].sum() if len(df_filtrado) > 0 else 0
        st.metric("Total Honorários (R$)", f"R$ {total_honorarios:,.2f}")

    # Alertas automáticos
    st.subheader("⚠️ Alertas")
    if len(df_filtrado) > 0:
        alertas = df_filtrado[df_filtrado["Documentos Anexados (%)"] < 100]
        if not alertas.empty:
            st.warning(f"{len(alertas)} precatórios com documentos incompletos (<100%)")
            with st.expander("Ver detalhes dos alertas"):
                st.dataframe(
                    alertas[["Número", "Credor", "Situação", "Documentos Anexados (%)"]].reset_index(drop=True))
        else:
            st.success("✅ Todos os precatórios têm documentos completos!")
    else:
        st.info("Nenhum dado encontrado com os filtros aplicados.")

    # Gráficos interativos
    if len(df_filtrado) > 0:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Precatórios por Situação")
            fig_situacao = px.histogram(df_filtrado, x="Situação", color="Situação", text_auto=True,
                                        title="Distribuição por Situação")
            fig_situacao.update_layout(showlegend=False)
            st.plotly_chart(fig_situacao, use_container_width=True)

        with col2:
            st.subheader("💰 Honorários por Advogado")
            honorarios_por_advogado = df_filtrado.groupby("Credor", as_index=False)["Honorário (5%)"].sum()
            fig_honorarios = px.bar(honorarios_por_advogado,
                                    x="Credor", y="Honorário (5%)",
                                    title="Honorários Totais por Advogado")
            st.plotly_chart(fig_honorarios, use_container_width=True)

        st.subheader("📋 Documentos Anexados por Precatório")
        fig_docs = px.bar(df_filtrado, x="Número", y="Documentos Anexados (%)", color="Situação",
                          title="Percentual de Documentos Anexados")
        st.plotly_chart(fig_docs, use_container_width=True)

        # Tabela detalhada
        st.subheader("📋 Tabela Detalhada")
        st.dataframe(df_filtrado.reset_index(drop=True), use_container_width=True)


# -------------------------------------------------
# Página de Análises Avançadas
# -------------------------------------------------
def analises_avancadas(df_filtrado):
    st.title("📈 Análises Avançadas")

    if len(df_filtrado) > 0:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💹 Distribuição de Valores")
            fig_hist = px.histogram(df_filtrado, x="Valor", nbins=20,
                                    title="Distribuição dos Valores dos Precatórios")
            st.plotly_chart(fig_hist, use_container_width=True)

        with col2:
            st.subheader("🎯 Correlação Valor vs Documentos")
            fig_scatter = px.scatter(df_filtrado, x="Valor", y="Documentos Anexados (%)",
                                     color="Situação", title="Valor vs % Documentos Anexados")
            st.plotly_chart(fig_scatter, use_container_width=True)

    else:
        st.info("Nenhum dado encontrado com os filtros aplicados.")


# -------------------------------------------------
# Página de Relatórios
# -------------------------------------------------
def relatorios(df_filtrado):
    st.title("📋 Relatórios")

    if len(df_filtrado) > 0:
        st.subheader("📊 Resumo Estatístico")
        st.dataframe(df_filtrado.describe(), use_container_width=True)

        st.subheader("📈 Relatório por Situação")
        relatorio_situacao = df_filtrado.groupby("Situação").agg({
            "Valor": ["count", "sum", "mean"],
            "Honorário (5%)": "sum",
            "Documentos Anexados (%)": "mean"
        }).round(2)
        st.dataframe(relatorio_situacao, use_container_width=True)
    else:
        st.info("Nenhum dado encontrado com os filtros aplicados.")


# -------------------------------------------------
# Página de Configurações
# -------------------------------------------------
def configuracoes():
    st.title("⚙️ Configurações")

    st.subheader("🎨 Personalização")
    st.info(
        "A alteração de tema não é suportada diretamente em tempo de execução. Por favor, use as configurações do Streamlit no menu hambúrguer (☰) no canto superior direito para mudar o tema.")

    st.subheader("📊 Configurações de Dados")
    taxa_honorarios = st.slider("Taxa de Honorários (%):", 1, 10, 5)

    st.subheader("🔔 Notificações")
    alertas_email = st.checkbox("Receber alertas por email")
    limite_documentos = st.slider("Limite para alerta de documentos (%):", 50, 100, 90)

    if st.button("💾 Salvar Configurações"):
        st.success("Configurações salvas com sucesso!")


def export_excel(dataframe):
    try:
        path = "/home/ubuntu/relatorio_precatorios.xlsx"
        dataframe.to_excel(path, index=False)
        return path
    except Exception as e:
        st.error(f"Erro ao exportar: {e}")
        return None


# -------------------------------------------------
# Aplicação Principal
# -------------------------------------------------
def main():
    # Carregar dados
    df = carregar_dados()

    # Criar menu lateral e obter seleções
    pagina_selecionada, filtros = criar_menu_lateral()

    # Aplicar filtros
    df_filtrado = aplicar_filtros(df, filtros)

    # Navegação entre páginas
    if pagina_selecionada == "📊 Dashboard Principal":
        dashboard_principal(df_filtrado)
    elif pagina_selecionada == "📈 Análises Avançadas":
        analises_avancadas(df_filtrado)
    elif pagina_selecionada == "📋 Relatórios":
        relatorios(df_filtrado)
    elif pagina_selecionada == "⚙️ Configurações":
        configuracoes()

    # Verificar se deve exportar
    if hasattr(st.session_state, "exportar") and st.session_state.exportar:
        arquivo = export_excel(df_filtrado)
        if arquivo:
            st.success(f"✅ Relatório exportado como {arquivo}")
        st.session_state.exportar = False


if __name__ == "__main__":
    main()

# Para executar o projeto:
# streamlit run projeto_modificado.py

