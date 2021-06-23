FROM node:14
COPY package*.json ./
WORKDIR /usr/src/app
EXPOSE 8080
RUN npm install
COPY . .
CMD [ "node", "index.js" ]
