

## usfeul cURLs


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
docker run --name testing-postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```
```bash
createdb -h localhost -p 5432 -U postgres algorithms
```

```bash
chmod 0600 .my_pgpass
```

```bash
PGSERVICEFILE=.pg_service.conf python manage.py runserver
```

> export ENV for session usage
> ```bash
>export PGSERVICEFILE=.pg_service.conf 
>```

```python
In [1]: from algorithms.models import Algorithm
```