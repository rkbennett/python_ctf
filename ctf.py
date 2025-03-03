import io
import os
import sys
import json
import base64
import logging
import argparse
import subprocess
import urllib.request
from troubleshooting import get_network_stuff, get_file_stuff
from copy import deepcopy
from inspect import stack
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def _flg_dcrpt(flg):
    dcrpt_k = b"bdaa48cf-edba-4dbe-9aa3-dbcf6d17"
    iv = b'd\x12\x1f\x9b\xd6=\xa4H_^ih\xda\x9cO\xbe'
    cipher = Cipher(algorithms.AES(dcrpt_k), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(flg) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

class ctf_logging_formatter(logging.Formatter):
    grey = "\x1b[38;20m"
    cyan = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    log_format = "%(levelname)s:%(message)s"

    logger_formats = {
        logging.DEBUG: grey + log_format + reset,
        logging.INFO: cyan + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset
    }

    def format(self, record):
        log_fmt = self.logger_formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(ctf_logging_formatter())
logging.getLogger().addHandler(log_handler)

logging.warning(_flg_dcrpt(b'&<\x8fX?z{\xb3\x81T54nFlO\xd0f\xa9\x82c\xf5\xc0T\xbe\xa7\\~\x82\xde\xf3\xe9'))

ctf_dict = {"foo": "bar", "baz": "bin", "lorum": "ipsum"}
ctf_array = [i for i in sys.modules.keys()]
dir_arr = ["UnicodeError", "types", "bool", "locale", "quit", "ipsum", "call", "sleep", "locals", "PIPE"]

def show_me_some_attrs(os_dict):
    if os_dict == dir(os):
        logging.warn(_flg_dcrpt(b'\x84\x87\xba;t4\xad#\xbdg\xb0\xb56\xce?/\xfb\x8d\r\xe9\xf9\x18\x97\xcaj\x83\x07\x02\xfd\x90\xad\x08'))

def too_many_lines(multiline_str):
    if "\n" in multiline_str:
        logging.warn(_flg_dcrpt(b"\xc4\x90\x9c\x9d\x90\xb8\xab\x18\xf0\xe8\xeb\xe1\xcb\x0fC\x95\x9eW\x19\xf6H\x8e'\xc3\xde\xeaZ\xfdHb\xb9M"))

def its_functional(funct):
    if type(funct) == type(too_many_lines):
        if funct("foo") == b"foo":
            logging.warning(_flg_dcrpt(b'\xc01L\xbc\xf0\x0ch\xdb\x8d\xee\x88\xdaP?\xe2\x15W\x88q8\xc6WDM(\xc5\xba\xeb\xbfsVw'))

def you_are_being_a_dict(val):
    if isinstance(val, dict):
        logging.warning(_flg_dcrpt(b'$\xe6\x8dY\xc9\xfdUd\xc6\x97b+\xbcv\xe41o]\x1f(\xbb^\x0f\xe3\x0f\x97\x05{\xa3\xc2:\x92'))

def get_set(val):
    if isinstance(val, set):
        logging.warning(_flg_dcrpt(b"\xf4#\xbb\xf8'Xbo\xbc\xfda\xeb\x80o\xdd\xfe\xa6*\x7f#\x86uE\xcf\xa5\xe2E8\xb0\xefz\xea"))

def just_a_tuple(val):
    if isinstance(val, tuple):
        logging.warning(_flg_dcrpt(b"\xdc\x92?\x121\x86\xbe\x1c7\xe8\x84(\xa2\xd6'\xfd\x88\xfc\xb2\xb93\xbfJ$\xee\rE\xfb/\xac\xce\xa4"))

def stringing_me_along(val):
    if isinstance(val, str):
        logging.warning(_flg_dcrpt(b'\xc3\x15\xa6{\x01(\x18\xca8"\x05\x0cQ7Sx\xa8\xec\xdd8\xb5\xf9\xe3,|4\xbd\xdc\xb2\xcc\xe7\xe8'))

def bark_worse_than_its_byte(val):
    if isinstance(val, bytes):
        logging.warning(_flg_dcrpt(b'\x18!,\x01n-E\x06J\xf6\x8b\x0b\xd3<\xd7[\xad2\xd6)>\x05\xca+\x12\xdbWnE$\x1d\xa3\xe2h\xdd)\xef\xa0\x91\xff\xefQ\xc4 \x8a{\xbd\x9a'))

def making_a_list(val):
    if isinstance(val, list):
        logging.warning(_flg_dcrpt(b'\xc6"\x1bf\xd7\x12\xba*\x04Y3H\xc14;I\x95\x8adu\xfcHl\x80\n"\n\xe2\xb9uQ\xf7'))

def whatever_floats_your_boat(flt):
    if isinstance(flt, float):
        logging.warning(_flg_dcrpt(b'\xf7:\xd6\xc3g\xdb\xfc.\xa6\xce[\xa1A\xf0:\xdb\xcb\\\xe9b\xc7\x9e\xa8\x86\x030\x92\xb4\x04\xdc@%'))

def ctf_test():
    if 'ctf_test' in globals() and globals()['ctf_test'].__module__ == "ctf":
        logging.warning(_flg_dcrpt(b'\xe8\xeb~\x87\xf3\xcd\x99\x8d\rI\x10\x7fJ\xebj\xbd\xa5\xdf\x9f\xb5(?^#9Xk<\xc2Kf\x19'))

class ctf_class(object):
    def __init__(self):
        logging.warning(_flg_dcrpt(b'w\x12&\x9aMv\x90\xe5=\xca\xef5nE\x9e\xd7\xbb!;\xf8\xdez \xef\x8f\x8bK>\x12\xb6\x0f!\x9d\x8e\x88\xafD\xa4\xa2\x93\xd4\x92\xb5\x8e\x07\xe6\xb9\x07'))
    
    def call_me(self):
        if stack()[1].function == "call_me_function":
            logging.warning(_flg_dcrpt(b"\xc1\x06'\x9c\xb5\xed}\xa5\x1e=\x98uB\x18\r\xef<0T\xa1Qe\x88\x04\xa2\xa5Lm\xb7MN\r"))

def out_of_context(funct):
    if type(funct) == type(too_many_lines) and funct("foobarbazbinlorumipsumdolor") == "arba":
        logging.warn(_flg_dcrpt(b"\x9d\x8b\xd4'\x13\x07\xab\xc8\x0c\xe8q\x03\x11\x95(\xe7\x80\x9b\xd0\xc1&\xda\x14\x9a\x98\\\xf7\x00g\xdb\xad\x0b"))

def say_again(cls):
    if type(cls) != type(ctf_class):
        return
    c = cls()
    if 'repeat' in dir(c) and 'append' in dir(c):
        pass
    else:
        return
    if c.repeat("foo", 4) == "foofoofoofoo" and c.append("foo","bar") == "foobar":
        logging.warn(_flg_dcrpt(b"\xfcz\x89\x82j)`n\xe6P\x89/\xdfGG\xc8z\x92]vz\xb2h\xbb\xfb\x07\x87;\xb0x\x03xn\x93\xf5\x15d{u\xc6'z\xc0\x19\xeb\xb1\xab\xd6"))

def wide_range(rng):
    if isinstance(rng, range) and rng.start == 0 and rng.stop == 10:
        logging.warn(_flg_dcrpt(b'V\t[_;.c\xfc\x08n\xf1e\x14\x11U\xbd\x17\xd8\xa6\xa1~\x00\xee\xf0i\xe4\xed\x9a\x1a\xd6\xf4\xbcq\x1e\xcb\n\x80\xd2?\xbe\xc2,\xde\xe6\x96pP\x16'))

def loopy(arr):
    if arr == [f"for {i}" for i in ctf_array]:
        logging.warn(_flg_dcrpt(b'\xfd1\xb6^\xee\xef\xb90&\x9c\x07\xd5M\xef\x04\x17\xe0\xbbv\xf4\xffN\xcdD.?\xf1K\xf0^\xfb\xa5'))

def contextual(arr):
    if arr == ctf_array[3:]:
        logging.warn(_flg_dcrpt(b'X\xb3\xb3\x98a\x08t\x05\x03!FU:\x01\xc6\x1c\x8f\x03\xda2\x14*\xfa\xc7\xed\x13$]\xc8\xfad\xc5'))

def additionally(arr):
    tmp_array = ctf_array + dir(subprocess)
    if arr == tmp_array:
        logging.warning(_flg_dcrpt(b'\xce\xbdL\x01\x02Z\x06\xb2\xc1R\x88\x8b\x85\xed\x84\xcb\xe1R\x15\x03\x9b\xa2\xf1tZ\xf0d\x0cA\xb0\xf1W'))

def you_in_or_out(arr):
    if arr == [(i in dir(subprocess)) for i in dir_arr]:
        logging.warning(_flg_dcrpt(b'0\xad\xf1\x87\x0e\x85\xf5\xd4\x85\x1cUa\xcf\x8cM\xd1'))

def get_me_sorted_out(arr):
    tmparr = deepcopy(ctf_array)
    tmparr.sort()
    if arr == tmparr:
        logging.warning(_flg_dcrpt(b'\xf8\xb9\x06\xf3\x83IIq<\xda\x8f\x1d\x806,/\xbd\xccK@q\x19\xa3R\x9a\x1a;\xf4P\xa3\x13\x06'))

def join_us(str_arr):
    if str_arr == ', '.join(ctf_array):
        logging.warning(_flg_dcrpt(b"Gq\xe96\xfd\xf5\x04\xe6\x01\xca\x1e\x14M\xc0SW\x9a\x1a\xae\xe0'i\xb4Q}\x8d\x08\x0c\xee\x9ed!\xfa\x19\xbf\xa3\xb4\xbeA\xb0^\xd5{`\x03\x90\xa5!"))

def adding_a_member(d):
    if isinstance(d, dict) and "fleeb" in d and d.pop("fleeb") == "plumbus" and d == ctf_dict:
        logging.warning(_flg_dcrpt(b"\xa7\xb6\xb7%n'\x96\xca.\x81\xfc\xf9=^h\xaca\x90\xbc\xb4Ks\xb4\xcf\x86\x19\xc3\x15\xed\xfd\x95^"))

def the_whole_package(pkg):
    if pkg.__path__ == "fleeb":
        logging.warning(_flg_dcrpt(b'\xcb\xf5\x8b\xec\x11\xc1\x9d\x9e\xa9H\xe9Uk\xd5j\xbe\xe3\xfd)\x04\xc2L\xf8\xc83\x12\xb9pZ\x8eJ\xde'))

def stay_classy(cls):
    if type(cls) != type(ctf_class):
        return
    c = cls()
    if 'addition' in dir(c) and 'subtraction' in dir(c) and 'division' in dir(c) and 'multiplication' in dir(c):
        pass
    else:
        return
    if c.addition(3,3) == 6 and c.subtraction(5, 3) == 2 and c.division(25, 5) == 5 and c.multiplication(10, 186) == 1860:
        logging.warn(_flg_dcrpt(b'\x9f\x0f\xf7\x16<\x92\\<\xe9\xb7\xa0a\xc8o\x14\x0b5h\xbfE\x1fm\x9c\xcf7t.\xab\xb4\x19\xd9\x97'))

def super_secret_string(enc_str):
    if enc_str == base64.b64encode(dir_arr[0].encode()):
        logging.warn(_flg_dcrpt(b'[U\x96\x94\xf3y\x97\xba\x9b(\x1c\x01\xce\xf1\xa7\xdf\xf6I\xa4\\\x9e9\x96\x102\xfa1=\x99\x99\xc5\x92'))

def hyperminimalist(dict_str):
    if dict_str == json.dumps(ctf_dict):
        logging.warning(_flg_dcrpt(b'=i\x84\x06\xf8\x8b\xd4FR\xf2O\n\xe5\xc2\xc6\xcaTO\x96iT\\B\xcf\x08\xbct\xf8^\x85O-\x0b\xea\xca\xf1o\x13n\xda\x1dWC\x14\xc9L"\x1d'))

def what_is_the_internet(resp):
    r = urllib.request.urlopen("http://www.msftncsi.com/ncsi.txt").read()
    if r == resp or resp == r.decode():
        logging.warning(_flg_dcrpt(b'K\x0bt\xe7\xbb\xcdn\xa6\xb1Wg\x9b,\xd6\xba\xa8\xc4\x9b\xb3,5\x14\x86\xf6\x17\xc8\x0f\xdb\xb4\xde\x83:'))

def did_you_try_asking(request):
    flag = _flg_dcrpt(b'C\xf9<\x0f\xe8\x1fw\xd2\x81j8\x93\xd1R\x00Y&\x04\x10\x8f\x1f(7\xd5\xdecC\xba\xfe\x1e]/\x90}\x9c;\x19\x8b\x1e$\x88\x9d\x88\xdd\xbc\x1b-p')

    output = io.StringIO()
    sys.stdout = output

    try:
        exec(request)
    except Exception as e:
        sys.stdout = sys.__stdout__
        logging.warn(e)
    finally:
        sys.stdout = sys.__stdout__

    captured_output = output.getvalue()
    output.close()
    
    logging.warning(f"Is this what you asked for? {captured_output}")

def so_argumentative():
    parser = argparse.ArgumentParser(description='With the right arg you may get a flag (rendered by argparse)')
    parser.add_argument('-f', '--flag', action='store_true', help='Prints the flag')
    if len(sys.argv) < 2:
        parser.print_help()
    args = parser.parse_args()
    if args.flag:
        logging.warning(_flg_dcrpt(b'\xfaeD\x82\r\x9e\x1d\xf4\x90\xf7/\x1f\xfe|\xf7\x0b\x15\xca\xb1\xf7A\xeb\xa0\xef\xb8\x00\x12\x07:\\\x8c\x11'))

def network_error():
    ns_stuff = get_network_stuff("http://www.msftncsi.com/ncsi.txt")
    if ns_stuff == urllib.request.urlopen("http://www.msftncsi.com/ncsi.txt").read():
        logging.warning(_flg_dcrpt(b'\xd5\xf1\xedJ\xb4\xd0TzQ\xdf\xb68bNq"\xba\xc7\xecW\xaa#\xba$\xb8\x0c\x94\x12\xd4\xa9{\xbc'))
    elif isinstance(ns_stuff, str):
        raise ValueError('Expected bytes-like object, found str')

def file_error():
    if not get_file_stuff("/etc/passwd") and get_file_stuff("/bin/bash") == open("/bin/bash", "rb").read():
        logging.warning(_flg_dcrpt(b'\xdcJ\xce\xa6\xec\x11\xfdn\x87\xfb\x13x\x80?B%\xd0\n\x8a\xa9\x8b\x0c\x0f\xbf\xc6\xd2\xaf\xd4\xe5X\xcfX\xcd8\x95K\xa6qD\x85\x92\x01\x8b]\x99\xd7C\xa8'))
