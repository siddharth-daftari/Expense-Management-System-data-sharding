FROM python:2.7
COPY . /app3
WORKDIR /app3
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5003
CMD ["app.py"]
