FROM python:3.7-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update gcc libc-dev linux-headers && rm -rf /var/cache/apk/*
RUN pip install --no-cache-dir -r requirements.txt
# RUN apk add --no-cache py3-psutil

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

EXPOSE 5000