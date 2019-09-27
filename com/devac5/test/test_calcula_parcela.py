import pytest
from com.devac5.calcula_parcela import valorPagamento

def valorPagamento():
	calcula_parcela = valorPagamento
	assert valorPagamento([10, 2]) == 10.50 , "O resultado será 10.50"

def valorPagamento1():
	calcula_parcela = valorPagamento
	assert valorPagamento([10, 0]) == 10 , "O resultado será 10"

def valorPagamento2():
	calcula_parcela = valorPagamento
	assert valorPagamento([0, 0]) == 0 , "O resultado será 0"