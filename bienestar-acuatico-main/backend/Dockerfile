FROM node:20-alpine
WORKDIR /app

# Copiar dependencias e instalarlas
COPY package*.json ./
RUN npm install

# Copiar el resto del código
COPY . .

EXPOSE 4100

# Comando para iniciar el servidor
CMD ["npm", "run", "dev"]