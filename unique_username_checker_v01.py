import requests
import json
import csv
import pprint
import time

#this is not supposed to be raised
class BruhException(Exception):
    pass

#Given username and auth to check the status of the username
def check_username_availability(username, auth):
    url = 'https://discord.com/api/v9/users/@me'

    def patch_request(username):
        data = {'username':username, 'password':''}
        response = requests.patch(url, headers={'authorization':auth}, json=data)
        return response.json()

    response_json = patch_request(username)
    #rate limited
    while response_json['message'] == 'You are being rate limited.':
        #print(f'rate limited, retry after {response_json["retry_after"]}')
        time.sleep(response_json['retry_after'])
        response_json = patch_request(username)

    try:
        #this wouldn't normally happen
        if 'errors' not in response_json:
            print('\nwtf\n')
            raise BruhException
        
        if 'username' not in response_json['errors']:
            return 'available'
        
        if response_json['errors']['username']['_errors'][0]['code'] == 'USERNAME_ALREADY_TAKEN':
            return 'taken'

        if response_json['errors']['username']['_errors'][0]['code'] == 'BASE_TYPE_BAD_LENGTH':
            return 'bad_name'

    except KeyError as e:
        print(e)
        pprint.pprint(response_json)

    except BruhException:
        pprint.pprint(response_json)




#Handles going through username files and storing the results
def going_through_name_files(config):
    auth = config['authorization']

    #get paths to username files
    for username_file in config['paths_to_username_files']:

        #open username_file
        with open(username_file, mode='r') as username_json_file:
            usernames = json.load(username_json_file)
        
            #guard statement for whether checked already
            if usernames[0] == "##THIS FILE HAS BEEN CHECKED##":
                print(f'{username_file} has been checked')
                continue

            #open result file
            with open(f'./results/{username_file.split("/")[-1].split(".json")[0]}.csv', mode='w', newline='') as results_csv_file:
                writer = csv.writer(results_csv_file, delimiter=' ')

                #going through usernames in this username file
                available_count = 0
                for index, username in enumerate(usernames):
                    name_status = check_username_availability(username, auth)
                    print(f'{username:<10.10} {name_status:<10.10} ({index+1}/{len(usernames)} of {username_file}) \t\t\t\t', end='\n'if name_status == 'available' else '\r')

                    time.sleep(1.5)
                    available_count += 1 if name_status == 'available' else 0
                    writer.writerow((username, name_status))


        print(f'\n{username_file} has been checked!! {available_count} available ones\n')
        #Mark as checked 
        with open(username_file, mode='w') as username_json_file:
            usernames.insert(0, "##THIS FILE HAS BEEN CHECKED##")
            json.dump(usernames, username_json_file, indent=4)







def main():
    with open('config.json', mode='r') as f:
        config = json.load(f)

    going_through_name_files(config)

if __name__ == '__main__':
    main()
