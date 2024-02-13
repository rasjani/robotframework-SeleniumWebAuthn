*** Settings ***
Documentation   Check if plugin can be loaded
Suite Setup     Generic Suite Setup
Suite Teardown  Generic Suite Teardown
Library         SeleniumLibrary  plugins=${CURDIR}/../src/SeleniumWebAuthn
Resource        resources.robot
Library         Collections

*** Variables ***
${BROWSER}     chrome
${DEFAULT_CONFIG}   /Users/rasjani/src/omat/robotframework-SeleniumWebAuthn/default.json

*** Test Cases ***
Plugin Loads
  Load Webauthn Configs   ${DEFAULT_CONFIG}
  Activate Virtual Authenticator

User inititates registration @ webauthn.ui
  Load Webauthn Configs   ${DEFAULT_CONFIG}
  Activate Virtual Authenticator

  ${user_postfix}=    Get Random Postfix
  ${test_user}=   Set Variable    test_user_${user_postfix}

  Go To           https://webauthn.io
  Input Text      //*[@id="input-email"]    ${test_user}
  Click Element   //*[@id="register-button"]
  Sleep           2 second
  Element Should Be Visible   xpath://div[contains(@class, 'alert-success')]
  Click Element   //*[@id="login-button"]
  Sleep           2 second
  Element Should Not Be Visible   xpath://div[contains(@class, 'alert-danger')]
  Page Should Contain   You're logged in

#User inititates registration @ webauthn.me
#  Go To           https://webauthn.me/
#  Click Element   //*[@id="onetrust-accept-btn-handler"]
#  Sleep           5 seconds
#  Input Text      //input[@class="tutorial-step-1-input"]      test_user_006
#  Sleep           1 second
#  Click Element   //button[text()='Register']
#  Sleep           10 second

*** Keywords ***
Generic Suite Setup
  Setup Web Environment   ${BROWSER}    about:blank

Generic Suite Teardown
  Teardown Web Environment
