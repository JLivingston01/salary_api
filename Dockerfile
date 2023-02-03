FROM python:3.11-slim-buster
COPY ./requirements.txt /api/requirements.txt
WORKDIR /api
RUN pip install -r requirements.txt
COPY . /api
RUN python scripts/etl/update_salaries.py
ENTRYPOINT ["flask","--app","api/api.py","run","--host=0.0.0.0","--port=5000"]