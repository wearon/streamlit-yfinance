# app/Dockerfile

FROM lambci/lambda:build-python3.9

RUN yum -y install gcc-c++ pkgconfig poppler-cpp-devel poppler-utils python-devel redhat-rpm-config

RUN pip install -U pip-tools && \
pip install -U pdftotext && \
pip install -U zappa

RUN virtualenv --verbose /venv

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]