FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myDir
WORKDIR /myDir
COPY . /myDir/
# install google chrome
FROM python:2.7-stretch




# chromeDriver v2.35
RUN wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ADD selenium-base-image/xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
RUN ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
    && chmod 777 /usr/bin/chromium-browser

RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python docsy/manage.py makemigrations
RUN python docsy/manage.py migrate
CMD ["python", "docsy/manage.py","runserver","0.0.0.0:8000"]
WORKDIR /myDir/docsy
RUN python manage.py test receptionist/
