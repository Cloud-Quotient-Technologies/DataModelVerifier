*** Settings ***
Documentation	        A test suite with tests to perform BGP functional tests on DUT
Metadata 		Version          	 1.0
...	         	More Info         	 For more information about Robot Framework see http://robotframework.org
...               	Author            	
...               	Date             	   
...	                Executed At  	         ${HOST}
...		        Test Framework           Robot Framework Python

Resource          	Resource.robot


*** Test Cases ***
Interface Configuration
    INTF_TC1
    INTF_TC2
    INTF_TC3
    INTF_TC4
    INTF_TC5
    INTF_TC6
    INTF_TC7
    INTF_TC8
    INTF_TC9
    INTF_TC10
    INTF_TC11
    INTF_TC12
    INTF_TC13
    INTF_TC14
    INTF_TC15
    INTF_TC16

ARP Configurations
    ARP_TC1
    ARP_TC2

LLDP COnfigs
    LLDP_TC1
    LLDP_TC2
    LLDP_TC3
    LLDP_TC4
    LLDP_TC5
    LLDP_TC6

Loopback Configs
    LO_TC1
    LO_TC2

VLAN Configs
    VLAN_TC1
    VLAN_TC2

BGP Configuration
    BGP_TC1
    BGP_TC2
    BGP_TC3
    BGP_TC4
    BGP_TC5
    BGP_TC6
    BGP_TC7
    BGP_TC8
    BGP_TC9
    BGP_TC10
    BGP_TC11
    BGP_TC12
    BGP_TC13
    BGP_TC14
    BGP_TC15
    BGP_TC16
    BGP_TC17
    BGP_TC18
    BGP_TC19
    BGP_TC20
    BGP_TC21
    BGP_TC22
    BGP_TC23
    BGP_TC24

Clean UP
 
   CLEAN_TC1
   CLEAN_TC2
   CLEAN_TC3
   CLEAN_TC4
   CLEAN_TC5
   CLEAN_TC6
   
