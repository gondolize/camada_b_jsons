import json

# Lê o JSON(escolha se quer ver da tree_base ou camadab_base)
with open('camadab_base.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Usa set para armazenar EANs únicos
eans_unicos = set()

# Adiciona cada EAN ao set
for item in dados:
    ean = item.get("ean")
    if ean:
        eans_unicos.add(ean)

# Exibe resultado
print(f"Quantidade de EANs únicos: {len(eans_unicos)}")
