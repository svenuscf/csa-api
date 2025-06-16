# Cisco Secure Access (CSA) Automation

Python scripts to automate internal network and tunnel group (NTG) management via Cisco Secure Access (SSE) API.

## 🔧 Features

- ✅ List internal networks and their NTG association
- 🔄 Bulk reassign internal networks from one NTG to another
- 🔐 OAuth2-based token authentication
- 🧼 No secrets stored in code

## 🗂️ Project Structure
.  
├── `.env` # Stores CLIENT_ID and CLIENT_SECRET (excluded from git)  
├── `auth_helper.py` # Auth module using OAuth2 client credentials  
├── `get-ntg.py` # Lists internal networks and their NTG mappings  
├── `reassign-ntg.py` # Reassigns a single internal network to another NTG  
├── `bulk-reassign-ntg.py` # Reassigns all internal networks from one NTG to another  


## 🔐 Setup

1. Install dependencies:

```bash
pip install python-dotenv requests requests-oauthlib
```

2. Create a .env file:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
``` 
Note that you will need to create an API key in CSA portal, and give it the correct privileges, e.g. Deployments Read/Write.  
Then copy the API Key name as the CLIENT_ID and the key secret as CLIENT_SECRET.  

3. Run the script:

```
python3 bulk-reassign-ntg.py
```
