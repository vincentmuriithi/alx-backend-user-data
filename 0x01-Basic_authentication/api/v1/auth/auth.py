#!/usr/bin/env python3
"""
This  module contains the auth class
"""
from flask import request
from typing import List, TypeVar


clas Auth:
    """
    Manages the Authentication API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path is authorized or not
        """

        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[:-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header for a request object
        """
        if request is None:
            return None
        header = request.headers.get("Authorization")
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Returns a user instance form information from the request header
        """
        return None
