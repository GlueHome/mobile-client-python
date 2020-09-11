from mobile_client.auth import AuthClient
from mobile_client.client import MobileClient
import argparse


def main(config: argparse.Namespace):
    token = AuthClient(client_id=config.client_id).get_token(username=config.username, password=config.password)
    print(f'Issued token: {token}')

    client = MobileClient(token)
    notifications = client.get_notifications()

    if len(notifications) == 0:
        print(f'No key approvals pending for {config.username}')
        return

    print(f'Pending notifications found: {notifications}')

    if config.approve:
        client.approve_notification(notifications[0])
        print(f'Notification at {notifications[0].uri} was approved')
    else:
        client.reject_notification(notifications[0])
        print(f'Notification at {notifications[0].uri} was rejected')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, help='Glue account username')
    parser.add_argument('--password', type=str, help='Glue account password')
    parser.add_argument('--client-id', type=str, help='Glue app authentication client id')
    parser.add_argument('--approve', action='store_true', help='Approves the first key request it finds')
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
