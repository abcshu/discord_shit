prepare some json files in the form of SOME_USERNAME_FILE.json with your targeted usernames list in the file.

create a "config.json" in the form of config_template.json

put ur authorization (something that looks like XXXXXXXXXXXXXXXXXXXXXXXX.XX-XXX.XXXXXXXXXXXXXXX_XXX-XXXXXXXXXXXXXXXXXX) 
and ur list of paths (absolute or relative to unique_username_checker_vXX.py) to username files in config.json

after going through all the usernames of a file, the program will insert ##THIS FILE HAS BEEN CHECKED## as the first element of said file. (saved progress) 

create "results" folder for the program to store results



to find ur authorization, 

log into discord from browser; 
open up DevTools and choose "Network"; 
type some shit in any input field in discord to have requests sending;
check the header of ur request and you should be able to locate ur authorization.

![find auth](./where_is_auth.png?raw=true "auth")


note: haven't implemented checkng if names follows discord's naming rule, so there are false positives (you should be able to spot those easily).
