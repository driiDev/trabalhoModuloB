print('Bem-vindo a loja da Andrielle Soares da Silva')

valorDoPedido = float(input('Entre com o valor do pedido: '))
quantidadeParcelas = int(input('Entre com a quantidade de parcelas: '))


def calcular_valores(valorDoPedido, quantidadeParcelas, juros): # recebe os valores como parâmetro
    valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas
    return valorDaParcela, valorTotalParcelado # retorna os valores calculados

def mostrar_valores(valorDaParcela, valorTotalParcelado):
    print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
    print(f'O valor Total Parcelado é de: R$ {valorTotalParcelado:.2f}')

if quantidadeParcelas < 4:
    juros = 0 / 100

elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4/100

elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100

elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100

else:
    juros = 32 / 100

valorDaParcela, valorTotalParcelado = calcular_valores(valorDoPedido, quantidadeParcelas, juros)
mostrar_valores(valorDaParcela, valorTotalParcelado)
