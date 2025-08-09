# Django Webhook Relay Service

A Django-based webhook relay service that securely receives incoming webhook data and forwards it to one or more destinations configured for an account.  
Each account is assigned a unique secret token (`CL-X-TOKEN`) to authenticate incoming webhook requests.  
Destinations include their own URLs, HTTP methods, and custom headers, and are automatically deleted when the associated account is deleted.

---

## 📌 Features
- Account creation with unique secret token
- Destination management (linked to accounts)
- Secure incoming data endpoint with `CL-X-TOKEN` authentication
- Forwarding webhook data to multiple destinations per account
- Cascading deletion of destinations when an account is deleted
- Simple, token-based authentication for webhook senders

---

## 📦 Tech Stack
- Django REST Framework
- Requests library for HTTP forwarding

---

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
https://github.com/Mhd-Asjad/django-webhook-relay-service.git
cd django-webhook-relay-service
```
