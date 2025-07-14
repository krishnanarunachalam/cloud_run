import requests
import json

def get_access_token():
    """Gets an access token from the SecureAuth endpoint."""
    url = "https://ssodev.sanmina.com/secureauth249/OidcToken.aspx"
    data = {
        "grant_type": "client_credentials",
        "scope": "oauth",
        "client_id": "e437afb5495d43b889ba46967d7853e9",
        "client_secret": "9a93011c111190234ed1f6cb8a3a622338fcd2589435d64cb3418e84c22804ba"
    }
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()["access_token"]

def create_service_request(access_token):
    """Creates a service request using the provided access token."""
    url = "https://itdev.sanmina.com/hdapi/ittest/roboship/SR/Creation"
    headers = {
        "Accept": "application/json, text/json, application/xml, text/xml",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    body = {
        "GroupId": 246,
        "GroupName": "Enterprise Application / IT and Automation",
        "CaseTypeId": 5,
        "CaseTypeName": "Web Service",
        "CategoryId": 204,
        "CategoryName": "Service Request Tool",
        "ProblemTypeId": 1232,
        "ProblemTypeName": "SR - General Support",
        "LanguageId": 1,
        "LanguageName": "English",
        "AssigneeId": 87865,
        "AssigneeName": "Jonathas Morais",
        "AssigneeEmailAddress": "jonathas.morais@sanmina.com",
        "EmployeeEmailAddress": None,
        "RequesterId": 87865,
        "RequesterName": "Jonathas Morais",
        "RequesterEmailAddress": "jonathas.morais@sanmina.com",
        "RequesterTelephoneNumber": "+52 33 3668 9800 x6981",
        "SubmitterId": 87865,
        "SubmitterName": "Jonathas Morais",
        "SubmitterEmailAddress": "jonathas.morais@sanmina.com",
        "SolutionId": 30,
        "SolutionName": "Administratively Closed - submitted without essential information or prematurely or without necessary reviews and approvals or as a trouble ticket when it should have been a work request or a change request.",
        "StatusId": 4,
        "StatusName": "Resolved",
        "LocationId": 5076,
        "LocationName": "Asia/Pacific, IN, Chen* Connection #0 to host ittest.sanmina.com left intactnai (G01/6110) A3, Phase II, MEPZ Special Economic Zone, Tambaram",
        "PriorityId": 3,
        "PriorityName": "P3",
        "SubStatusId": 0,
        "SubStatusName": "",
        "SummaryText": "Automated SR",
        "CreationDate": "2017-06-09T13:36:05.21Z",
        "TargetDate": "2017-06-11T02:35:00Z",
        "LocalTimeZoneCode": "",
        "WorkLogEntries": 0,
        "DescriptionText": "This is a test",
        "ResolutionText": "No longer required.",
        "IsEditable": True,
        "Attachments": 0,
        "ChangeRequestId": 0,
        "ChangeRequestName": "Asia/Pacific, IN, Chennai (G01/6110)",
        "IsChangeRequestRequired": False,
        "IsProductionChangeRequired": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        token = get_access_token()
        print(f"Successfully retrieved access token: {token}")
        sr_response = create_service_request(token)
        print("Successfully created service request:")
        print(json.dumps(sr_response, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
