# WorkspaceImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The workspace image ID | [optional] 
**workspace_id** | **str** | The workspace ID | [optional] 
**registry** | **str** | The registry of the image | [optional] 
**repository** | **str** | The repository of the image | [optional] 
**tag** | **str** | The tag of the image | [optional] 
**platform** | **str** | The platform of the image | [optional] 
**digest** | **str** | The digest of the image index manifest.  | [optional] 

## Example

```python
from workspace_client.models.workspace_image import WorkspaceImage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceImage from a JSON string
workspace_image_instance = WorkspaceImage.from_json(json)
# print the JSON string representation of the object
print WorkspaceImage.to_json()

# convert the object into a dict
workspace_image_dict = workspace_image_instance.to_dict()
# create an instance of WorkspaceImage from a dict
workspace_image_form_dict = workspace_image.from_dict(workspace_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


