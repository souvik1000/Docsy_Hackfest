FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
COPY . /myDir/
RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python docsy/manage.py makemigrations
RUN python docsy/manage.py migrate
CMD ["python", "docsy/manage.py","runserver","0.0.0.0:8000"]
WORKDIR /docsy
RUN python manage.py test
