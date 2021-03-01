class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        print(f"SALDO ANTERIOR:{conta.saldo()}")
        conta.atualiza(self._selic)
        self._saldo_total = conta.saldo()
        print(f"SALDO FINAL:{self._saldo_total}")