FROM python:3.8

WORKDIR /URL

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY /website ./website

COPY ./main.py .

CMD ["python", "main.py"]