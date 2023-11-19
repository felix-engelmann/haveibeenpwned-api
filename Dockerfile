FROM python:3.11
MAINTAINER Felix Engelmann "fe-docker@nlogn.org"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
