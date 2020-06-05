#!/bin/bash
app="docker.flashcards"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/flashcards ${app}