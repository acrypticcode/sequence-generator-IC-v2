<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The project allows the user to select between eight possible modular integer sequences. The available options are the Sylvester, Padovan, Pell, Lucas, and Fibbonacci sequences as well as the perfect squares, the powers of three, and the triangular numbers. The user selects one of these sequences at a time using ui_in[2:0]. The user also selects a clock divider setting correspoding to the desired speed that they want the IC to generate terms of the sequence. The speed varies from 1 term per second to 50,000 terms per second and is set using ui_in[6:3]. 

## How to test

Use ui_in bits 0-2 to select which of the eight sequences will be run. 

## External hardware

External hardware is not needed for this project.
