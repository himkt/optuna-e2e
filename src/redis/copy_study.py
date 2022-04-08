import optuna


print("redis copy")
optuna.copy_study(from_study_name="test", from_storage="redis://redis:6379", to_study_name="test", to_storage="sqlite:///data/redis_copy.db")


print("done")
