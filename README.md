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

Marcos Garcia Labadie | Well Christina Costa Sousa 

**Professores:** Lucas Machado da Palma e Vinícius Zanandrea

---

## 📋 Sobre o sistema

O **SisClínica** é um sistema de gerenciamento de clínicas desenvolvido em Python puro, com arquitetura MVC estrita e execução totalmente via terminal. O sistema gerencia cadastros de clínicas, pacientes, profissionais e tipos de atendimento, além de registrar atendimentos, procedimentos e pagamentos, com emissão de relatórios gerenciais.

---

## ⚙️ Funcionalidades

<details>
<summary><strong>📁 Cadastros (CRUD completo)</strong></summary>

- 🏥 Clínica (CNPJ, horários de funcionamento, profissionais vinculados)
- 🧑‍⚕️ Paciente (nome social, identidade de gênero, PCD, cor/raça)
- 👨‍⚕️ Profissional (especialidade, registro)
- 📋 Tipo de Atendimento

</details>

<details>
<summary><strong>📝 Registros</strong></summary>

- 📅 Atendimento (vinculado à clínica, paciente e profissional, com validação de horário)
- 🩺 Procedimento (catálogo geral e itens por atendimento)
- 💳 Pagamento (Dinheiro, PIX ou Cartão)

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

A classe base `Pessoa` foi desenvolvida além do mínimo exigido pelo enunciado, incorporando campos de inclusão social presentes em **todos** os subtipos (`Paciente`, `Profissional`, `Responsavel`):

| Campo | Descrição |
|---|---|
| `nome_social` | Sobrepõe o nome civil em todas as exibições, conforme a **Lei nº 8.727/2016** |
| `identidade_genero` | Campo aberto para autodeclaração |
| `pcd` | Indica se a pessoa é Pessoa com Deficiência |
| `cor_raca` | Enum com as cinco categorias oficiais do **IBGE** (Branca, Preta, Parda, Amarela, Indígena) |

> Todos os campos são opcionais e validados com as exceções customizadas do projeto.

---

## 📏 Regras de negócio

| # | Regra |
|---|---|
| Regra 1 | Pacientes menores de 18 anos exigem cadastro de responsável legal |
| Regra 2 | Atendimentos só podem ser agendados dentro do horário de funcionamento da clínica |
| Regra 3 | A data do pagamento não pode ser posterior à data do atendimento |

---

## 🏗️ Arquitetura

```
SisClinica/
├── main.py                          # Ponto de entrada
├── model/                           # Entidades e regras de validação
│   ├── Pessoa.py                    # Classe abstrata base
│   ├── Paciente.py
│   ├── Profissional.py
│   ├── Responsavel.py
│   ├── Clinica.py
│   ├── TipoAtendimento.py
│   ├── Atendimento.py
│   ├── ItemProcedimento.py          # Composição com Atendimento
│   ├── CatalogoProcedimento.py
│   ├── Pagamento.py                 # Classe abstrata base
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
| ♦ Composição | `Atendimento` → `ItemProcedimento` — item não existe fora do atendimento |
| ◇ Agregação | `Clinica` → `Profissional` — profissional existe independentemente |
| → Associação | `Pagamento` → `Atendimento` e `Paciente` |

### Herança

- `Pessoa` *(ABC)* → `Paciente`, `Profissional`, `Responsavel`
- `Pagamento` *(ABC)* → `PagamentoDinheiro`, `PagamentoPix`, `PagamentoCartao`

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.10 ou superior — sem dependências externas.

```bash
python main.py
```

---

## 📐 Diagrama UML

O diagrama de classes completo está disponível em dois formatos:
- [`diagrama_SisClinica.png`](./diagrama_SisClinica.png) — para visualização rápida
- [`diagrama_SisClinica.svg`](./diagrama_SisClinica.svg) — vetorial, zoom sem perder qualidade

---

<div align="center">
</div>
