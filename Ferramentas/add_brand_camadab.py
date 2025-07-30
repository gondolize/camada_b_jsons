import json
import re
from collections import OrderedDict

# Lê o arquivo original
with open('produtos.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

novo_dados = []

# Reorganiza os campos para garantir que "ean" fique por último
for item in dados:
    brand = item["mandatory_terms"][0] if item["mandatory_terms"] else ""
    
    novo_item = OrderedDict()
    novo_item["mandatory_terms"] = item["mandatory_terms"]
    ##novo_item["optional_terms"] = item["optional_terms"]
    novo_item["brand"] = brand
    novo_item["ean"] = item["ean"]
    
    novo_dados.append(novo_item)

# Serializa com indentação
json_formatado = json.dumps(novo_dados, indent=4, ensure_ascii=False, separators=(',', ': '))

# Regex: mantém listas simples em uma linha
json_formatado = re.sub(
    r'\[\n\s+(".*?")((?:,\n\s*".*?")*)\n\s+\]',
    lambda m: '[' + ', '.join(x.strip() for x in (m.group(1) + m.group(2)).split(',')) + ']',
    json_formatado
)

# Salva no arquivo final
with open('produtos_com_brand_tree.json', 'w', encoding='utf-8') as f:
    f.write(json_formatado)
