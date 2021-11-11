#!/bin/bash


docker build -t floridameniptool .
docker run -t -d -p 5000 --name floridameniptool_server floridameniptool
