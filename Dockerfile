FROM python:latest
MAINTAINER Felix Engelmann "fe-docker@nlogn.org"
COPY api /api
WORKDIR /api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api/api.py"]