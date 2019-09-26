import pytest
from com.devac5.calcula_parcela import valorPagamento

def valorPagamento():
	calcula_parcela = valorPagamento
	assert valorPagamento([10, 2]) == 10.50 , "O resultado será 10.50"

