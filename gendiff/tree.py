
def diff(dict1, dict2):
    """Создает различия между 2-мя словарями и возвращает список"""
    result = []
    keys = sorted(list(set(dict1.keys()) | set(dict2.keys())))
    for key in keys:
        node = {'name': key}
        if key not in dict1:
            node['key'] = key
            node['status'] = 'added'
            node['data'] = dict2[key]
        elif key not in dict2:
            node['key'] = key
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif dict1[key] == dict2[key]:
            node['key'] = key
            node['status'] = 'not changed'
            node['data'] = dict1[key]
        else:
            node['key'] = key
            node['status'] = 'changed'
            node['data before'] = dict1[key]
            node['data after'] = dict2[key]
        result.append(node)
    return result
