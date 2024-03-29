FROM python

COPY ./requirements.txt /home/myapp/requirements.txt
RUN pip install -r /home/myapp/requirements.txt
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/
COPY api.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/app.py