FROM python:3.12

# As if you were doing "cd .."
WORKDIR /app

COPY . .
# RUN command: like trying to run a linux command
RUN pip install -r requirements.txt

CMD [ "python", "src/circle.py" ]
