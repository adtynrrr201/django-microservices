# Django Microservices

A monolithic Django repository structured for microservices deployment. Contains authentication, order, and payment services, deployed individually via Docker and GitHub Actions.

## Services
- `auth_service`: Port 8001
- `order_service`: Port 8002
- `payment_service`: Port 8003

## Deployment
Automated via GitHub Actions to a Tailscale-connected home server.

### Pipeline
1. **CI**: Tests against PostgreSQL 16.
2. **CD**: Builds and pushes Docker images to Docker Hub (`aditya101001/<service>`).
3. **Deploy**: Connects via Tailscale and pulls/runs updated containers on the server.

## Local Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d db
python manage.py migrate
python manage.py runserver
```
