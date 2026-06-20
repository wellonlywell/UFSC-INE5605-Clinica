SisClínica — Regras e Critérios de Avaliação
Critérios de Avaliação (INE5605)
Critério	Peso
Cadastros — inclusão, exclusão, alteração e listagem	2,0
Registros — atendimento, procedimento e pagamento	1,5
Relatórios — 4 relatórios implementados	1,5
Entrega da Parte 1 e Parte 2	0,5
Diagrama UML — qualidade e consistência	0,5
Associação, agregação e composição (um exemplo de cada)	1,0
Herança e classes abstratas	1,0
Tratamento de exceções	1,0
MVC correto	1,0
Total	10,0

________________________________________
Regras do Enunciado
Regra 1 — Atendimento de menor Paciente com menos de 18 anos completos só pode ser atendido se tiver responsável legal cadastrado no sistema.

Regra 2 — Horário da clínica O atendimento deve ocorrer inteiramente dentro do horário de funcionamento da clínica. Tanto a hora de início quanto a hora de fim são verificadas.

Regra 3 — Data do pagamento O pagamento deve ser realizado até a data do atendimento. Pagamentos com data posterior ao atendimento são bloqueados.

Regra 4 — Modalidades de pagamento Três modalidades disponíveis: Dinheiro, Pix (exige CPF do pagador com 11 dígitos), Cartão (exige número com 13 a 19 dígitos e bandeira).

Regra 5 — Pagamento parcial O sistema permite pagamentos parciais do mesmo atendimento. O saldo restante é calculado acumulando todos os pagamentos já registrados para aquele atendimento.

________________________________________
Regras Adicionais Implementadas
Regra A — Nome social Se o paciente ou profissional tiver nome social cadastrado, ele substitui o nome civil em todas as exibições do sistema, conforme legislação brasileira.

Regra B — Campos de inclusão A classe Pessoa possui campos opcionais de inclusão: PCD (boolean), cor/raça (categorias IBGE), identidade de gênero e nome social. Esses campos não interferem nas regras de negócio.

Regra C — CPF único Não é permitido cadastrar dois pacientes ou dois profissionais com o mesmo CPF.

Regra D — Descrição única no catálogo Não é permitido cadastrar dois procedimentos com a mesma descrição no catálogo.

Regra E — Exclusão bloqueada se em uso Um procedimento do catálogo não pode ser excluído se já foi utilizado em algum atendimento. O histórico dos atendimentos é preservado.

Regra F — Alteração livre no catálogo O nome e o custo de um procedimento do catálogo podem ser alterados a qualquer momento. Os itens já criados em atendimentos anteriores mantêm os valores do momento da realização — o histórico não é afetado.

Regra G — Catálogo sem profissional fixo O CatalogoProcedimento não é vinculado a um profissional específico, pois qualquer profissional pode solicitar qualquer serviço do catálogo. O profissional responsável pelo pedido é registrado no ItemProcedimento no momento do atendimento.

Regra H — Profissional no ItemProcedimento O ItemProcedimento registra o profissional do atendimento como responsável pelo pedido, refletindo a prática clínica real onde o nome do médico consta no pedido de exame.

Regra I — Valor total do atendimento O valor total a pagar em um atendimento é a soma do valor base da consulta com os custos de todos os procedimentos adicionados. O pagamento é calculado sobre esse total, não apenas sobre o valor base.

