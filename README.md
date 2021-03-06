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

Use `pip install [--user] requirements.txt` to install required package(s).

## Some fun with Db2 and JWT
See [how I some fun setting up Db2 to accept JWT for authenticating users](Db2_JWT.md).