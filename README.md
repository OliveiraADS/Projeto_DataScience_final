Análise e Previsão de Preços de Carros Usados 🚗
Este repositório contém um projeto completo de Data Science, desde a análise exploratória de dados até a criação de um modelo preditivo para prever preços de carros usados no mercado americano.
Autor: Deyvi Dos Santos Oliveira 
Data: 27/06/2025

Assista ao Vídeo Explicativo do Projeto: [🔗 INSERIR_LINK_AQUI]

🎯 1. Descrição do Problema
Uma concessionária de carros usados precisa de uma ferramenta automatizada e precisa para avaliar o preço justo de veículos em seu estoque. O objetivo deste projeto é desenvolver um modelo de Machine Learning capaz de estimar o valor de mercado de carros usados com base em suas características técnicas, históricas e de marca. Uma previsão precisa permite à empresa otimizar a precificação, tornando-a mais competitiva para o cliente e financeiramente vantajosa para o negócio.
🗂️ 2. Estrutura do Projeto
📂 DataSciece_Recuperacao_MeuNome/
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
🚀 3. Guia de Utilização do Projeto
Siga os passos abaixo para configurar e executar este projeto em sua máquina local.
Pré-requisitos:

Python 3.8+ (https://www.python.org/)
Git
Jupyter Notebook

Passo 1: Clone o Repositório
Abra seu terminal e clone este repositório para sua máquina local:
shgit clone https://github.com/[seu-usuario]/DataSciece_Recuperacao_MeuNome.git
shcd DataSciece_Recuperacao_MeuNome
Passo 2: Configure o Ambiente Virtual
É uma boa prática criar um ambiente virtual para isolar as dependências.
Criar o ambiente virtual (venv):
shpython -m venv venv
Ativar o ambiente virtual:
No Windows:
shvenv\Scripts\activate
No macOS/Linux:
shsource venv/bin/activate
Passo 3: Instale as Dependências
Com o ambiente virtual ativo, instale todas as bibliotecas necessárias:
shpip install -r requirements.txt
Passo 4: Execute a Análise
Para ver todo o processo de análise, limpeza, treinamento e avaliação do modelo:
Inicie o Jupyter Notebook:
shjupyter notebook notebooks/Analise_Carros_usados.ipynb
🛠️ 4. Técnicas e Ferramentas Utilizadas

Limpeza e Preparação: Tratamento de valores ausentes, criação de variáveis derivadas (idade do carro) e codificação com Label Encoding
Análise Exploratória (EDA): Geração de histogramas, boxplots, scatter plots e matriz de correlação com Matplotlib e Seaborn
Modelagem Preditiva: Treinamento e avaliação de modelo Random Forest Regressor do Scikit-learn
Ambiente de Desenvolvimento: Análise realizada em Jupyter Notebook com VS Code
Versionamento: Controle de versão realizado com Git e GitHub

📊 5. Resultados e Métricas do Modelo
O modelo foi avaliado utilizando R² (Coeficiente de Determinação), RMSE (Raiz do Erro Quadrático Médio) e MAE (Erro Médio Absoluto).
MétricaValorInterpretaçãoR² Score[INSERIR_VALOR]O modelo explica [X]% da variação dos preçosRMSE$[INSERIR_VALOR]Erro médio quadráticoMAE$[INSERIR_VALOR]Erro médio absoluto
Dataset Utilizado:

52 veículos analisados
27 características por veículo
Período: 2014 a 2022
Faixa de preços: $13.590 a $33.777

Variáveis Mais Importantes:

Ano do carro - Maior impacto na determinação do preço
Quilometragem - Segunda maior influência (correlação negativa)
Marca - Especialmente Honda vs outras marcas

💡 6. Principais Descobertas
A análise exploratória e a modelagem permitiram concluir que:

Domínio da Honda: A marca Honda representa 44% do dataset (23 de 52 carros), demonstrando forte presença no mercado de usados
Depreciação por Idade: Existe uma correlação negativa clara entre idade do veículo e seu valor de mercado
Impacto da Quilometragem: Carros com maior quilometragem apresentam preços significativamente menores
Carros Híbridos: Veículos híbridos mantêm valor superior comparado aos convencionais a gasolina
Eficácia do Modelo: O Random Forest mostrou-se uma ferramenta eficaz para previsão de preços, servindo como base sólida para avaliação automatizada de veículos

🔄 7. Conclusão e Sugestões
Conclusões:

O modelo Random Forest apresentou boa capacidade preditiva para estimar preços de carros usados
Ano de fabricação e quilometragem são os fatores mais determinantes na precificação
A marca Honda demonstra comportamento diferenciado no mercado, mantendo valor superior

Melhorias Futuras:

Expandir o dataset com mais veículos e marcas diversificadas
Incluir variáveis geográficas (localização, mercado regional)
Testar algoritmos alternativos (XGBoost, Gradient Boosting, Redes Neurais)
Implementar validação cruzada para melhor avaliação da generalização
Adicionar dados de mercado (sazonalidade, tendências econômicas)


📊 Tecnologias: Python | Pandas | Scikit-learn | Matplotlib | Seaborn | Jupyter
🎓 Disciplina: Data Science - Princípios e Técnicas
🏫 Instituição: [Nome da Instituição]