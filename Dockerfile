



FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY ./test/ /code/
CMD python manage.py runserver 0.0.0.0:8000
