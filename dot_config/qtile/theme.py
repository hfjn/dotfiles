import json
from os import path

from path import qtile_path


def load_theme():
    theme = "nord"

    theme_file = qtile_path / "themes" / f"{theme}.json"
    if not theme_file.is_file():
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


colors = load_theme()
