# pesenik
Song storage

## Requirements

[pyenv](https://github.com/pyenv/pyenv)

```bash
pyenv install 3.8.2
pyenv virtualenv 3.8.2 pesenik
pyenv local pesenik
pip install -r requirements.txt -r requirements.dev.txt
```

### Add requirement

- add requirement to requirements.in
- run `update_requirements.sh`

### Code-style

Проверка кода:
```bash
prospector
```

Исправления код-стайла:
```bash
black .
isort
```
