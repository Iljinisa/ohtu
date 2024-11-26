*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallo  kalle12356
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle2828282
    Input New Command  
    Input Credentials  kalle  kalle2828282
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle2828282
    Output Should Contain  Username must be at least 3 characters long and contain only lowercase letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kall__  kalle2828282
    Output Should Contain  Username must be at least 3 characters long and contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  kallo  ka8
    Output Should Contain  Password must be at least 8 characters long and contain at least one non-letter character


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallo  kasdsduduewc
    Output Should Contain  Password must be at least 8 characters long and contain at least one non-letter character




