FROM python:2.7
COPY . /app2
WORKDIR /app2
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5002
CMD ["app.py"]
