from __future__ import print_function
import pprint
from googleapiclient.discovery import build
from google.oauth2 import credentials, service_account
 
# Scopes required by this endpoint -> https://developers.google.com/drive/api/v3/reference/permissions/update
SCOPES = ["https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive.readonly",
          "https://www.googleapis.com/auth/drive.metadata.readonly",
          "https://www.googleapis.com/auth/drive.metadata",
          "https://www.googleapis.com/auth/drive.photos.readonly"]

# Service Account Credentials to be used. How to create at https://developers.google.com/workspace/guides/create-credentials#service-account
SERVICE_ACCOUNT_FILE = 'yourServiceAccountCredentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes= SCOPES)
delegated_creds = credentials.with_subject('UserToBeImpersonated@yourdomain.com')

service = build('drive', 'v3', credentials = delegated_creds)

""" 
Requiered parameters -> https://developers.google.com/drive/api/v3/reference/permissions/update#parameters
To get the below use: 
https://github.com/Yancy-Godoy/GoogleWorkspace_DriveSDK/blob/main/listFilePermissions.py
https://github.com/Yancy-Godoy/GoogleWorkspace_DriveSDK/blob/main/listFilesFromAnotherUser.py
"""
userfileID = 'FileIDContainingTheRoleToUpdate'
permissionID = 'UserPermissionID'

"""
In this scenario, user in question was an owner of this file, here we will be changing the permissionID to be a reader instead.
"""

parameters = {
    'role': 'reader' # new role to be assigned
    }

results = service.permissions().update(fileId=userfileID,permissionId=permissionID, body=parameters,fields='*').execute()

pprint.pprint(results)
