# Software-Testing-Test-Driven-Development
Test Driven Development

Description
For this assignment you will utilize TDD to implement the following specification:

check_pwd accepts a string and returns a boolean: True if it meets the criteria listed below, otherwise it returns False:

Must be between 8 and 20 characters (inclusive)
Must contain at least one lowercase letter
Must contain at least one uppercase letter
Must contain at least one digit
Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste to avoid missing characters) These are the only permitted symbols
You may assume that only strings will be sent to the check_pwd.

This should look familiar, it is the specification we used in Week 5's Random Testing Exploration. The difference is that you now have to use
TDD to create this function.

You may be thinking, "Couldn't we just copy what you wrote in the examples?" The answer is no. First, it doesn't work 100% correctly. Second, 
for this assignment you will have to show your work.

To accomplish this, you will be using a private GitHub repo to maintain a change log for each step of the TDD process. I have provided the 
TDD steps below in case you forgot.

TDD Steps
Write a test
Run all currently written tests
If the tests all pass, return to Step 1
If a test fails, proceed to Step 3
Write the bare minimum of code to make the test pass
Run all the currently written tests
If tests all pass, return to Step 1
If the failing test is still failing, return to Step 3
Occasionally evaluate if the code can be refactored to reduce duplication or eliminate no longer used parts of the code
Eventually stop development after adding "enough" tests without triggering a new failure
You are required to follow these steps when writing your code. You will need to maintain a file with the code you are writing and a 
file that houses your tests. If you write large chunks of the implementation at once or more than a single test at a time, you will 
lose points. You will create a new commit each time you do either of the following:

Write a failing test
Implement code to cause a failing test to pass
Each commit requires a message describing the changes. The message for each type of commit is as follows:

Name of the test you wrote and a brief description of what part of the specification you are testing
Briefly describe the changes you made to the code and if it caused the test to pass
Sample Workflow
Read specification
Write first test and run it to ensure it fails
Commit changes, "Wrote test1 to see if an empty string is rejected correctly"
Write the bare minimum implementation to get the test to pass
Run test to see if it passes
Commit changes, "Made check_pwd return False no matter what, it passed"
Write second test...
Please note, you need to commit your changes after writing a test, but BEFORE you write the code to make it pass. You then need to
commit your changes BEFORE writing another test. So, write test and commit, then write implementation and commit.

It is very important you follow these steps carefully as we will be checking your commit history to see that you adhered to the TDD process.

In order to submit this assignment, you will need to host your work on a private GitHub repo. You will also need to ensure that you 
have coeCS362 added as a collaborator on the repo. Failure to do this will result in your assignment not receiving a grade.
