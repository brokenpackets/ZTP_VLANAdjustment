from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Device

vlanRangeStart = '4000'
vlanRangeEnd = '4094'

# Check if Device is in ZTP Mode:
if CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_STATE) == 'true':
    device_ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
    device_user = CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_USERNAME)
    device_pass =CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_PASSWORD)
    device = Device(device_ip,device_user,device_pass)
    iflist = device.runCmds(['enable','show interfaces status'])[1]['response']
    vlanOrder = device.runCmds(['enable', 'configure', 'vlan internal order ascending range '+vlanRangeStart+' '+vlanRangeEnd])
    for item in iflist['interfaceStatuses'].keys():
       if item.startswith('Ethernet'):
           device.runCmds(['enable','configure','interface '+item,'shutdown'])
           device.runCmds(['enable','configure','interface '+item,'no shutdown'])
else:
    pass
#end device set-up.
