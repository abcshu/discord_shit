create a config.json in the form of config_template.json

put ur authorization (something that looks like XXXXXXXXXXXXXXXXXXXXXXXX.XX-XXX.XXXXXXXXXXXXXXX_XXX-XXXXXXXXXXXXXXXXXX) and ur list of username in config.json

to find ur authorization, 

log into discord from browser; 
open up DevTools and choose "Network"; 
type some shit in any input field in discord to have requests sending;
check the header of ur request and you should be able to locate ur authorization.

![find auth](./where_is_auth.png?raw=true "auth")
