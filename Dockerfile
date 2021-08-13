FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get -y update && apt install -y build-essential

ARG HOME='/root'
ARG project_dir=/projects/
RUN apt-get install -y git
RUN pip install --upgrade pip && pip install autopep8
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . $project_dir
CMD ["uvicorn", "app:app", "--reload","--host", "0.0.0.0", "--port", "8000", "--log-level", "trace"]