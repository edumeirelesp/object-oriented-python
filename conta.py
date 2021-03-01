import abc


class Conta(abc.ABC):

    def __init__(self, numero, cliente , saldo, limite):
        self._numero = numero
        self._titular = cliente.to_string()
        self._saldo = saldo
        self._limite = limite

    def saldo(self):
        return self._saldo

    @abc.abstractmethod
    def atualiza(self, taxa):
        # self._saldo += self._saldo * taxa
        pass

    def deposita(self, valor):
        if valor < 0:
            raise ValueError("Você tentou deposita um valor negativo!")
        else:
            self._saldo += valor

    def saca(self, valor):
        if valor < 0:
            raise ValueError("Você tentou sacar um valor negativo!")

        else:
            if self._saldo >= valor:
                self._saldo -= valor
                return True

            else:
                return False

    def transfere(self, destino, valor):
        if not self.saca(valor):
            return False

        else:
            destino.deposita(valor)

    def extrato(self):
        return f"~~~~~~~~~~~~~~~~~~~~~~~\nTitular: {self._titular}\nNumero da conta: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}"
