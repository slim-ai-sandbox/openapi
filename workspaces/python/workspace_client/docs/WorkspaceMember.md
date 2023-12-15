# WorkspaceMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_icon** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_profile** | [**ProfileInfo**](ProfileInfo.md) |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from workspace_client.models.workspace_member import WorkspaceMember

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMember from a JSON string
workspace_member_instance = WorkspaceMember.from_json(json)
# print the JSON string representation of the object
print WorkspaceMember.to_json()

# convert the object into a dict
workspace_member_dict = workspace_member_instance.to_dict()
# create an instance of WorkspaceMember from a dict
workspace_member_form_dict = workspace_member.from_dict(workspace_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


