FROM node:20-alpine
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 4200

# Forzamos a Angular a exponerse hacia la red de Docker
CMD ["npm", "start", "--", "--host", "0.0.0.0"]