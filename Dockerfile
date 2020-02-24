FROM python:3

ADD ./PythonBackend /PythonBackend

RUN pip3 install paho-mqtt
RUN pip3 install typing

CMD [ "python3", "PythonBackend/Objects.py" ]