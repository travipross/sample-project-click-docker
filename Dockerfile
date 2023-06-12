FROM python:3.9

COPY setup.py setup.cfg
COPY setup.cfg setup.py
COPY sample_project/ sample_project/

RUN pip install setuptools
RUN python3 -m pip install ./sample_project

ENTRYPOINT ["sample-project"]