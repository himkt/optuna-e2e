import optuna

from objective import objective


study1 = optuna.create_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna")
study1.optimize(objective, n_trials=10)
study2 = optuna.create_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna")
study2.optimize(objective, n_trials=10)
study3 = optuna.create_study(study_name="test", storage="sqlite:///data/sample.db")
study3.optimize(objective, n_trials=10)


print(study1)
print(study2)
print(study3)

print("done")