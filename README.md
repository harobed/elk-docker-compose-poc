## Start services

```
$ docker-compose up -d
$ docker-compose logs -f
```

## Send one Gelf log message

```
$ ./send_udp_gelf_log.sh
```


## Generate fake json-file log

```
$ pip install -r requirements.txt
$ ./fakelog.py > logs/json-file.log
```

## Connect Docker to Graylog:

```
$  docker run --log-driver=gelf --log-opt gelf-address=udp://127.0.0.1:12201 --log-opt gelf-compression-type=gzip --rm -it ubuntu bash
root@1cb70f449905:/# echo "Msg"
Msg
```


## Urls list

* Kopf: http://localhost:9200/_plugin/kopf/
* Kibana: http://localhost:5601/


