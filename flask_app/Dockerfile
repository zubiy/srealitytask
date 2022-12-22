FROM python:latest
WORKDIR /usr/src/srealitytask/flask_app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip install Flask psycopg2 python-dotenv
COPY . .
CMD ["python", "app.py"]
