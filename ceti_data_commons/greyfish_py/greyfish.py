# Author: Carter Brown
import requests
import shutil

# In meeting -
# What parameters to pass - which params are static (serverip, gk?)


# Create user in Greyfish
# user_id: The user's Greyfish ID
# Returns status code in case of no network problems
# Returns -1 in case of connection error, timeout, etc.
def create_user(user_id):
    try:
        response = requests.get(f'http://$SERVER_IP:2003/grey/create_user/$gk/{user_id}')
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(e)
        return -1


# Delete user in Greyfish
# user_id: The user's Greyfish ID
# Returns status code in case of no network problems
# Returns -1 in case of connection error, timeout, etc.
def delete_user(user_id):
    try:
        response = requests.get(f'http://$SERVER_IP:2003/grey/delete_user/$gk/{user_id}')
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(e)
        return -1


# Upload a file to Greyfish
# user_id: The user's Greyfish ID
# file_path: Local path to file
# Returns status code in case of no network problems
# Returns -1 in case of connection error, timeout, etc.
def upload_file(user_id, file_path):
    files = {
        'file': open(file_path, 'rb'),
    }
    try:
        response = requests.post(f'http://$SERVER_IP:2003/grey/upload/$gk/{user_id}/PATH++TO++DIR', files=files)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(e)
        return -1


# Download a file from Greyfish
# user_id: The user's Greyfish ID
# filename: Name of the file stored in Greyfish
# ---- TODO:
# Figure out what this should return - reference:
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
# Currently downloads a file from Greyfish and stores it as the same name
# Returns ?
def download_file(user_id, filename):
    url = f'http://$SERVER_IP:2000/grey/grey/$gk/{user_id}/{filename}/PATH++TO++DIR'
    try:
        with requests.get(url, stream=True) as r:
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    except requests.exceptions.RequestException as e:
        print(e)
        return -1
