VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"
ADMIN_TOKEN = "Se7KyydjP7V7rqCq67b4DbNIDMR2F5jubRI9KtQE4orP5zdpmuWgCWXYFOMovZSA"
DEFAULT_USER_TOKEN = "MIIFLTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQI/aYRRU9ba"


def is_admin(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return ADMIN_TOKEN
    else:
        return DEFAULT_USER_TOKEN
