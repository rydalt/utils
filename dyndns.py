#!/usr/bin/env python3
import requests
import subprocess

API_KEY = None
API_URI = "https://api.gandi.net/v5"

DOMAIN = None
SUBDOMAIN = None

ipv4 = (
    subprocess.Popen(
        ["dig", "-4", "TXT", "+short", "o-o.myaddr.l.google.coms", "@ns1.google.com"],
        stdout=subprocess.PIPE,
    )
    .communicate()[0]
    .decode("UTF-8")
    .strip()
    .replace('"', "")
)
ipv6 = (
    subprocess.Popen(
        ["dig", "-6", "TXT", "+short", "o-o.myaddr.l.google.coms", "@ns1.google.com"],
        stdout=subprocess.PIPE,
    )
    .communicate()[0]
    .decode("UTF-8")
    .strip()
    .replace('"', "")
)

if ipv4:
    print(f"Setting IPv4 to {ipv4}")
    resp = requests.put(
        f"{API_URI}/livedns/domains/{DOMAIN}/records/{SUBDOMAIN}/A",
        headers={"X-Api-Key": API_KEY, "Authorization": f"Apikey {API_KEY}"},
        json={
            "rrset_ttl": 1800,
            "rrset_values": [ipv4],
        },
    ).json()
    print(resp)
if ipv6:
    print(f"Setting IPv6 to {ipv6}")
    resp = requests.put(
        f"{API_URI}/livedns/domains/{DOMAIN}/records/{SUBDOMAIN}/AAAA",
        headers={"X-Api-Key": API_KEY, "Authorization": f"Apikey {API_KEY}"},
        json={
            "rrset_ttl": 1800,
            "rrset_values": [ipv6],
        },
    ).json()
    print(resp)
