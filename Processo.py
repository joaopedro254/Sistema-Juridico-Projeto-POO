class Processo:
    def __init__(self, desc, custo, decisao, status, pessoa, advogado, audiencias):
        self._descricao = desc
        self._custo = custo
        self._decisao = decisao
        self._status = status
        self._pessoa = pessoa
        self._advogado = advogado
        self._audiencias = audiencias

    
    def audiencias_temp(self, tempo):
        
        for i in range(len(self._audiencias)):
            if self.audiencias[i].duracao >= tempo:
                print(f'.{self.audiencias[i].data_da_audiencia}')
                print(f'.{self.audiencias[i].recomendacao}')
            print('')
               
    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @property
    def custo(self):
        return self._custo

    @custo.setter
    def custo(self, novo_custo):
        self._custo = novo_custo

    @property
    def decisao(self):
        return self._decisao

    @decisao.setter
    def decisao(self, nova_decisao):
        self._decisao = nova_decisao

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @property
    def pessoa(self):
        return self._pessoa

    @pessoa.setter
    def pessoa(self, nova_pessoa):
        self._pessoa = nova_pessoa

    @property
    def advogado(self):
        return self._advogado

    @advogado.setter
    def advogado(self, novo_advogado):
        self._advogado = novo_advogado

    @property
    def audiencias(self):
        return self._audiencias

    @audiencias.setter
    def audiencias(self, novas_audiencias):
        self._audiencias = novas_audiencias

    def __str__(self):
        saida = ''

        for i in range(len(self._audiencias)):
            saida = saida + '{}'.format(self._audiencias[i]) + ' '
        return "descrição: {},custo: {}, decisão: {}, status: {}, pessoa => nome: {}, cpf: {}, advogado => cod_OAB: {}, nome: {}, audiencias => {}".format(self._descricao, self._custo, self._decisao, self._status, self._pessoa.nome, self._pessoa.cpf, self._advogado.cod_oab, self._advogado.nome, saida)
