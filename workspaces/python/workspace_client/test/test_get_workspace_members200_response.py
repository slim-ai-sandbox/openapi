# coding: utf-8

"""
    Slim Workspaces REST API

    This is the Workspace REST API 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from workspace_client.models.get_workspace_members200_response import GetWorkspaceMembers200Response

class TestGetWorkspaceMembers200Response(unittest.TestCase):
    """GetWorkspaceMembers200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetWorkspaceMembers200Response:
        """Test GetWorkspaceMembers200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWorkspaceMembers200Response`
        """
        model = GetWorkspaceMembers200Response()
        if include_optional:
            return GetWorkspaceMembers200Response(
                status = workspace_client.models.basic_api_reply.BasicAPIReply(
                    error = 'something bad happened', 
                    success = True, ),
                cursor = workspace_client.models.cursor.Cursor(
                    prev = 'SG93IG1hbnkgZGV2ZWxvcGVycyBkb2VzIGl0IHRha2UgdG8gc2NyZXcgaW4gYSBsaWdodGJ1bGI=', 
                    next = 'Tm9uZS4gSXRzIGEgaGFyZHdhcmUgcHJvYmxlbS4=', ),
                data = workspace_client.models.workspace_members.WorkspaceMembers(
                    workspace_id = '3d047892-68f1-11ee-8c99-0242ac120002', 
                    name = 'Awesome Containers', 
                    org_id = 'rko.12345678901234567890', 
                    members = [
                        workspace_client.models.workspace_member.WorkspaceMember(
                            workspace_id = '3d047892-68f1-11ee-8c99-0242ac120002', 
                            org_id = 'rko.12345678901234567890', 
                            org_name = 'Contain Co', 
                            org_icon = 'https://cdn.co/containco.png', 
                            account_id = 'rka.12345678901234567890', 
                            account_profile = workspace_client.models.profile_info.ProfileInfo(
                                name = 'John Doe', 
                                primary_email = 'john@containco.com', 
                                notifications_email = 'notifications@containco.com', 
                                job_title = 'CISO', 
                                design_partner_email = 'design@containco.com', 
                                work_email = 'work@containco.com', 
                                organization = 'Container Company', 
                                activity = 'Active', ), 
                            role = 'collaborator', )
                        ], )
            )
        else:
            return GetWorkspaceMembers200Response(
        )
        """

    def testGetWorkspaceMembers200Response(self):
        """Test GetWorkspaceMembers200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
