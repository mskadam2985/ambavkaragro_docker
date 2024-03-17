FROM python:3.10.13-bullseye
WORKDIR /ambavkaragro_web
COPY ./ambavkaragro_docker ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /ambavkaragro_web/requirements.txt --no-cache-dir

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn","ambavkaragro.wsgi:application","--bind", "0.0.0.0:8000" ]