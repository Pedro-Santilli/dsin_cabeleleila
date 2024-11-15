# Sistema de Agendamento - Documentação

## 1. Visão Geral

Este sistema de agendamento é uma aplicação web desenvolvida em Flask que permite aos usuários realizar, visualizar e editar agendamentos. O sistema também inclui funcionalidades administrativas para gerenciar todos os agendamentos.

## 2. Estrutura do Projeto

O projeto está organizado em diferentes arquivos e módulos:

- [main.py](http://main.py): Arquivo principal que inicializa a aplicação Flask
- routes/auth.py: Gerencia autenticação e registro de usuários
- routes/agendamento.py: Lida com as operações de agendamento
- routes/admin.py: Contém funcionalidades administrativas
- templates/ver_agendamentos.html: Template para exibir agendamentos

## 3. Detalhamento dos Módulos

### 3.1 [main.py](http://main.py)

Este arquivo configura e inicializa a aplicação Flask, registrando os blueprints necessários.

### 3.2 routes/auth.py

Gerencia a autenticação e registro de usuários.

- load_df_users(): Carrega os dados dos usuários do arquivo Excel
- save_df_users(df): Salva os dados dos usuários no arquivo Excel
- login(): Rota para autenticação de usuários
- cadastrar(): Rota para registro de novos usuários

### 3.3 routes/agendamento.py

Contém as funcionalidades principais de agendamento.

- load_df_service(): Carrega os dados de agendamentos do arquivo Excel
- save_df_service(df): Salva os dados de agendamentos no arquivo Excel
- agendamento(): Rota para exibir o formulário de agendamento
- efetuar_agendamento(): Processa o novo agendamento
- ver_agendamentos(): Exibe os agendamentos do usuário
- edit(): Exibe o formulário de edição de agendamento
- editar(): Processa a edição do agendamento

### 3.4 routes/admin.py

Contém funcionalidades administrativas.

- ver_agendamentos_admin(): Exibe todos os agendamentos para o admin
- edit_admin(): Exibe o formulário de edição para o admin
- editar_admin(): Processa a edição de agendamento pelo admin

### 3.5 templates/ver_agendamentos.html

Template HTML para exibir a lista de agendamentos do usuário.

## 4. Funcionalidades Principais

### 4.1 Autenticação e Registro

Os usuários podem se cadastrar e fazer login. As credenciais são verificadas contra os dados armazenados em um arquivo Excel.

### 4.2 Agendamento

Os usuários podem criar novos agendamentos. O sistema verifica conflitos de horário e limita um agendamento por semana por usuário.

### 4.3 Visualização de Agendamentos

Os usuários podem ver seus próprios agendamentos. Administradores podem ver todos os agendamentos.

### 4.4 Edição de Agendamentos

Os usuários podem editar seus agendamentos, desde que sejam com mais de dois dias de antecedência. Administradores podem editar qualquer agendamento.

## 5. Armazenamento de Dados

Os dados são armazenados em arquivos Excel:

- usuariosdb.xlsx: Armazena informações dos usuários
- servico.xlsx: Armazena os agendamentos

## 6. Segurança

O sistema implementa verificações básicas de segurança:

- Autenticação de usuários
- Verificação de conflitos de agendamento
- Restrição de edição de agendamentos próximos

## 7. Melhorias Futuras

- Implementar um banco de dados relacional em vez de arquivos Excel
- Adicionar mais validações de entrada
- Implementar um sistema de notificações por email
- Melhorar a interface do usuário com JavaScript e AJAX
