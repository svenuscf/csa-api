
from auth_helper import get_secure_access_token
import requests

BASE_URL = "https://api.sse.cisco.com"  # Replace if you're using region-specific endpoint

TOKEN = get_secure_access_token()

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_internal_networks():
    url = f"{BASE_URL}/deployments/v2/internalnetworks"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_network_tunnel_groups():
    url = f"{BASE_URL}/deployments/v2/networktunnelgroups"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    networks = get_internal_networks()
    ntgs = get_network_tunnel_groups()

    ntgs_list = ntgs['data']
    ntg_map = {ntg['id']: ntg['name'] for ntg in ntgs_list}

    for net in networks:
        net_name = net.get('name')
        subnet = f"{net.get('ipAddress')}/{net.get('prefixLength')}"
        tunnel_id = net.get('tunnelId')
        associated_ntg = ntg_map.get(tunnel_id, tunnel_id or 'Unassigned')

        print(f"Network: {net_name} ({subnet}) → NTG: {associated_ntg}")
