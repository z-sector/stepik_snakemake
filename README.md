### Download project
```bash
https://github.com/z-sector/stepik_snakemake.git
```

### Create virtual environment
Install pipenv
```bash
pip install pipenv
```
Go to the directory with the project and create a virtual environment specifying the version of the interpreter
```bash
pipenv --python 3.7
```
Activate the virtual environment of the project
```bash
pipenv shell
```
Exit the virtual environment shell
```bash
exit
```
Install packages
```bash
sudo apt install python3-dev
pipenv install 'snakemake<=3.13.3'
```

### Start pipeline
```bash
snakemake
```
Force the execution of the selected target or the first rule regardless of already created output
```bash
snakemake -f
```
Force the execution of the selected (or the first) rule and all rules it is dependent on regardless of already created output
```bash
snakemake -F
```
The workflow definition in a snakefile
```bash
snakemake -s ExampleSnakefile
```

### Start bio pipeline
Start docker
```bash
docker run -it --rm -v $(pwd)/BSnakefile:/mnt/Snakefile --entrypoint snakemake test
```
Or
```bash
docker run -it --rm -v $(pwd)/Snakefile:/mnt/Snakefile test
# in the container, execute the commands
snakemake
```