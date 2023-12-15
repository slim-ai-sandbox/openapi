# coding: utf-8

"""
    Slim Workspaces REST API

    This is the Workspace REST API 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkspaceImage(BaseModel):
    """
    WorkspaceImage
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The workspace image ID")
    workspace_id: Optional[StrictStr] = Field(default=None, description="The workspace ID", alias="workspaceID")
    registry: Optional[StrictStr] = Field(default=None, description="The registry of the image")
    repository: Optional[StrictStr] = Field(default=None, description="The repository of the image")
    tag: Optional[StrictStr] = Field(default=None, description="The tag of the image")
    platform: Optional[StrictStr] = Field(default=None, description="The platform of the image")
    digest: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The digest of the image index manifest. ")
    __properties: ClassVar[List[str]] = ["id", "workspaceID", "registry", "repository", "tag", "platform", "digest"]

    @field_validator('digest')
    def digest_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^sha256:[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^sha256:[0-9a-f]{64}$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WorkspaceImage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkspaceImage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "workspaceID": obj.get("workspaceID"),
            "registry": obj.get("registry"),
            "repository": obj.get("repository"),
            "tag": obj.get("tag"),
            "platform": obj.get("platform"),
            "digest": obj.get("digest")
        })
        return _obj


