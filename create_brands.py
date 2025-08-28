import json
import os

OUTPUT_FILE = "marcas.json"

# Carrega lista existente se já houver(OBS: NÃO EDITAR A LISTA EXISTENTE MARCAS.JSON)
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        marcas_data = json.load(f)
else:
    marcas_data = []

# Função para gerar um EAN fictício de 13 dígitos(NÃO MEXER)
def gerar_ean(base=7190000000000, indice=1):
    return str(base - indice)  # Decrementa os eans para evitar duplicatas(NÃO MEXER)

# Lista de novas marcas
novas_marcas = ["Sorriso",
"Listerine",
"Guimarães Produtos de Limpeza",
"Nissin",
"Novo Frescor",
"Brilhante",
"Brilha Sul",
"Alvex",
"Dyssan",
"Klarex",
"Matacura",
"Tacolac",
"Casa KM",
"Peroba",
"Zeppelin",
"Jimo",
"Aplik",
"Best Lite",
"Sulino",
"Personal",
"Clara",
"Inspira",
"Lysoform",
"Florax",
"Santo Brilho",
"Brilholac",
"Gota Limpa",
"Taklim",
"Aquafast",
"Comfort",
"Uau",
"Ramar",
"Ar Gradável",
"Mili",
"Doble",
"Raid",
"Mat Inset",
"Mortein",
"SBP",
"Saif",
"Esfrebom",
"Secar",
"Ypê",
"Qboa",
"Lady Prime",
"Widi Care",
"Kamalẽao Color",
"Felps Professional",
"Braé",
"Forever Liss Professional",
"Alfaparft MIlano",
"Lowell Professional",
"Haskell Cosmética Natural",
"Truss Professional",
"Dimension",
"Plush"]

# Descobrir quantos já existem para não repetir
ultimo_indice = len(marcas_data)

for i, marca in enumerate(novas_marcas, start=1):
    
    if not any(item["brand"] == marca for item in marcas_data):
        ean = gerar_ean(indice=ultimo_indice + i)
        novo_item = {
            "mandatory_terms": [marca],
            "optional_terms": [marca],
            "brand": marca,
            "ean_brand": ean,
            "ean": ean
        }
        marcas_data.append(novo_item)


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(marcas_data, f, indent=4, ensure_ascii=False)

print("Arquivo atualizado:", OUTPUT_FILE)
