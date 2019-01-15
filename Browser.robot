*** Settings ***
Library         browserInteraction.Browser

*** Test Cases ***
Chrome Browser Launch
    launchChrome  ${None}
Maximize The Browser
    maximizeBrowser
Enter The URl
    enterURL
Get The Title
    getTitle
Reload The Page
    reloadPage
Do Clicks
    clickElement
Get All The Details
    getOtherDetails
Close Or Quit The Browser
    closeTheBrowser
