FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
COPY . /myDir/
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python docsy/manage.py makemigrations
RUN python docsy/manage.py migrate
CMD ["python", "docsy/manage.py","runserver","0.0.0.0:8000"]
WORKDIR /myDir/docsy
RUN python manage.py test receptionist/
