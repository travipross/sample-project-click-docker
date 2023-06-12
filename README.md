# sample-project-click-docker
Sample containerized CLI Python project structure.


## Installation

### Python / Native
Install locally via:

```
pip install .
```

Run via:
```
sample-project --help
sample-project cmd1 --help
sample-project cmd2 --help
sample-project cmd3 --help
```

### Docker
Build docker container via:
```
scripts/build_docker.sh
```

After building, run via:
```
docker run --rm --name sample-project-container --help
```

Note that the `--help` argument is passed directly to the python program. This is because the Dockerfile specifies `hfss-tools` as the Docker "entrypoint", which precedes any Docker "command" issued with a `docker run` statement (in the form of `docker run <container> <command>`).
