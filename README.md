## Build Status

GitHub Actions Status [![Build and Deploy](https://github.com/o2-edyou/edyouapp-api/actions/workflows/ci.yml/badge.svg)](https://github.com/o2-edyou/edyouapp-api/actions/workflows/ci.yml)

ArgoCD Prod App Status [![ArgoCD Prod App Status](https://argocd.do.hassnat.com/api/badge?name=edyou-prod-apps)](https://argocd.internal.edyou.io/applications)

ArgoCD Dev App Status [![ArgoCD Dev App Status](https://argocd.do.hassnat.com/api/badge?name=edyou-dev-apps)]([https://argocd.do.hassnat.com/applications/edyou-dev-apps](https://argocd.internal.edyou.io/applications))

----

# EDYOU Microservices Setup

To set up and run the EDYOU Microservices, please ensure you have the required software installed and follow the provided instructions.

## Prerequisites

- [Python (version 3.11 or above)](https://www.python.org/downloads/)
- [direnv](https://direnv.net/docs/installation.html)
- [docker]()
- [Rye](https://rye.astral.sh/)

### Recommended

- [PyCharm IDE](https://www.jetbrains.com/pycharm/download)


## Technologies Used

- Most services are built using Python's FastAPI.
- MongoDB serves as the database.
- Kafka is employed for Pub/Sub and as a message queue system.
- Redis (planned) for caching, storing token states, and more.
- Docker for containerizing the local development environment.

## Development Setup
```bash
rye sync
rye run devserver
```

### Essential: Pre-commit Installation

Before you start working on the project and commit your code, ensure you have `pre-commit` installed.

```bash
brew install pre-commit
pre-commit install # Installs the pre-commit hooks in your local git repo. Run this at the project root.
pre-commit install --hook-type commit-msg
pre-commit run --all-files
```

### Running with docker

```bash
docker-compose up -d
```

Visit [http://localhost:8090/social](http://localhost:8080/auth) to access the Swagger documentation for the API.

## Author

@Hassnat Ahmad

---
