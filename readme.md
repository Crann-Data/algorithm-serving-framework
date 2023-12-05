

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
docker run --name testing-postgres -e POSTGRES_PASSWORD=password -d postgres
```
```bash
createdb -h localhost -p 5432 -U postgres algorithms
```

```bash
PGSERVICEFILE=.pg_service.conf python manage.py runserver
```
