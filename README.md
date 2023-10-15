# redisgraph


## deploy redisgraph
we use docker-compose to deploy the redisgraph in our cluster, the deploy yaml is also included under deploy directory
please make sure that you have
```
Docker version 19.03.9
docker-compose version 1.24.1
```
enter the deploy directory then excute command
```
docker-compose up -d
```
then if not problems shown up, the redisgraph will start, exposed port 6379, password is included in conf files

## generate graph and queries
with limitation of memory our linux machine, we choose sf=0.1
you can run the following command to generate data, and please make sure you have already have the sf0.1 directory in current path
```
docker run \
    --mount type=bind,source="$(pwd)/sf0.1",target=/out \
    ldbc/datagen-standalone:0.5.0-2.12_spark3.2 --parallelism 1 -- --format csv --scale-factor 0.1 --mode raw
```

after generating the data, enter the `${pwd}/sf0.1/graphs/csv/raw/composite-merged-fk` directory
setting enviroment variable
```
export LDBC_DATA_DIRECTORY=`pwd`
```

then you need tools from `https://github.com/ldbc/ldbc_snb_example_data`
enter the `ldbc_snb_example_data` directory
you need to downloads DuckDB if it's not yet available
run the following command
```
./load.sh ${LDBC_DATA_DIRECTORY} --no-header
./transform.sh
./export.sh
```
then the data will be processed and stored in the data directory in the current path
the data we need is in `data/csv-only-ids-projected-fk`
there is also another problems in here, in redisgraph and use redisgraph bulk loader, the id must be identical, so the header has to be preprocessed in advance, you can either choose to process it manually or just use the processed csv files under our github directory `parameters`

the queries are accquired from `https://github.com/ldbc/ldbc_snb_interactive_v1_impls/cypher/queries`

## load graph
install the redisgraph-bulk-loader
```
pip install redisgraph-bulk-loader==0.10.2
```
please note that `redisgraph-bulk-loader==0.10.2` requires `redis==4.3.6`

setting enviroment variable IMPORT_DATA_DIR_PROJECTED_FK, which should be the data directory mentioned above

after install the module using the command from `command` file to insert the data into redis, remember to change password if you don't have one or changed, which is configured in conf file, we apply bulking in the same machine that we deploy redisgraph, if you trying to connect to different redisgraph client that not in your machine, please add other parameters, you can check the instructions in redis-bulk-loader github pages


## run the queries to check the system
in this stage, you can first install requirements by
```
pip install -r requirements.txt # in our github directory
```
change the ip address, port and password in `config/config.yaml`

then run to check the system
```
python main.py
```

## about the queries
LDBC benchmark gives a lot of queries to test your database, you can get it from `https://github.com/ldbc/ldbc_snb_interactive_v1_impls`. redisgraph database runs cypher query, so choose the corresponding folder.

data generator gives nodes and relations between nodes. first randomly make 20 samples in relation csv files, second format the cypher query with samples attributes such as id, etc. then run the cypher in redisgraph and get the cypher results, compare it with the csv samples to check whether it's correct.

in manager.py, different functions are defined specifically for different cyphers, ids in samples were passed into function as param, eventually as cypher's param. unfortunately data generator generate data randomly, which means alot properties are missing, cause alot cyphers dysfunctional. to solve this problem we might update cyphers or data
