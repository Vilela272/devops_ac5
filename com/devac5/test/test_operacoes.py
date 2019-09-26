from pytest
from com.devac5.operacoes import Multiplicacao

class TestOperacoes(TestCase):

	def test_mult():
		operacoes = Multiplicacao
		assert operacoes.mult([5,5]), 25, "Resultado 25" 
