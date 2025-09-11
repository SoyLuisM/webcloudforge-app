FROM node:22.19.0-alpine3.22 AS dev-deps
WORKDIR /app
COPY package.json package.json
RUN npm install

FROM node:22.19.0-alpine3.22 AS builder
WORKDIR /app
COPY --from=dev-deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM nginx:1.29.1-alpine AS prod
EXPOSE 80
# RUN addgroup mi_grupo && adduser -S -G mi_grupo mi_usuario
# COPY --chown=mi_usuario:mi_grupo --from=builder /app/dist /usr/share/nginx/html
COPY --from=builder /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
# USER mi_usuario
CMD [ "nginx", "-g", "daemon off;" ]
