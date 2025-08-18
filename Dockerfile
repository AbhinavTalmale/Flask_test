FROM python:3.12.7-slim-bullseye
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code
COPY . .

CMD ["python3", "-m","flask","--app","loan","run", "--host", "0.0.0.0"]