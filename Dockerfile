
FROM python:3.11.3-alpine3.18
LABEL mantainer="bernardo181105@gmail.com"

# Impede o Python de gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Saída do Python será exibida imediatamente no console ou em  outros dispositivos de saída, sem ser armazenada em buffer. Em resumo, visualizae os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1


COPY /src/finances /finances
COPY scripts /scripts

# Entra na pasta finances no container
WORKDIR /src/finances

# A porta 8000 estará disponível para conexões externas ao container
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /finances/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts



ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]
