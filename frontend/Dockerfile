FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0", "frontendCRUD_product.py"]