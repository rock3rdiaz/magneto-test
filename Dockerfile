FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN apt-get -y update
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN chmod +x /app/entry_point.sh
CMD ["/app/entry_point.sh"]