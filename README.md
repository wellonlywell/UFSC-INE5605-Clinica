<div align="center">

# 🏥 SisClínica

**Sistema de Gestão de Clínicas — Terminal**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Arquitetura](https://img.shields.io/badge/Arquitetura-MVC-6B4FBB?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)
![UFSC](https://img.shields.io/badge/UFSC-INE5605-003da5?style=for-the-badge)

*Trabalho prático da disciplina INE5605 — Desenvolvimento de Sistemas Orientados a Objetos I*  
*Universidade Federal de Santa Catarina — Semestre 2026/1*

</div>

---

## 👩‍💻 Dupla

**Estudantes:** Marcos Garcia Labadie e Well Christina Costa Sousa 

**Professores:** Lucas Machado da Palma e Vinícius Zanandrea

---

## 📋 Sobre o sistema

O **SisClínica** é um sistema de gerenciamento de clínicas desenvolvido em **Python puro**, utilizando arquitetura **MVC** e execução totalmente via terminal.

O sistema permite o gerenciamento de clínicas, pacientes, profissionais, tipos de atendimento, catálogo de procedimentos, atendimentos, pagamentos e emissão de relatórios gerenciais.

---

## ⚙️ Funcionalidades

<details>
<summary><strong>📁 Cadastros (CRUD completo)</strong></summary>

- 🏥 Clínica
- 🧑‍⚕️ Paciente
- 👨‍⚕️ Profissional
- 👤 Responsável
- 📋 Tipo de Atendimento
- 🩺 Catálogo de Procedimentos

</details>

<details>
<summary><strong>📝 Registros</strong></summary>

- 📅 Atendimento
- 🧾 Registro de procedimentos por atendimento
- 💳 Pagamentos em Dinheiro, Pix e Cartão

</details>

<details>
<summary><strong>📊 Relatórios</strong></summary>

- Procedimentos mais realizados
- Procedimentos mais caros e mais baratos
- Clínicas com mais atendimentos
- Atendimentos mais caros e mais baratos

</details>

---

## 💜 Campos inclusivos em `Pessoa`

A classe abstrata `Pessoa` foi desenvolvida além do mínimo exigido pelo enunciado, incorporando campos de inclusão social presentes em **todos** os subtipos (`Paciente`, `Profissional`, `Responsavel`):

| Campo | Descrição |
|---|---|
| `nome_social` | Sobrepõe o nome civil em todas as exibições, conforme a **Lei nº 8.727/2016** |
| `identidade_genero` | Campo aberto para autodeclaração |
| `pcd` | Indica se a pessoa é Pessoa com Deficiência |
| `cor_raca` | Enum com as cinco categorias oficiais do **IBGE** (Branca, Preta, Parda, Amarela, Indígena) |

> Todos os campos são opcionais e validados com as exceções customizadas do projeto.

---

## 📏 Principais regras de negócio

| # | Regra |
|---|---|
| Regra 1 | Pacientes menores de 18 anos exigem responsável legal cadastrado. |
| Regra 2 | Atendimentos devem ocorrer dentro do horário de funcionamento da clínica. |
| Regra 3 | O pagamento deve ocorrer até a data do atendimento. |
| Regra 4 | O sistema permite pagamentos parciais para um mesmo atendimento. |

> **Observação:** A documentação completa das regras de negócio, critérios de avaliação e decisões de modelagem adotadas pela equipe encontra-se em [`REGRAS.md`](./REGRAS.md).

---

## 🏗️ Arquitetura

```
SisClinica/
├── main.py                          # Ponto de entrada
├── model/                           # Entidades e regras de validação
│   ├── Pessoa.py                    # Classe abstrata 
│   ├── Paciente.py
│   ├── Profissional.py
│   ├── Responsavel.py               
│   ├── Clinica.py
│   ├── TipoAtendimento.py
│   ├── Atendimento.py
│   ├── ItemProcedimento.py          # Composição com Atendimento
│   ├── CatalogoProcedimento.py
│   ├── Pagamento.py                 # Classe abstrata 
│   ├── PagamentoDinheiro.py
│   ├── PagamentoPix.py
│   ├── PagamentoCartao.py
│   └── CorRaca.py                   # Enum com categorias IBGE
├── view/                            # Telas (apenas input/print)
├── control/                         # Controladores (lógica e ponte MVC)
└── exceptions/                      # Exceções customizadas
    ├── dado_invalido_exception.py
    └── regra_negocio_exception.py
```

### Relações UML implementadas

| Tipo | Relação |
|---|---|
| ♦ Composição | `Paciente` → `Responsavel` — o responsável faz parte do cadastro do paciente menor |
| ♦ Composição | `Atendimento` → `ItemProcedimento` — o item existe apenas dentro de um atendimento |
| ◇ Agregação | `Clinica` → `Profissional` — o profissional existe independentemente da clínica |
| → Associação | `Pagamento` → `Atendimento` |
| → Associação | `Pagamento` → `Paciente` |

### Herança

- `Pessoa` *(classe abstrata)* → `Paciente`, `Profissional` e `Responsavel`
- `Pagamento` *(classe abstrata)* → `PagamentoDinheiro`, `PagamentoPix` e `PagamentoCartao`

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.10 ou superior — sem dependências externas.

```bash
python main.py
```

---

## 📐 Diagrama UML

O diagrama de classes do projeto está disponível em dois formatos:

- [`diagrama_SisClinica.png`](./diagrama_SisClinica.png) — visualização rápida.
- [`diagrama_SisClinica.svg`](./diagrama_SisClinica.svg) — versão vetorial para ampliação sem perda de qualidade.

<div align="center">

**SisClínica**

Projeto desenvolvido para a disciplina **INE5605 — Desenvolvimento de Sistemas Orientados a Objetos I**  
Universidade Federal de Santa Catarina (UFSC)

</div>
