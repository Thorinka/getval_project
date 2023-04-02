def get_val(collection, key, default='git'):
    try:
        collection[key]
    except:
        return default
    return collection[key]

