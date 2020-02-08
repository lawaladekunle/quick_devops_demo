# This docker image consists of a python development environment and also the code for the flask app 

FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
WORKDIR /app
COPY requirements.txt /app
COPY app.py /app
RUN pip install -r /app/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
