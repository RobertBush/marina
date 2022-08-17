## Instructions to run
    docker compose up --build

then visit
    http://localhost:8000
for a swagger-ui experience to explore the API.


### Note for Apple M1 Chip Users
If you are on a M-1 Apple Mac, you will need to issue the following command:

    export DOCKER_DEFAULT_PLATFORM=linux/amd64

to force the m1 chip to run things through rosetta. This is a bug in libpq. You will need to have this env var exported before building your containers. 