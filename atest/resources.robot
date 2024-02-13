*** Settings ***
Documentation   Helper keywords and variables
Library         Process

*** Keywords ***
Teardown Web Environment
  [Documentation]  Closes all browsers
  Close All Browsers

Setup Web Environment
  [Arguments]  ${BROWSER}  ${URL}
  [Documentation]  Opens a browser with given url
  ${URL}=  Set Variable  ${URL}
  Open Browser  ${URL}  browser=${BROWSER}

Get Random Postfix
  ${postfix}=   Evaluate    str(random.randint(1,10000)).zfill(5)
  RETURN    ${postfix}
