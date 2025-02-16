import csv

def reduzir_preco(csv_entrada, csv_saida, coluna_preco, coluna_desconto):
    with open(csv_entrada, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = list(leitor)
    
    if coluna_preco not in dados[0] or coluna_desconto not in dados[0]:
        raise ValueError(f"Colunas '{coluna_preco}' ou '{coluna_desconto}' não encontradas no arquivo CSV.")
    
    for linha in dados:
        try:
            preco_atual = float(linha[coluna_preco].strip() or 0)  
            desconto_atual = float(linha[coluna_desconto].strip() or 0)
        except ValueError:
            print(f"Erro ao converter os valores: {linha}")
            continue  

        novo_preco = preco_atual * 0.77 #change here / discount %
        novo_desconto = (desconto_atual / preco_atual) * novo_preco if preco_atual != 0 else 0
        
        linha[coluna_preco] = f"{novo_preco:.2f}"
        linha[coluna_desconto] = f"{novo_desconto:.2f}"
    
    with open(csv_saida, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
        escritor.writeheader()
        escritor.writerows(dados)
    
    print(f"Arquivo atualizado salvo como: {csv_saida}")

reduzir_preco("input.csv", "output.csv", "price", "discountValue")
