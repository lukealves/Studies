endereco = "Rua Vila Strangiato 78, apartamento 2112, Embu das Artes, São Paulo, SP, 19780-012"


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)