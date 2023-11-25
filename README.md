# Projeto de Automação Residencial

Este repositório contém o código fonte de um projeto de automação residencial. O projeto é dividido em duas branches:

## Branch1: Código 1

A `branch1` contém o código fonte referente à funcionalidade do Código 1. Este código é responsável por interagir com o usuário, solicitar uma senha, criptografá-la e verificar se a senha fornecida pelo usuário coincide com a senha armazenada.

### Como Usar

1. Certifique-se de estar na `branch1`.
2. Execute o arquivo `hashlibebe.py`.
3. Siga as instruções para fornecer uma senha e verificar se está correta.

## Branch2: Código 2

A `branch2` contém o código fonte referente à funcionalidade do Código 2. Este código também lida com senhas, mas realiza o teste de comparação apenas internamente, sem informar o usuário sobre a corretude da senha.

### Como Usar

1. Certifique-se de estar na `branch2`.
2. Execute o arquivo `hashlibebe2.py`.
3. O código realizará o teste de comparação internamente.

## GitHub Actions

Este projeto utiliza o GitHub Actions para automatizar os testes em ambas as branches. A configuração para o GitHub Actions está no arquivo `testes.yml`. Na `branch1`, os testes são executados com o comando `python hashlibebe.py`, enquanto na `branch2`, é usado o `pytest hashlibebe2.py`.

---

**Observação:** Certifique-se de ter o Python e as dependências necessárias instaladas antes de executar os scripts. Veja as instruções no arquivo `requirements.txt`.

Para mais detalhes, consulte os códigos e as configurações no repositório.


