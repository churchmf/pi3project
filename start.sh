#!/bin/sh
# build angular app
#npm install -g @angular/cli
#npm install --prefix ./angular-app/my-app
#ng build ./angular-app/my-app --prod

# bring up nginx and angular app
docker-compose up -d

# stream video to nginx
raspivid -o - -t 0 -vf -hf -fps 10 -b 500000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://localhost:1935/live/test &