# Use elastic opensource version as runtime
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:7.9.1

# Avoid error from bootstrap checks
USER root
RUN echo "discovery.type: single-node" >> /usr/share/elasticsearch/config/elasticsearch.yml
