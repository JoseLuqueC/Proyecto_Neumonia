.PHONY: help install run test lint build up down

help:
	@echo "Comandos disponibles:"
	@echo "  make install - Instala las dependencias con uv"
	@echo "  make run     - Ejecuta la aplicación principal"
	@echo "  make test    - Ejecuta las pruebas con pytest"
	@echo "  make lint    - Revisa el código buscando errores"
	@echo "  make build   - Construye la imagen Docker"
	@echo "  make up      - Levanta el entorno con Docker Compose"
	@echo "  make down    - Detiene el entorno de Docker"

install:
	uv sync

run:
	uv run python -m src.main

test:
	uv run pytest test/

lint:
	uv run ruff check src/ test/

build:
	docker build -t neumonia-app .

up:
	docker compose up -d

down:
	docker compose down
