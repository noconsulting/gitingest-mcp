FROM python:3.12.8

LABEL authors=[PGenly,Exifs]

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "src/main.py"]