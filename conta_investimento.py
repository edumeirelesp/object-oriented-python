from conta import Conta


class ContaInvestimento(Conta):

    def get_valor_imposto(self):
        return self._saldo * 0.03

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5