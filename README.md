

Realize fork do projeto para a sua conta

Clone o projeto a partir da sua conta
```sh
git clone https://github.com/{sua_conta}/challenge-life
```

Crie uma branch chamada desafiov1
```sh
git checkout -b desafiov1
```

## Objetivo
O desafio do curso é criar uma aplicação backend com fast API usando a mesma estutura da aplicação apresentada no curso. Se trata de uma aplicação que faz a gestão de Eventos.

Temos tres dominios para desenvolver
- Usuarios (Users) - usuarios que se cadastram na app para participar de um evento
- Eventos (Events) - eventos cadastrados pelos promotores que posteriormente possam usados pelos usuarios realizar as reservas
- Registro (Registration) - registro de um usuario a um evento

## Creterios de avaliação

- O projeto deve ser disponibilizado via github e compartilhado para correção. Durante o desenvolvimento você pode realizar PR para a master e ir abrindo novas branchs consecutivas (desafiov1, desafiov2, desafiov3) isso depende da organização individual de cada um mas é importante para se familializar com esse fluxo.

- O projeto deve seguir a estrutura do projeto new life bank
```json
├── app
│   ├── commons
│   ├── config
│   ├── domain
│   │   ├── user
│   │   ├── events
│   │   └── registration
│   └── main.py
```
- Ao menos 2 dominios precisam ser implementados (user e events) o registration é bonus

- Pode utilizar a base do sqlite ou Posgres, faça o que vc se sentir mais confortavel (No caso de Posgre crie o Docker-compose do projeto)

- O projeto deve rodar em qualquer ambiente, crie o passo a passo para que qualquer pessoa consiga executar o projeto (veja exemplo do new_life_bank)

- Crie um arquivo database.sql com os comandos DDL para criar a tabela, mesmo que não seja utilizado por conta do ORM é importante para validar o entendimento do relacionamento das tabelas

- Se atente as regras de validação de cada contexto, estão marcadas como `regras` (importante, regras é sempre validada na camada service ou no schema do pydantic)

* bonus - Crie o docker da aplicação

## Exemplos de APIS

GET	/api/v1/users	Recuperar uma lista de usuarios

Response:
```json
  {
    "id": 1,
    "active": true,
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "email": "marshmccall@ultrimax.com"
  }
```
GET	/api/v1/users/{id}	Recuperar um usuario especifico

Response:
```json
  {
    "id": 1,
    "active": true,
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "email": "marshmccall@ultrimax.com"
  }
```

POST /api/v1/users	Criar um usuario
```
regra: um usuario deve ter no minimo 18 anos
regra: o email deve ser unico por usuario
```
Request: 
```json
  {
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",    
    "email": "marshmccall@ultrimax.com"
  }
```

Response:
```json
  {
    "id": 1,
    "active": true,
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "email": "marshmccall@ultrimax.com"
  }
```

PUT /api/v1/users	Atualizar um usuario
```
regra: deve respeitar as mesmas regras do cadastro
```
Response:
```json
  {
    "age": 28,
    "name": "Marsh Mccall",
    "gender": "male",
    "email": "marshmccall@ultrimax.com"
  }
```

POST /api/v1/event	Criar um evento
```
regra: a data deve ser maior que a data atual
```
Request:
```json
{
    "name": "my event",
    "description": "meetup dev conf",
    "start": "2018-05-12T02:00:00Z",
    "end": "2018-05-12T02:00:00Z",
    "online_event": false,
    "location_address": "xxxxx",
    "organizer_email": "teste@gmail.com", 
    "capacity": 100
  }

```

Response:
```json
{
    "id": 123,
    "name": "my event",
    "description": "meetup dev conf",
    "start": "2018-05-12T02:00:00Z",
    "end": "2018-05-12T02:00:00Z",
    "online_event": false,
    "location_address": "xxxxx",
    "organizer_email": "teste@gmail.com",
    "status": "ACTIVE", 
    "capacity": 100,
  }

```

PUT /api/v1/event/{id}	Atualizar um evento

Request:
```json
{
    "name": "my event",
    "description": "meetup dev conf",
    "start": "2018-05-12T02:00:00Z",
    "end": "2018-05-12T02:00:00Z",
    "online_event": false,
    "location_address": "xxxxx",
    "organizer_email": "teste@gmail.com",
    "listed": false,
    "capacity": 100,
  }
```

Response:
```json
{
    "id": 123,
    "name": "my event",
    "description": "meetup dev conf",
    "start": "2018-05-12T02:00:00Z",
    "end": "2018-05-12T02:00:00Z",
    "online_event": false,
    "location_address": "xxxxx",
    "organizer_email": "teste@gmail.com",
    "status": "ACTIVE", 
    "capacity": 100,
  }

```
GET	/api/v1/event/{id}	recuperar um evento especifico

Response:
```json
{
    "id": 123,
    "name": "my event",
    "description": "meetup dev conf",
    "start": "2018-05-12T02:00:00Z",
    "end": "2018-05-12T02:00:00Z",
    "online_event": false,
    "location_address": "xxxxx",
    "organizer_email": "teste@gmail.com",
    "status": "ACTIVE", 
    "capacity": 100,
  }
```

POST /api/v1/event/{event_id}/registration	Registrar um evento
```
regra: deve existir uma vaga disponivel para se cadastrar (repeitar a capacidade total)
regra: um usuario não pode fazer mais do que uma reserva
```
Request:
```json
{
    "user_email": "teste@gmail.com" 
}
```

Response:
```json
{
    "user_email": "teste@gmail.com" 
    "registration_status": "RESERVED" 
}
```

GET /api/v1/event/{event_id}/registration/{user_email} recupera o status de um evento
Response:
```json
{
    "user_email": "teste@gmail.com" 
    "registration_status": "CANCELED" 
}
```

PATCH /api/v1/event/{event_id}/registration/{user_email} Desregistrar um evento (mudar o status)
Request:
```json
{
    "registration_status": "CANCELED" 
}
```
