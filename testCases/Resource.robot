*** Settings ***
Documentation     Resource file containing all the keyword definition from the TestSuite file.
...               This file integrates robot testcases and the python API for FlexSwitch.

Library           ../lib/curlCmdtester.py
Variables         config.py    
 
*** Keywords ***
Execute Curl Command
    [Arguments]    ${Device}    ${objURL}    ${reqMethod}    ${payload}    ${ExpectedResponse} 
    ${result}=    Run Keyword    curlCmdTester    ${Device}    ${objURL}    ${reqMethod}    ${payload}    ${ExpectedResponse}    
    Run Keyword If    ${result}==True    Log    Configuration Successful
    ...    ELSE    FAIL    Configuration Failed

# INTERFACE 

INTF_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC1_objURL}    ${TC1_reqMethod}    ${TC1_payload}    ${TC1_ExpectedResponse}    
    
INTF_TC2
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC2_objURL}    ${TC2_reqMethod}    ${TC2_payload}    ${TC2_ExpectedResponse}     
    
INTF_TC3
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC3_objURL}    ${TC3_reqMethod}    ${TC3_payload}    ${TC3_ExpectedResponse}     
    
INTF_TC4
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC4_objURL}    ${TC4_reqMethod}    ${TC4_payload}    ${TC4_ExpectedResponse}     
    
INTF_TC5
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC5_objURL}    ${TC5_reqMethod}    ${TC5_payload}    ${TC5_ExpectedResponse}      
    
INTF_TC6
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${TC6_objURL}    ${TC6_reqMethod}    ${TC6_payload}    ${TC6_ExpectedResponse}          
    
INTF_TC7
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC7_objURL}    ${TC7_reqMethod}    ${TC7_payload}    ${TC7_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC8
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC8_objURL}    ${TC8_reqMethod}    ${TC8_payload}    ${TC8_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC9
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC9_objURL}    ${TC9_reqMethod}    ${TC9_payload}    ${TC9_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC10
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC10_objURL}    ${TC10_reqMethod}    ${TC10_payload}    ${TC10_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC11
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC11_objURL}    ${TC11_reqMethod}    ${TC11_payload}    ${TC11_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC12
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC12_objURL}    ${TC12_reqMethod}    ${TC12_payload}    ${TC12_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC13
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC13_objURL}    ${TC13_reqMethod}    ${TC13_payload}    ${TC13_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
    
INTF_TC14
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC14_objURL}    ${TC14_reqMethod}    ${TC14_payload}    ${TC14_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist          
   
INTF_TC15
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC15_objURL}    ${TC15_reqMethod}    ${TC15_payload}    ${TC15_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist    
    
INTF_TC16
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${TC16_objURL}    ${TC16_reqMethod}    ${TC16_payload}    ${TC16_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist    
   
# ARP
ARP_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${ARP1_objURL}    ${ARP1_reqMethod}    ${ARP1_payload}    ${ARP1_ExpectedResponse}
     
ARP_TC2
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${ARP2_objURL}    ${ARP2_reqMethod}    ${ARP2_payload}    ${ARP2_ExpectedResponse}    
    

#LLDP
LLDP_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP1_objURL}    ${LLDP1_reqMethod}    ${LLDP1_payload}    ${LLDP1_ExpectedResponse}    

LLDP_TC2
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP2_objURL}    ${LLDP2_reqMethod}    ${LLDP2_payload}    ${LLDP2_ExpectedResponse}    
	
LLDP_TC3
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP3_objURL}    ${LLDP3_reqMethod}    ${LLDP3_payload}    ${LLDP3_ExpectedResponse}    
	
LLDP_TC4
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP4_objURL}    ${LLDP4_reqMethod}    ${LLDP4_payload}    ${LLDP4_ExpectedResponse}    
	
LLDP_TC5
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP5_objURL}    ${LLDP5_reqMethod}    ${LLDP5_payload}    ${LLDP5_ExpectedResponse}    
	
LLDP_TC6
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LLDP6_objURL}    ${LLDP6_reqMethod}    ${LLDP6_payload}    ${LLDP6_ExpectedResponse}    

# Loopback
LO_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${LO1_objURL}    ${LO1_reqMethod}    ${LO1_payload}    ${LO1_ExpectedResponse}    

LO_TC2
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${LO2_objURL}    ${LO2_reqMethod}    ${LO2_payload}    ${LO2_ExpectedResponse}   
    Run Keyword If    ${result}==False    Log    Loopback has been deleted
    ...    ELSE    FAIL    Object does not exist

# VLAN
VLAN_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${VLAN1_objURL}    ${VLAN1_reqMethod}    ${VLAN1_payload}    ${VLAN1_ExpectedResponse}  

VLAN_TC2
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${VLAN2_objURL}    ${VLAN2_reqMethod}    ${VLAN2_payload}    ${VLAN2_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    VLAN has been deleted
    ...    ELSE    FAIL    Object does not exist


# BGP CONFIGURATION ######################################################

BGP_TC1
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP1_objURL}    ${BGP1_reqMethod}    ${BGP1_payload}    ${BGP1_ExpectedResponse}    
    
BGP_TC2
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT2}    ${BGP2_objURL}    ${BGP2_reqMethod}    ${BGP2_payload}    ${BGP2_ExpectedResponse}    
    
BGP_TC3
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP3_objURL}    ${BGP3_reqMethod}    ${BGP3_payload}    ${BGP3_ExpectedResponse}    
    
BGP_TC4
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT2}    ${BGP4_objURL}    ${BGP4_reqMethod}    ${BGP4_payload}    ${BGP4_ExpectedResponse}    
   
BGP_TC5
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP5_objURL}    ${BGP5_reqMethod}    ${BGP5_payload}    ${BGP5_ExpectedResponse}    
   
BGP_TC6
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP6_objURL}    ${BGP6_reqMethod}    ${BGP6_payload}    ${BGP6_ExpectedResponse}    
    
BGP_TC7
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP7_objURL}    ${BGP7_reqMethod}    ${BGP7_payload}    ${BGP7_ExpectedResponse}    
    
BGP_TC8
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${BGP8_objURL}    ${BGP8_reqMethod}    ${BGP8_payload}    ${BGP8_ExpectedResponse}
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist     
        
    
BGP_TC9
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP9_objURL}    ${BGP9_reqMethod}    ${BGP9_payload}    ${BGP9_ExpectedResponse}    
    
BGP_TC10
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT2}    ${BGP10_objURL}    ${BGP10_reqMethod}    ${BGP10_payload}    ${BGP10_ExpectedResponse}    
    
BGP_TC11
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP11_objURL}    ${BGP11_reqMethod}    ${BGP11_payload}    ${BGP11_ExpectedResponse}    
    
BGP_TC12
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP12_objURL}    ${BGP12_reqMethod}    ${BGP12_payload}    ${BGP12_ExpectedResponse}    
    
BGP_TC13
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP13_objURL}    ${BGP13_reqMethod}    ${BGP13_payload}    ${BGP13_ExpectedResponse}    
    
BGP_TC14
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP14_objURL}    ${BGP14_reqMethod}    ${BGP14_payload}    ${BGP14_ExpectedResponse}    
   
BGP_TC15
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP15_objURL}    ${BGP15_reqMethod}    ${BGP15_payload}    ${BGP15_ExpectedResponse}    
    
BGP_TC16
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP16_objURL}    ${BGP16_reqMethod}    ${BGP16_payload}    ${BGP16_ExpectedResponse}    
    
BGP_TC17
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP17_objURL}    ${BGP17_reqMethod}    ${BGP17_payload}    ${BGP17_ExpectedResponse}    
    
BGP_TC18
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP18_objURL}    ${BGP18_reqMethod}    ${BGP18_payload}    ${BGP18_ExpectedResponse}    
    
BGP_TC19
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP19_objURL}    ${BGP19_reqMethod}    ${BGP19_payload}    ${BGP19_ExpectedResponse}    
    
BGP_TC20
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${BGP20_objURL}    ${BGP20_reqMethod}    ${BGP20_payload}    ${BGP20_ExpectedResponse}
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist      
    
BGP_TC21
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${BGP21_objURL}    ${BGP21_reqMethod}    ${BGP21_payload}    ${BGP21_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist      
    
BGP_TC22
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${BGP22_objURL}    ${BGP22_reqMethod}    ${BGP22_payload}    ${BGP22_ExpectedResponse}
    Run Keyword If    ${result}==False    Log    Found Expected Response
    ...    ELSE    FAIL    Object does not exist      
        
   
BGP_TC23
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${BGP23_objURL}    ${BGP23_reqMethod}    ${BGP23_payload}    ${BGP23_ExpectedResponse}    
   
BGP_TC24
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT2}    ${BGP24_objURL}    ${BGP24_reqMethod}    ${BGP24_payload}    ${BGP24_ExpectedResponse}    
   


#Clean UP ##################################################################


CLEAN_TC1
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${CP1_objURL}    ${CP1_reqMethod}    ${CP1_payload}    ${CP1_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist     
    
CLEAN_TC2
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT2}    ${CP2_objURL}    ${CP2_reqMethod}    ${CP2_payload}    ${CP2_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist     
    

CLEAN_TC3
    Run Keyword and continue on Failure    Execute Curl Command    ${DUT1}    ${CP3_objURL}    ${CP3_reqMethod}    ${CP3_payload}    ${CP3_ExpectedResponse}    
    
CLEAN_TC4
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT2}    ${CP4_objURL}    ${CP4_reqMethod}    ${CP4_payload}    ${CP4_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist     
    
CLEAN_TC5
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT1}    ${CP5_objURL}    ${CP5_reqMethod}    ${CP5_payload}    ${CP5_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist     
    
CLEAN_TC6
    ${result}=    Run Keyword and continue on Failure    curlCmdTester    ${DUT2}    ${CP6_objURL}    ${CP6_reqMethod}    ${CP6_payload}    ${CP6_ExpectedResponse}    
    Run Keyword If    ${result}==False    Log    IP Unconfigured
    ...    ELSE    FAIL    Object does not exist     
    






























