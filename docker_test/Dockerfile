FROM python:3.7.5
USER root
ADD ./test /opt/test
ADD run.sh /root
ADD requirements.txt /root
WORKDIR /root
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/root/run.sh"]
