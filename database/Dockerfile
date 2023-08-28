FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y
RUN pip3 install -r requirements.txt

CMD [ "python", "schema_products.py" ]