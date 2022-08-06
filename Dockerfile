FROM python:3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]

# docker build -t flask-kubernetes .
# docker run -d -p 5000:5000 flask-kubernetes