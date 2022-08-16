import subprocess
from invoke import task


@task
def bounce(ctx):
    print("bouncing")
    ctx.run("docker compose down -t 0")
    ctx.run("docker compose up --build")
    print("bounced")
