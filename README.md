<div align="center">

# 🏥 SisClínica

**Sistema de Gestão de Clínicas — Interface Gráfica**

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

O **SisClínica** é um sistema de gerenciamento de clínicas desenvolvido em **Python**, utilizando arquitetura **MVC**, persistência em arquivo com padrão **DAO** e **interface gráfica** construída com **FreeSimpleGUI**.

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

## 📏 Regras de negócio

> Para a lista completa de regras de negócio e critérios de avaliação, consulte [REGRAS.md](./REGRAS.md).

---

## 🏗️ Arquitetura
```
SisClinica/
├── main.py # Ponto de entrada
├── requirements.txt # Dependências (FreeSimpleGUI)
├── README.md
├── REGRAS.md
├── diagrama_SisClinica.png # Diagrama UML
├── diagrama_SisClinica.svg # Diagrama UML (vetorial)
├── assets/ # Ícone da aplicação
│ └── icone_cruz_arcoiris.ico
├── model/ # Entidades e regras de validação
│ ├── Pessoa.py # Classe abstrata
│ ├── Paciente.py
│ ├── Profissional.py
│ ├── Responsavel.py
│ ├── Clinica.py
│ ├── TipoAtendimento.py
│ ├── Atendimento.py
│ ├── ItemProcedimento.py # Composição com Atendimento
│ ├── CatalogoProcedimento.py
│ ├── Pagamento.py # Classe abstrata
│ ├── PagamentoDinheiro.py
│ ├── PagamentoPix.py
│ ├── PagamentoCartao.py
│ └── CorRaca.py # Enum com categorias IBGE
├── view/ # Telas gráficas (FreeSimpleGUI)
│ ├── tela_atendimento.py
│ ├── tela_catalogo_procedimento.py
│ ├── tela_clinica.py
│ ├── tela_paciente.py
│ ├── tela_pagamento.py
│ ├── tela_profissional.py
│ ├── tela_relatorio.py
│ ├── tela_responsavel.py
│ ├── tela_sistema.py
│ └── tela_tipo_atendimento.py
├── control/ # Controladores (lógica e ponte MVC)
│ ├── controlador_atendimento.py
│ ├── controlador_catalogo_procedimento.py
│ ├── controlador_clinica.py
│ ├── controlador_paciente.py
│ ├── controlador_pagamento.py
│ ├── controlador_profissional.py
│ ├── controlador_relatorios.py
│ ├── controlador_responsavel.py
│ ├── controlador_sistema.py
│ └── controlador_tipo_atendimento.py
├── dao/ # Persistência (pickle) — ver seção própria abaixo
│ ├── dao_base.py # Classe genérica: get_all() / save_all()
│ ├── dao_clinica.py
│ ├── dao_tipo_atendimento.py
│ ├── dao_atendimento.py
│ ├── dao_pagamento.py
│ ├── dao_paciente.py
│ ├── dao_profissional.py
│ ├── dao_responsavel.py
│ └── dao_catalogo_procedimento.py
├── dados/ # Gerado automaticamente — arquivos .pkl
└── exceptions/ # Exceções customizadas
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

## 💾 Persistência de Dados

O sistema usa o padrão **DAO (Data Access Object)** para gravar os cadastros em disco com `pickle`, de forma que os dados sobrevivam ao fechamento do programa. `dao/dao_base.py` concentra a lógica genérica de leitura/escrita (`get_all()` / `save_all()`); cada entidade tem um DAO concreto que só informa o arquivo a usar.

| Entidade | DAO | Status |
|---|---|---|
| Clínica | `dao_clinica.py` | ✅ Implementado |
| Tipo de Atendimento | `dao_tipo_atendimento.py` | ✅ Implementado |
| Atendimento | `dao_atendimento.py` | ✅ Implementado |
| Pagamento | `dao_pagamento.py` | ✅ Implementado |
| Paciente | `dao_paciente.py` | ✅ Implementado |
| Profissional | `dao_profissional.py` | ✅ Implementado |
| Responsável | `dao_responsavel.py` | ✅ Implementado |
| Catálogo de Procedimentos | `dao_catalogo_procedimento.py` | ✅ Implementado |

Os arquivos `.pkl` ficam em `dados/`, criada automaticamente na primeira execução. Cada operação de cadastro (incluir, alterar, excluir, vincular) já salva no disco imediatamente — não existe um passo separado de "salvar antes de sair", o que também protege contra perda de dados em caso de fechamento abrupto do programa.

**Detalhe de implementação:** como cada entidade é salva em um arquivo próprio, mas há objetos que referenciam outros (ex: `Atendimento` referencia `Clinica`/`TipoAtendimento`, `Pagamento` referencia `Atendimento`), o sistema reconecta essas referências aos objetos oficiais logo após carregar os dados, via `__revincular_referencias()` nos controladores correspondentes. Sem isso, comparações de identidade (ex: "este atendimento já tem pagamento?") voltariam a falhar depois de reabrir o programa, mesmo com os dados corretos salvos em disco.

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.10 ou superior

1. Instale as dependências:
```bash
   pip install -r requirements.txt
```
2. Execute o sistema:
```bash
   python main.py
```

---

## 📐 Diagrama UML

O diagrama de classes do projeto está disponível em dois formatos:

- [`diagrama_SisClinica.png`](./diagrama_SisClinica.png) — visualização rápida.
- [`diagrama_SisClinica.svg`](./diagrama_SisClinica.svg) — versão vetorial para ampliação sem perda de qualidade.

<div align="center">
