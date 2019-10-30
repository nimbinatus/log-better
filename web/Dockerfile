FROM node:alpine
MAINTAINER Laura Santamaria <laura@nimbinatus.com>

RUN adduser -D -g "" -u 1001 webrun
RUN mkdir -p /webbase /usr/webbase

COPY . /webbase
RUN yarn install --production
RUN yarn global add serve
RUN cd /webbase && yarn run build

VOLUME /usr/webbase
WORKDIR /webbase

USER webrun

EXPOSE 8081

CMD ["serve", "-s", "build", "-l", "8081"]