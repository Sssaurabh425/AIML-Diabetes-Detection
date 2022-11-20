FROM python:3.9

# Expose port you want your app on
EXPOSE 8080

# Upgrade pip and install requirements
COPY . /app
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory

WORKDIR /app

# Run
ENTRYPOINT ["streamlit", "run", "app.py", "–server.port=8080", "–server.address=0.0.0.0"]