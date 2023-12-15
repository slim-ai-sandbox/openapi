# GetWorkspaceMembers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BasicAPIReply**](BasicAPIReply.md) |  | [optional] 
**cursor** | [**Cursor**](Cursor.md) |  | [optional] 
**data** | [**WorkspaceMembers**](WorkspaceMembers.md) |  | [optional] 

## Example

```python
from workspace_client.models.get_workspace_members200_response import GetWorkspaceMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceMembers200Response from a JSON string
get_workspace_members200_response_instance = GetWorkspaceMembers200Response.from_json(json)
# print the JSON string representation of the object
print GetWorkspaceMembers200Response.to_json()

# convert the object into a dict
get_workspace_members200_response_dict = get_workspace_members200_response_instance.to_dict()
# create an instance of GetWorkspaceMembers200Response from a dict
get_workspace_members200_response_form_dict = get_workspace_members200_response.from_dict(get_workspace_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


