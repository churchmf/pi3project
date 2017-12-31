FROM nginx
RUN npm install -g @angular/cli
RUN npm install
RUN ng build --prod
COPY nginx.conf /etc/nginx/nginx.conf
COPY dist/prod /usr/share/nginx/html
EXPOSE 80