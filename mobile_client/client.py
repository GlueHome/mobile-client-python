from mobile_client.rest import RestClient
from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from bs4 import BeautifulSoup
from urllib.parse import urljoin


MOBILE_API_URL = 'https://mobile.gluehome.net'


@dataclass_json
@dataclass
class Notification:
    uri: str


class MobileNotificationClient(RestClient):
    def __init__(self):
        super().__init__(base_url=MOBILE_API_URL)

    def complete_notification(self, notification_url: str, approve: bool = True, lock_id: str = None) -> None:
        """
        Completes the Key Approval Notification either by approving or rejecting.
        If lock_id is specified, then it picks that from the list, else it selects the first.
        """
        soup = BeautifulSoup(self.get(notification_url), 'html.parser')
        form = soup.find(id='access-approved-callback-form' if approve else 'access-rejected-callback-form')
        path = form.attrs['action']
        body = {}
        if approve and 'key' in path:
            opts = soup.find(id='inlineFormCustomSelect').find_all('option')
            vals = map(lambda o: o.attrs['value'], opts)
            if lock_id is None:
                body['lockId'] = next(vals, None)
            else:
                if lock_id not in list(vals):
                    raise Exception('Lock ID {} not found in request'.format(lock_id))
                body['lockId'] = lock_id
        self.post(urljoin(notification_url, path), body)


class MobileClient(RestClient):
    def __init__(self, token):
        super().__init__(base_url=MOBILE_API_URL, auth=f'Bearer {token}')
        self.notification_client = MobileNotificationClient()

    def get_notifications(self) -> List[Notification]:
        return Notification.schema().loads(self.get('api/v1/notifications'), many=True)

    def approve_notification(self, notification: Notification, selected_lock_id: str = None) -> None:
        self.notification_client.complete_notification(notification.uri, True, selected_lock_id)

    def reject_notification(self, notification: Notification) -> None:
        self.notification_client.complete_notification(notification.uri, False)
