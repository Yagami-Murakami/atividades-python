nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", percentual_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))
