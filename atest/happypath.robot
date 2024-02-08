*** Settings ***
Documentation   Check if plugin can be loaded
Suite Setup     Generic Suite Setup
Suite Teardown  Generic Suite Teardown
Library         SeleniumLibrary  plugins=${CURDIR}/../src/SeleniumWebAuthn
Resource        resources.robot
Library         Collections

*** Variables ***
${URL}          https://webauthn.io/
#${BROWSER}      headlesschrome
${BROWSER}     chrome

*** Test Cases ***
Plugin Loads
  Initial Webauthn Keyword

User inititates registration
  Go To           ${URL}
  Add Authenticator
  Input Text      //*[@id="input-email"]    test_user_007
  Sleep           1 second
  Click Element   //*[@id="register-button"]
  Sleep           1 second

*** Keywords ***
Generic Suite Setup
  Setup Web Environment   ${BROWSER}    ${URL}

Generic Suite Teardown
  Teardown Web Environment

