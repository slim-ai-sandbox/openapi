# BasicAPIReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | [optional] 
**success** | **bool** | true on success | 

## Example

```python
from workspace_client.models.basic_api_reply import BasicAPIReply

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAPIReply from a JSON string
basic_api_reply_instance = BasicAPIReply.from_json(json)
# print the JSON string representation of the object
print BasicAPIReply.to_json()

# convert the object into a dict
basic_api_reply_dict = basic_api_reply_instance.to_dict()
# create an instance of BasicAPIReply from a dict
basic_api_reply_form_dict = basic_api_reply.from_dict(basic_api_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


