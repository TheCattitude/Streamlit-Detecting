# ####### 👇 SIMPLE SOLUTION (x86 and M1) 👇 ########
FROM python:3.8.12-buster
WORKDIR /prod
COPY . .
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install .
CMD uvicorn speeches.api.fast:app --host 0.0.0.0 --port $PORT

