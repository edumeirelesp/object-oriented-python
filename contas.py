from collections.abc import MutableSequence

from conta import Conta


class Contas(MutableSequence):
    _dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, item):
        return self._dados[item]

    def __setitem__(self, key, value):
        if isinstance(value, Conta):
            self._dados[key] = value

        else:
            raise ValueError(f"Valor {value} não é de Conta!!")

    def __delitem__(self, key):
        del self._dados[key]

    def insert(self, index, value):
        if isinstance(value, Conta):
            return self._dados.insert(index, value)

        else:
            raise ValueError(f"Valor {value} não é de Conta!!")


if __name__ == '__main__':
    contas = Contas()

    print(contas)