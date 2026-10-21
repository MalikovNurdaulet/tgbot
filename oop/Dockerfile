FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Almaty

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .
COPY functions.py .
COPY oop/ ./oop/
COPY syllabus/ ./syllabus/

CMD ["python", "-u", "bot.py"]
