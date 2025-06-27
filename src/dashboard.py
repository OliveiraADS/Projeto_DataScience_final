import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="🏠 Previsão de Preços de Casas",
    page_icon="🏠",
    layout="wide"
)

# Título principal
st.title("🏠 Dashboard - Previsão de Preços de Casas")
st.markdown("### 📊 Insira as características da casa e obtenha o preço previsto instantaneamente!")
st.markdown("---")

# =========================================
# CARREGAR DADOS E MODELO
# =========================================

@st.cache_data
def carregar_dados():
    """Carrega e processa os dados"""
    try:
        df = pd.read_csv('data/train.csv')
        colunas_simples = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'YearBuilt', 'OverallQual', 'SalePrice']
        df_limpo = df[colunas_simples].copy()
        df_limpo = df_limpo.dropna()
        return df_limpo
    except FileNotFoundError:
        st.error("❌ Arquivo data/train.csv não encontrado!")
        # Criar dados exemplo para demonstração
        np.random.seed(42)
        n_samples = 1000
        data = {
            'GrLivArea': np.random.normal(1500, 500, n_samples),
            'BedroomAbvGr': np.random.randint(1, 6, n_samples),
            'FullBath': np.random.randint(1, 4, n_samples),
            'YearBuilt': np.random.randint(1950, 2023, n_samples),
            'OverallQual': np.random.randint(1, 11, n_samples),
            'SalePrice': np.random.normal(200000, 80000, n_samples)
        }
        return pd.DataFrame(data)

@st.cache_resource
def carregar_modelo():
    """Carrega modelo treinado ou treina um novo"""
    try:
        modelo = joblib.load('models/house_price_model.pkl')
        return modelo
    except FileNotFoundError:
        # Se não existir, treina um modelo simples
        df = carregar_dados()
        if df is not None:
            X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'YearBuilt', 'OverallQual']]
            y = df['SalePrice']
            modelo = LinearRegression()
            modelo.fit(X, y)
            return modelo
        return None

# Carregar dados
df = carregar_dados()
modelo = carregar_modelo()

# =========================================
# LAYOUT EM COLUNAS
# =========================================

col1, col2 = st.columns([1, 2])

with col1:
    st.header("🔧 Configure sua Casa")
    
    # INPUTS DO USUÁRIO (baseado no exemplo)
    st.subheader("📋 Características da Casa")
    
    # Área da casa
    area = st.slider(
        "🏠 Área da Casa (sq ft)", 
        min_value=500, 
        max_value=5000, 
        value=2000,  # Valor do exemplo
        step=50
    )
    
    # Número de quartos
    quartos = st.selectbox(
        "🛏️ Número de Quartos", 
        options=[1, 2, 3, 4, 5, 6],
        index=2  # 3 quartos (valor do exemplo)
    )
    
    # Número de banheiros
    banheiros = st.selectbox(
        "🚿 Número de Banheiros", 
        options=[1, 2, 3, 4],
        index=1  # 2 banheiros (valor do exemplo)
    )
    
    # Ano de construção
    ano = st.slider(
        "📅 Ano de Construção", 
        min_value=1950, 
        max_value=2023, 
        value=2010,  # Valor do exemplo
        step=1
    )
    
    # Qualidade geral
    qualidade = st.slider(
        "⭐ Qualidade Geral (1-10)", 
        min_value=1, 
        max_value=10, 
        value=7,  # Valor do exemplo
        step=1
    )
    
    st.markdown("---")
    
    # BOTÃO DE PREVISÃO
    if st.button("🎯 CALCULAR PREÇO", type="primary"):
        if modelo is not None:
            # Fazer previsão (igual ao exemplo do código)
            casa_exemplo = [[area, quartos, banheiros, ano, qualidade]]
            preco_previsto = modelo.predict(casa_exemplo)[0]
            
            # Mostrar resultado
            st.success(f"💰 **Preço Previsto: ${preco_previsto:,.2f}**")
            
            # Salvar no session state para mostrar na coluna 2
            st.session_state['preco_previsto'] = preco_previsto
            st.session_state['casa_config'] = {
                'area': area,
                'quartos': quartos, 
                'banheiros': banheiros,
                'ano': ano,
                'qualidade': qualidade
            }

with col2:
    st.header("📊 Resultados e Análises")
    
    # Mostrar resultado da previsão
    if 'preco_previsto' in st.session_state:
        st.subheader("🏠 Previsão da sua Casa")
        
        # Card com resultado
        st.markdown(f"""
        <div style="background-color: #e8f4fd; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4;">
        <h3 style="color: #1f77b4;">💰 Preço Previsto: ${st.session_state['preco_previsto']:,.2f}</h3>
        <p style="color: #000000;"><strong>Configuração:</strong></p>
        <ul style="color: #000000;">
        <li>📏 Área: {st.session_state['casa_config']['area']} sq ft</li>
        <li>🛏️ Quartos: {st.session_state['casa_config']['quartos']}</li>
        <li>🚿 Banheiros: {st.session_state['casa_config']['banheiros']}</li>
        <li>📅 Ano: {st.session_state['casa_config']['ano']}</li>
        <li>⭐ Qualidade: {st.session_state['casa_config']['qualidade']}/10</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # COMPARAÇÃO COM CASAS SIMILARES REAIS
        st.subheader("🔍 Casas Similares no Dataset")
        
        # Buscar casas similares
        config = st.session_state['casa_config']
        area_min, area_max = config['area'] * 0.9, config['area'] * 1.1
        ano_min, ano_max = config['ano'] - 5, config['ano'] + 5
        qual_min, qual_max = max(1, config['qualidade'] - 1), min(10, config['qualidade'] + 1)
        
        casas_similares = df[
            (df['GrLivArea'].between(area_min, area_max)) &
            (df['BedroomAbvGr'] == config['quartos']) &
            (df['FullBath'] == config['banheiros']) &
            (df['YearBuilt'].between(ano_min, ano_max)) &
            (df['OverallQual'].between(qual_min, qual_max))
        ].head(5)
        
        if len(casas_similares) > 0:
            # Mostrar casas similares
            st.success(f"✅ Encontradas {len(casas_similares)} casas similares no dataset!")
            
            # Calcular estatísticas
            preco_medio_real = casas_similares['SalePrice'].mean()
            preco_min_real = casas_similares['SalePrice'].min()
            preco_max_real = casas_similares['SalePrice'].max()
            
            # Cards de comparação
            col_prev, col_real = st.columns(2)
            
            with col_prev:
                st.markdown(f"""
                <div style="background-color: #fff2e6; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800;">
                <h4 style="color: #ff9800; margin: 0;">🤖 Nosso Modelo</h4>
                <h3 style="margin: 5px 0; color: #000000;">${st.session_state['preco_previsto']:,.0f}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            with col_real:
                st.markdown(f"""
                <div style="background-color: #e8f5e8; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
                <h4 style="color: #4caf50; margin: 0;">🏠 Casas Reais (Média)</h4>
                <h3 style="margin: 5px 0; color: #000000;">${preco_medio_real:,.0f}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            # Análise da precisão
            diferenca = st.session_state['preco_previsto'] - preco_medio_real
            erro_percentual = abs(diferenca) / preco_medio_real * 100
            
            if abs(diferenca) < 10000:
                cor_alerta = "success"
                icone = "✅"
                status = "Excelente"
            elif abs(diferenca) < 25000:
                cor_alerta = "info"
                icone = "ℹ️"
                status = "Boa"
            else:
                cor_alerta = "warning"
                icone = "⚠️"
                status = "Razoável"
            
            getattr(st, cor_alerta)(f"""
            {icone} **Precisão {status}:** Diferença de ${abs(diferenca):,.0f} ({erro_percentual:.1f}%)
            
            📊 **Faixa de preços reais:** ${preco_min_real:,.0f} - ${preco_max_real:,.0f}
            """)
            
            # Tabela detalhada das casas similares
            with st.expander("📋 Ver detalhes das casas similares"):
                casas_display = casas_similares[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'YearBuilt', 'OverallQual', 'SalePrice']].copy()
                casas_display.columns = ['Área (sq ft)', 'Quartos', 'Banheiros', 'Ano', 'Qualidade', 'Preço Real']
                casas_display['Preço Real'] = casas_display['Preço Real'].apply(lambda x: f"${x:,.0f}")
                st.dataframe(casas_display, use_container_width=True)
        
        else:
            # Busca mais ampla se não encontrar casas similares
            st.warning("⚠️ Não encontramos casas exatamente iguais. Buscando casas similares...")
            
            casas_amplas = df[
                (df['GrLivArea'].between(config['area'] * 0.8, config['area'] * 1.2)) &
                (df['BedroomAbvGr'].between(max(1, config['quartos'] - 1), config['quartos'] + 1)) &
                (df['YearBuilt'].between(config['ano'] - 10, config['ano'] + 10))
            ].head(10)
            
            if len(casas_amplas) > 0:
                preco_medio_amplo = casas_amplas['SalePrice'].mean()
                st.info(f"""
                🔍 **Casas com características similares:**
                - {len(casas_amplas)} casas encontradas
                - Preço médio: ${preco_medio_amplo:,.0f}
                - Sua previsão: ${st.session_state['preco_previsto']:,.0f}
                - Diferença: ${abs(st.session_state['preco_previsto'] - preco_medio_amplo):,.0f}
                """)
            else:
                st.error("❌ Não foram encontradas casas similares no dataset para comparação.")
        
    # Estatísticas do dataset
    if df is not None:
        st.subheader("📈 Estatísticas do Dataset")
        
        col2_1, col2_2, col2_3 = st.columns(3)
        
        with col2_1:
            st.metric(
                "🏠 Total de Casas", 
                f"{len(df):,}"
            )
            
        with col2_2:
            st.metric(
                "💰 Preço Médio", 
                f"${df['SalePrice'].mean():,.0f}"
            )
            
        with col2_3:
            st.metric(
                "📏 Área Média", 
                f"{df['GrLivArea'].mean():.0f} sq ft"
            )

# =========================================
# GRÁFICOS
# =========================================

if df is not None:
    st.markdown("---")
    st.header("📊 Visualizações dos Dados")
    
    # Tabs para diferentes gráficos
    tab1, tab2, tab3 = st.tabs(["📈 Área vs Preço", "📊 Distribuição de Preços", "🔥 Correlações"])
    
    with tab1:
        # Gráfico área vs preço
        fig = px.scatter(
            df, 
            x='GrLivArea', 
            y='SalePrice',
            title="Relação entre Área e Preço das Casas",
            labels={'GrLivArea': 'Área (sq ft)', 'SalePrice': 'Preço ($)'}
        )
        
        # Adicionar ponto da casa do usuário se existir
        if 'casa_config' in st.session_state:
            fig.add_trace(go.Scatter(
                x=[st.session_state['casa_config']['area']], 
                y=[st.session_state['preco_previsto']],
                mode='markers',
                marker=dict(size=15, color='red'),
                name='Sua Casa'
            ))
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Histograma de preços
        fig = px.histogram(
            df, 
            x='SalePrice', 
            nbins=50,
            title="Distribuição dos Preços das Casas"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        # Mapa de correlação
        correlation_matrix = df.corr()
        fig = px.imshow(
            correlation_matrix,
            title="Correlação entre Variáveis",
            aspect="auto",
            color_continuous_scale=[[0, 'white'], [0.5, 'lightcoral'], [1, 'darkred']],
            zmin=-1, zmax=1
        )
        fig.update_layout(
            title_font_color='black',
            font_color='black'
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================================
# EXEMPLOS PRÉ-DEFINIDOS
# =========================================

st.markdown("---")
st.header("🏠 Exemplos Pré-definidos")
st.markdown("Clique nos botões abaixo para testar diferentes tipos de casas:")

col_ex1, col_ex2, col_ex3 = st.columns(3)

with col_ex1:
    if st.button("🏠 Casa Simples"):
        st.session_state.update({
            'area_ex': 1200,
            'quartos_ex': 2,
            'banheiros_ex': 1,
            'ano_ex': 1980,
            'qualidade_ex': 5
        })

with col_ex2:
    if st.button("🏡 Casa Média"):
        st.session_state.update({
            'area_ex': 2000,
            'quartos_ex': 3,
            'banheiros_ex': 2,
            'ano_ex': 2010,
            'qualidade_ex': 7
        })

with col_ex3:
    if st.button("🏰 Casa Luxo"):
        st.session_state.update({
            'area_ex': 3500,
            'quartos_ex': 5,
            'banheiros_ex': 4,
            'ano_ex': 2020,
            'qualidade_ex': 9
        })

# Mostrar exemplo selecionado
if 'area_ex' in st.session_state:
    casa_exemplo = [[
        st.session_state['area_ex'],
        st.session_state['quartos_ex'],
        st.session_state['banheiros_ex'],
        st.session_state['ano_ex'],
        st.session_state['qualidade_ex']
    ]]
    
    if modelo is not None:
        preco_exemplo = modelo.predict(casa_exemplo)[0]
        
        st.info(f"""
        🏠 **Exemplo Selecionado:**
        - Área: {st.session_state['area_ex']} sq ft
        - Quartos: {st.session_state['quartos_ex']}
        - Banheiros: {st.session_state['banheiros_ex']}
        - Ano: {st.session_state['ano_ex']}
        - Qualidade: {st.session_state['qualidade_ex']}/10
        
        💰 **Preço Previsto: ${preco_exemplo:,.2f}**
        """)

# =========================================
# FOOTER
# =========================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
<p>🎓 Projeto desenvolvido para Data Science - Princípios e Técnicas</p>
<p>🔧 Dashboard criado com Streamlit | 🤖 Modelo: Regressão Linear</p>
</div>
""", unsafe_allow_html=True)