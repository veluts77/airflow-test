# Info

Option for cluster in corp cloud (with csi-ceph-ssd-ug1-retain storage class)

# Installation

## Create namespace

```
kubectl create namespace airflow
```

## Install helm chart

```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm search repo airflow
```

```sh
helm install -f values.yaml airflow apache-airflow/airflow --namespace airflow  --debug 
```

# Upgrade
! May suffer from low resources on small cluster !

```sh
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yaml --debug
```
# See also

https://marclamberti.com/blog/airflow-on-kubernetes-get-started-in-10-mins/

# Known issues

## Create user job may create no admin user

Запустить команду в поде вебсервера:

```
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```
