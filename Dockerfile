FROM public.ecr.aws/docker/library/python:3

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]