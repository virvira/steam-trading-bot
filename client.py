from steampy.client import SteamClient
import os

from steampy.exceptions import InvalidCredentials
from steampy.models import GameOptions

steamguard_path = os.path.join('Steamguard.json')

login = 'awesomezfarm8'
password = 'X2_qCa5X'
api_key = 'F9415F975FC5CF5320FAE95F404D65CF'

steam_client = SteamClient(api_key)

try:
    steam_client.login(login, password, steamguard_path)
except (ValueError, InvalidCredentials):
    print('Your login credentials are invalid!')
    exit(1)
else:
    print('Finished! Logged in into Steam')


game = GameOptions.DOTA2
summaries = steam_client.get_my_inventory(game)

# params = {'key': api_key, 'appid': 570, 'steamid': 76561199487356486}
# summaries = steam_client.api_call('GET', 'IEconService', 'GetTradeOffersSummary', 'v1', params).json()

print(summaries)
