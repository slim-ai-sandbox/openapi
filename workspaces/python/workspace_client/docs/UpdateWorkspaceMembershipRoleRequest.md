# UpdateWorkspaceMembershipRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_org_id** | **str** | The ID of the selected organization. | [optional] 
**role** | **str** | The new role for the workspace membership. | [optional] 

## Example

```python
from workspace_client.models.update_workspace_membership_role_request import UpdateWorkspaceMembershipRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceMembershipRoleRequest from a JSON string
update_workspace_membership_role_request_instance = UpdateWorkspaceMembershipRoleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateWorkspaceMembershipRoleRequest.to_json()

# convert the object into a dict
update_workspace_membership_role_request_dict = update_workspace_membership_role_request_instance.to_dict()
# create an instance of UpdateWorkspaceMembershipRoleRequest from a dict
update_workspace_membership_role_request_form_dict = update_workspace_membership_role_request.from_dict(update_workspace_membership_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


