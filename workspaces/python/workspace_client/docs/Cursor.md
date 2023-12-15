# Cursor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **str** | cursor value for the previous page | [optional] 
**next** | **str** | cursor value for the next page | [optional] 

## Example

```python
from workspace_client.models.cursor import Cursor

# TODO update the JSON string below
json = "{}"
# create an instance of Cursor from a JSON string
cursor_instance = Cursor.from_json(json)
# print the JSON string representation of the object
print Cursor.to_json()

# convert the object into a dict
cursor_dict = cursor_instance.to_dict()
# create an instance of Cursor from a dict
cursor_form_dict = cursor.from_dict(cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


