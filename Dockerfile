FROM python:3.11.7

WORKDIR /HomeWork_2_2

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
