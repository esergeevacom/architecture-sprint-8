from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    log_level: Optional[str] = "NOTSET"

    project_name: str = Field(..., description="Заголовок проекта")
    port: str = Field("8000")

    environment: str
    frontend_app_api_url: str


class KeyCloakSettings(BaseSettings):
    url: str
    client_id: str
    client_secret: str
    realm: str

    @property
    def token_url(self):
        return f"{self.url}/auth/realms/{self.realm}/protocol/openid-connect/token"

    model_config = SettingsConfigDict(env_prefix="KEYCLOAK_")


settings = Settings()
keycloak_settings = KeyCloakSettings()
