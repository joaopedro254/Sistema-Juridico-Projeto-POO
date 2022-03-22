class Advogado:
    def __init__(self, oab, nome, processos):
        self._cod_oab = oab
        self._nome = nome
        self._processos = processos

    @property
    def cod_oab(self):
        return self._cod_oab
    @property
    def nome(self):
        return self._nome
    @property
    def processos(self):
        return self._processos
    @cod_oab.setter
    def cod_oab(self, newCod_oab):
        self._cod_oab = newCod_oab
    @nome.setter
    def nome(self, newNome):
        self._nome = newNome
    @processos.setter
    def processos(self, newProcessos):
        self._processos = newProcessos

    def __str__(self):
        saida = ''
        for i in range(len(self._processos)):
            saida += f'{self._processos[i]}'
        return f'Cod. OAB: {self._cod_oab}, Nome: {self._nome}, Processos: {saida}'

    def lista_clientes(self):
        lista = []
        for i in range(len(self._processos)):
            if self._processos[i].pessoa.nome not in lista:
                lista.append(self._processos[i].pessoa.nome)
        
        saida = ''
        for k in range(len(lista)):
            saida += f'{lista[k]} \n'
        return saida

    def valor_ganho_ADV(self):
        valorTotal = 0
        for i in range(len(self._processos)):
            valorTotal += self._processos[i].custo.valor
        return valorTotal

    def processos_deferidos(self, teste):
        cont = 0
        for i in range(len(self._processos)):
            if self._processos[i].decisao == teste:
                cont += 1
        
        if teste == True:
            return f'\n{cont} processo(s) defendido(s) por {self._nome} foi(ram) deferido(s)\n'
        else:
            return f'\n{cont} processos(s) defendido(s) por {self._nome} foi(ram) indeferido(s)\n'

        
