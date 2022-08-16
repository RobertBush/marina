If you are on a M-1 Apple Mac, you will need to issue the following command:

    export DOCKER_DEFAULT_PLATFORM=linux/amd64

to force the m1 chip to run things through rosetta. This is a bug in libpq.