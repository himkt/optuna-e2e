import optuna


print("redis delete")
optuna.delete_study(study_name="test", storage="redis://redis:6379")


print("sqlite copy to redis")
optuna.copy_study(from_study_name="test", from_storage="sqlite:///data/redis_copy.db", to_study_name="test", to_storage="redis://redis:6379")


print("done")
