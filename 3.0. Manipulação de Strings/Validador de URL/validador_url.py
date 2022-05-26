'''
Verifica se a base da URL está de acordo com o padrão correto.

Exemplos de URLs válidas:
    mobank.com/cambio
    mobank.com.br/cambio
    www.mobank.com/cambio
    www.mobank.com.br/cambio
    http://www.mobank.com/cambio
    http://www.mobank.com.br/cambio
    https://www.mobank.com/cambio
    https://www.mobank.com.br/cambio

Exemplos de URL inválidas:
    https://mobank/cambio
    http://mobank.naoexiste/cambio
    ht:mobank.naoexiste/cambio
'''
# https://www.mobank.com.br/cambio
import re

url = 'www.mobank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?mobank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")