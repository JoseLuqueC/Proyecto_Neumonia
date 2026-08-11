# Usamos la imagen OFICIAL de uv proporcionada por sus creadores (Astral)
# Esto garantiza que NO usamos pip en absoluto en ninguna parte del proceso
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Copiar el archivo de configuración de dependencias de uv
COPY pyproject.toml .

# Crear el entorno virtual e instalar dependencias estrictamente con uv
RUN uv venv && uv sync --no-dev || true

# Copiar el código fuente de nuestra aplicación
COPY src/ src/

# Comando por defecto para ejecutar usando el entorno de uv
CMD ["uv", "run", "python", "src/main.py"]
