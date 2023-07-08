import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.56.105",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )


netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>MELLA-MEZA-PAILAHUEQUE</hostname>
  </native>
</config>
"""

netconf_reply = m.get_config(source="running", filter=netconf_filter)
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        