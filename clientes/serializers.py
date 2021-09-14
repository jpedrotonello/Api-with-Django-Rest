from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        return data
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome não é válido"})
        return data
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular não é válido."})

"""     def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não pode haver números neste campo.")
        return nome
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos.")
        return rg """
