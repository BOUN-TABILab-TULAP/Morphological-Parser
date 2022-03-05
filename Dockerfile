
FROM docker.io/python:3.7

COPY . /workspace
WORKDIR /workspace

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt

EXPOSE 4444
CMD ["gunicorn", "-w", "2", "--chdir",  "./morphological_parser/", "api:app", "-b", "0.0.0.0:4444"]
