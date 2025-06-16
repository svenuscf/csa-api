import requests

BASE_URL = "https://api.sse.cisco.com"

TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjcyNmI5MGUzLWQ1MjYtNGMzZS1iN2QzLTllYjA5NWU2ZWRlOSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1bWJyZWxsYS1hdXRoei9hdXRoc3ZjIiwic3ViIjoib3JnLzgzMTI3MTkvY2xpZW50L2JmMjI2NmI4NjBmNDQ2YzRhZDk0OTBmYWExYjA3NjM2IiwiZXhwIjoxNzUwMTE0NTQzLCJuYmYiOjE3NTAxMTA5NDMsImlhdCI6MTc1MDExMDk0Mywic2NvcGUiOiJkZXBsb3ltZW50cy5uZXR3b3Jrczp3cml0ZSBkZXBsb3ltZW50cy5uZXR3b3JrczpyZWFkIGRlcGxveW1lbnRzLnJvYW1pbmdjb21wdXRlcnM6d3JpdGUgZGVwbG95bWVudHMucm9hbWluZ2NvbXB1dGVyczpyZWFkIGRlcGxveW1lbnRzLnJvYW1pbmdjb21wdXRlcnNvcmdpbmZvOnJlYWQgZGVwbG95bWVudHMuaW50ZXJuYWxuZXR3b3Jrczp3cml0ZSBkZXBsb3ltZW50cy5pbnRlcm5hbG5ldHdvcmtzOnJlYWQgZGVwbG95bWVudHMuaW50ZXJuYWxkb21haW5zOndyaXRlIGRlcGxveW1lbnRzLmludGVybmFsZG9tYWluczpyZWFkIGRlcGxveW1lbnRzLnZpcnR1YWxhcHBsaWFuY2VzOndyaXRlIGRlcGxveW1lbnRzLnZpcnR1YWxhcHBsaWFuY2VzOnJlYWQgZGVwbG95bWVudHMuc2l0ZXM6d3JpdGUgZGVwbG95bWVudHMuc2l0ZXM6cmVhZCBkZXBsb3ltZW50cy5kYXRhY2VudGVyczpyZWFkIGRlcGxveW1lbnRzLnR1bm5lbHM6d3JpdGUgZGVwbG95bWVudHMudHVubmVsczpyZWFkIGRlcGxveW1lbnRzLm5ldHdvcmtkZXZpY2VzOndyaXRlIGRlcGxveW1lbnRzLm5ldHdvcmtkZXZpY2VzOnJlYWQgZGVwbG95bWVudHMucG9saWNpZXM6d3JpdGUgZGVwbG95bWVudHMucG9saWNpZXM6cmVhZCBkZXBsb3ltZW50cy52cG46d3JpdGUgZGVwbG95bWVudHMudnBuOnJlYWQgZGVwbG95bWVudHMuYWFhOndyaXRlIGRlcGxveW1lbnRzLmFhYTpyZWFkIGRlcGxveW1lbnRzLmRldmljZXMuc3dnOndyaXRlIGRlcGxveW1lbnRzLmRldmljZXMuc3dnOnJlYWQgZGVwbG95bWVudHMuZGV2aWNlcy5leHBvcnQ6d3JpdGUgZGVwbG95bWVudHMuZGV2aWNlcy5leHBvcnQ6cmVhZCBkZXBsb3ltZW50cy5kZXZpY2VzLnJlZ2lzdHJhdGlvbjp3cml0ZSBkZXBsb3ltZW50cy5kZXZpY2VzLnN5bmM6d3JpdGUgZGVwbG95bWVudHMubmV0d29ya3R1bm5lbGdyb3Vwczp3cml0ZSBkZXBsb3ltZW50cy5uZXR3b3JrdHVubmVsZ3JvdXBzOnJlYWQgZGVwbG95bWVudHMucmVnaW9uczpyZWFkIGRlcGxveW1lbnRzLmlkZW50aXRpZXM6d3JpdGUgZGVwbG95bWVudHMuaWRlbnRpdGllczpyZWFkIGRlcGxveW1lbnRzLnRhZ2RldmljZXM6d3JpdGUgZGVwbG95bWVudHMudGFnZGV2aWNlczpyZWFkIGRlcGxveW1lbnRzLnRhZ3M6d3JpdGUgZGVwbG95bWVudHMudGFnczpyZWFkIGRlcGxveW1lbnRzLnJlc291cmNlY29ubmVjdG9yczp3cml0ZSBkZXBsb3ltZW50cy5yZXNvdXJjZWNvbm5lY3RvcnM6cmVhZCBkZXBsb3ltZW50cy5oeWJyaWR6dG5hLmRldmljZXM6d3JpdGUgZGVwbG95bWVudHMuaHlicmlkenRuYS5kZXZpY2VzOnJlYWQgZGVwbG95bWVudHMuaHlicmlkenRuYS5jb21taXRzOndyaXRlIGRlcGxveW1lbnRzLmh5YnJpZHp0bmEuY29tbWl0czpyZWFkIGRlcGxveW1lbnRzLmh5YnJpZHp0bmEucmVzb3VyY2VzOndyaXRlIGRlcGxveW1lbnRzLmh5YnJpZHp0bmEucmVzb3VyY2VzOnJlYWQgZGVwbG95bWVudHMuaHlicmlkenRuYS5ydWxlczpyZWFkIGRlcGxveW1lbnRzLmh5YnJpZHp0bmEuZm1jczpyZWFkIGRlcGxveW1lbnRzLmRuc2ZvcndhcmRlcnM6d3JpdGUgZGVwbG95bWVudHMuZG5zZm9yd2FyZGVyczpyZWFkIHBvbGljaWVzLmRlc3RpbmF0aW9ubGlzdHM6d3JpdGUgcG9saWNpZXMuZGVzdGluYXRpb25saXN0czpyZWFkIHBvbGljaWVzLmRlc3RpbmF0aW9uczp3cml0ZSBwb2xpY2llcy5kZXN0aW5hdGlvbnM6cmVhZCBwb2xpY2llcy5kbHBpbmRleGVyOndyaXRlIHBvbGljaWVzLmRscGluZGV4ZXI6cmVhZCBwb2xpY2llcy5ydWxlczp3cml0ZSBwb2xpY2llcy5ydWxlczpyZWFkIHBvbGljaWVzLnByaXZhdGVyZXNvdXJjZWdyb3Vwczp3cml0ZSBwb2xpY2llcy5wcml2YXRlcmVzb3VyY2Vncm91cHM6cmVhZCBwb2xpY2llcy5wcml2YXRlcmVzb3VyY2Vjb25uZWN0aXZpdHkuenRhOndyaXRlIHBvbGljaWVzLnByaXZhdGVyZXNvdXJjZXM6d3JpdGUgcG9saWNpZXMucHJpdmF0ZXJlc291cmNlczpyZWFkIHBvbGljaWVzLmFwcHBvcnRhbHM6d3JpdGUgcG9saWNpZXMuYXBwcG9ydGFsczpyZWFkIHBvbGljaWVzLmV2YWx1YXRlcnVsZXM6d3JpdGUgcG9saWNpZXMudGVuYW50Y29udHJvbHNwcm9maWxlczpyZWFkIHBvbGljaWVzLmFwcHJpc2twcm9maWxlbWFuYWdlcjp3cml0ZSBwb2xpY2llcy5hcHByaXNrcHJvZmlsZW1hbmFnZXI6cmVhZCBwb2xpY2llcy5hcHBsaWNhdGlvbmxpc3RzOndyaXRlIHBvbGljaWVzLmFwcGxpY2F0aW9ubGlzdHM6cmVhZCBwb2xpY2llcy5pcHNjb25maWc6d3JpdGUgcG9saWNpZXMuaXBzY29uZmlnOnJlYWQgcG9saWNpZXMuc2V0dGluZ3M6d3JpdGUgcG9saWNpZXMuc2V0dGluZ3M6cmVhZCBwb2xpY2llcy5uZXR3b3Jrb2JqZWN0czp3cml0ZSBwb2xpY2llcy5uZXR3b3Jrb2JqZWN0czpyZWFkIHBvbGljaWVzLm5ldHdvcmtncm91cHM6d3JpdGUgcG9saWNpZXMubmV0d29ya2dyb3VwczpyZWFkIHBvbGljaWVzLnNlcnZpY2VvYmplY3RzOndyaXRlIHBvbGljaWVzLnNlcnZpY2VvYmplY3RzOnJlYWQgcG9saWNpZXMuc2VydmljZWdyb3Vwczp3cml0ZSBwb2xpY2llcy5zZXJ2aWNlZ3JvdXBzOnJlYWQgcG9saWNpZXMuZGxwLmRscGFhczpyZWFkIHBvbGljaWVzLmZlZWRzOndyaXRlIHBvbGljaWVzLmZlZWRzOnJlYWQgcG9saWNpZXMuc2VjdXJpdHlwcm9maWxlczpyZWFkIHBvbGljaWVzLmNhdGVnb3JpZXM6cmVhZCBwb2xpY2llcy5jYXRlZ29yeXNldHRpbmdzOnJlYWQgcG9saWNpZXMuYXBwbGljYXRpb25jYXRlZ29yaWVzOnJlYWQgcG9saWNpZXMuYXBwbGljYXRpb25zOnJlYWQiLCJhdXRoel9kb25lIjpmYWxzZX0.TngnI6kAb_l6-qrYP9pbC4cwDhmW9y0DN27U1yJDqdz9OBD00n1iFPrdDt1y7HOXla5vKpqzUCrcFsZLN3HOl9dit9lAg_gvj5XuqoipNCVYvHvTC56zbrRSH1dafmkY74jiGNknMjG_I5ChiVVuL-0vMIMVGpFCyV4Jd3GM8uXLiv6sV2OxBG7GkdqX7XPPEXI4RYhGaEN1MZ8DpfrUagTM8Bb47XoauHKd59-cNWOVw4cvUd4uhPGjnDdj34IYfJIvRBsvb1BB-qLvxvWjh0vXnZ_97EPAH5wM02_vwtlGBriUJpKGa7HjZnhQc_dDCqRwRIdcbKfPMam7tF5_7w"

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
