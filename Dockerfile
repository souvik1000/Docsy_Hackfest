FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
COPY . /myDir/
RUN pip install -r requirements.txt
CMD python docsy/manage.py runserver 0.0.0.0:8000
