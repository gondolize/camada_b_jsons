import json
import re
from collections import OrderedDict


brand_ean_map = {
    "PANTENE": "7500000000001",
    "EUDORA": "7200000000002",
    "ABOVE": "7300000000003",
    "VULT": "7400000000004",
    "MONANGE": "7500000000005",
    "TRESEMME": "7600000000006",
    "CLEAR": "7700000000007",
    "SHOULDERS": "7110000000008",
    "ELSEVE": "7800000000002",
    "DOVE": "7891150000000",
    "SEDA": "7900000000009",
    "PALMOLIVE": "7100000000001",
    "DARLING": "7130000000013",
    "OX": "7130000000014",
    "SALON":"7150000000015",
    "RAVOR":"7160000000016",
    "NOVEX":"7170000000017",
    "ORIGEM":"7180000000018"
    
}
brands =["PANTENE","EUDORA","ABOVE","VULT","MONANGE","TRESEMME","CLEAR","SHOULDERS","ELSEVE","DOVE","SEDA","PALMOLIVE","DARLING"]

# Lê o arquivo original
with open('camadab_base.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

novo_dados = []

# Reorganiza os campos para garantir que "ean" fique por último
for item in dados:
    mandatory_items=item["mandatory_terms"]
    for manditm in mandatory_items:
        if brands.__contains__(manditm):
            brand=manditm
        
    ean_brand = brand_ean_map.get(brand, "0")

    
    novo_item = OrderedDict()
    novo_item["mandatory_terms"] = item["mandatory_terms"]
    novo_item["optional_terms"] = item["optional_terms"]
    novo_item["brand"] = brand
    novo_item["ean_brand"] = ean_brand
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
with open('produtos_com_ean_brand.json', 'w', encoding='utf-8') as f:
    f.write(json_formatado)
