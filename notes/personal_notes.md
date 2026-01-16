docker compose up 
docker compose down
docker network ls
docker ps -a
cd pipeline

Using uv to install libraries is faster and adds them to the pyproject.toml file as dependancies to have in the container

Once docker compose up is used a port is created that can be opened in the browser for PGAdmin, enter in password and user name and becuase using a docker compose file the previous server we created plus the tables will still be there

Can use following code to create new table, just change file name and month or year
docker run -it \
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips_2021_1 \
    --year=2021 \
    --month=1 \
    --chunksize=100000
