#!/bin/sh
# build angular app
#npm install -g @angular/cli
#npm install --prefix ./angular-app/my-app
#ng build ./angular-app/my-app --prod

# bring up nginx and angular app
docker-compose build
docker-compose up -d

# stream video to nginx
raspivid -o - -t 0 --mode 5 --annotate 12 | ffmpeg -loglevel warning -re -f h264 -i - -vcodec copy -f flv rtmp://localhost:1935/dash/test &