*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallee
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail With Message   Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  kallee
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Register Credentials
    Register Should Fail With Message   Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle132
    Submit Register Credentials
    Register Should Fail With Message   Password and password confirmation do not match

Login After Successful Registration
    Set Username  kalleb
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Register Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kalleb
    Set Password  kalle1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kb
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail With Message   Username must be at least 3 characters
    Click Link  Login
    Set Username  kb
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Submit Register Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
