# MembershipAcceptRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_org_id** | **str** | The ID of the organization that is joining. | [optional] 
**invite_code** | **str** | The invitation code for joining the organization. | [optional] 
**action** | **str** | The action to take (accept or decline). | [optional] 

## Example

```python
from workspace_client.models.membership_accept_request import MembershipAcceptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipAcceptRequest from a JSON string
membership_accept_request_instance = MembershipAcceptRequest.from_json(json)
# print the JSON string representation of the object
print MembershipAcceptRequest.to_json()

# convert the object into a dict
membership_accept_request_dict = membership_accept_request_instance.to_dict()
# create an instance of MembershipAcceptRequest from a dict
membership_accept_request_form_dict = membership_accept_request.from_dict(membership_accept_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


