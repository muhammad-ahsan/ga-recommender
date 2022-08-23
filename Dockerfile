FROM python:3.8
MAINTAINER Muhammad Ahsan <muhammad.ahsan@gmail.com>

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get -q update && apt-get install -y --no-install-recommends gcc supervisor && rm -rf /var/lib/apt/lists/*

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile
WORKDIR /usr/src/app

COPY app.py ./
COPY swagger ./swagger
COPY templates ./templates
COPY src ./src


# Non production deployment
CMD ["python", "app.py"]
EXPOSE 5000
# PRODUCTION DEPLOYMENT

# COPY uwsgi.ini .
# COPY supervisord.conf /etc/supervisor/conf.d/
# RUN pip install pipenv uwsgi
# CMD ["supervisord", "-n"]