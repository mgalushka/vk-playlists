# -*- coding: utf-8 -*-

import requests
import settings
import sys
import traceback

import vk

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            # print('Searching: {}'.format(sys.argv[1]))
            # search = sys.argv[1].decode('utf-8', 'ignore')
            # print('Searching: {}'.format(search))
            search = u'Ингмар Бергман'
            # session = vk.Session(access_token=settings.ACCESS_TOKEN)
            # api = vk.API(session)
            # r = api.video.search(q=search)

            payload = {
                'access_token': settings.ACCESS_TOKEN,
                'q': search,
                'filters': 'mp4,long',
                'adult': 0,
                'sort': 1,
                'hd': 1,
                'longer': 3600,
                'count': 200,
                'v': 5.62,
            }
            r = requests.get(
                'https://api.vk.com/method/video.search',
                payload,
            )

            print(u'Found videos: {}'.format(r.text))
        else:
            print('Empty search, nothing found.')
    except Exception as e:
        print(str(e))
        traceback.print_stack()
