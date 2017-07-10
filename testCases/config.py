
#Global Variables
Protocol = "http"
Port = "8080"
DUT1 = "172.17.0.5"
DUT1_Intfref1 = "fpPort11"
DUT1_Intfref2 = "fpPort12"
DUT2 = "172.17.0.4"
DUT2_Intfref1 = "fpPort21"
DUT2_Intfref2 = "fpPort22"
Username = None
Password = None

#TestCase Specific Parameters

#INTERFACE
TC1_reqMethod = "POST"
TC1_objURL = "public/v1/config/IPv4Intf"
TC1_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""%DUT1_Intfref1        #Valid values passed
TC1_ExpectedResponse = """Success"""

TC2_reqMethod = "POST"
TC2_objURL = "public/v1/config/IPv4Intf"
TC2_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""%DUT1_Intfref1
TC2_ExpectedResponse = """Error: Already configured. Delete and Update operations are allowed."""  #Trying to configure IP on interface that is already configured

TC3_reqMethod = "PATCH"
TC3_objURL = "public/v1/config/IPv4Intf"
TC3_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.1/24"}"""%DUT1_Intfref1
TC3_ExpectedResponse = """Error: Nothing to be updated."""                                         #Trying to update with same values

TC4_reqMethod = "PATCH"
TC4_objURL = "public/v1/config/IPv4Intf"
TC4_payload = """{"IntfRef":"%s","IpAddr":"10.0.0.2/24","AdminState":"UP"}"""%DUT1_Intfref1       #Trying to update with different values
TC4_ExpectedResponse = "Success"

TC5_reqMethod = "PATCH"
TC5_objURL = "public/v1/config/IPv4Intf"
TC5_payload = """{"IntfRef":"%s","IpAddr":"10.0.0.2/24","AdminState":"DOWN"}"""%DUT1_Intfref1     #Trying to update the default value, for instance value of "AdminState" from "UP" to "DOWN"
TC5_ExpectedResponse = "Success"

TC6_reqMethod = "PATCH"
TC6_objURL = "public/v1/config/IPv4Intf"
TC6_payload = """{"IntfRef":"%s","IpAddr":"10.0.0.2/24","AdminState":"UP"}"""%DUT1_Intfref1       #Updating again to a default value 
TC6_ExpectedResponse = "Success"

TC7_reqMethod = "PATCH"
TC7_objURL = "public/v1/config/IPv4Intf"
TC7_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2"}"""%DUT1_Intfref1           #Missing Subnet mask
TC7_ExpectedResponse = """Internal error processing CreateIPv4Intf: ip address validation failed, as ip address: 10.0.0.1 is network/broadcast ip address\n"""

TC8_reqMethod = "PATCH"
TC8_objURL = "public/v1/config/IPv4Intf"
TC8_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.256/24"}"""%DUT1_Intfref1      #Invalid IP address
TC8_ExpectedResponse = """Internal error processing UpdateIPv4Intf: During ipv4 operation, ipv6 address: 10.0.0.256/24 is not allowed """

TC9_reqMethod = "PATCH"
TC9_objURL = "public/v1/config/IPv4Intf"
TC9_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2/33"}"""%DUT1_Intfref1         #Invalid Subnet mask
TC9_ExpectedResponse = """Internal error processing UpdateIPv4Intf: During ipv4 operation, ipv6 address: 10.0.0.2/33 is not allowed """

TC10_reqMethod = "POST"
TC10_objURL = "public/v1/config/IPv4Intf"
TC10_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""%DUT2_Intfref1         #Invalid Intfref while creating
TC10_ExpectedResponse = "Internal error processing CreateIPv4Intf: Invalid interface reference provided in ip intf config object: %s\n"%DUT2_Intfref1

TC11_reqMethod = "PATCH"
TC11_objURL = "public/v1/config/IPv4Intf"
TC11_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""%DUT2_Intfref1         #Invalid Intfref while updating 
TC11_ExpectedResponse = "Error: Failed to find entry."

TC12_reqMethod = "POST"
TC12_objURL = "public/v1/config/IPv4Intf"
TC12_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2\24"}"""%DUT1_Intfref1         #Invalid Slash while creating
TC12_ExpectedResponse = """Error: Failed to get object handle. invalid character '\\x14' in string literal"""

TC13_reqMethod = "POST"
TC13_objURL = "public/v1/config/IPv4Intf"
TC13_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2\24"}"""%DUT1_Intfref1         #Invalid Slash while updating
TC13_ExpectedResponse = """Error: Failed to get object handle. invalid character '\\x14' in string literal"""

TC14_reqMethod = "POST"
TC14_objURL = "public/v1/config/IPv4Intf"
TC14_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"10.0.0.2/24"}"""%DUT1_Intfref2        #Configuring 2nd interface of the same router in same network as that of first interface
TC14_ExpectedResponse = """Internal error processing CreateIPv4Intf: Failed to create ipv4 intf, matching ipv4 intf already exists"""

TC15_reqMethod = "DELETE"                                                                           
TC15_objURL = "public/v1/config/IPv4Intf"
TC15_payload = """{"IntfRef":"%s"}"""%DUT1_Intfref1                                                 #Deleting the valid interface
TC15_ExpectedResponse = "Success"

TC16_reqMethod = "DELETE"
TC16_objURL = "public/v1/config/IPv4Intf"
TC16_payload = """{"IntfRef":"%s"}"""%DUT1_Intfref1                                                 #Re-Deleting the interface
TC16_ExpectedResponse = "Error: Failed to find entry."


#VLAN Configuration Parameters
VLAN1_reqMethod = "POST"
VLAN1_objURL = "public/v1/config/Vlan"
VLAN1_payload = """{"VlanId":300,"AdminState":"UP","Description":"This is for testing","AutoState":"UP", "IntfList":["%s","%s"]}"""%(DUT1_Intfref1,DUT1_Intfref2)
VLAN1_ExpectedResponse = "Success"


VLAN2_reqMethod = "DELETE"
VLAN2_objURL = "public/v1/config/Vlan"
VLAN2_payload = """{"VlanId":300}"""
VLAN2_ExpectedResponse = "Success"

#ARP Configurtion parameters
ARP1_reqMethod = "PATCH"
ARP1_objURL = "public/v1/config/ArpGlobal"
ARP1_payload = """{"Vrf":"default", "Timeout":600}"""
ARP1_ExpectedResponse = "Error: Failed to find entry."


ARP2_reqMethod = "PATCH"
ARP2_objURL = "public/v1/config/ArpGlobal"
ARP2_payload = """{"Vrf":"default", "Timeout":600}"""
ARP2_ExpectedResponse = "Success"


#LLDP Configurtion parameters

LLDP1_reqMethod = "PATCH"
LLDP1_objURL = "public/v1/config/LLDPIntf"
LLDP1_payload = """{"IntfRef":"%s", "TxRxMode":"TxRx","Enable": false }"""%DUT1_Intfref1
LLDP1_ExpectedResponse = "Success"

LLDP2_reqMethod = "PATCH"
LLDP2_objURL = "public/v1/config/LLDPIntf"
LLDP2_payload = """{"IntfRef":"%s", "TxRxMode":"TxOnly","Enable": false }"""%DUT1_Intfref1
LLDP2_ExpectedResponse = "Success"

LLDP3_reqMethod = "PATCH"
LLDP3_objURL = "public/v1/config/LLDPIntf"
LLDP3_payload = """{"IntfRef":"%s", "TxRxMode":"RxOnly","Enable": false }"""%DUT1_Intfref1
LLDP3_ExpectedResponse = "Success"

LLDP4_reqMethod = "PATCH"
LLDP4_objURL = "public/v1/config/LLDPGlobal"
LLDP4_payload = """{"Vrf":"default", "TranmitInterval":30, "TxRxMode":"TxOnly", "Enable":false, "SnoopAndDrop":false}"""
LLDP4_ExpectedResponse = "Success"

LLDP5_reqMethod = "PATCH"
LLDP5_objURL = "public/v1/config/LLDPGlobal"
LLDP5_payload = """{"Vrf":"default", "TranmitInterval":30, "TxRxMode":"RxOnly", "Enable":false, "SnoopAndDrop":false}"""
LLDP5_ExpectedResponse = "Success"

LLDP6_reqMethod = "PATCH"
LLDP6_objURL = "public/v1/config/LLDPGlobal"
LLDP6_payload = """{"Vrf":"default", "TranmitInterval":30, "TxRxMode":"TxRx", "Enable":false, "SnoopAndDrop":false}"""
LLDP6_ExpectedResponse = "Success"

#Create Loopback
LO1_reqMethod = "POST"
LO1_objURL = "public/v1/config/LogicalIntf"
LO1_payload = """{"Name":"lo1", "Type":"Loopback"}"""
LO1_ExpectedResponse = "Success"

LO2_reqMethod = "DELETE"
LO2_objURL = "public/v1/config/LogicalIntf"
LO2_payload = """{"Name":"lo1"}"""
LO2_ExpectedResponse = "Success"

#BGP Configurtion parameters

#For interface configuration
BGP1_reqMethod = "POST"
BGP1_objURL = "public/v1/config/IPv4Intf"
BGP1_payload = """{"IntfRef":"%s","AdminState":"UP","IpAddr":"192.168.0.1/24"}"""%DUT1_Intfref1             #Configure IP on first device-----DUT1
BGP1_ExpectedResponse = "Success"

BGP2_reqMethod = "POST"
BGP2_objURL = "public/v1/config/IPv4Intf"
BGP2_payload = """{"IntfRef":"s%","AdminState":"UP","IpAddr":"192.168.0.2/24"}"""%DUT2_Intfref1             #Configure IP on first device-----DUT2
BGP2_ExpectedResponse = "Success"

#For BGP Global
BGP3_reqMethod = "PATCH"
BGP3_objURL = "public/v1/config/BGPGlobal"
BGP3_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":false}"""                          #Enable BGP Global on DUT1
BGP3_ExpectedResponse = "Success"

BGP4_reqMethod = "PATCH"
BGP4_objURL = "public/v1/config/BGPGlobal"
BGP4_payload = """{"ASNum":"201","RouterId":"2.2.2.2","Disabled":false}"""                          #Enable BGP Global on DUT2
BGP4_ExpectedResponse = "Success"

BGP5_reqMethod = "PATCH"
BGP5_objURL = "public/v1/config/BGPGlobal"
BGP5_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":false}"""                          #Trying to update with already existing values
BGP5_ExpectedResponse = "Error: Nothing to be updated."

BGP6_reqMethod = "PATCH"
BGP6_objURL = "public/v1/config/BGPGlobal"
BGP6_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":true}"""                           #Trying to update with different values
BGP6_ExpectedResponse = "Success"

BGP7_reqMethod = "PATCH"
BGP7_objURL = "public/v1/config/BGPGlobal"
BGP7_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":false}"""                          #Trying to update values
BGP7_ExpectedResponse = "Success"

BGP8_reqMethod = "PATCH"
BGP8_objURL = "public/v1/config/BGPGlobal"
BGP8_payload = """{"ASNum":"201","RouterId":"2.2.2"}"""                                             #Invalid RouterID
BGP8_ExpectedResponse = "Internal error processing UpdateBGPGlobal: BGPGlobal: Router id 1.1.1.1 is not valid"

#For BGP Neighbor === EBGP

BGP9_reqMethod = "POST"
BGP9_objURL = "public/v1/config/BGPv4Neighbor"
BGP9_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1         #Configuring Neighbors on DUT1
BGP9_ExpectedResponse = "Success"

BGP10_reqMethod = "POST"
BGP10_objURL = "public/v1/config/BGPv4Neighbor"
BGP10_payload = """{"PeerAS":"200","NeighborAddress":"192.168.0.1","IntfRef":"%s"}"""%DUT2_Intfref1         #Configuring Neighbors on DUT2
BGP10_ExpectedResponse = "Success"

BGP11_reqMethod = "POST"
BGP11_objURL = "public/v1/config/BGPv4Neighbor"
BGP11_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1          #Trying to configure neighbor that is already configured
BGP11_ExpectedResponse = "Error: Already configured. Delete and Update operations are allowed."

BGP12_reqMethod = "PATCH"
BGP12_objURL = "public/v1/config/BGPv4Neighbor"
BGP12_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1          #Trying to update with already existing values
BGP12_ExpectedResponse = "Error: Nothing to be updated."

BGP13_reqMethod = "PATCH"
BGP13_objURL = "public/v1/config/BGPv4Neighbor"
BGP13_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.3","IntfRef":"%s"}"""%DUT1_Intfref1           #Updating different values
BGP13_ExpectedResponse = "Success"

BGP14_reqMethod = "PATCH"
BGP14_objURL = "public/v1/config/BGPv4Neighbor"
BGP14_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":false}"""%DUT1_Intfref1   #updating using same default values
BGP14_ExpectedResponse = "Error: Nothing to be updated."

BGP15_reqMethod = "PATCH"
BGP15_objURL = "public/v1/config/BGPv4Neighbor"
BGP15_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":true}"""%DUT1_Intfref1    #updating
BGP15_ExpectedResponse = "Success"

BGP16_reqMethod = "PATCH"
BGP16_objURL = "public/v1/config/BGPv4Neighbor"
BGP16_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":false}"""%DUT1_Intfref1    #Updating again to  default value
BGP16_ExpectedResponse = "Success"

BGP17_reqMethod = "PATCH"
BGP17_objURL = "public/v1/config/BGPv4Neighbor"
BGP17_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":false,"MaxPrefixesThresholdPct":80}"""%DUT1_Intfref1
BGP17_ExpectedResponse = "Error: Nothing to be updated."

BGP18_reqMethod = "PATCH"
BGP18_objURL = "public/v1/config/BGPv4Neighbor"
BGP18_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":false,"MaxPrefixesThresholdPct":100}"""%DUT1_Intfref1      #Max = 80
BGP18_ExpectedResponse = "Error"

BGP19_reqMethod = "PATCH"
BGP19_objURL = "public/v1/config/BGPv4Neighbor"
BGP19_payload = """{"PeerAS":"201","NeighborAddress":"192.168.0.2","IntfRef":"%s","Disabled":false,"MaxPrefixesThresholdPct":60}"""%DUT1_Intfref1  
BGP19_ExpectedResponse = "Success"

BGP20_reqMethod = "DELETE"
BGP20_objURL = "public/v1/config/BGPv4Neighbor"
BGP20_payload = """{"NeighborAddress":"192.168.0.3","IntfRef":"%s"}"""%DUT1_Intfref1                          #Trying to delete an entry that is not existing
BGP20_ExpectedResponse = "Error: Failed to find entry."

BGP21_reqMethod = "DELETE"
BGP21_objURL = "public/v1/config/BGPv4Neighbor"
BGP21_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1                         #Trying to delete an entry
BGP21_ExpectedResponse = "Success"

BGP22_reqMethod = "DELETE"
BGP22_objURL = "public/v1/config/BGPv4Neighbor"
BGP22_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1                          #Trying to Re-Delete an entry
BGP22_ExpectedResponse = "Error: Failed to find entry."


BGP23_reqMethod = "PATCH"
BGP23_objURL = "public/v1/config/BGPGlobal"
BGP23_payload = """{"ASNum":"201","RouterId":"1.1.1.1","Disabled":true}"""
BGP23_ExpectedResponse = "Success" 

BGP24_reqMethod = "PATCH"
BGP24_objURL = "public/v1/config/BGPGlobal"
BGP24_payload = """{"ASNum":"201","RouterId":"2.2.2.2","Disabled":true}"""
BGP24_ExpectedResponse = "Success"

#Clean up parameters
CP1_reqMethod = "DELETE"
CP1_objURL = "public/v1/config/IPv4Intf"
CP1_payload = """{"IntfRef":"%s"}"""%DUT1_Intfref1
CP1_ExpectedResponse = "Success"

CP2_reqMethod = "DELETE"
CP2_objURL = "public/v1/config/IPv4Intf"
CP2_payload = """{"IntfRef":"%s"}"""%DUT2_Intfref1
CP2_ExpectedResponse = "Success"

CP3_reqMethod = "PATCH"
CP3_objURL = "public/v1/config/BGPGlobal"
CP3_payload = """{"ASNum":"200","RouterId":"1.1.1.1","Disabled":true}"""
CP3_ExpectedResponse = "Success"

CP4_reqMethod = "PATCH"
CP4_objURL = "public/v1/config/BGPGlobal"
CP4_payload = """{"ASNum":"201","RouterId":"2.2.2.2","Disabled":true}"""
CP4_ExpectedResponse = "Success"

CP5_reqMethod = "DELETE"
CP5_objURL = "public/v1/config/BGPv4Neighbor"
CP5_payload = """{"NeighborAddress":"192.168.0.2","IntfRef":"%s"}"""%DUT1_Intfref1
CP5_ExpectedResponse = "Success"

CP6_reqMethod = "DELETE"
CP6_objURL = "public/v1/config/BGPv4Neighbor"
CP6_payload = """{"NeighborAddress":"192.168.0.1","IntfRef":"%s"}"""%DUT2_Intfref1
CP6_ExpectedResponse = "Success"
