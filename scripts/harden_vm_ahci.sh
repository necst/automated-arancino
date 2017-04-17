if [ $# -eq 0 ]
  then
    echo "[*] Please add vm name!"
    echo "[*] Available vms:"
    VBoxManage list vms | awk {' print $1 '} | sed 's/"//g'
    exit
fi 
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSFirmwareMajor  '147'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSFirmwareMinor  '73'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseDate    '10/03/2013'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseMajor   '15'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSReleaseMinor   '53'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVendor 'Insyde'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBIOSVersion    'F.35'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardAssetTag  'Type2 '
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardBoardType '10'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardLocInChass    'Type2 '
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardProduct   'string:1963'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardSerial    '1A48FAFB1F7B4C'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardVendor    'Hewlett-Packard'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiBoardVersion   'KBC Version 93.49'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisAssetTag    '5CG34415JJ'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisSerial  '8BC1E9F33EC04E4BB860F'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisType    '10'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisVendor  'Hewlett-Packard'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiChassisVersion 'Chassis Version'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiOEMVBoxRev 'LOC#yyy'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiOEMVBoxVer 'ABS 70/71 78 79 7A 7B'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiProcManufacturer   'Intel(R) Corporation'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiProcVersion    'Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemFamily   '103C_5335KV G=N L=CON B=HP S=ENV'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemProduct  'HP ENVY 15 Notebook PC'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemSKU  'E4N80EA#ABZ'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemSerial   '33648847AB'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemUuid '64585D57-7B2B-4C9A-9AC4-85BDD664A96F'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemVendor   'Hewlett-Packard'
VBoxManage setextradata "$1" VBoxInternal/Devices/pcbios/0/Config/DmiSystemVersion  'string:0887100000305B00000320100'
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/ModelNumber "Hitachi HTS543232A7A384"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/FirmwareRevision "ES2OA60W"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port0/SerialNumber "2E3024L1T2V9KA"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ModelNumber "Slimtype DVD A  DS8A8SH"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/FirmwareRevision "KAA2"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/SerialNumber "ABCDEF0123456789"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIVendorId "Slimtype"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIProductId "DVD A  DS8A8SH"
VBoxManage setextradata "$1" VBoxInternal/Devices/ahci/0/Config/Port1/ATAPIRevision "KAA2"
# No CD-ROM detected: ** No values to retrieve **
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/CustomTable
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiOemId   'HPQOEM'
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiCreatorId   'ACPI'
VBoxManage setextradata "$1" VBoxInternal/Devices/acpi/0/Config/AcpiCreatorRev  '00040000'
VBoxManage modifyvm "$1" --macaddress1  a0d3c14fd569
