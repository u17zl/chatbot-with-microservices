FROM alpine:latest
RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip
WORKDIR /service
COPY ./app /service
RUN pip3 install -r requirements.txt
EXPOSE 5000
WORKDIR /service/service1
CMD chmod +x  __init__.py
CMD python3 __init__.py
