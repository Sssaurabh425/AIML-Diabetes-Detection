FROM python:3.9

COPY . /diabetes

WORKDIR /diabetes

EXPOSE 8501

RUN pip3 install -r requirements.txt
# Expose port you want your app on


# Run
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]