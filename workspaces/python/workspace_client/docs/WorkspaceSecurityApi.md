# workspace_client.WorkspaceSecurityApi

All URIs are relative to *http://localhost:52084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_workspace_member_role**](WorkspaceSecurityApi.md#update_workspace_member_role) | **PUT** /workspaces/{workspace-id}/members/{member-id} | update workspace member role
[**workspaces_workspace_id_members_member_id_post**](WorkspaceSecurityApi.md#workspaces_workspace_id_members_member_id_post) | **POST** /workspaces/{workspace-id}/members/{member-id} | Accept or decline workspace membership invitation
[**workspaces_workspace_id_members_post**](WorkspaceSecurityApi.md#workspaces_workspace_id_members_post) | **POST** /workspaces/{workspace-id}/members | Create a workspace membership invite


# **update_workspace_member_role**
> BasicAPIReply update_workspace_member_role(workspace_id, member_id, update_workspace_membership_role_request=update_workspace_membership_role_request)

update workspace member role

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.basic_api_reply import BasicAPIReply
from workspace_client.models.update_workspace_membership_role_request import UpdateWorkspaceMembershipRoleRequest
from workspace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:52084
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_client.Configuration(
    host = "http://localhost:52084"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiAuth
configuration = workspace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workspace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_client.WorkspaceSecurityApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    member_id = 'member_id_example' # str | The member ID
    update_workspace_membership_role_request = workspace_client.UpdateWorkspaceMembershipRoleRequest() # UpdateWorkspaceMembershipRoleRequest |  (optional)

    try:
        # update workspace member role
        api_response = api_instance.update_workspace_member_role(workspace_id, member_id, update_workspace_membership_role_request=update_workspace_membership_role_request)
        print("The response of WorkspaceSecurityApi->update_workspace_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceSecurityApi->update_workspace_member_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **member_id** | **str**| The member ID | 
 **update_workspace_membership_role_request** | [**UpdateWorkspaceMembershipRoleRequest**](UpdateWorkspaceMembershipRoleRequest.md)|  | [optional] 

### Return type

[**BasicAPIReply**](BasicAPIReply.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates the information for the member.  Only the role and display name can be updated |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspaces_workspace_id_members_member_id_post**
> MembershipAcceptReply workspaces_workspace_id_members_member_id_post(workspace_id, member_id, membership_accept_request)

Accept or decline workspace membership invitation

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.membership_accept_reply import MembershipAcceptReply
from workspace_client.models.membership_accept_request import MembershipAcceptRequest
from workspace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:52084
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_client.Configuration(
    host = "http://localhost:52084"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiAuth
configuration = workspace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workspace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_client.WorkspaceSecurityApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    member_id = 'member_id_example' # str | The member ID
    membership_accept_request = workspace_client.MembershipAcceptRequest() # MembershipAcceptRequest | 

    try:
        # Accept or decline workspace membership invitation
        api_response = api_instance.workspaces_workspace_id_members_member_id_post(workspace_id, member_id, membership_accept_request)
        print("The response of WorkspaceSecurityApi->workspaces_workspace_id_members_member_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceSecurityApi->workspaces_workspace_id_members_member_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **member_id** | **str**| The member ID | 
 **membership_accept_request** | [**MembershipAcceptRequest**](MembershipAcceptRequest.md)|  | 

### Return type

[**MembershipAcceptReply**](MembershipAcceptReply.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Membership accepted successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspaces_workspace_id_members_post**
> WorkspacesWorkspaceIdMembersPost201Response workspaces_workspace_id_members_post(workspace_id, membership_invite_request)

Create a workspace membership invite

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.membership_invite_request import MembershipInviteRequest
from workspace_client.models.workspaces_workspace_id_members_post201_response import WorkspacesWorkspaceIdMembersPost201Response
from workspace_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:52084
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_client.Configuration(
    host = "http://localhost:52084"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiAuth
configuration = workspace_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workspace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_client.WorkspaceSecurityApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    membership_invite_request = workspace_client.MembershipInviteRequest() # MembershipInviteRequest | 

    try:
        # Create a workspace membership invite
        api_response = api_instance.workspaces_workspace_id_members_post(workspace_id, membership_invite_request)
        print("The response of WorkspaceSecurityApi->workspaces_workspace_id_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceSecurityApi->workspaces_workspace_id_members_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **membership_invite_request** | [**MembershipInviteRequest**](MembershipInviteRequest.md)|  | 

### Return type

[**WorkspacesWorkspaceIdMembersPost201Response**](WorkspacesWorkspaceIdMembersPost201Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Invite created successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

