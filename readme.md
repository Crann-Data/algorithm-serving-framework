

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
