from conta import Conta
from saldo_insuficiente import SaldoInsuficienteError


class ContaCorrente(Conta):

    def get_valor_imposto(self):
        return self._saldo * 0.01

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        if valor < 0:
            raise ValueError("Você tentou deposito um valor negativo!")

        else:
            self._saldo += valor - 0.10

    def  saca(self, valor):
        if valor < 0:
            raise ValueError("Você tentou sacar um valor negativo!")
        elif self._saldo < valor:
            raise SaldoInsuficienteError()
        else:
            self._saldo -= (valor + 0.10)

