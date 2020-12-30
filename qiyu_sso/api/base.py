from typing import Optional

from oauthlib.oauth2.rfc6749.clients import WebApplicationClient

from forms.client_base import ClientBaseForm
from forms.login import LoginArgs

__all__ = ["BaseAPI"]


class BaseAPI(object):
    """
    基础 API 定义
    """

    def __init__(self, uri: str, client_id: str, client_secret: str):
        """
        :param uri: OAuth 服务的接口
        :param client_id:     应用 ID (允许对外公开)
        :param client_secret: 应用机密 (必须保密)
        """
        self._uri = uri
        self._client_id = client_id
        self._client_secret = client_secret

    def get_login_url(self, args: LoginArgs) -> str:
        """
        获取登录的地址

        :param args:
        :return:
        """
        client = self._get_oauth_client(args)
        return client.prepare_request_uri(
            uri=args.server_uri,
            scope=args.scope,
            state=args.state,
            redirect_uri=args.redirect_uri,
        )

    @staticmethod
    def _get_oauth_client(
        form: ClientBaseForm, code: Optional[str] = None
    ) -> WebApplicationClient:
        return WebApplicationClient(
            client_id=form.client_id, code=code, client_secret=form.client_secret
        )
