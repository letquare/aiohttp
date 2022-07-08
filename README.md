# Base deployment project

### The first thing to do is run docker and build the project.

#### Command to build a container

```dockerfile
    docker-compose up -d --build
```

After the container is built, it will be possible to check the operation of the API

Check on: http://0.0.0.0:8080/hello/


### Now Databases!

Apply migrations at folder: migrations/versions
Run command:
```dockerfile
    sudo docker exec {name_container_web} alembic upgrade head
```
If all good, you to see answer:

"INFO [alembic.runtime.migration] Running upgrade ae34635ed36d -> c190b70379d2, create table ..."


if the folder was empty or you changed the database structure,
then you should create migrations*
```dockerfile
    sudo docker exec {name_container_web} alembic revision -m 'Name of the migration' --autogenerate

```

At the moment we have a database but it is empty.
It must be filled in according to the database structure.

First you need to transfer the csv file and info to the docker container.

```dockerfile
    docker cp {name_file.csv} {name_container_db}:/home
```
if the copy was successful, you will not see any message.

Now let's go to the database:
```
    sudo docker exec -it postgres psql -U root
```
```postgres-sql
    \c postgres
```
"You are now connected to database "postgres" as user "root"

```postgres-sql
    COPY name_table FROM '/home/{name_file.csv}' WITH (FORMAT csv);
```

### Now our API ready for work!

## Manipulation with API


1. First you need to get a login and password

* Send a 'get' request to: http://0.0.0.0:8080/get_login/

return:
```
    {
    "user": {
        "login": "your_login",
        "password": "your_password"
    }
}
```


2. Then we get JWT

* Send a 'post' request to: http://0.0.0.0:8080/get_token/

request
```
    {
    "login": "your_login",
    "password": "your_login"
}
```

return:
```
    "access_token": "your_token"
```

3. Getting data from the database and using a token

* We send a 'get' request to http://0.0.0.0:8080/get_data/ 

And add in headers:
   * Authorization : Bearer {your_token}