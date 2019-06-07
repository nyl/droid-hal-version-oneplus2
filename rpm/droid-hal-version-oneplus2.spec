# rpm_device is in 99% cases $DEVICE
%define rpm_device oneplus2
# rpm_vendor is in 99% cases $VENDOR
%define rpm_vendor oneplus
# Manufacturer and device name to be shown in UI
%define vendor_pretty OnePlus
%define device_pretty Two
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
