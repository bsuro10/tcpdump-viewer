FROM registry.access.redhat.com/ubi8/python-36-flask
WORKDIR /app
COPY record.sh /app
COPY main.py /app
CMD ["python3","-m","flask","main.py"]
