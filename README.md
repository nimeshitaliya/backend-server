## Backend: 

Here we are using the `flask` server as a backend server which following includes APIs.

1. `GET /` -> { "healthcheck": "ok" }
2. `GET /page/message` -> { "message": "hola" }

## CI/CD

- [GitHub Actions](./.github)
- Trigger on `push` request on this branch
- Runes on `GitHub-hosted` runner
- Steps performed by GitHub Actions workflow
1. Clone the latest repo
2. docker build
3. docker tag
4. docker push (on `nitaliya/api-server:master` public docker registry)

## Note: 
### Enhancement
- Use private docker registry - this need docker login on ec2 instance and GitHub runner
- Push two image on registry `latest`, and `master-v*`
- The `self-hosted` runner run GitHub actions
- Write GitHub actions to `lint` and `test` change on push or pull-request
