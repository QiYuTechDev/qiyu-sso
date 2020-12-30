from pydantic import Field

from .client_base import ClientBaseForm

__all__ = ["LoginArgs"]


class LoginArgs(ClientBaseForm):
    redirect_uri: str = Field(..., title="跳转 URI")
    state: str = Field(..., title="状态", description="请保持唯一性,可以随机生成")
    scope: str = Field(..., title="权限范围", description="申请的权限范围")
