# 🚗 Análise e Previsão de Preços de Carros Usados

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-green.svg)](https://scikit-learn.org/)

Este repositório contém um projeto completo de Data Science, desde a análise exploratória de dados até a criação de um modelo preditivo para prever preços de carros usados no mercado americano.

**Autor:** [Seu Nome]  
**Data:** 27/06/2025  
**Vídeo Explicativo:** [🔗 INSERIR_LINK_AQUI]

---

## 🎯 Descrição do Problema

Uma concessionária de carros usados precisa de uma ferramenta automatizada e precisa para avaliar o preço justo de veículos em seu estoque. O objetivo deste projeto é desenvolver um modelo de Machine Learning capaz de estimar o valor de mercado de carros usados com base em suas características técnicas, históricas e de marca.

**Benefícios esperados:**
- Otimização da precificação
- Maior competitividade para o cliente
- Vantagem financeira para o negócio

---

## 📁 Estrutura do Projeto

```
DataSciece_Recuperacao_MeuNome/
│
├── 📂 data/
│   └── 📄 used_cars.csv
│
├── 📂 img/
│   ├── 🖼️ analise_precos.png
│   ├── 🖼️ correlacao_matriz.png
│   ├── 🖼️ analise_categorias.png
│   └── 🖼️ resultados_modelo.png
│
├── 📂 models/
│   ├── 📦 modelo_precos_carros.pkl
│   ├── 📦 label_encoders.pkl
│   └── 📦 features_info.pkl
│
├── 📂 notebooks/
│   └── 📓 Analise_Carros_usados.ipynb
│
├── 📂 src/
│   └── (Scripts Python reutilizáveis)
│
├── 📜 requirements.txt
└── 📄 README.md
```

---

## 🚀 Guia de Instalação e Execução

### Pré-requisitos

- [Python 3.8+](https://www.python.org/)
- Git
- Jupyter Notebook

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/[seu-usuario]/DataSciece_Recuperacao_MeuNome.git
cd DataSciece_Recuperacao_MeuNome
```

### Passo 2: Configure o Ambiente Virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### Passo 3: Instale as Dependências

```bash
ip install pandas numpy matplotlib seaborn scikit-learn plotly jupyter
```

### Passo 4: Execute a Análise

```bash
jupyter notebook notebooks/Analise_Carros_usados.ipynb
```

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Limpeza e Preparação:** Tratamento de valores ausentes, criação de variáveis derivadas (idade do carro) e codificação com Label Encoding
- **Análise Exploratória (EDA):** Geração de histogramas, boxplots, scatter plots e matriz de correlação com Matplotlib e Seaborn
- **Modelagem Preditiva:** Treinamento e avaliação de modelo Random Forest Regressor do Scikit-learn
- **Ambiente de Desenvolvimento:** Análise realizada em Jupyter Notebook com VS Code
- **Versionamento:** Controle de versão realizado com Git e GitHub

---

## 📊 Resultados e Métricas do Modelo

### Métricas de Avaliação

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **R² Score** | [INSERIR_VALOR] | O modelo explica [X]% da variação dos preços |
| **RMSE** | $[INSERIR_VALOR] | Erro médio quadrático |
| **MAE** | $[INSERIR_VALOR] | Erro médio absoluto |

### Características do Dataset

- **52 veículos** analisados
- **27 características** por veículo
- **Período:** 2014 a 2022
- **Faixa de preços:** $13.590 a $33.777

### Variáveis Mais Importantes

1. **Ano do carro** - Maior impacto na determinação do preço
2. **Quilometragem** - Segunda maior influência (correlação negativa)
3. **Marca** - Especialmente Honda vs outras marcas

---

## 💡 Principais Descobertas

### Insights da Análise

- **Domínio da Honda:** A marca Honda representa 44% do dataset (23 de 52 carros), demonstrando forte presença no mercado de usados
- **Depreciação por Idade:** Existe uma correlação negativa clara entre idade do veículo e seu valor de mercado
- **Impacto da Quilometragem:** Carros com maior quilometragem apresentam preços significativamente menores
- **Carros Híbridos:** Veículos híbridos mantêm valor superior comparado aos convencionais a gasolina
- **Eficácia do Modelo:** O Random Forest mostrou-se uma ferramenta eficaz para previsão de preços

---

## 🔄 Conclusões e Próximos Passos

### Conclusões

✅ O modelo Random Forest apresentou boa capacidade preditiva para estimar preços de carros usados  
✅ Ano de fabricação e quilometragem são os fatores mais determinantes na precificação  
✅ A marca Honda demonstra comportamento diferenciado no mercado, mantendo valor superior  

### Melhorias Futuras

- [ ] Expandir o dataset com mais veículos e marcas diversificadas
- [ ] Incluir variáveis geográficas (localização, mercado regional)
- [ ] Testar algoritmos alternativos (XGBoost, Gradient Boosting, Redes Neurais)
- [ ] Implementar validação cruzada para melhor avaliação da generalização
- [ ] Adicionar dados de mercado (sazonalidade, tendências econômicas)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

## 📚 Contexto Acadêmico

**Disciplina:** Data Science - Princípios e Técnicas  
**Instituição:** [Nome da Instituição]

---

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através de [seu-email@exemplo.com]

---

<div align="center">
  <strong>Feito com ❤️ e Python</strong>
</div>
