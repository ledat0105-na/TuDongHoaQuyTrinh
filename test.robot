*** Settings ***
Library          SeleniumLibrary

*** Variables ***
${URL}          https://the-internet.herokuapp.com/login
${BROWSER}      chrome

${VALID_USER}   tomsmith
${VALID_PASS}   SuperSecretPassword!

${INVALID_USER}  abcxyz
${INVALID_PASS}  123456

*** Test Cases ***
Login Successfully
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Title Should Be    The Internet

    Input Text    id=username    ${VALID_USER}
    Input Text    id=password    ${VALID_PASS}

    Click Button    css=button.radius

    Page Should Contain    You logged into a secure area!

    Sleep    3s
    Close Browser


Login Failed
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Title Should Be    The Internet

    Input Text    id=username    ${INVALID_USER}
    Input Text    id=password    ${INVALID_PASS}

    Click Button    css=button.radius
    Page Should Contain    Your username is invalid!

    Sleep    3s
    Close Browser