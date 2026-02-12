import os
import json
import argparse
import sys
import requests

# Constants
BASE_URL = "https://api.cloudflare.com/client/v4"

def load_config():
    """Load configuration from environment variables."""
    zones = {}

    # Load zones from environment variables
    # Expected format: CLOUDFLARE_ZONE_ID or CLOUDFLARE_ZONE_ID_<NAME>
    for key, value in os.environ.items():
        if key.startswith("CLOUDFLARE_ZONE_ID_"):
            name = key.replace("CLOUDFLARE_ZONE_ID_", "").lower()
            zones[name] = value
        elif key == "CLOUDFLARE_ZONE_ID":
            domain = os.environ.get("DOMAIN_NAME", "default")
            zones[domain] = value

    return {
        "zones": zones,
        "account_id": os.environ.get("CLOUDFLARE_ACCOUNT_ID"),
        "api_token": os.environ.get("CLOUDFLARE_API_TOKEN")
    }

def get_headers(api_token):
    return {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

def get_security_level(zone_id, api_token):
    """Get the current security level."""
    url = f"{BASE_URL}/zones/{zone_id}/settings/security_level"
    try:
        response = requests.get(url, headers=get_headers(api_token))
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            return data["result"]["value"]
        else:
            print(f"Error for zone {zone_id}: {data.get('errors')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed for zone {zone_id}: {e}")
        return None

def set_security_level(zone_id, api_token, level):
    """Set the security level."""
    valid_levels = ["off", "essentially_off", "low", "medium", "high", "under_attack"]
    if level not in valid_levels:
        print(f"Error: Invalid security level {level}. Must be one of: {', '.join(valid_levels)}")
        return False

    url = f"{BASE_URL}/zones/{zone_id}/settings/security_level"
    payload = {"value": level}

    try:
        response = requests.patch(url, headers=get_headers(api_token), json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            print(f"Successfully set security level for zone {zone_id} to: {data['result']['value']}")
            return True
        else:
            print(f"Error for zone {zone_id}: {data.get('errors')}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed for zone {zone_id}: {e}")
        return False

def list_dns_records(zone_id, api_token):
    """List DNS records for the zone."""
    url = f"{BASE_URL}/zones/{zone_id}/dns_records"
    try:
        response = requests.get(url, headers=get_headers(api_token))
        response.raise_for_status()
        data = response.json()
        if data.get("success"):
            print(f"DNS Records for zone {zone_id}:")
            for record in data["result"]:
                print(f"  {record['type']} {record['name']} -> {record['content']} (ID: {record['id']})")
            return True
        else:
            print(f"Error for zone {zone_id}: {data.get('errors')}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed for zone {zone_id}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Manage Cloudflare Zone Settings")
    parser.add_argument("--status", action="store_true", help="Get current security level for all configured zones")
    parser.add_argument("--set", dest="security_level", help="Set security level for all configured zones")
    parser.add_argument("--list-dns", action="store_true", help="List DNS records for all configured zones")
    parser.add_argument("--domain", help="Target a specific domain/zone label instead of all")

    args = parser.parse_args()

    config = load_config()

    if not config["api_token"]:
        print("Error: Missing CLOUDFLARE_API_TOKEN environment variable.")
        sys.exit(1)

    if not config["zones"]:
        print("Error: No zones configured. Set CLOUDFLARE_ZONE_ID or CLOUDFLARE_ZONE_ID_<NAME>.")
        sys.exit(1)

    target_zones = config["zones"]
    if args.domain:
        if args.domain in config["zones"]:
            target_zones = {args.domain: config["zones"][args.domain]}
        else:
            print(f"Error: Zone label {args.domain} not found in configuration. Available: {', '.join(config['zones'].keys())}")
            sys.exit(1)

    for label, zone_id in target_zones.items():
        print(f"--- Processing Zone: {label} (ID: {zone_id}) ---")
        if args.status:
            level = get_security_level(zone_id, config["api_token"])
            if level:
                print(f"Current Security Level: {level}")

        if args.security_level:
            set_security_level(zone_id, config["api_token"], args.security_level)

        if args.list_dns:
            list_dns_records(zone_id, config["api_token"])

    if not (args.status or args.security_level or args.list_dns):
        parser.print_help()

if __name__ == "__main__":
    main()
