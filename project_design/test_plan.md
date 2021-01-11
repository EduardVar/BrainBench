# Test Plan
## How test cases of different levels (frontend, backend units, integration) are organized
### R1
#### Kieran is responsible for the text cases for R1
* R1.1 - If the user hasn’t logged in, show the login page
    * Frontend
* R1.2 - The login page has a message that by default says 'please login'
    * Frontend 
* R1.3 - If the user has logged in, redirect to the user profile page
    * Integration 
* R1.4 - The login page provides a login form which requests two fields: email and passwords
    * Frontend
* R1.5 - The login form can be submitted as a POST request to the current URL (/login)
    * Integration
* R1.6.1, 1.6.2, 1.6.3  - Validate that the #email, #password field takes the correct inputs - Cannot be empty
    * Integration
* R1.7.1, 1.7.2 - Validate that the #email field takes the correct inputs - all cases
    * Integration
* R1.8.1, 1.8.2, 1.8.3, 1.8.4 - Validate that the #password field takes the correct inputs - all cases
    * Integration
* R1.9.1, R1.9.2 - Validate that the #password field takes the correct inputs - all cases
    * Integration
* R1.10.1, R1.10.2 - If email/password are correct, redirect to /, Otherwise, redirect to /login and show message 'email/password combination incorrect'
    * Integration

### R2
#### Eduard is responsible for the test cases for R3
* R2.1.1 - If the user has logged in, redirect back to the user profile page
    * Front End
* R2.2.1 - If the user is not logged in, show the user registration page with the correct fields
    * Frontend
* R2.3.1 - Validate the /register page has a #email, #password, #password2, and #name field
    * Integration
* R2.4.1 Validate the registration page #email field accepts valid inputs
    * Backend
* R2.4.2 Validate that an email is not in use
    * Backend
* R2.4.3 Validate that the field #password accepts valid inputs
    * Backend
* R2.4.4 Validate that the field #password2 accepts valid inputs
    * Backend
* R2.4.5 Validate that the #password and #password2 fields receive a matching input
    * Backend
* R2.4.6 Validate that the #name field takes the correct inputs
    * Backend
* R2.5.1 Validate that a user is created properly
    * Integration

### R3
#### Andrew is responsible for the test cases for R3
* R3.1 - If the user is not logged in, redirect to login page
    * Frontend
* R3.2 - This page shows a header ‘Hi {}’.format(user.name)
    * Integration
* R3.3 - This page shows user balance.**
    * Integration
* R3.4 - This page shows a logout link, pointing to /logout
    * Frontend
* R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
    * Integration
* R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
    * Integration
* R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity
    * Frontend
* R3.8 - This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
    * Integration
* R3.9.1 - [post] ticket submitted is received by /sell - positive
    * Backend
* R3.10.1 - [post] ticket submitted is received by /buy - positive
    * Backend
* R3.10.2 - [post] ticket submitted is received by /buy - negative
    * Backend
* R3.11.1 - [post] ticket submitted is received by /update - positive
    * Backend
* R3.11.1 - [post] ticket submitted is received by /update - negative
    * Backend

### R7
#### Andrew is responsible for the test cases in R7
* R7.1 - Test logged out redirect on /
    * Frontend
* R7.2 - Test logged out redirect on /sell
    * Frontend
* R7.3 - Test logged out redirect on /update
    * Frontend
* R7.4 - Test logged out redirect on /buy
    * Frontend

### R8
#### Vivian is responsible for the test cases in R8
* R8.1.1 For any other requests except the ones above, the system should return a 404 error
    * Frontend
* R8.1.2 For /, the system should not return a 404 error
    * Frontend
* R8.1.3 For /login, the system should not return a 404 error
    * Frontend
* R8.1.4 For /register, the system should not return a 404 error
    * Frontend
* R8.1.5 For /logout, the system should not return a 404 error
    * Frontend
* R8.1.6 For /buy, the system should not return a 404 error
    * Frontend
* R8.1.7 For /sell, the system should not return a 404 err
    * Frontend


## The order of the test cases (which level first which level second)
The prirotiy order for test cases will be:
1) Front End
2) Backend
3) Integration

## Techniques and tools used for testing
* Techniques: automated test with qa327_test
* Tools for testing: Github Actions CLI, pytest

## Test environments (all the local environment and the cloud environment) for the testing
* Local environment:Developer Machines
* Cloud environment: Github actions, Github servers

## Responsibility (who is responsible for which test case, and in case of failure, who should you contact)
* In case of failure, contact whoever who “commit”ed the crime

## Budget Management  (how to monitor, keep track and minimize unnecessary cost)
* Repo owner (Kirynn) can check the remaining minutes. Moving forward, will have repo owner check the CI after every big update to a branch (makes sure we’re not overdoing it)
* Minimize unnecessary cost: Run tests locally
