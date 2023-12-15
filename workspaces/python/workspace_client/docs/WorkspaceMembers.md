# WorkspaceMembers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**members** | [**List[WorkspaceMember]**](WorkspaceMember.md) |  | [optional] 

## Example

```python
from workspace_client.models.workspace_members import WorkspaceMembers

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembers from a JSON string
workspace_members_instance = WorkspaceMembers.from_json(json)
# print the JSON string representation of the object
print WorkspaceMembers.to_json()

# convert the object into a dict
workspace_members_dict = workspace_members_instance.to_dict()
# create an instance of WorkspaceMembers from a dict
workspace_members_form_dict = workspace_members.from_dict(workspace_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


