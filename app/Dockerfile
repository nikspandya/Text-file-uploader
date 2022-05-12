FROM python:3.8-buster


COPY . /main

WORKDIR /main

# Always need the latest version
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 8610

CMD [ "run.py" ]