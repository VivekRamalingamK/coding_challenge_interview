FROM python:3.9
COPY . /translations_api
WORKDIR /translations_api
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["API_Flask.py"]
