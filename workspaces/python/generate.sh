rm -r -f workspace_client
openapi-generator-cli generate -i ../openapi.yml -g python -o .  -c config.yaml  
rm openapitools.json	
rm workspace_client_README.md

