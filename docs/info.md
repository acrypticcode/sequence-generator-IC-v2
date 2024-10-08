<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project allows the user to select between eight possible modular integer sequences. The available options are the Sylvester, Padovan, Pell, Lucas, and Fibbonacci sequences as well as the perfect squares, the powers of three, and the triangular numbers. The user selects one of these sequences at a time using ui_in[2:0]. The user also selects a clock divider setting correspoding to the desired speed that they want the IC to generate terms of the sequence. The speed varies from 1 term per second to 50,000 terms per second and is set using ui_in[6:3]. Toggle reset to high and back to low to restart the current sequence at its 1st term, and switch enable to low to pause the generator at its current term until enable is set back to high. 



## How to test

If you do not have access to a logic analyzer or other equipment capable of measuring output pin signals that change frequently, keep the clock divider pins ui_in[6:3] set to a value near the maximum so that the output will be at a sufficiently low frequency to be measured. For a simple test, use ui_in[6:3] to select a term of the sequence and check to see whether the first several terms generated by the IC match the mathematically correct values of the sequence terms. Continue this process for larger terms and different sequences until you are satisfied that their values are correct. Press the reset button after testing each sequence and ensure that the IC restarts at the first term. Use the enable button to pause and restart the chip several times during the test.

Of course, more thorough tests than the one described can be designed for this device. Feel free to check out my test bench in GitHub.

## External hardware

All that is needed is controls and displays to set the inputs and read the outputs.
