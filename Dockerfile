FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
build-essential \
curl \
software-properties-common \
git \
&& rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/AlexanderEyfler/first_streamlit_app .
RUN pip3 install -r requirements.txt
EXPOSE 8051
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT [ "streamlit", "run", "0_Main_page.py", "--server.port=8501", "--server.address=0.0.0.0" ]