FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y cron

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY cronjob /etc/cron.d/price-tracker
RUN sed -i 's/\r$//' /etc/cron.d/price-tracker
RUN chmod 0644 /etc/cron.d/price-tracker

RUN touch /app/logs/cron.log

CMD ["cron", "-f"]

