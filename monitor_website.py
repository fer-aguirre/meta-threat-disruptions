import requests
import hashlib
import os

def get_website_content(url):
    response = requests.get(url)
    return response.text

def compute_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def has_website_changed(url):
    current_content = get_website_content(url)
    current_hash = compute_hash(current_content)

    previous_hash = os.getenv('PREVIOUS_HASH')

    if previous_hash != current_hash:
        os.environ['PREVIOUS_HASH'] = current_hash
        return True

    return False

if __name__ == "__main__":
    url = "https://transparency.meta.com/es-la/metasecurity/threat-reporting/"
    if has_website_changed(url):
        print("Website has changed.")
    else:
        print("No changes detected.")
