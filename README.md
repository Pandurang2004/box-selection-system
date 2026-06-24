# AI-Assisted Box Selection System

## Overview

This project is a Django-based REST API that recommends the most suitable shipping box for a product based on its dimensions and weight.

The system evaluates available boxes and selects the most cost-effective box that satisfies both dimension and weight constraints.

This project was developed as part of a Python/Django Developer technical assignment.

---

## Features

* Shipping box recommendation API
* Dimension validation
* Weight capacity validation
* Cost-based box selection
* Django Admin integration
* Automated unit and API tests
* Service-layer architecture

---

## Technology Stack

* Python 3.12
* Django 6.0.6
* Django REST Framework
* SQLite
* Postman (API Testing)

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd box-selection-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## Running the Application

```bash
python manage.py runserver
```

Application URL:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## API Endpoint

### Recommend Box

**Endpoint**

```http
POST /api/recommend/
```

### Sample Request

```json
{
    "length": 5,
    "width": 5,
    "height": 5,
    "weight": 2
}
```

### Sample Response

```json
{
    "recommended_box": "Small Box",
    "cost": "50.00",
    "box_dimensions": {
        "length": 10.0,
        "width": 10.0,
        "height": 10.0
    },
    "max_weight": 5.0
}
```

### No Suitable Box Found

```json
{
    "message": "No suitable box found"
}
```

---

## Testing

Run all tests:

```bash
python manage.py test
```

Test Result:

```text
Found 8 test(s).
........
----------------------------------------------------------------------
Ran 8 tests in 0.044s

OK
```

---

## Design Decisions

### Service Layer

Business logic is separated into a dedicated service class (`BoxRecommendationService`) to improve maintainability and testability.

### Validation

Input validation is handled using Django REST Framework serializers.

### Recommendation Logic

A box is considered valid when:

1. Product dimensions fit within box dimensions.
2. Product weight is less than or equal to the box's maximum weight capacity.

Among all valid boxes, the system selects:

1. The lowest-cost box.
2. If multiple boxes have the same cost, the box with the smallest volume.

---

## Project Structure

```text
box-selection-system/
│
├── box_selection/
├── shipping/
│   ├── tests/
│   │   ├── test_api.py
│   │   └── test_service.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── urls.py
│   └── views.py
│
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
├── requirements.txt
├── db.sqlite3
└── manage.py
```

---

## Author

**Pandurang Sidram Bhosale**

Python/Django Developer Assignment Submission
