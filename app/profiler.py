import cProfile


def profiler( func):
    def wrapper (*args, **kwargs):
        profile_filename = f"profiles/{func.__name__}.prof"
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper