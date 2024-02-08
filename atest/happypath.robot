*** Settings ***
Documentation   Check if plugin can be loaded
Suite Setup     Generic Suite Setup
Suite Teardown  Generic Suite Teardown
Library         SeleniumLibrary  plugins=${CURDIR}/../src/SeleniumWebAuthn
Resource        resources.robot
Library         Collections

*** Variables ***
${URL}          https://www.webauthn.io
${BROWSER}      headlesschrome

*** Keywords ***
Generic Suite Setup
  Setup Web Environment   ${BROWSER}    ${URL}

Generic Suite Teardown
  Teardown Web Environment


*** Test Cases ***
  Log To Console    Hello World
