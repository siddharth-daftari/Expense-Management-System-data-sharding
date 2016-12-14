FROM python:2.7
COPY . /testFile
WORKDIR /testFile
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 8000
CMD ["testFile.py"]

