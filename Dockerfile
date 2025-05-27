FROM python:3.12.8

LABEL authors=[PGenly,Exifs]

COPY requirements.txt .
COPY gitingest-0.1.4.tar.gz .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3", "src/main.py"]