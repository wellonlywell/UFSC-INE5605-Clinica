def vincular_profissional_clinica(self):
    if not self.__clinicas:
        self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
        return
    self.listar_clinicas()
    cnpj = self.__tela_clinica.seleciona_clinica()
    clinica = self.buscar_por_cnpj(cnpj)

    if clinica is None:
        self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
        return

    ctrl_profissional = self.__controlador_sistema.controlador_profissional

    if not ctrl_profissional.get_profissionais():
        self.__tela_clinica.mostra_mensagem("Nenhum profissional cadastrado.")
        return

    ctrl_profissional.listar_profissionais()
    cpf = self.__tela_clinica.seleciona_profissional()
    profissional = ctrl_profissional.buscar_por_cpf(cpf)

    if profissional is None:
        self.__tela_clinica.mostra_mensagem("Profissional não encontrado.")
        return

    try:
        clinica.adicionar_profissional(profissional)
        self.__tela_clinica.mostra_mensagem("Profissional vinculado à clínica com sucesso!")
    except DadoInvalidoException as e:
        self.__tela_clinica.mostra_mensagem(f"Erro ao vincular profissional: {e}")

def remover_profissional_clinica(self):
    if not self.__clinicas:
        self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
        return
    self.listar_clinicas()
    cnpj = self.__tela_clinica.seleciona_clinica()
    clinica = self.buscar_por_cnpj(cnpj)

    if clinica is None:
        self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
        return

    if not clinica.profissionais:
        self.__tela_clinica.mostra_mensagem("Esta clínica não possui profissionais vinculados.")
        return

    self.__tela_clinica.mostra_profissionais_da_clinica(clinica)
    cpf = self.__tela_clinica.seleciona_profissional()

    profissional_encontrado = None

    for profissional in clinica.profissionais:
        cpf_profissional = "".join(c for c in profissional.cpf if c.isdigit())
        cpf_buscado = "".join(c for c in cpf if c.isdigit())

        if cpf_profissional == cpf_buscado:
            profissional_encontrado = profissional
            break

    if profissional_encontrado is None:
        self.__tela_clinica.mostra_mensagem("Profissional não encontrado nesta clínica.")
        return

    try:
        clinica.remover_profissional(profissional_encontrado)
        self.__tela_clinica.mostra_mensagem("Profissional removido da clínica com sucesso!")
    except DadoInvalidoException as e:
        self.__tela_clinica.mostra_mensagem(f"Erro ao remover profissional: {e}")

def listar_profissionais_clinica(self):
    if not self.__clinicas:
        self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
        return
    self.listar_clinicas()
    cnpj = self.__tela_clinica.seleciona_clinica()
    clinica = self.buscar_por_cnpj(cnpj)

    if clinica is None:
        self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")
        return

    self.__tela_clinica.mostra_profissionais_da_clinica(clinica)