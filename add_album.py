import requests
import settings
import sys
import traceback

import vk

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            # session = vk.Session(access_token=settings.ACCESS_TOKEN)
            # api = vk.API(session)
            # https: // api.vk.com / method / audio.search?q =
            search = sys.argv[1]
            # api.audio.addAlbum(title=album_name)

            session = vk.Session(access_token=settings.ACCESS_TOKEN)
            api = vk.API(session)
            api.video.search(q=album_name)

            payload = {
                'access_token': settings.ACCESS_TOKEN,
                'title': album_name,
                # 'privacy': 'nobody',
                'v': 5.62,
            }
            r = requests.get(
                'https://api.vk.com/method/audio.addAlbum',
                payload,
            )
            print(r.text)
            print('Added album: {}'.format(album_name))
        else:
            print('Empty album, nothing added.')
    except Exception as e:
        print(str(e))
        traceback.print_stack()
