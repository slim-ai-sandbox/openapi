# MembershipAcceptReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the membership acceptance. | [optional] 

## Example

```python
from workspace_client.models.membership_accept_reply import MembershipAcceptReply

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipAcceptReply from a JSON string
membership_accept_reply_instance = MembershipAcceptReply.from_json(json)
# print the JSON string representation of the object
print MembershipAcceptReply.to_json()

# convert the object into a dict
membership_accept_reply_dict = membership_accept_reply_instance.to_dict()
# create an instance of MembershipAcceptReply from a dict
membership_accept_reply_form_dict = membership_accept_reply.from_dict(membership_accept_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


