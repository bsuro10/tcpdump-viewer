FROM bsuro10/python-36-flask
WORKDIR /app
ENV FLASK_APP main.py
COPY record.sh .
COPY main.py .
EXPOSE 5000
CMD ["python3","-m","flask","run"]
