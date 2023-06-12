FROM ubuntu:20.04

COPY setup.py .
COPY sample_project .

RUN pip install sample_project

ENTRYPOINT ["sample-project"]