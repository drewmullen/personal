FROM node:7

WORKDIR /usr/src/app

COPY package.json package.json
COPY server.js server.js

RUN npm install

EXPOSE 80

ENTRYPOINT ["npm", "start"]
