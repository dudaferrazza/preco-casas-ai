# 🏢 Preço de Casas

O sistema permite que o usuário informe dados de um imóvel e receba uma **estimativa de valor de mercado**.

---

# 📊 Dataset

O modelo foi treinado utilizando um dataset contendo:

- Área do imóvel (m²)
- Quantidade de quartos
- Quantidade de banheiros
- Preço do imóvel

Exemplo de dados:

| Área | Quartos | Banheiros | Preço |
|-----|-----|-----|-----|
| 50 | 1 | 1 | 150000 |
| 60 | 2 | 1 | 180000 |
| 75 | 2 | 2 | 250000 |
| 100 | 3 | 2 | 350000 |
| 120 | 3 | 3 | 450000 |
| 150 | 4 | 3 | 600000 |
| 200 | 4 | 4 | 800000 |
| 250 | 5 | 4 | 1000000 |
| 300 | 5 | 5 | 1300000 |

Esses dados são utilizados para treinar o modelo de previsão.

---

# ⚙️ Treinamento do modelo

O modelo foi treinado utilizando Regressão Linear, que identifica a relação entre as variáveis de entrada e o preço do imóvel.

Arquivo responsável:

```
train.py
```

Processo realizado:

1. Leitura do dataset
2. Separação das variáveis
3. Treinamento do modelo
4. Salvamento do modelo em arquivo `.pkl`

---

# 📁 Estrutura do projeto

```
preco-casas-ai
│
├── app.py
├── train.py
├── dataset.csv
├── model.pkl
├── requirements.txt
└── README.md
```

Descrição dos arquivos:

- **app.py** → Interface do sistema com Streamlit  
- **train.py** → Script de treinamento do modelo  
- **dataset.csv** → Base de dados utilizada  
- **model.pkl** → Modelo treinado salvo  
- **requirements.txt** → Dependências do projeto  

---

# ▶️ Como executar o projeto

### Clonar o repositório

```bash
git clone https://github.com/dudaferrazza/preco-casas-ai.git
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Treinar o modelo (opcional)

```bash
python train.py
```

### Executar a aplicação

```bash
streamlit run app.py
```
