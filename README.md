# haveibeenpwned-api

Running any web service with user accounts requires some form of passwords.
A good measure to ensure that your users have good passwords, is to check them against a list of breached passwords. This practice is also suggested by [NIST SP 800-63](https://www.nist.gov/itl/tig/projects/special-publication-800-63).

Troy Hunt is providing a great API to check for compromised passwords at https://haveibeenpwned.com/Passwords .
Whoever feels uncomfortable to send parts of your users password hashes to a remote API, wants to check them against a local database.
Fortunately the complete set of over half a billion passwords is also available for download.

This project aims to provide a self hosted password checking API, which works as https://haveibeenpwned.com/API/v2 .

## Currently implemented endpoints

### `/range/<hash>`

This endpoint returns a list of all sha1 hashes with the supplied prefix and their occurence.

## Preparation

The file provided is not directly usable for efficient lookups.
The frequency count after each hash leads to variable length records. Therefore we zero padd all frequency counts to the maximum required digits.

* download the sha1 hashes (ordered by hash), approximately 10GB
* unzip the archive, approximately 25GB `.txt` file
* search the highest frequency count:
```bash
python scripts/largest.py pwned-passwords-sha1-ordered-by-hash-v4.txt
```
* for v4, this is 23174662, meaning you need at least a padding of 8
* create constant length records (watch out, this requires another 28GB)
```bash
python scripts/prepare.py pwned-passwords-sha1-ordered-by-hash-v4.txt 10 pwned.txt
```

only the `pwned.txt` file is required at the service.

## Installation

The api runs as a Flask app. The easiest way is to deploy it as a docker service:

```
docker run -d -v /path_to_pwned.txt:/srv/pwned.txt -p 5000:5000 felixengelmann/haveibeenpwned-api
```

or rebuild the image

```bash
docker build -t haveibeenpwned-api:latest .
docker run -d -v /path_to_pwned.txt:/srv/pwned.txt -p 5000:5000 haveibeenpwned-api
```

Alternatively, you can run the Flask app in a virtual environment

```bash
virtualenv env
source ./env/bin/activate
python run.py
```
which serves the api at port 5000.

## Usage Example

To integrate the check into, e.g. a Django app, you can use https://github.com/jamiecounsell/django-pwned-passwords and set the `PWNED_VALIDATOR_URL` in you django settings to point to your custom instance at `https://your-domain.com:5000/range/{short_hash}`