*** Settings ***
Documentation   Check if plugin can be loaded
Suite Setup     Generic Suite Setup
Suite Teardown  Generic Suite Teardown
Library         SeleniumLibrary  plugins=${CURDIR}/../src/SeleniumWebAuthn
Resource        resources.robot
Library         Collections

*** Variables ***
${URL}          http://www.webauthn.io
${BROWSER}      headlesschrome

*** Keywords ***
Generic Suite Setup
  Setup Web Environment   ${BROWSER}    ${URL}

Generic Suite Teardown
  Teardown Web Environment


*** Test Cases ***
Cookies With Firefox
  ${FF}

Cookies With Chrome
  ${GC}
