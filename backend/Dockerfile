FROM python:3.12-alpine3.21
#
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#
RUN chown -R appuser:appgroup /app
USER appuser
#
EXPOSE ${EXPOSE_PORT}
CMD ["sh", "entrypoint.sh"]