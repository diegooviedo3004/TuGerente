FROM python:3.8.14-buster 

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN \
  apt-get -y update && \
  apt-get -y install --no-install-recommends \
    gcc \
    build-essential \
    dnsutils \
    default-mysql-client \
    libmariadb-dev-compat \
    postgresql-client \
    xmlsec1 \
    git \
    uuid-runtime \
    libcurl4-openssl-dev \
    && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists && \
  true

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
