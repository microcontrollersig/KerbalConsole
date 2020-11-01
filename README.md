# KerbalConsole

Inspirations for custom control panel.

![Kerbal Console](https://github.com/microcontrollersig/KerbalConsole/raw/main/original.jpg)

![Nicer Kerbal Console](https://github.com/microcontrollersig/KerbalConsole/raw/main/nicekerbalcontroller.jpg)

![Slick Kerbal Console](https://github.com/microcontrollersig/KerbalConsole/raw/main/slick.jpg)

![Modular Kerbal Console](https://github.com/microcontrollersig/KerbalConsole/raw/main/3INZrTm.jpeg)

![Shiny Kerbal Console](https://raw.githubusercontent.com/microcontrollersig/KerbalConsole/main/kspc1000.jpg)

# Parts

[Click here](https://github.com/microcontrollersig/KerbalConsole/tree/main/BOM)

# Design decisions

- hardware construction of console
- number and type of buttons, joystick, sliders etc.
- Arduino/PI/ESP32/ESP866 or combination thereof.

# Interface between micro and PC

#### Kerbal-specific

[KSPSerialIO](https://forum.kerbalspaceprogram.com/index.php?/topic/60281-hardware-plugin-arduino-based-physical-display-serial-port-io-tutorial-24-11-19/)

[KSPEthernetIO](https://forum.kerbalspaceprogram.com/index.php?/topic/191502-ksp-181-kspethernetio-012-android-client-02-beta-ethernet-based-remote-control/)

![KSPEthernetIO Android](https://github.com/microcontrollersig/KerbalConsole/raw/main/kspethernetio.jpg)


#### General

Use a Atmega32U4 device (Arduino Leonardo, Arduino Pro Micro), can act as virtual Gamepad/keyboard/mouse/joystick.

[Details here](https://www.instructables.com/Arduino-LeonardoMicroATMega32u4-As-GamepadGame-Con/)

# Software 


# Links

https://www.instructables.com/KerbalController-a-Custom-Control-Panel-for-Rocket

[DIY Cockpit KSP Controller Hardcore](https://www.youtube.com/watch?v=eBzI0qZArbw)

[KerbalController Gameplay](https://www.youtube.com/watch?v=9oeIzzsnIAE)

[Flight simulator trim wheel](https://www.youtube.com/watch?v=hSsKeeY5NgM&list=PLC66292176B625E2A&index=24)
