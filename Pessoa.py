class Pessoa:
    def __init__(self, cpf, nome, processos):
        self._cpf = cpf
        self._nome = nome
        self._processos = processos
    
    @property
    def cpf(self):
        return self._cpf
    @property
    def nome(self):
        return self._nome
    @property
    def processos(self):
        return self._processos
    @cpf.setter
    def cpf(self, newCPF):
        self._cpf = newCPF
    @nome.setter
    def nome(self, newNome):
        self._nome = newNome
    @processos.setter
    def processos(self, newProcessos):
        self._processos = newProcessos

    def __str__(self):
        saida = ''
        for i in range(len(self._processos)):
            saida += f'{self._processos[i]} '
        return f'CPF: {self._cpf}, Nome: {self._nome}, Processos: {saida}'

    def num_decisoes(self, dec):
        cont = 0
        for i in range(len(self._processos)):
            if self._processos[i].decisao == dec:
                cont += 1
        
        if dec == True:
            return f'\n{cont} processo(s) foi(ram) deferido(s)\n'
        else:
            return f'\n{cont} processos(s) foi(ram) indeferido(s)\n'

    def custo_total(self):
        custoTotal = 0
        for i in range(len(self._processos)):
            custoTotal += self._processos[i].custo.valor
        return custoTotal

    def custo_total_adv(self, cod_oab):
        lista = []
        for i in range(len(self._processos)):
            if self._processos[i].advogado.cod_oab == cod_oab:
                lista.append(self._processos[i])
        
        custoTotal = 0
        for i in range(len(lista)):
            custoTotal += lista[i].custo.valor
        return custoTotal