FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --no-cache-dir flask
EXPOSE 8080
<<<<<<< HEAD
ENV DB_HOST="localhost:3307/"
ENV MASTER_USER="root"
ENV MASTER_PASSWORD="root"
CMD ["python", "app.py"]
COPY static/ /app/static/
=======
ENV DB_HOST="localhost:3306"
ENV MASTER_USER="root"
ENV MASTER_PASSWORD="root"
CMD ["python", "app.py"]
>>>>>>> 02185a2 (updated)
