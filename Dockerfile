FROM dockerfile/python


ADD setup.py /opt/install/setup.py

WORKDIR /opt/install

RUN pip install -e .
