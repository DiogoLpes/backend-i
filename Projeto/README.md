4. Sistema de Reservas para um Restaurante com FastAPI e Typer
Descrição: Um sistema para gerenciar reservas em um restaurante, com uma API para integração com sites ou aplicativos e um CLI para uso interno.

Funcionalidades:

FastAPI:

GET /reservations: Listar todas as reservas.
POST /reservations: Criar uma nova reserva.
PUT /reservations/{id}: Atualizar uma reserva existente.
DELETE /reservations/{id}: Cancelar uma reserva.
GET /availability: Verificar disponibilidade de mesas em um horário específico.

Typer (CLI):
reservation add: Adicionar uma reserva (ex: reservation add --name "João" --date "2023-10-15" --time "19:00").

reservation list: Listar reservas.
reservation update: Atualizar uma reserva (ex: reservation update --id 1 --time "20:00").
reservation delete: Cancelar uma reserva (ex: reservation delete --id 1).
reservation availability: Verificar disponibilidade.
Banco de Dados: PostgreSQL.

Extras:
Autenticação de usuários.
Integração com Docker e Docker Compose.
