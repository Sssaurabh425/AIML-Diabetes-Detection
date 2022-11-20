FROM python:3.9

COPY . /diabetes

WORKDIR /diabetes

EXPOSE $PORT

RUN pip3 install -r requirements.txt
# Expose port you want your app on


# Run
CMD streamlit run --server.port $PORT app.py