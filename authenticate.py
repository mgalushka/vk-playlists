import requests
import settings


if __name__ == '__main__':
    payload = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'redirect_uri': settings.REDIRECT_URL,
        'code': settings.CODE,
    }
    r = requests.post(
        'https://oauth.vk.com/access_token',
        payload,
    )
    print(r.text)
