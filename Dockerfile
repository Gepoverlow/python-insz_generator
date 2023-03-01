FROM python:3.8-slim-buster
WORKDIR /python_insz_generator
COPY requirements.txt  requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn" , "-b" , "0.0.0.0:8000" , "api.app:__hug_wsgi__"]
EXPOSE 8000