from auth_helper import get_secure_access_token
import requests

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
    return response.json()["data"]

def update_tunnel_binding(existing_net, new_tunnel_id):
    url = f"{BASE_URL}/deployments/v2/internalnetworks/{existing_net['originId']}"
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
    print("\n🔄 Fetching data from Cisco Secure Access...\n")

    networks = get_internal_networks()
    ntgs = get_network_tunnel_groups()
    ntg_map = {ntg["id"]: ntg["name"] for ntg in ntgs}

    print("Available Tunnel Groups:\n")
    for idx, ntg in enumerate(ntgs):
        print(f"[{idx}] {ntg['name']} (ID: {ntg['id']})")

    src_index = int(input("\nSelect the SOURCE NTG to move from [0-N]: "))
    dst_index = int(input("Select the TARGET NTG to move to [0-N]: "))

    src_ntg_id = ntgs[src_index]["id"]
    dst_ntg_id = ntgs[dst_index]["id"]
    src_ntg_name = ntgs[src_index]["name"]
    dst_ntg_name = ntgs[dst_index]["name"]

    print(f"\n🔍 Finding internal networks assigned to: {src_ntg_name}")

    to_update = [net for net in networks if net.get("tunnelId") == src_ntg_id]

    print(f"Found {len(to_update)} internal network(s) to update:\n")

    for net in to_update:
        subnet = f"{net['ipAddress']}/{net['prefixLength']}"
        print(f" - {net['name']} ({subnet})")

    confirm = input(f"\n⚠️ Confirm reassignment to {dst_ntg_name}? (yes/no): ").strip().lower()

    if confirm == "yes":
        for net in to_update:
            try:
                update_tunnel_binding(net, dst_ntg_id)
                print(f"✅ Updated {net['name']}")
            except Exception as e:
                print(f"❌ Failed to update {net['name']}: {e}")
    else:
        print("❌ Operation cancelled.")

