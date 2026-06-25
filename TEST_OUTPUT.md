# Test Execution Report

## Environment

* Python: 3.12
* Django: 6.0.6
* Django REST Framework
* Database: SQLite

---

## Automated Test Execution

### Command Executed

```bash
python manage.py test
```

### Terminal Output

```text
Found 8 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 0.044s

OK

Destroying test database for alias 'default'...
```

---

## API Testing

The API endpoint was manually tested using Postman.

**Endpoint**

```http
POST /api/recommend/
```

**Request Body**

```json
{
    "length": 5,
    "width": 5,
    "height": 5,
    "weight": 2
}
```

**Expected Response**

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

---

## Postman Verification

A Postman screenshot demonstrating a successful API request and response has been included in the repository under the `screenshots/` directory.

Example:

```text
screenshots/postman-success.png
```

---

## Result

* All automated unit tests passed successfully.
* API endpoint validated through Postman.
* Recommendation logic verified for valid and invalid scenarios.
