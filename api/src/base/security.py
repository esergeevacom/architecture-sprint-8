from fastapi import HTTPException, Security, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from src.base.settings import keycloak_settings

from keycloak import KeycloakOpenID

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=keycloak_settings.url,
    tokenUrl=keycloak_settings.token_url,
)


keycloak_openid = KeycloakOpenID(
    server_url=keycloak_settings.url,
    client_id=keycloak_settings.client_id,
    realm_name=keycloak_settings.realm,
    client_secret_key=keycloak_settings.client_secret,
)


async def get_payload(token: str = Security(oauth2_scheme)) -> dict:
    try:
        return keycloak_openid.decode_token(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
