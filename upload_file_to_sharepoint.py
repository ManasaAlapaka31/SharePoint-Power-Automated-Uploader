#!/usr/bin/env python3
import os
import requests
import subprocess
import sys
import json

def send_mail(file_name: str,sharepoint_name: str, file_link: str,script_name: str,description: str):
    Subject=f"{script_name} | {description}"
    Body=f"The file has been uploaded successfully to the {sharepoint_name} SharePoint."
    full_body = f"{Body}\n\nFile Name: {file_name}\nFile Link: {file_link}"
    body_str_encoded_to_byte = full_body.encode()
    return_stat = subprocess.run([f"mail", f"-s {Subject}", "Alapaka.Manasa@lumen.com"], input=body_str_encoded_to_byte)


def upload_file_to_sharepoint_via_pa(file_path,sharepoint_name,script_name,description):
	file_name = os.path.basename(file_path)
	
	folder_name = "GIVE FOLDER NAME HERE"
	msg=f"Script: {script_name}\n Description: {description}"
	
	url = "YOUR POWER AUTOMATE URL"
	url += f"&folderpath={folder_name}&filename={file_name}&msg={msg}"
	
	with open(file_path, 'rb') as file_obj:
		files = {'file': (file_name, file_obj)}
		response = requests.post(url, files=files)
	if response.status_code == 200:
		print(f"File '{file_name}' uploaded successfully.")
	elif response.status_code == 202:
		print(f"File '{file_name}' upload accepted and is being processed.")
	else:
		print(f"Failed to upload file '{file_name}'. Status Code: {response.status_code}, Response: {response.text}")
	# Parse the JSON response
	response_data = json.loads(response.text)

	# Extract the link value
	file_link = response_data.get('link')

	if response.status_code == 200:
		send_mail(file_name, sharepoint_name, file_link, script_name, description)
		

if __name__ == "__main__":
    if len(sys.argv) ==5: 
        upload_file_to_sharepoint_via_pa(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python3 sharepoint_v1.py <file_path> <sharepoint_name> <script_name> <description>")


