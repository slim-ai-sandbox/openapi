# AddWorkspaceImage201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BasicAPIReply**](BasicAPIReply.md) |  | [optional] 
**data** | [**WorkspaceImage**](WorkspaceImage.md) |  | [optional] 

## Example

```python
from workspace_client.models.add_workspace_image201_response import AddWorkspaceImage201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkspaceImage201Response from a JSON string
add_workspace_image201_response_instance = AddWorkspaceImage201Response.from_json(json)
# print the JSON string representation of the object
print AddWorkspaceImage201Response.to_json()

# convert the object into a dict
add_workspace_image201_response_dict = add_workspace_image201_response_instance.to_dict()
# create an instance of AddWorkspaceImage201Response from a dict
add_workspace_image201_response_form_dict = add_workspace_image201_response.from_dict(add_workspace_image201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


