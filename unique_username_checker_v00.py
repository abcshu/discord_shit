import requests
import json
#import pprint

def check_username_avability(config):
    url = 'https://discord.com/api/v9/users/@me'
    auth = config['authorization']

    def patch_request(username):
        data = {'username':username, 'password':''}
        response = requests.patch(url, headers={'authorization':auth}, json=data)

        return response.json()

    for username in config['usernames']:
        response_json = patch_request(username)
        #pprint.pprint(response_json)
        try:
            if response_json['errors']['username']['_errors'][0]['code'] == 'USERNAME_ALREADY_TAKEN':
                print(f'{username} \ttaken')
        except KeyError:
            print(f'{username} \tavailible')



def main():
    with open('config.json', mode='r') as f:
        config = json.load(f)

    check_username_avability(config)

if __name__ == '__main__':
    main()
