FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]