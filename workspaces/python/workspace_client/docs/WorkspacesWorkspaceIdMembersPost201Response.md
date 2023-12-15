# WorkspacesWorkspaceIdMembersPost201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BasicAPIReply**](BasicAPIReply.md) |  | 
**invite_code** | **str** | The code for the invite | 

## Example

```python
from workspace_client.models.workspaces_workspace_id_members_post201_response import WorkspacesWorkspaceIdMembersPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacesWorkspaceIdMembersPost201Response from a JSON string
workspaces_workspace_id_members_post201_response_instance = WorkspacesWorkspaceIdMembersPost201Response.from_json(json)
# print the JSON string representation of the object
print WorkspacesWorkspaceIdMembersPost201Response.to_json()

# convert the object into a dict
workspaces_workspace_id_members_post201_response_dict = workspaces_workspace_id_members_post201_response_instance.to_dict()
# create an instance of WorkspacesWorkspaceIdMembersPost201Response from a dict
workspaces_workspace_id_members_post201_response_form_dict = workspaces_workspace_id_members_post201_response.from_dict(workspaces_workspace_id_members_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


