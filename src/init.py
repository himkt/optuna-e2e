import optuna
import pymssql

from objective import objective


def create_mssql_database() -> None:
    conn = pymssql.connect("mssql", "sa", "optuna-test-5ZYB")
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE optuna")


create_mssql_database()


print("mysql")
study1 = optuna.create_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna")
study1.optimize(objective, n_trials=10)
print("postgresql")
study2 = optuna.create_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna")
study2.optimize(objective, n_trials=10)
print("sqlite")
study3 = optuna.create_study(study_name="test", storage="sqlite:///data/sample.db")
study3.optimize(objective, n_trials=10)
print("mssql")
study4 = optuna.create_study(study_name="test", storage="mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8")
study4.optimize(objective, n_trials=10)
print("redis")
study5 = optuna.create_study(study_name="test", storage="redis://redis:6379")
study5.optimize(objective, n_trials=10)

print(study1)
print(study2)
print(study3)
print(study4)
print(study5)

print("done")
