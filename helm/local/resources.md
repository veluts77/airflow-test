| workload           | CPU requests | RAM requests | CPU limits | RAM limits |
|--------------------|--------------|--------------|------------|------------|
| workers            | 1000m        | 2000Mi       | 1500m      | 2000Mi     |
| -logGroomerSidecar | 100m         | 100Mi        | 100m       | 100Mi      |
| scheduler          | 200m         | 1000Mi       | 500m       | 1000Mi     |
| -logGroomerSidecar | 100m         | 100Mi        | 100m       | 100Mi      |
| createUserJob      | 100m         | 200Mi        | 300m       | 200Mi      |
| migrateDatabaseJob | 200m         | 500Mi        | 300m       | 500Mi      |
| webserver          | 1000m        | 2000Mi       | 1500m      | 2000Mi     |
| triggerer          | 200m         | 500Mi        | 400m       | 500Mi      |
| statsd             | 100m         | 100Mi        | 200m       | 200Mi      |
| redis              | 200m         | 500Mi        | 300m       | 500Mi      |
| postgresql         | 200m         | 500Mi        | 1000m      | 1000Mi     |
