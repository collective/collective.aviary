*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Test cases ***

Test Aviary photo editor
    Enable Autologin as  Site Administrator
    Go To  ${PLONE_URL}/image/view

    # clicking on Transform must load the Aviary photo editor
    Click Link  Transform
    Wait Until Page Contains Element  id=avpw_holder
    Page Should Contain  Photo Editor

    # breadcrumbs, edit bar and footer should still be visible
    Element Should Be Visible  id=portal-breadcrumbs
    Element Should Be Visible  id=edit-bar
    Element Should Be Visible  id=portal-footer

    # TODO: test that portlet columns are hidden on Transform view
