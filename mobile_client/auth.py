from warrant import Cognito


class AuthClient(object):
    def __init__(self, client_id, region: str = 'eu-west-1', pool_id: str = 'U1dJh7Gx5'):
        self.client_id = client_id
        self.region = region
        self.user_pool = f'{region}_{pool_id}'

    def get_token(self, username: str, password: str) -> str:
        u = Cognito(self.user_pool, self.client_id, self.region, username=username)
        u.authenticate(password=password)
        return u.access_token
