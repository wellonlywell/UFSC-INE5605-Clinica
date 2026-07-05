# SisClínica — Regras e Critérios de Avaliação

## Critérios de Avaliação da Tarefa 1 (INE5605)

Os critérios abaixo correspondem aos itens utilizados na avaliação da Tarefa 1 da disciplina INE5605 — Desenvolvimento de Sistemas Orientados a Objetos I.

| Critério | Peso |
|-----------|:----:|
| Cadastros — inclusão, exclusão, alteração e listagem | 2,0 |
| Registros — atendimento, procedimento e pagamento | 1,5 |
| Relatórios — 4 relatórios implementados | 1,5 |
| Entrega da Parte 1 e Parte 2 | 0,5 |
| Diagrama UML — qualidade e consistência | 0,5 |
| Associação, agregação e composição (um exemplo de cada) | 1,0 |
| Herança e classes abstratas | 1,0 |
| Tratamento de exceções | 1,0 |
| MVC correto | 1,0 |
| **Total** | **10,0** |

## Critérios de Avaliação da Tarefa 2 (INE5605)

Os critérios abaixo correspondem aos itens utilizados na avaliação da Tarefa 2 da disciplina INE5605 — Desenvolvimento de Sistemas Orientados a Objetos I.

| Critério | Peso |
|-----------|:----:|
| Cadastro de Pessoas, Clínicas e Tipos de Atendimento (CRUD) | 1,0 |
| Registro de Atendimentos, Procedimentos e Pagamentos | 1,0 |
| Geração de relatório(s) | 1,0 |
| Qualidade da notação UML e consistência com o código | 2,0 |
| Interface gráfica funcional | 2,0 |
| Persistência em arquivo (padrão DAO) | 2,0 |
| MVC e separação em camadas | 1,0 |
| **Total** | **10,0** |

---

## Regras do Enunciado

### Regra 1 — Atendimento de pacientes menores de idade

Pacientes com menos de 18 anos completos devem possuir responsável legal cadastrado no sistema.
Essa regra é aplicada tanto no cadastro quanto na alteração dos dados do paciente. Caso uma alteração torne o paciente menor de idade sem responsável cadastrado, a alteração é bloqueada.

### Regra 2 — Horário de funcionamento da clínica

O atendimento deve ocorrer integralmente dentro do horário de funcionamento da clínica.
O sistema verifica tanto o horário de início quanto o horário de término do atendimento.

### Regra 3 — Data do pagamento

O pagamento deve ser realizado até a data do atendimento.
Pagamentos com data posterior ao atendimento são bloqueados pelo sistema.

### Regra 4 — Formas de pagamento

O sistema possui três modalidades de pagamento:

- Dinheiro
- Pix (CPF do pagador com 11 dígitos)
- Cartão (número do cartão entre 13 e 19 dígitos e bandeira)

### Regra 5 — Pagamentos parciais

Um mesmo atendimento pode receber vários pagamentos.
O saldo restante é calculado considerando a soma de todos os pagamentos já registrados para aquele atendimento.

---

## Regras adicionais implementadas pela equipe

### Regra A — Nome social

Quando informado, o nome social substitui o nome civil em todas as exibições do sistema, conforme a legislação brasileira.

### Regra B — Campos de inclusão

A classe abstrata `Pessoa` possui os seguintes campos opcionais:

- Nome social
- Identidade de gênero
- Pessoa com Deficiência (PcD)
- Cor/Raça (categorias oficiais do IBGE)

Esses campos ampliam o cadastro, mas não alteram as regras de negócio do sistema.

### Regra C — Exclusão de procedimento utilizado

Um procedimento do catálogo não pode ser excluído caso já tenha sido utilizado em algum atendimento.
Essa regra preserva a consistência e o histórico do sistema.

### Regra D — Alterações no catálogo

A descrição e o custo de um procedimento podem ser alterados a qualquer momento.
As alterações afetam apenas atendimentos futuros.
Itens de procedimentos já registrados permanecem com os valores existentes no momento da realização do atendimento, preservando o histórico.

### Regra E — Catálogo independente de profissionais

O CatalogoProcedimento representa os procedimentos disponíveis na clínica.
Os procedimentos não pertencem a um profissional específico e podem ser solicitados por qualquer profissional habilitado.

### Regra F — Profissional responsável pelo procedimento

O `ItemProcedimento` registra o profissional responsável pela solicitação do procedimento durante o atendimento.
Essa informação preserva o histórico do procedimento dentro do atendimento e reflete a prática utilizada em clínicas e laboratórios, nos quais o profissional solicitante acompanha pedidos de exames, procedimentos e encaminhamentos.

---

## Regras específicas da Tarefa 2

### Regra G — Persistência de dados
Os dados cadastrados devem sobreviver ao fechamento do sistema. Cada operação de cadastro (incluir, alterar, excluir, vincular) é salva em disco imediatamente via padrão DAO com pickle, sem exigir um passo separado de "salvar antes de sair".

### Regra H — Interface gráfica
Nenhuma tela (`view/`) pode usar `input()` ou `print()` diretamente. Toda entrada e saída de dados deve ocorrer via componentes gráficos (FreeSimpleGUI).
