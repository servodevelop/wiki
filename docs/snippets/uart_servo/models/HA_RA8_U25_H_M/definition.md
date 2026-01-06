<!--
Snippet: Bus Servo model definition block
Authoring note:
- Typora won't expand include-markdown directives; MkDocs build will.
- Keep assets next to this snippet so relative paths stay simple.
-->

<!--start:model_intro-->
### Model definition

**HA8/RA8-U25(H)-M** is a high‑torque UART/RS‑485 bus servo with metal gears and absolute position feedback.

![Torque / Speed curve](images/torque_speed_curve.png)

Key points:
- Operating voltage: 6–8.4 V
- Stall torque: 25 kg·cm (example)
- Absolute encoder: 12-bit
<!--end:model_intro-->

<!--start:pinout-->
### Pinout (example)

| Pin | Name | Notes |
|---|---|---|
| 1 | V+ | Power |
| 2 | GND | Ground |
| 3 | DATA | UART/RS-485 |
<!--end:pinout-->
