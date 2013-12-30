*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Test cases ***

Test transform view
    Enable Autologin as  Site Administrator
    Go To  ${PLONE_URL}/image/view
    Click Link  Transform
    Page Should Contain  Photo Editor
    Page Should Contain Element  id=avpw_holder
    Element Should Be Visible  id=edit-bar
    Element Should Be Visible  id=portal-footer-wrapper
