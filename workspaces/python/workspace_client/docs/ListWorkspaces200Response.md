# ListWorkspaces200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BasicAPIReply**](BasicAPIReply.md) |  | [optional] 
**count** | **int** | count of data records | [optional] 
**cursor** | [**Cursor**](Cursor.md) |  | [optional] 
**data** | [**List[Workspace]**](Workspace.md) |  | [optional] 

## Example

```python
from workspace_client.models.list_workspaces200_response import ListWorkspaces200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspaces200Response from a JSON string
list_workspaces200_response_instance = ListWorkspaces200Response.from_json(json)
# print the JSON string representation of the object
print ListWorkspaces200Response.to_json()

# convert the object into a dict
list_workspaces200_response_dict = list_workspaces200_response_instance.to_dict()
# create an instance of ListWorkspaces200Response from a dict
list_workspaces200_response_form_dict = list_workspaces200_response.from_dict(list_workspaces200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


