*** Settings ***
Resource  resource.robot
Test Setup  Create New User Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kallee  kalle1234
    Output Should Contain  User with username kallee already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password must contain a special character

*** Keywords ***
Create New User Command
    Create User  kallee  kalle123
    Input New Command
