[main]
mixinsdir: device/intel/mixins/groups

[mapping]
product.mk: device.mk

[groups]
android_ia: default
sepolicy: permissive
graphics: android_ia(gen9+=true,hwc2=true,vulkan=true,drmhwc=false,minigbm=true)
media: android_ia
device-type: tablet
ethernet: dhcp
debugfs: default
storage: default
display-density: default
usb-gadget: g_ffs
adb_net: true
kernel: android_ia
bluetooth: btusb
boot-arch: android_ia
audio: android_ia
wlan: iwlwifi
cpu-arch: skl
cpuset: 4cores
rfkill: true(force_disable=)
dexpreopt: enabled
disk-bus: auto
usb: host+acc
lights: true
config-partition: enabled
