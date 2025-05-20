FROM python:3.12.8

LABEL authors=py-mcp

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "server.py"]