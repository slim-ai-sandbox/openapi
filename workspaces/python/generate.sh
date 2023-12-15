rm -r -f workspace_client
openapi-generator-cli generate -i ../../../saas-backend-platform/services/workspace/api/http/v2/openapi.yml -g python -o .  -c config.yaml  

