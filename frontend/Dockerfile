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
COPY --from=builder /app/dist /usr/share/nginx/html
CMD [ "nginx", "-g", "daemon off;" ]
