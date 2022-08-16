FROM python:3.9-bullseye
RUN apt update && apt install -y libpq-dev
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY manage.py manage.py
RUN mkdir /marina
ENV PYTHONPATH=$PYTHONPATH:/marina
COPY kickoff_marina.sh /kickoff_marina.sh
CMD ["/usr/bin/env", "bash", "/kickoff_marina.sh"]
