
def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    module_name = getattr(obj, '__module__', '__main__')
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }
    return info


number_info = introspection_info(42)
print(number_info)
