FROM python:latest
WORKDIR /usr/src/srealitytask/srealitycrawl
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip install scrapy psycopg2 python-dotenv
COPY . .
CMD ["scrapy", "crawl", "sreality"]
