## Set your project's environment
1. Install pyenv and setup. (Optional)
```shell
brew install pyenv
pyenv install 3.10.7
pyenv local 3.10.7
```

2. Install direnv and setup. (Optional)
> Poetry v1.1.2 does not support reading .env file. (v1.2 plugin does)
```shell
brew install direnv
direnv allow
```

3. Install Poetry and setup.
```shell
curl -sSL https://install.python-poetry.org | python3 -
poetry install
poetry shell
poetry env use 3.10
```

## Python Version
> 3.10.7

## [pyenv](https://github.com/pyenv/pyenv) (Optional)
1. Getting Pyenv (how to download please follow Pyenv's README)
2. Set up your shell environment for Pyenv
3. Restart your shell
4. Install a Python version using python-build 
```shell
pyenv install 3.10.7
```
5. Set the local application-specific Python version(s)
```shell
cd /path/Mahjong && pyenv local 3.10.7
```

## [poetry](https://python-poetry.org/docs/)
#### Install Poetry
#### For Mac users
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
#### For Windows users
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## [direnv](https://github.com/direnv/direnv)
#### For Mac users
```shell
brew install direnv
```
#### For Windows users
1. Download installer from [Releases](https://github.com/direnv/direnv/releases)
2. Follow instructions in Issue #343
   - [How to run on windows?](https://github.com/direnv/direnv/issues/343)
3. Installing direnv on Windows 
   - [Steps to install direnv on Windows](https://gist.github.com/rmtuckerphx/4ace28c1605300462340ffa7b7001c6d)
#### Append the following command into the startup script
- For bash (~/.bash_profile or ~/.bashrc)
```shell
eval "$(direnv hook bash)"
```
- For zsh (~/.zshrc)
```shell
eval "$(direnv hook zsh)"
```

## Web Development
* Web Framework: [FastAPI](https://fastapi.tiangolo.com/)
* Web Application Server: [uvicorn](https://www.uvicorn.org/)

```shell
poetry shell
uvicorn main:app — reload
```
or

```shell
poetry run uvicorn main:app — reload
```
