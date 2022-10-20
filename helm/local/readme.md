# Info

Option for local one node cluster like "Rancher in docker"

# Installation

## Install Storage class and PVs first

```
kubectl apply -f add_pvs.yaml --namespace airflow
```

## Install helm

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
