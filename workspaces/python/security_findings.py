import os

import workspace_client
from workspace_client.exceptions import ApiException as ApiException

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiAuth
configuration = workspace_client.Configuration(
    host=os.environ["HOST"],
    # Define the username and password as environment variables.
    # username is usually api.token
    # password is a token that can be generated in the slim UI under Personal Info / Tokens tab
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workspace_client.ApiClient(configuration) as api_client:
    if configuration.host == 0:
        configuration.host = "https://platform.slim.dev"

    # Create an instance of the API class
    api_instance = workspace_client.WorkspacesApi(api_client)
    api_instance.api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = 'CERT_NONE'
    api_instance.api_client.rest_client.pool_manager.connection_pool_kw['assert_hostname'] = False

    try:
        workspaceName = "unit-test"
        workspaceId = None
        # Create a new workspace
        api_response = api_instance.list_workspaces()
        print("The response of WorkspacesApi->list_workspaces ", api_response.count, "\n")
        for workspace in api_response.data:
            if workspace.name == workspaceName:
                workspaceId = workspace.id

        list_vuln_response = api_instance.list_workspace_vulnerabilities(workspaceId)
        vuln = list_vuln_response.data[0]
        print("The response of WorkspacesApi->list_workspace_vulnerabilities ", vuln.id, "\n")
        update_req = workspace_client.UpdateSecurityFindingRequest()
        update_req.status = "investigation"
        api_instance.update_workspace_vulnerability(vuln.workspace_id,
                                                    vuln.workspace_release_id,
                                                    vuln.workspace_release_digest_id,
                                                    vuln.id,
                                                    update_req)

        comment_req = workspace_client.AddSecurityFindingCommentRequest()
        comment_req.comment = "test comment"
        comment_req.thread_name="test thread"
        api_instance.add_comment_to_security_finding(vuln.workspace_id,
                                                     vuln.workspace_release_id,
                                                     vuln.workspace_release_digest_id,
                                                     vuln.id,
                                                     comment_req)

    except ApiException as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
