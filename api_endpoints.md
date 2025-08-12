# 📡 API Endpoints – Django Webhook Relay Service

Base URL (Local):

https://weebhook-service.onrender.com/api/accounts


## 1. Save Account
**POST** `/save-account/save-account/`

**Request Body (JSON)**
```
{
  "email": "client@example.com",
  "name": "Client App"
}

```
**Response (200 OK)**
```
{
  "account_id": "809b58a5-e1b3-4c2e-af7b-2ca37b495aa1",
  "secret_token": "abc123xyz789"
}

```

## 2. Create Destination
**POST** `/destination/save-destination/`

**Request Body (JSON)**
```
{
  "account": "809b58a5-e1b3-4c2e-af7b-2ca37b495aa1",
  "url": "https://webhook.site/your-destination-id",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  }
}

```

**Response**
```
{
  "message": "Destination saved successfully."
}
```
## 3. Get Destinations for Account

**GET** `/destinations/<account_id>/`
Example:

`GET /destinations/809b58a5-e1b3-4c2e-af7b-2ca37b495aa1/`

**Response**

```
[
  {
    email: "example@gmail.com"
  },
  destination : {
    "url": "https://webhook.site/12345",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    }
  }
]

```

## 4. Incoming Data (Webhook Endpoint)
**POST** `/incoming-data/`

**Headers**

`CL-X-Token: abc123xyz789`

**Request Body (JSON)**
 
```
{
  "event": "user.created",
  "email": "john@example.com"
}

```
**Response**

```
{
  "message": "Data pushed successfully."
}

```

## 5. Delete Account

**DELETE** `/delete-account/<account_id>/`

**Example:**

`DELETE /delete-account/809b58a5-e1b3-4c2e-af7b-2ca37b495aa1/`

**Response**
```
{
  "message": "Account and its destinations deleted successfully."
}

```
