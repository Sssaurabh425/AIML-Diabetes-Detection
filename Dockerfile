FROM python:3.9



COPY . /app
# Copy app code and set working directory
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt



# Expose port you want your app on
EXPOSE $PORT

# Run
ENTRYPOINT ["streamlit", "run", "app.py", "–server.port=$PORT", "–server.address=0.0.0.0"]