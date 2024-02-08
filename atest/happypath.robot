*** Settings ***
Documentation   Check if plugin can be loaded
Suite Setup     Generic Suite Setup
Suite Teardown  Generic Suite Teardown
Library         SeleniumLibrary  plugins=${CURDIR}/../src/SeleniumWebAuthn
Resource        resources.robot
Library         Collections

*** Variables ***
${URL}          https://webauthn.io/
${BROWSER}      headlesschrome

*** Test Cases ***
Happy Path
  Log To Console    Before Keyword
  Initial Webauthn Keyword
  Log To Console    After

*** Keywords ***
Generic Suite Setup
  Setup Web Environment   ${BROWSER}    ${URL}

Generic Suite Teardown
  Teardown Web Environment

