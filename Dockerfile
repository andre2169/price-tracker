# 1. Imagem base: Python oficial
FROM python:3.11-slim

# 2. Diretório de trabalho dentro do container
WORKDIR /app

# 3. Copiar dependências primeiro (melhora cache)
COPY requirements.txt .

# 4. Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o resto do código
COPY . .

# 6. Comando padrão do container
CMD ["python", "main.py"]
