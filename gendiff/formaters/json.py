import json as json_global


def render_json(diff) -> str:
    """Возвращает формат Json."""
    return json_global.dumps(diff)
