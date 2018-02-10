FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "indexer.py" ]
