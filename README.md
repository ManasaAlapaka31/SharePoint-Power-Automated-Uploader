# SharePoint-Power-Automated-Uploader

## Overview

The `upload_file_to_sharepoint.py` script automates the process of uploading files to a specific folder in SharePoint and sends an email notification & Teams channel notification. This is achieved by interfacing with a custom Power Automate flow that handles the file upload.

## Setup Instructions

### Setting Up the Power Automate Flow

1. **Create a new Automated Cloud Flow** in Power Automate.
   - Choose the trigger as "When an HTTP request is received."
<img width="461" alt="image" src="https://github.com/user-attachments/assets/9757c843-9f3d-4be4-9047-def886299761">

2. **Add an action**: `Create file` in SharePoint
   - Specify the folder path and file name based on the HTTP request.
<img width="341" alt="image" src="https://github.com/user-attachments/assets/5042fb2b-10f3-4fd5-8500-9bac2644e7a3">

3. **Add an action**: `Get file properties`
   - Retrieve properties of the uploaded file (Link of the file in sharepoint).
<img width="335" alt="image" src="https://github.com/user-attachments/assets/0107b8cd-289f-449e-9adb-9b9b81ac5abe">

4. **Add an actions in parallel branch to previous step(Get file properties)**: `Post message in a chat or channel`& `Respond to a Power App or flow`
   - Post a notification about the file upload in Microsoft Teams.
   - Send a confirmation back to the calling script.
<img width="813" alt="image" src="https://github.com/user-attachments/assets/b9060e4d-1846-4e41-b3c8-0fc3be6242a4">

5. **Save the flow** and note the HTTP POST URL generated by the trigger.


## Script Configuration

1. Install the required Python package:
`pip install requests`
