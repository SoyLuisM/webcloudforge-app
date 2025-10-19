FROM node:22.19.0-alpine3.22 AS dev-deps
WORKDIR /app
COPY package.json package.json
RUN npm install

FROM node:22.19.0-alpine3.22 AS builder
WORKDIR /app
COPY --from=dev-deps /app/node_modules ./node_modules
COPY . .
RUN npm run build


FROM nginx:1.29.1-alpine3.22 AS prod
EXPOSE ${FRONTEND_PORT_INTERN}
COPY --from=builder /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/templates/nginx.conf.template
COPY nginx/nginx_global.conf /etc/nginx/nginx.conf
CMD [ "nginx", "-g", "daemon off;" ]
