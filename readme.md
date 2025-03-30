# Bootcamp API - Usando Python com Flask

Projeto desenvolvido para disciplina de `Bootcamp Desenvolvimento e Projetos de Sistema` pelo `Grupo 1`
- [Diagramas UML e MER](/img) 
- [Documentação](/pdf)

## Objetivo
- Criar uma API que disponibiliza a consulta, criação, edição e exclusão de alunos e cursos.

## Pré Requisitos
- [Git](https://git-scm.com/downloads) - Para baixar o projeto e fazer o versionamento do código
- [Python 3.12+](https://www.python.org/downloads/) - Executa o código
- [Visual Studio Code](https://code.visualstudio.com/download) - IDE para desenvolvimento "Recomendada pelo grupo"
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) - Para rodar a aplicação dentro de um container e garantir ambiente estável
- [Docker Compose](https://docs.docker.com/compose/) - Para facilitar a criação de container. Geralmente já vem com o Docker Desktop mas se não estiver instalado busque na documentação

## Baixar o projeto para sua máquina local

Clonar o repositório para sua máquina local
```bash
git clone https://github.com/vinilima2/bootcamp-api-python-flask
```

Acessar o diretório do projeto
```bash
cd bootcamp-api-python-flask
```

<br/>

## Como rodar o projeto
OBS: Todos os seguintes comandos estão sendo executados dentro da pasta do projeto - `bootcamp-api-python-flask`

### Docker - Windows
Para criar o container e executar a aplicação. Caso não queira que ela execute em segundo plano adicione `-d` ao final do comando
```bash
# Criar uma nova imagem e subir ela em um container
docker-compose.exe up --build
```

Para parar o container ou remover a imagem e o container
```bash
docker-compose.exe down
```

<br/>

### Linux ou Git - Bash
Baixar as dependências do projeto
```bash
# Instalar dependências
pip install -r requirements.txt
```

Rodar o script para iniciar o programa junto da configuração da base de dados
```bash
# Executar projeto
./run.sh
```

<br/>

### Windows - CMD ou Powershell
Por meio do CMD ou Powershell que podem ser acessados pelo terminal rode os seguintes comandos
```bash
# Instalar dependências
pip install -r requirements.txt
```
> Importante analisar o código do script para entender os comandos executados, o mesmo comando pode ser rodado diretamente pelo terminal

Rodar o script para iniciar o programa junto da configuração da base de dados
```bash
# Executar projeto
./run.sh
```
> Importante analisar o código do script para entender os comandos executados, o mesmo comando pode ser rodado diretamente pelo terminal

Lembrando que também é possível rodar o comando da seção [Linux ou Git](#linux-ou-git---bash) basta ter instalado o Git com o Git Bash.

## Documentação da API - Swagger

A API possui documentação interativa utilizando Swagger UI. Após iniciar a aplicação, você pode acessar a documentação em:

```
http://localhost:5000/swagger
```

Recursos da documentação Swagger:
- Visualização de todos os endpoints disponíveis
- Descrição detalhada de cada rota
- Modelos de requisição e resposta
- Possibilidade de testar os endpoints diretamente pela interface

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feat/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feat/nova-funcionalidade`)
5. Abra um Pull Request

## Texto explicativo sobre o BD.

Tabela Aluno:
Chave Primária – cpf:
Aqui, a coluna CPF (Cadastro de Pessoa Física) é usada como chave primária. Essa é uma escolha interessante, pois o CPF é, em geral, único para cada pessoa.
Observação: Em alguns casos, pode ser desejável usar um identificador auto-incrementado como chave primária e manter o CPF como um campo único para garantir acesso rápido, mas isso depende do design e das regras do negócio.
Detalhamento dos Campos:
CPF: Armazena nùmero de documento único e exclusivo de cada pessoa.
MATRICULA: Guarda número da matricula de cada aluno para cada curso.
NOME: Registra nome do aluno.
DATA_NASCIMENTO: Armazena a data que o aluno nasceu. Pode ser no formato DD/MM/AAAA ou MM/DD/AAAA.
TELEFONE: Salva o número para contato com o aluno.
E-MAIL: Salva o e-mail para contato com o aluno.
STATUS: Registra se a mattricula do aluno está Ativa (1) ou Inativa (0).

Tabela Curso:
Chave Primária Auto-incrementada – id:
O campo ID é definido como chave primária com a cláusula AUTOINCREMENT , o que garante que cada novo registro receba automaticamente um identificador único. Isso é bastante comum para tabelas onde se deseja gerar um identificador sem depender de um dado natural.
Detalhamento dos Campos:
NOME : Guarda o nome do curso.
TURNO: Pode indicar o período (manhã, tarde, noite) em que o curso é oferecido.
CARGA_HORARIA: Representa a carga horária total do curso. O tamanho especificado (INTERGER) indica uma limitação que, na prática, pode ser apenas uma sugestão, dependendo do SGBD utilizado.


Tabela AlunoCurso:
Tabelas de Associação (Tabela de Relacionamento N:N):
Esta tabela estabelece o relacionamento de muitos para muitos entre alunos e cursos. Cada registro indica que um determinado aluno (identificado pelo CPF) está associado a um curso (identificado pelo ID).
Chave Primária Auto-incrementada – id:
Assim como em CURSO, a coluna ID é usada para identificar unicamente cada registro na tabela AlunoCurso com o AUTOINCREMENT.
Chaves Estrangeiras (FOREIGN KEY):
aluno_cpf: Referencia o campo CPF da tabela ALUNO.
urso_id: Referencia o campo ID da tabela CURSO.
Essas definições ajudam a garantir a integridade referencial, ou seja, cada associação deve ter um aluno e um curso existentes.

         [Aluno]                           [Curso]
          (cpf) <-------------------------> (id)
           |                                  |
           |            [AlunoCurso]          |
           |         (id AUTOINCREMENT)       |
           |      aluno_cpf  |   curso_id     |
           +-----------------+----------------+




