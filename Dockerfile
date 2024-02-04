FROM python:3.10.13

COPY . /src

WORKDIR /src

EXPOSE 8080

CMD ["python", "tserver.py"]
