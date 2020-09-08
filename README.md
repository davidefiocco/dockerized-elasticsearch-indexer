# Start and index Elasticsearch in containers

Example showing how to index an Elasticsearch db using the Python client within a Docker container, as in https://stackoverflow.com/questions/48711455/create-dockerized-elasticsearch-index-using-a-python-script-running-in-docker/48712414#48712414  

Run with

```bash
docker-compose build
docker-compose up
```

## Troubleshooting

Check https://github.com/docker-library/elasticsearch/issues/111 in case of troubles in the logs with `vm.max_map_count`.