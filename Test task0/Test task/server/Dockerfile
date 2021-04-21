FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
EXPOSE 8080
COPY server0.py /
COPY parsetext.py /
CMD ["python","server0.py"]


