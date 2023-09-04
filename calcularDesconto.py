precoProduto = float(input("Informe o preço do produto: "))
descontoProduto = float(input("Informe o Valor do Desconto: "))

def valorDesconto(precoProduto, descontoProduto):
    descontoFinal = precoProduto * descontoProduto / 100
    return descontoFinal

def valorFinal(precoProduto, descontoProduto):
    desconto = valorDesconto(precoProduto, descontoProduto)
    precofinal = precoProduto - desconto
    return precofinal

resultadoDesconto = valorDesconto(precoProduto, descontoProduto)
resultadoFinal = valorFinal(precoProduto, descontoProduto)

print("O Valor do Desconto é:", resultadoDesconto)
print("O Valor Final é:", resultadoFinal)
