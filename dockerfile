FROM ubuntu:18.04

MAINTAINER Your Name "quan.poko2000@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flashcards/requirements.txt

WORKDIR /flashcards

RUN pip install -r requirements.txt

COPY . /flashcards

ENTRYPOINT [ "python3" ]

CMD [ "flashcards.py" ]