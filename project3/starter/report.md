Aqeel Hussain
Professor Wu
ET-721
November 15, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

When I initially did the test, the initial test coverage was 53%. I added more tests and additional code to 'app/models.py' and 'app/routes.py', which helped to increase the test coverage from 53% to 100%, showcasing a major improvement from my initial results. I ended up with 26 tests total, and all of them passed successfully.

## Untested Code: Effects

Before I added more tests, I took the time to make sure I fully understood all the features and different use cases of the application. Some of the functions and API routes were not covered in the initial testing, so I had to make sure they would work successfully in different situations. Testing the API manually was not bad, but it was also time-consuming as I had to send requests and check the responses myself without overlooking anything. Having only a few tests limited my understanding of how the API worked. Once I added more tests, I gained a better understanding of the API, including its routes, expected responses, validation rules, and possible errors.

## Adding Tests

I added more tests by examining the initial code to identify which functions and API routes needed additional testing. I expanded the model tests to cover fruit creation, invalid names, negative quantities, non-integer quantities, average quantities, and the most common fruit. I then added search tests for fruit names, varieties, seasons, minimum quantities, maximum quantities, and searches that return no results. For API testing, I added tests for retrieving, updating, deleting, and searching for fruits, including situations where a fruit could not be found. A unit test checks an individual function or method separately, while an API test checks whether an API endpoint responds correctly to an HTTP request.

## Automation

Automated test coverage made the testing process much easier and faster. Instead of having to manually check every function and API endpoint, I could simply run pytest on the application. I used Coverage.py to check how much of the code was executed by the tests and identify which areas needed more testing. I also created an HTML coverage report to examine the results in more detail.

## New Features

Working with the baseline code and testing different parts of the application helped me understand the process of gradually making changes. When adding or improving features, you need to make sure that the existing functionality still works correctly. Having tests provided a greater sense of security because I could check whether my changes caused any problems. It also encouraged me to focus more on testing throughout the development process rather than rushing everything at the last minute.

## Future

Writing tests is an important part of software development because it helps developers find errors, understand the code, and improve an application's reliability. I hope to become more comfortable with writing unit tests and API tests before and after implementing new features.