# JWT utility
Encode or decode [JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token).

Small utility to encode payloads as JWT using either HS256 or RS256, it is loosely based on the sample from the [Python jwt package](https://pypi.org/project/jwt/).

Usage:
```
JWTutil.py [--help] [-k <keyfile>] [-s <secret>] [-t <token>]

Encode or decode JSON Web Tokens (JWT)
  --help | -h                      : print this help
  --keyfile=keyfile | -k keyfile   : file with private key for RS256 encoding
  --secret=secret   | -s secret    : secret phrase for HS256 encoding
  --token=token     | -t token     : JWT to decode
```