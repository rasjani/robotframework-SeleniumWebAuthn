*** Settings ***
Documentation   Helper keywords and variables
Library         Process

*** Variables ***
${FF}           Firefox
${GC}           Chrome

*** Keywords ***
Teardown Web Environment
  [Documentation]  Closes all browsers
  Close All Browsers

Setup Web Environment
  [Arguments]  ${BROWSER}  ${URL}
  [Documentation]  Opens a browser with given url
  ${URL}=  Set Variable  ${URL}
  Open Browser  ${URL}  browser=${BROWSER}
