FROM  python:3.9

RUN pip3 install --upgrade pip

COPY requirements.txt /opt/
RUN pip3 --no-cache-dir install -r /opt/requirements.txt

WORKDIR /opt

COPY ["app.py", "/opt"]

EXPOSE 5001

CMD ["python3", "app.py"]