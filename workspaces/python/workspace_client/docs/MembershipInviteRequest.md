# MembershipInviteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | list of zero or more emails to invite | [optional] 
**expires_at** | **float** | The date and time the invite expires in unix time format.  If not specified, the invite will expire in 7 days.  | [optional] 

## Example

```python
from workspace_client.models.membership_invite_request import MembershipInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInviteRequest from a JSON string
membership_invite_request_instance = MembershipInviteRequest.from_json(json)
# print the JSON string representation of the object
print MembershipInviteRequest.to_json()

# convert the object into a dict
membership_invite_request_dict = membership_invite_request_instance.to_dict()
# create an instance of MembershipInviteRequest from a dict
membership_invite_request_form_dict = membership_invite_request.from_dict(membership_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


