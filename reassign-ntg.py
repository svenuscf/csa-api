import requests
from auth_helper import get_secure_access_token

BASE_URL = "https://api.sse.cisco.com"

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

def update_tunnel_binding(existing_net, new_tunnel_id):
    network_id = existing_net["originId"]
    url = f"{BASE_URL}/deployments/v2/internalnetworks/{network_id}"

    payload = {
        "name": existing_net["name"],
        "ipAddress": existing_net["ipAddress"],
        "prefixLength": existing_net["prefixLength"],
        "tunnelId": new_tunnel_id
    }

    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    networks = get_internal_networks()
    ntgs = get_network_tunnel_groups()["data"]
    ntg_map = {ntg["id"]: ntg["name"] for ntg in ntgs}

    print("\nAvailable Internal Networks:\n")
    for i, net in enumerate(networks):
        net_id = net["originId"]
        name = net["name"]
        subnet = f"{net['ipAddress']}/{net['prefixLength']}"
        tunnel_id = net.get("tunnelId")
        ntg_name = ntg_map.get(tunnel_id, "Unassigned")
        print(f"[{i}] {name} ({subnet}) → {ntg_name}")

    index = int(input("\nSelect the network to reassign [0-N]: "))
    selected = networks[index]

    print("\nAvailable Tunnel Groups (NTGs):")
    for j, ntg in enumerate(ntgs):
        print(f"[{j}] {ntg['name']} (ID: {ntg['id']})")

    new_index = int(input("\nSelect the new NTG [0-N]: "))
    new_ntg_id = ntgs[new_index]['id']

    result = update_tunnel_binding(selected, new_ntg_id) 
    print("\n✅ NTG reassignment successful.")
