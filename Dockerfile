FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh

EXPOSE 5000

CMD ["sh", "/app/run.sh"]