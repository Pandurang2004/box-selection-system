# AI Usage Report

## AI Tool(s) Used
- ChatGPT (OpenAI)

## Purpose of AI Usage
AI assistance was used to:
- Understand the assignment requirements.
- Design the Django project structure.
- Review architecture decisions.
- Suggest implementation approaches for the box recommendation service.
- Suggest test cases and documentation structure.
- Help troubleshoot Django configuration and test execution issues.

## Prompts Used
Examples of prompts used during development:

1. "How should I structure a Django project for a box recommendation system?"
2. "Suggest a service layer implementation for box selection."
3. "How can I test a Django REST API endpoint?"
4. "Suggest unit test cases for a box recommendation algorithm."
5. "Help resolve Django test discovery errors."
6. "Review API design and project structure."

## Accepted Outputs
The following AI suggestions were accepted and implemented after review:
- Separation of business logic into a dedicated service layer.
- Django REST Framework API structure.
- Test case ideas for service and API validation.
- Documentation structure for README and TEST_OUTPUT files.

## Modified or Rejected Outputs
The following suggestions were modified before implementation:
- Response payload structure was customized.
- Test organization was adjusted to fit the final project layout.
- Box recommendation logic was reviewed and refined before use.
- Project-specific naming and implementation details were changed to match assignment requirements.

## Mistakes or Issues Identified
During development, the following issues were identified and corrected:
- Django test discovery conflict caused by test module structure.
- Initial project configuration issues related to environment setup.
- Minor adjustments were required to ensure correct API routing and testing.

## Verification Process
All AI-assisted outputs were manually reviewed and verified by:
1. Reviewing generated code before implementation.
2. Running the Django development server.
3. Testing API endpoints using Postman.
4. Executing automated test cases using Django's test framework.
5. Verifying expected responses and error handling.
6. Refactoring code where necessary.

## Final Validation
The final solution was validated through:
- Manual API testing
- Django Admin verification
- Automated test execution

Test Result:

Found 8 test(s)

........

Ran 8 tests successfully

Status: PASSED

## Conclusion
AI was used as a development assistant for guidance, troubleshooting, and code review support. Final implementation decisions, integration, testing, debugging, and verification were performed manually.