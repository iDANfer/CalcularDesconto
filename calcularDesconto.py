precoProduto = float(input("Informe o preço do produto: "))
descontoProduto = float(input("Informe o Valor do Desconto em %:"))


def valorDesconto(precoProduto, descontoProduto):
    descontoFinal = precoProduto * descontoProduto / 100
    return descontoFinal


def valorFinal(precoProduto, descontoProduto):
    desconto = valorDesconto(precoProduto, descontoProduto)
    precofinal = precoProduto - desconto
    return precofinal


resultadoDesconto = valorDesconto(precoProduto, descontoProduto)
resultadoFinal = valorFinal(precoProduto, resultadoDesconto)

print("O Valor Final é:", resultadoFinal)
