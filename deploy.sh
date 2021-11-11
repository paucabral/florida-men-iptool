#!/bin/bash


docker build -t floridameniptool .
docker run -t -d -p 5050:5050 --name floridameniptool_server floridameniptool
