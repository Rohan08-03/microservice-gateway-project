# Microservice Gateway Project

API Gateway connecting 3 microservices (Product, User, Health) across VMs using VirtualBox and Nginx.

## Architecture

```
Client
  │
  ▼
vm-gateway (192.168.56.10) ← Nginx API Gateway
  │
  ├── /users      → vm-user-service    (192.168.56.11:3001)
  ├── /products   → vm-product-service (192.168.56.12:3002)
  └── /health     → Returns gateway status directly
```

## Folder Structure

```
microservice-gateway-project/
├── gateway_data/
│   └── nginx_default.conf       # Nginx config for the API Gateway
├── user_data/
│   └── app.py                   # User microservice (port 3001)
├── product_data/
│   └── app.py                   # Product microservice (port 3002)
└── README.md
```

## VM Setup

| VM Name              | IP Address      | Role             |
|----------------------|-----------------|------------------|
| vm-gateway           | 192.168.56.10   | Nginx API Gateway |
| vm-user-service      | 192.168.56.11   | User Service     |
| vm-product-service   | 192.168.56.12   | Product Service  |

All VMs are connected on the same VirtualBox Host-Only network (`192.168.56.x`).

## How to Run

### 1. Start User Service (on vm-user-service)
```bash
python3 user_data/app.py
```

### 2. Start Product Service (on vm-product-service)
```bash
python3 product_data/app.py
```

### 3. Start API Gateway (on vm-gateway)
Copy `gateway_data/nginx_default.conf` to `/etc/nginx/sites-enabled/default`, then:
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Testing

Run these on vm-gateway to verify everything works:

```bash
# Get all products via gateway
curl http://192.168.56.10/products

# Get all users via gateway
curl http://192.168.56.10/users

# Check gateway health
curl http://192.168.56.10/health
```

## Expected Responses

**Products:**
```json
[{"id":1,"name":"Laptop","price":999.99},{"id":2,"name":"Mouse","price":25.5},{"id":3,"name":"Keyboard","price":75.0}]
```

**Users:**
```json
[{"id":1,"name":"Alice","email":"alice@example.com"},{"id":2,"name":"Bob","email":"bob@example.com"},{"id":3,"name":"Charlie","email":"charlie@example.com"}]
```

**Health:**
```json
{"status":"OK","service":"APIGateway"}
```
