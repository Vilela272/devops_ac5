import pytest
from com.devac5.operacoes import Multiplicacao

class TestOperacoes():

	def test_mult():
		operacoes = Multiplicacao
		assert test_mult([5,5]) == 25, "Resultado 25" 
