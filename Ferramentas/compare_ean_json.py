import json

def comparar_json(tree_file, camadab_file, output_file="resultado.json"):
    # Carrega os arquivos
    with open(tree_file, "r", encoding="utf-8") as f:
        tree_data = json.load(f)

    with open(camadab_file, "r", encoding="utf-8") as f:
        camadab_data = json.load(f)

    # Extrai os EANs do tree_base
    eans_tree = {item["ean"] for item in tree_data}

    # Filtra apenas os itens da camadab_base cujo EAN não está no tree_base
    diff_items = [item for item in camadab_data if item["ean"] not in eans_tree]

    # Remove campos indesejados
    for item in diff_items:
        item.pop("optional_terms", None)
        item.pop("ean_brand", None)

    # Gerar string com listas inline
    json_str = ",\n".join(
        json.dumps(item, ensure_ascii=False, separators=(', ', ': '))
        for item in diff_items
    )

    # Recolocar indentação de 4 espaços só nos objetos principais
    json_str = json_str.replace("{", "{\n    ").replace("}", "\n}")

    # Salvar em arquivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(json_str)

    print(f"✅ Comparação concluída! {len(diff_items)} itens salvos em {output_file}")


if __name__ == "__main__":
    comparar_json("tree_base.json", "camadab_base.json")
