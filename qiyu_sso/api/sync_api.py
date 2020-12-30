from .base import BaseAPI

__all__ = ["QiYuSSOSync"]


class QiYuSSOSync(BaseAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
