from flask import Response
import json
from pathlib import Path


def get_project_root() -> Path:
        return Path(__file__).parent.parent


def make_error_message(message, status):
        json_message = {}
        json_message["error"] = message

        return Response(json.dumps(json_message), status=status)
        