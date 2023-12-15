# workspace_client.WorkspacesApi

All URIs are relative to *http://localhost:52084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workspace_image**](WorkspacesApi.md#add_workspace_image) | **POST** /workspace/{workspace-id}/images | Add a new image to the workspace
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create a new workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace-id} | delete the workspace
[**delete_workspace_member**](WorkspacesApi.md#delete_workspace_member) | **DELETE** /workspaces/{workspace-id}/members/{member-id} | delete member from workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace-id} | get the workspace
[**get_workspace_images**](WorkspacesApi.md#get_workspace_images) | **GET** /workspace/{workspace-id}/images | get workspace images
[**get_workspace_member**](WorkspacesApi.md#get_workspace_member) | **GET** /workspaces/{workspace-id}/members/{member-id} | get workspace member
[**get_workspace_members**](WorkspacesApi.md#get_workspace_members) | **GET** /workspaces/{workspace-id}/members | get workspace members
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /workspaces | List workspaces the user has permissions to access
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace-id} | update the workspace


# **add_workspace_image**
> AddWorkspaceImage201Response add_workspace_image(workspace_id, workspace_image=workspace_image)

Add a new image to the workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.add_workspace_image201_response import AddWorkspaceImage201Response
from workspace_client.models.workspace_image import WorkspaceImage
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    workspace_image = workspace_client.WorkspaceImage() # WorkspaceImage |  (optional)

    try:
        # Add a new image to the workspace
        api_response = api_instance.add_workspace_image(workspace_id, workspace_image=workspace_image)
        print("The response of WorkspacesApi->add_workspace_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->add_workspace_image: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **workspace_image** | [**WorkspaceImage**](WorkspaceImage.md)|  | [optional] 

### Return type

[**AddWorkspaceImage201Response**](AddWorkspaceImage201Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> CreateWorkspace201Response create_workspace(workspace=workspace)

Create a new workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.create_workspace201_response import CreateWorkspace201Response
from workspace_client.models.workspace import Workspace
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace = workspace_client.Workspace() # Workspace |  (optional)

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(workspace=workspace)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | [**Workspace**](Workspace.md)|  | [optional] 

### Return type

[**CreateWorkspace201Response**](CreateWorkspace201Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(workspace_id)

delete the workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID

    try:
        # delete the workspace
        api_instance.delete_workspace(workspace_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 

### Return type

void (empty response body)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The workspace was deleted |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_member**
> delete_workspace_member(workspace_id, member_id)

delete member from workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    member_id = 'member_id_example' # str | The member ID

    try:
        # delete member from workspace
        api_instance.delete_workspace_member(workspace_id, member_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **member_id** | **str**| The member ID | 

### Return type

void (empty response body)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Member was deleted |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> CreateWorkspace201Response get_workspace(workspace_id)

get the workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.create_workspace201_response import CreateWorkspace201Response
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID

    try:
        # get the workspace
        api_response = api_instance.get_workspace(workspace_id)
        print("The response of WorkspacesApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 

### Return type

[**CreateWorkspace201Response**](CreateWorkspace201Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the given workspace |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_images**
> GetWorkspaceImages200Response get_workspace_images(workspace_id)

get workspace images

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.get_workspace_images200_response import GetWorkspaceImages200Response
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID

    try:
        # get workspace images
        api_response = api_instance.get_workspace_images(workspace_id)
        print("The response of WorkspacesApi->get_workspace_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace_images: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 

### Return type

[**GetWorkspaceImages200Response**](GetWorkspaceImages200Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the list of images for the given workspace |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_member**
> GetWorkspaceMember200Response get_workspace_member(workspace_id, member_id)

get workspace member

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.get_workspace_member200_response import GetWorkspaceMember200Response
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    member_id = 'member_id_example' # str | The member ID

    try:
        # get workspace member
        api_response = api_instance.get_workspace_member(workspace_id, member_id)
        print("The response of WorkspacesApi->get_workspace_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **member_id** | **str**| The member ID | 

### Return type

[**GetWorkspaceMember200Response**](GetWorkspaceMember200Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the member details for the given workspace |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_members**
> GetWorkspaceMembers200Response get_workspace_members(workspace_id)

get workspace members

Retrieve a list of members for a specific workspace.

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.get_workspace_members200_response import GetWorkspaceMembers200Response
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID

    try:
        # get workspace members
        api_response = api_instance.get_workspace_members(workspace_id)
        print("The response of WorkspacesApi->get_workspace_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 

### Return type

[**GetWorkspaceMembers200Response**](GetWorkspaceMembers200Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ListWorkspaces200Response list_workspaces()

List workspaces the user has permissions to access

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.list_workspaces200_response import ListWorkspaces200Response
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
    api_instance = workspace_client.WorkspacesApi(api_client)

    try:
        # List workspaces the user has permissions to access
        api_response = api_instance.list_workspaces()
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListWorkspaces200Response**](ListWorkspaces200Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> CreateWorkspace201Response update_workspace(workspace_id, workspace=workspace)

update the workspace

### Example

* Basic Authentication (ApiAuth):
```python
import time
import os
import workspace_client
from workspace_client.models.create_workspace201_response import CreateWorkspace201Response
from workspace_client.models.workspace import Workspace
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
    api_instance = workspace_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | The workspace ID
    workspace = workspace_client.Workspace() # Workspace |  (optional)

    try:
        # update the workspace
        api_response = api_instance.update_workspace(workspace_id, workspace=workspace)
        print("The response of WorkspacesApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The workspace ID | 
 **workspace** | [**Workspace**](Workspace.md)|  | [optional] 

### Return type

[**CreateWorkspace201Response**](CreateWorkspace201Response.md)

### Authorization

[ApiAuth](../README.md#ApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

