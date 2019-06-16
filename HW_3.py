from functools import lru_cache
import random
import string
import time


def read_input_pairs(filename):
    input_file = open(filename, "r")
    pairs = input_file.readlines()
    for each_pair in pairs:
        pairs_array = each_pair.split(",")
        if len(pairs_array) == 2:
            get_image_url_stub(float(pairs_array[0]), float(pairs_array[1]))


@lru_cache(maxsize=3000)
def get_image_url_stub(lat, long):
    key = key_from_lat_long(lat, long)
    random_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
    # print('Adding random number for url')
    fake_url = 'http://some_domain.com/' + str(key) + '-' + random_string
    # time.sleep(1)
    return{key: fake_url}


def key_from_lat_long(lat, long):
    if (-90.00 <= lat <= 90.00) and (-180.00 <= long <= 180.00):
        # print("Creating key from lat/long)")
        # time.sleep(1)
        return f'{"%.2f" % lat},{"%.2f" % long}'


read_input_pairs("coordinates.txt")
print(get_image_url_stub.cache_info())