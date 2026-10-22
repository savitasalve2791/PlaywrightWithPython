test_cases = {
    "TC001": {
        "tcid": "TC001",
        "tcname": "Verify Login with valid credentials",
        "steps": [
            "Open login page",
            "Enter valid username",
            "Enter valid password",
            "Click Login button"
        ],
        "expected_result": "User should be logged in successfully",
        "actual_result": "User logged in successfully",
        "result": "Pass"
    },

    "TC002": {
        "tcid": "TC002",
        "tcname": "Verify Login with invalid password",
        "steps": [
            "Open login page",
            "Enter valid username",
            "Enter invalid password",
            "Click Login button"
        ],
        "expected_result": "Error message should be displayed",
        "actual_result": "Error message displayed",
        "result": "Pass"
    },

    "TC003": {
        "tcid": "TC003",
        "tcname": "Verify Login with empty password",
        "steps": [
            "Open login page",
            "Enter valid username",
            "Leave password empty",
            "Click Login button"
        ],
        "expected_result": "Password required message should be displayed",
        "actual_result": "Password required message displayed",
        "result": "Pass"
    },

    "TC004": {
        "tcid": "TC004",
        "tcname": "Verify Forgot Password",
        "steps": [
            "Open login page",
            "Click Forgot Password"
        ],
        "expected_result": "Forgot password page should open",
        "actual_result": "Forgot password page opened",
        "result": "Fail"
    }
}

#count the number of Testcases
count=len(test_cases)
print(count)
#count total pass cases
pass_count=sum(1 for tc in test_cases.values()
               if tc["result"]=="Pass") #1 for tc -this part is usually for every testcases produce no.
Fail_count=sum(1 for tc in test_cases.values()
               if tc["result"]=="Fail")
print("Total number if cases-->",len(test_cases))
print("total number of pass cases-->",pass_count)
print("total number of fail cases-->",Fail_count)