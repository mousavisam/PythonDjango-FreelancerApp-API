#######  Development #########
FROM python:3.9
RUN apt -y update && apt -y install net-tools vim telnet curl


#######  Production #########
# FROM python:3.8-slim-buster


ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app



COPY requirements.txt /app/.

RUN pip install -r /app/requirements.txt


COPY main /app/main
#COPY deployment /app/.

EXPOSE 8100

# use this command to debug
#ENTRYPOINT ["tail", "-f", "/dev/null"]


