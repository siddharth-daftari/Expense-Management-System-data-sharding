FROM python:2.7
COPY . /app1
WORKDIR /app1
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5001
CMD ["app.py"]
