FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /myDir
WORKDIR /myDir
RUN pip3 install -r requirements.txt
COPY . /myDir/
CMD python manage.py runserver 0.0.0.0:8000
