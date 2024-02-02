FROM public.ecr.aws/docker/library/python:3

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]