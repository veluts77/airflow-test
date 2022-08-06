Демо airflow с парой Quarkus сервисов
-------------------------------------

Сборка
------
input-service
```
cd input-service
./mvnw package
docker build -f src/main/docker/Dockerfile.jvm -t quarkus/input-service-jvm .
cd ..
```
error-service
```
cd error-service
./mvnw package
docker build -f src/main/docker/Dockerfile.jvm -t quarkus/error-service-jvm .
cd ..
```


Запуск
------

```
docker compose up
```
после запуска сервисов в браузере открыть http://127.0.0.1:8080/

Добавление DB Connection
------------------------
- В UI Airflow перейти в Admin -> Connections
- Нажать "+" (add connection)
- Заполнить
  - Connection Id - tutorial_pg_conn
  - Connection Type - Postgres
  - Host - postgres
  - Schema - airflow
  - Login - airflow
  - Password - airflow
  - Port - 5432
- Save

Демо
----

Заполнение input таблицы данными
```
curl -X POST "http://localhost:8081/input?firstname=Bad&lastname=Examp1e"
curl -X POST "http://localhost:8081/input?firstname=Good&lastname=Example"
curl -X POST "http://localhost:8081/input?firstname=Good&lastname=Name"
```
Запуск DAG в Airflow

Просмотр результата в Airflow

Просмотр ошибок
```
docker logs airflow-test-error-service-1
```
Повторный запуск DAG в Airflow

Обработанные ранее имена повторно не обработаны (см UI Airflow и логи airflow-test-error-service-1)

Заполнение input таблицы новыми данными
```
curl -X POST "http://localhost:8081/input?firstname=8ad&lastname=Name"
curl -X POST "http://localhost:8081/input?firstname=Good&lastname=Example"
```
И последующий запуск с проверкой
