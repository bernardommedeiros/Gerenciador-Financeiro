# 💰 Gerenciador Financeiro

Sistema que possibilita ao usuário criar **balancetes**, associar **despesas** e **faturamentos**, com o objetivo de melhorar a **organização financeira pessoal** ou empresarial.

---

## 📘 Finalidade
Este projeto foi desenvolvido com o objetivo de auxiliar os usuários a compreender e gerenciar melhor sua saúde financeira. A aplicação oferece uma interface intuitiva e responsiva, permitindo registrar receitas e despesas de forma prática, organizar lançamentos por balancetes mensais e acompanhar o saldo disponível em tempo real.

Além disso, o sistema proporciona uma visão clara da situação financeira, ajudando na tomada de decisões mais conscientes e no planejamento pessoal ou empresarial. Com a possibilidade de categorizar despesas e faturamentos, o usuário consegue identificar padrões de consumo e oportunidades para economizar, tornando a gestão financeira mais eficiente e acessível.

<br>

## ✅ Funcionalidades
- Cadastro de **balancetes** (seções de finanças de um determinado período).
- Associação de **boletos** (despesas e faturamentos) a cada balancete.
- Cálculo automático de **saldo** por balancete.
- Autenticação com **cadastro, login e logout**.
- Interface responsiva utilizando **Bulma CSS**.
- Banco de dados **PostgreSQL** para armazenamento seguro.
- Ambiente totalmente **containerizado com Docker**.

---

## 🛠 Stack Utilizada

| Tecnologia          | Finalidade                                                   |
|---------------------|-------------------------------------------------------------|
| **Django**          | Framework monólito para construção das regras de negócio.             |
| **Bulma CSS**       | Estilização responsiva e moderna da interface.            |
| **Docker**          | Containerização da aplicação para garantir portabilidade e consistência.     |
| **Docker Compose**  | Orquestração dos serviçõs do projeto (aplicação e banco de dados).               |
| **PostgreSQL**      | Banco de dados relacional para armazenamento persistente. |

---

## ⚙️ Como Rodar o Projeto

Antes de tudo, certifique-se de ter instalado:
- **Docker**
- **Docker Compose**

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/gerenciador-financeiro.git
cd gerenciador-financeiro
```


### 2. Construção dos containers
```bash
  docker compose build
```

### 3. Subir os serviços
```bash
  docker compose up
```

### 3. O sistema estará disponível em:
```bash
  http://localhost:8000
```
