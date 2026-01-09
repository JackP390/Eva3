# 📅 Sistema de Reserva de Salas y Recursos

Sistema backend diseñado para gestionar la reserva de espacios físicos (salas de estudio/biblioteca) en un entorno universitario, evitando conflictos de horario y duplicidad.

## ⚡ Puntos Destacados
* **Modelado de Datos:** Estructura relacional sólida entre `Sala`, `Reserva` y `Usuario`.
* **Validación Lógica:** El sistema verifica disponibilidad antes de confirmar una reserva (evita *double-booking*).
* **Optimización de Consultas:** Diseño orientado a minimizar el impacto en la base de datos al listar reservas masivas.
* **Administración:** Panel de control para gestionar el inventario de salas disponibles.

## 🛠️ Tecnologías
* Python / Django
* Gestión de Fechas y Horarios (Datetime)
* SQLite3
