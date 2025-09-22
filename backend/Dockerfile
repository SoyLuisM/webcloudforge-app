FROM python:3.11.9-alpine3.20
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE ${EXPOSE_PORT}
CMD ["sh", "entrypoint.sh"]