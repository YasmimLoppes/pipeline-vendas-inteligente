import pandas as pd
import os

# Localiza a pasta raiz a partir da pasta scripts
diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_raiz = os.path.dirname(diretorio_script)
caminho_data = os.path.join(diretorio_raiz, 'data')

# Garante que a pasta 'data' exista
if not os.path.exists(caminho_data):
    os.makedirs(caminho_data)

# Dados para o portfólio (2026)
dados = {
    'data_compra': ['2026-01-01', '2026-01-10', '2026-02-01', '2026-02-15', '2026-03-01'],
    'categoria': ['Eletrônicos', 'Moda', 'Eletrônicos', 'Alimentos', 'Moda'],
    'valor': [1500.0, 250.0, 1200.0, 150.0, 300.0],
    'id_cliente': [101, 102, 101, 103, 104]
}
df = pd.DataFrame(dados)

# Salva os arquivos de fato
df.to_csv(os.path.join(caminho_data, 'vendas_bruto.csv'), index=False)
df.to_csv(os.path.join(caminho_data, 'vendas_limpo.csv'), index=False)

print("Sucesso! Arquivos gerados com dados reais na pasta data.")