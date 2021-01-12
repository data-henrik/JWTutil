#!/usr/bin/python3

# Small utility to encode payloads as JWT using either HS256 or RS256
# Based on sample from jwt package
#
# coded 2021 by Henrik Loeser

import json, sys, getopt
from datetime import datetime, timedelta, timezone

from jwt import JWT, jwk_from_dict, jwk_from_pem
from jwt.utils import get_int_from_datetime

# Change to your own payload
# Issue time (iat) to current time, expiration (exp) to now plus one hour

message = {
    'iss': 'data_henrik',
    'name': 'henrik',
    'iat': get_int_from_datetime(datetime.now(timezone.utc)),
    'exp': get_int_from_datetime(
        datetime.now(timezone.utc) + timedelta(hours=1)),
}

# print help on usage options
def printHelp():
    print('JWTutil.py [--help] [-k <keyfile>] [-s <secret>] [-t <token>]')
    print('Encode or decode JSON Web Tokens (JWT)')
    print()
    print('  --help | -h                      : print this help')
    print('  --keyfile=keyfile | -k keyfile   : file with private key for RS256 encoding')
    print('  --secret=secret   | -s secret    : secret phrase for HS256 encoding')
    print('  --token=token     | -t token     : JWT to decode')


def main(argv):
    #
    # Encode the message to JWT(JWS)
    #
    try:
        opts, args = getopt.getopt(argv, "hk:s:t:", ["help", "keyfile=", "secret=", "token="])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)

    # init JWT handler
    instance = JWT()

    # set expected parameters to empty
    keyfile =''
    secret =''

    # check for options
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # help requested
            printHelp()
            sys.exit()
        elif opt in ("-k", "--keyfile"):
            # keyfile with private key for RS256-based encoding present
            keyfile = arg
        elif opt in ("-s", "--secret"):
            # secret (should base64-encoded) for HS256-based encoding present
            secret = arg
        elif opt in ("-t", "--token"):
            # token to decode
            token = arg
            # now decode it
            # - do not verify
            # - do not check for expiration
            print("\nDecoded token header and payload:")
            header,message_bin,signature,signing_message=instance._jws._decode_segments(token)
            print(json.dumps(header, indent=2))
            print(json.dumps(instance.decode(token, do_verify=False, do_time_check=False), indent=2))

    # Now encode the message(s) to signed JWT depending on whether
    # - keyfile is provided (RS256)
    # - a base64-encoded secret is provided (HS256)
    if (keyfile != ''):
        # load the private key
        with open(keyfile, 'rb') as fh:
            signing_key = jwk_from_pem(fh.read())

        compact_jws = instance.encode(message, signing_key, alg='RS256')
        print("Token using RS256:")
        print(compact_jws)

    if (secret != ''):
        # load secret from JSON
        signing_key2 = jwk_from_dict({'kty': 'oct', 'k': secret})
        compact_jws = instance.encode(message, signing_key2, alg='HS256')
        print("Token using HS256:")
        print(compact_jws)

if __name__ == "__main__":
   main(sys.argv[1:])