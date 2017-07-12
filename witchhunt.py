#!/usr/bin/env python3

import argparse
import arrow
import pprint
import sys

import requests

DEFAULT_IP   = '192.168.1.103'
DEFAULT_PORT = '8989'
API_KEY = '61c800aa908648bf8ca4c2c45063344d'

def parse_args(args=None):
    parser = argparse.ArgumentParser('Sonarr WitchHunt')

def query(endpoint):
    print('Querying:', endpoint)
    return requests.get('http://{ip}:{port}/api/{endpoint}?apikey={api_key}'
            .format(ip=DEFAULT_IP, port=DEFAULT_PORT, endpoint=endpoint, api_key=API_KEY))

def find_show(title, shows):
    return next(show for show in shows if show['title'] == title)

if __name__ == '__main__':
    shows = query('series').json()
    pprint.pprint(sorted([show['title'] for show in shows]))
    nyws = find_show('The New Yankee Workshop', shows)
    pprint.pprint(nyws, depth=1)

    print(type(nyws['added']))
    print(arrow.get(nyws['added']).datetime)
    command = ['ffmpeg', '-v', 'error', '-sseof', '-%d' % SEEK_END_SEC, '-i', filename, '-f', 'null', '/tmp/test.log']
    subprocess.check_output(command, stderr=subprocess.STDOUT)
