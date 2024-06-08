#!/usr/bin/env python3
"""
This  module contains the auth class
"""

from flask import  requets
from typing import List, TypeVar


clas Auth:
    """
    Manages the Authentication API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False


    def authorization_header(self, request=None) -> str:
        return None


    def current_user(self, request=None) -> TypeVar("User"):
        return None
