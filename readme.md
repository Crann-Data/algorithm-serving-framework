# Algorithm Serving Framework - Version 0

This project's goal is to offer a reusable framework for deploying machine learning algorithms. The finished project should allow a user to upload, manage, deploy, and monitor a machine learning algorithm. The chosen model format is ONNX, other compatibilities are welcome.

## Key properties
- Receive ONNX file from user to create a model
- Allow user to create endpoint, and expose this on the server
- Allow user to make REST based inference calls to the model bound to this endpoint
- Return the reponses outwards to the user
- Extend and document CLI compatibility for CI/CD integration

### Nice to have's:
- Monitoring and usage metrics
- Return responses to alternative locations (MQTT, endpoint, or DB)
- Accept any model format and convert to ONNX

## Usfeul cURLs


```bash
curl localhost:4000/ -F "file=@test-image.jpg"
```

```bash
seq 1 50 | xargs -P5 -I{} curl localhost:4000/ -F "file=@test-image.jpg"
```

```bash
docker build . -t model-server && docker run -p 4000:4000 model-server
```

```bash
docker stats
```



```bash
docker run --name testing-postgres -e POSTGRES_PASSWORD=password -p 5432:5432 --restart unless-stopped -d postgres
```
```bash
createdb -h localhost -p 5432 -U postgres algorithms
```

>```bash
>chmod 0600 .my_pgpass
>```

```bash
PGSERVICEFILE=.pg_service.conf python manage.py makemigrations
```
```bash
PGSERVICEFILE=.pg_service.conf python manage.py migrate
```


```bash
PGSERVICEFILE=.pg_service.conf python manage.py createsuperuser
> Username (leave blank to use ''): 
> Email address: 
> Password: 
> Password (again): 
> Superuser created successfully.
```


```bash
PGSERVICEFILE=.pg_service.conf python manage.py runserver
```

>export ENV for session usage
> ```bash
>export PGSERVICEFILE=.pg_service.conf 
>```


```bash
docker run --name algorithmServing-celery-redis -p 6379:6379 --restart unless-stopped -d redis
```

```bash
python -m celery -A algorithmServing worker
```

```bash
celery --broker=redis://localhost:6379/0 flower
```