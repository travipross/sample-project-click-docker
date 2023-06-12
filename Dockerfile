FROM python:3.9

WORKDIR /workdir 

COPY setup.py setup.py
COPY setup.cfg setup.cfg
COPY sample_project/ sample_project/

RUN pip install .

ENTRYPOINT ["sample-project"]