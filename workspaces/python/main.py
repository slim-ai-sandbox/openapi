import os

import workspace_client
from workspace_client.exceptions import ApiException as ApiException

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiAuth
configuration = workspace_client.Configuration(
    host="https://platform.slim.dev",
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with workspace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_client.WorkspacesApi(api_client)
    api_instance.api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = 'CERT_NONE'
    api_instance.api_client.rest_client.pool_manager.connection_pool_kw['assert_hostname'] = False

    try:
        # Create a new workspace
        api_response = api_instance.list_workspaces()
        print("The response of WorkspacesApi->list_workspaces ", api_response.count, "\n")

        # Create a new workspace
        create_ws_req = workspace_client.CreateWorkspaceRequest(name="test-workspace")
        workspace = api_instance.create_workspace(create_ws_req)
        print("The response of WorkspacesApi->create_workspace ", workspace.data.name, "id: ", workspace.data.id, "\n")
        workspace = api_instance.update_workspace(workspace.data.id,
                                                  workspace_client.UpdateWorkspaceRequest(name="test-workspace-2"))
        print("The response of WorkspacesApi->update_workspace ", workspace.data.name, "id: ", workspace.data.id, "\n")
        api_instance.delete_workspace(workspace.data.id)
    except ApiException as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
