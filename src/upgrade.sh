#!env bash

echo "mysql"
optuna storage upgrade --storage mysql+pymysql://root:root@mysql:3306/optuna

echo "postgresql"
optuna storage upgrade --storage postgresql+psycopg2://root:root@postgresql/optuna

echo "sqlite"
optuna storage upgrade --storage sqlite:///data/sample.db

echo "mssql"
optuna storage upgrade --storage mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8
