# Brownie simple storage

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Deploy

### Ganache

```bash
brownie run scripts/deploy.py
```

### Rinkeby

```bash
brownie run scripts/deploy.py --network rinkeby
```

## Test

```bash
brownie test
```
