FROM python:3.13-slim

WORKDIR /app

# Instalar uv
RUN pip install uv

# Copiar configuración (si existe)
COPY pyproject.toml .

# Crear el entorno virtual y sincronizar (ajusta luego si añades dependencias)
RUN uv venv && uv sync --no-dev || true

# Copiar el código fuente
COPY src/ src/

# Comando por defecto
CMD ["uv", "run", "python", "src/main.py"]
