import requests
import json
import csv
import pprint
import time

class BruhException(Exception):
    pass

def check_username_availability(config):
    url = 'https://discord.com/api/v9/users/@me'
    auth = config['authorization']

    def patch_request(username):
        data = {'username':username, 'password':''}
        response = requests.patch(url, headers={'authorization':auth}, json=data)

        return response.json()

    with open('results.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ')

        for username in config['usernames']:
            time.sleep(1.5)
            response_json = patch_request(username)


            #rate limited
            while response_json['message'] == 'You are being rate limited.':
                print(f'rate limited, retry after {response_json["retry_after"]}')
                time.sleep(response_json['retry_after'])
                response_json = patch_request(username)


            try:
                if 'errors' not in response_json:
                    print('\nwtf\n')
                    raise BruhException
                
                if 'username' not in response_json['errors']:
                    print(f'\n{username}\tavailable\n')
                    writer.writerow([username, 'available'])
                    continue
                
                if response_json['errors']['username']['_errors'][0]['code'] == 'USERNAME_ALREADY_TAKEN':
                    print(f'{username}\ttaken')
                    writer.writerow([username, 'taken'])
                    continue

                if response_json['errors']['username']['_errors'][0]['code'] == 'BASE_TYPE_BAD_LENGTH':
                    print(f'{username}\tbad_name')
                    writer.writerow([username, 'bad_name'])
                    continue

            except KeyError as e:
                print(e)
                pprint.pprint(response_json)

            except BruhException:
                pprint.pprint(response_json)




def main():
    with open('config.json', mode='r') as f:
        config = json.load(f)

    check_username_availability(config)

if __name__ == '__main__':
    main()
