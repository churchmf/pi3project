FROM nginx
RUN npm install -g @angular/cli
WORKDIR /my-app
RUN npm install
RUN ng build --prod
COPY nginx.conf /etc/nginx/nginx.conf
COPY dist /usr/share/nginx/html
EXPOSE 80