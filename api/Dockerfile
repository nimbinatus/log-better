FROM python:alpine
MAINTAINER Laura Santamaria <laura@nimbinatus.com>

RUN python3 -m ensurepip
RUN pip3 install --upgrade pip \
  && pip3 install virtualenv

RUN adduser -D -g "" -u 1000 loggerapi
RUN mkdir -p /logger /venv /usr/logger
RUN chown -R loggerapi:loggerapi /logger /venv
ENV PYTHONPATH /logger

RUN virtualenv /venv
ENV PATH /venv/bin:${PATH}

COPY ./requirements.txt /logger/requirements.txt
RUN pip3 install -r /logger/requirements.txt
COPY . /logger

VOLUME /usr/logger
WORKDIR /logger

USER loggerapi

EXPOSE 8080

CMD ["python3", "-m", "server"]