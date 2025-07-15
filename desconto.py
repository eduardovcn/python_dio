descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()


# TODO: Aplique o desconto se o cupom for válido:

if cupom == 'DESCONTO10':
  preco_final = preco - (preco * descontos["DESCONTO10"])
  print(preco_final)
elif cupom == 'DESCONTO20':
  preco_final = preco - (preco * descontos["DESCONTO20"])
  print(preco_final)
else:
  print(preco)