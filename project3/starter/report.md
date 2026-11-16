Aqeel Hussain
Professor Wu
ET-721
November 15, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

When I initially tested the application, the test coverage was 53%. I added more tests and additional code to 'app/models.py' and 'app/routes.py', which helped increase the test coverage from 53% to 100%. This showed a major improvement compared to my initial results. I ended up with 31 tests in total, and all of them passed successfully.

## Untested Code: Effects

Before I added more tests, I took the time to make sure I fully understood all the features and different use cases of the application. Some of the functions and API routes were not covered in the initial testing, so I had to make sure they would work successfully in different situations. Testing the API manually was not bad, but it was also time-consuming because I had to send requests and check the responses myself without overlooking anything. Having only a few tests limited my understanding of how the API worked. Once I added more tests, I gained a better understanding of the API, including its routes, expected responses, validation rules, and possible errors.

## Adding Tests

I added more tests by examining the initial code to identify which functions and API routes needed additional testing. I expanded the model tests to cover fruit creation, invalid names, negative quantities, non-integer quantities, average quantities, the most common fruit, and expiration dates. I also added search tests for fruit names, varieties, seasons, minimum quantities, maximum quantities, and searches that return no results. For API testing, I added tests for retrieving, updating, deleting, and searching for fruits, including situations where a fruit could not be found. I also tested the new expiration-date functionality. A unit test checks an individual function or method separately, while an API test checks whether an API endpoint responds correctly to an HTTP request.

## Automation

Automated testing made the testing process much easier and faster. Instead of having to manually check every function and API endpoint, I could simply run pytest on the application. I used Coverage.py to check how much of the code was executed by the tests and identify which areas needed more testing. I also generated an HTML coverage report to examine the results in more detail. My final coverage report showed 100% coverage for both 'app/models.py' and 'app/routes.py', with zero missed statements out of 113 statements.

## New Features

I added a new feature that allows the application to track fruit expiration dates and identify expired fruits. In 'app/models.py', I added an 'expiration_date' field and an 'is_expired()' method to determine whether a fruit has passed its expiration date. In 'app/routes.py', I added a new API endpoint, '/api/fruits/expired', which returns a list of expired fruits. I also updated the fruit creation route to accept an expiration date. I wrote additional tests to verify that expiration dates are saved correctly, that expired fruits are returned, and that the endpoint returns an empty list when no fruits have expired. These tests helped me confirm that the new feature worked as expected without breaking the existing functionality.

## Future

Writing tests is an important part of software development because it helps developers find errors, understand the code, and improve an application's reliability. I hope to become more comfortable with writing unit tests and API tests before and after implementing new features. In future projects, I would like to continue using automated testing and code coverage tools to catch problems earlier, reduce manual testing, and make sure new changes do not negatively affect existing features.