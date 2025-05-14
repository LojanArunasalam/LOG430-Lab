FROM python:3

WORKDIR /home/log430/labs/LOG430-Lab

COPY . .

CMD [ "python", "./circle.py" ]
