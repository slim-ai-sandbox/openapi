# ProfileInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**primary_email** | **str** |  | [optional] 
**notifications_email** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**design_partner_email** | **str** |  | [optional] 
**work_email** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**activity** | **str** |  | [optional] 

## Example

```python
from workspace_client.models.profile_info import ProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileInfo from a JSON string
profile_info_instance = ProfileInfo.from_json(json)
# print the JSON string representation of the object
print ProfileInfo.to_json()

# convert the object into a dict
profile_info_dict = profile_info_instance.to_dict()
# create an instance of ProfileInfo from a dict
profile_info_form_dict = profile_info.from_dict(profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


