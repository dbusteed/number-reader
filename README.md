# lil' machine learning flask app for recognizing numbers

## checkout live app

i currently have it hosted on my raspberry pi [here](http://davis.mine.bz:5000)
(i might forget to update the DNS/IP, so apologies if the link is down)

navigate to `/ml` to enable "machine learning" mode, which allows the user to confirm predictions and add data to the system. this path is kinda hidden to prevent people from entering bad data.

## run on your local machine

1. `git clone https://github.com/dbusteed/number-reader`
2. `cd number-reader`
3. (optional) Start virtual environment
4. `pip install -r requirements.txt`
5. `python app.py`
6. open `localhost:5000` in a browser

NOTE: for UNIX machines use `pip3` and `python3`

## deploy on a raspberry pi

1. `git clone https://github.com/dbusteed/number-reader`
2. `cd number-reader`
3. `git checkout pi`
4. `docker build -t number-reader .` (may take ~30 min)
5. `docker run -p 5000:5000 -d number-reader`
6. open `<RPI_PUBLIC_IP>:5000` or `<DNS_NAME>:5000` in a browser

NOTE: i haven't tested this for running locally on a rpi, but it should probably work. if not try replacing the `python -m flask run --host=0.0.0.0` in the Dockerfile with `python -m flask run`
