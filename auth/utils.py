def validate_scopes(user_scopes: list[str], required_scopes: list[str]):
    if not all(scope in user_scopes for scope in required_scopes):
        raise PermissionError("You do not have the necessary permissions.")
