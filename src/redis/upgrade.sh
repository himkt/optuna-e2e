#!env bash

echo "sqlite"
optuna storage upgrade --storage sqlite:///data/redis_copy.db
