FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
COPY . /myDir/
# install google chrome




# chromeDriver v2.35
RUN wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip



RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python docsy/manage.py makemigrations
RUN python docsy/manage.py migrate
CMD ["python", "docsy/manage.py","runserver","0.0.0.0:8000"]
