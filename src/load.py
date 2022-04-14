import optuna

from objective import objective


print("mysql")
study1 = optuna.load_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna")
study1.optimize(objective, n_trials=10)
print("postgresql")
study2 = optuna.load_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna")
study2.optimize(objective, n_trials=10)
print("sqlite")
study3 = optuna.load_study(study_name="test", storage="sqlite:///data/sample.db")
study3.optimize(objective, n_trials=10)
print("mssql")
study4 = optuna.load_study(study_name="test", storage="mssql+pymssql://sa:optuna-test-5ZYB@mssql/optuna?charset=utf8")
study4.optimize(objective, n_trials=10)
print("redis")
study5 = optuna.load_study(study_name="test", storage="redis://redis:6379")
study5.optimize(objective, n_trials=10)

print(study1)
print(study2)
print(study3)
print(study4)
print(study5)

print("done")
