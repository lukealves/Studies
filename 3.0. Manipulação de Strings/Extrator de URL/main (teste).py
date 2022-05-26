# ExtratorURL no arquivo extrator_url.py
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"      

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e parâmetros
indice_interrogacao = url.find('?')                                              # indice_interrogacao = chama um método do objeto string chamado .find(), e passa para ele o ponto de interrogação entre aspas simples como parâmetro. E assim retornar a posição ou o índice do meu caractere interrogação nessa URL. 
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]                                     # Ela vai receber o fatiamento da minha URL original a partir de certa posição.
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1                       #A função len() retorna a quantidade de elementos de qualquer lista.
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)


# Os parâmetros da URL funcionam como se fossem variáveis que são passadas para o nosso programa. Por exemplo: temos a primeira variável "q=nome", e esse "q" é uma abreviação de query, do inglês, que significa "consulta", ou seja, qual foi a busca ou a consulta que foi feita.
# Na parte dos parâmetros da URL, teremos o "e comercial" (&), que serve para separar esses parâmetros. Então temos o nosso segundo parâmetro aqui, src, que é da abreviação de source, do inglês, origem, ou seja, vai indicar para a nossa aplicação qual foi a origem daquela consulta.
# a primeira que vem antes do ponto de interrogação, que é o que estamos chamando de base da URL, e essa parte que vem depois do ponto de interrogação, que é o que estamos chamando dos parâmetros da URL.

# Por Exemplo: "query=manipulação+de+strings":
  # “query” é o nome do parâmetro e “manipulação+de+strings” é o valor deste parâmetro.
  # A utilização dos símbolos de adição (+) é feita porque não podemos utilizar espaços em branco em URLs. Note que o símbolo “?” não faz parte dos parâmetros, pois é apenas o separador: base?parâmetros.

#  O fatiamento é uma funcionalidade do Python onde você consegue extrair um pedaço de uma string:
   # Por Exemplo: Temos uma variável 'texto' , e vou dar para essa variável o valor de uma string texto = ’abcde’. Essa String contém cinco caracteres começando no 0.
   # Isso significa que eu posso, por exemplo, acessar um dos caracteres através da posição. Para eu fazer isso eu utilizo os colchetes. Por exemplo, aqui em texto eu coloco o texto na posição texto[0] e ao apertar “Enter” ele me retornou o caractere ‘a’, porque é aquele caractere que está na posição 0.
    #>>> texto = 'abcde'
    #>>> texto[0]
    #>>> 'a'

# Se eu quiser extrair o "a" e o "b" eu preciso buscar por texto, posição 0: inicial e a posição final exclusiva 2, ou seja, até antes do 2, logo, a posição 1, texto[0:2]. E assim ele me retorna ’ab’.
    #>>> texto = 'abcde'
    #>>> texto[0]
    #'a'

    #>>> texto[0:1]
    #'a'

    #>>>texto[0:2]
    #'ab'

# O fatiamento é uma das características das strings no Python, porque elas são imutáveis, depois de serem criadas, elas não podem ser alteradas, você só pode geralmente extrair pedaços dela, que na verdade vão ser novas cópias a partir dela.

# Método find():
  # Exemplo: Temos a variável 'texto = ‘abcde’' e eu posso colocar aqui texto.find e eu quero buscar, por exemplo, a letra ‘c’, texto.find('c') . O que será que ele retorna? Retornou 2, que é a posição da letra ‘c’ naquela string original, ou seja, o ‘a’ na 0, ‘b’ na 1 e ‘c’ na 2.
    #>>> texto = 'abcde'
    #>>> texto.find('c')
    #2
  # Assim nós conseguiríamos dar um find no nosso ponto de interrogação para poder utilizar isso dinamicamente, ou seja, mesmo que a minha URL mude um pouco de tamanho, ele vai sempre retornar a posição do meu ponto de interrogação onde ele estiver.