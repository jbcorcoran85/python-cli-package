"""This module provides the RP To-Do model-controller."""
# rptodo/rptodo.py

from typing import Any, Dict, NamedTuple
from pathlib import Path
from rptodo.database import DatabaseHandler

class Todoer:
    """Doc String Requirement for class Todoer"""
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

class CurrentTodo(NamedTuple):
    """Doc String Requirement for class"""
    todo: Dict[str, Any]
    error: int