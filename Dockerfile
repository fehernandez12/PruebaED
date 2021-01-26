FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update -qq && apt-get install -y -qq \
    # Librerías estandar
    git less nano curl \
    ca-certificates \
    wget build-essential\
    # GeoDjango
    binutils libproj-dev gdal-bin \
    # Postgres
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*
RUN export LD_LIBRARY_PATH=/usr/local/lib
RUN ldconfig
COPY . /code/