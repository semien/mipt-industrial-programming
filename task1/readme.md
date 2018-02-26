## Запуск:
+ sudo docker-compose up -d
+ docker build ./producer -t task1_producer
+ docker run --net="host" -i -t task1_producer
