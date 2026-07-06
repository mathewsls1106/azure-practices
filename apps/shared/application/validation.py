def ensure_exists[T](entity: T, exception: Exception) -> T:
    if entity is None:
        raise exception
    return entity
