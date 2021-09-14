import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()

def celular_valido(numer_celular):
    """Verifica se o celular é válido (11 44444-5555)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numer_celular)
    return resposta