FROM ubuntu:18.04

RUN apt update && apt upgrade -y
RUN apt install -y python3-scipy python3-pip

# Cython must be installed first before scikit-learn
RUN pip3 install cython==0.29.7

COPY . /app
WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP app.py

RUN pip3 install -r requirements.txt 

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
