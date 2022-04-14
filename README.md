### Setup database

```sh
docker compose up --build
```

### Clean

```sh
docker compose down
```

### Run optimization with Optuna v2.10.0

```sh
docker compose run --rm optuna-210 bash
```

### Run optimization with Optuna v3.0.0

```sh
docker compose run --rm optuna-300 bash
```

---

### Migration

```sh
# Create study
docker compose run --rm optuna-210 python src/init.py

# Run migration on RDB
docker compose run --rm optuna-300 bash src/upgrade.sh

# Run migration on Redis
docker compose run --rm optuna-210 python src/redis/copy_study.py
docker compose run --rm optuna-300 bash src/redis/upgrade.sh
docker compose run --rm optuna-300 python src/redis/copy_back_study.py

# Resume study
docker compose run --rm optuna-300 python src/load.py
```
