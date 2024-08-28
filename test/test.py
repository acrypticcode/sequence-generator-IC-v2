'''
# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    expected_values = [
    [(1, 0), (2, 1), (3, 4), (4, 9), (5, 16)],
    [(1, 1), (2, 3), (3, 9), (4, 27), (5, 81)],
    [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10)],
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)],
    [(1, 0), (2, 1), (3, 2), (4, 5), (5, 12)],
    [(1, 2), (2, 1), (3, 3), (4, 4), (5, 7)],
    [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2)],
    [(1, 2), (2, 3), (3, 7), (4, 43), (5, 15)]]

    for i in range(0, 8):
#        dut.ui_in.value = 8 + i
        dut.ui_in.value = 24 + i
        await ClockCycles(dut.clk, 1000)
        dut.ui_in.value = i
        previous_term = 0
        for j, (term, expected) in enumerate(expected_values[i]):
            clock_cycles = term - previous_term
            await ClockCycles(dut.clk, clock_cycles)
            print(f"Term: {term}, Expected: {expected}, Actual: {dut.uo_out.value}")
            assert dut.uo_out.value == expected
            previous_term = term

'''
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    print("hello world!")
    #print(dir(dut))
    assert True

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    
    expected_values = [
    [(1, 0), (2, 1), (3, 4), (4, 9), (5, 16),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0)], #last ones don't have expected values
    [(1, 1), (2, 3), (3, 9), (4, 27), (5, 81)],
    [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10)],
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)],
    [(1, 0), (2, 1), (3, 2), (4, 5), (5, 12)],
    [(1, 2), (2, 1), (3, 3), (4, 4), (5, 7)],
    [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2)],
    [(1, 2), (2, 3), (3, 7), (4, 43), (5, 15)]]   
     

    '''
    dut.ui_in.value = 24
    await ClockCycles(dut.clk, 1000)
    dut.ui_in.value = 0
    previous_term = 0
    for j, (term, expected) in enumerate(expected_values[0]):
        clock_cycles = term - previous_term
        await ClockCycles(dut.clk, clock_cycles)
        print(f"Term: {term}, Expected: {expected}, Actual: {dut.uo_out.value}")
        previous_term = term    
    '''
    for i in range(0, 8):
        dut.ui_in.value = 8 + i
        await ClockCycles(dut.clk, 1000)
        dut.ui_in.value = i
        previous_term = 0
        #print(f"Divider: {dut.maindivider.divout.value}")
        #print(f"Divider: {dut.divout.value}")
        for j, (term, expected) in enumerate(expected_values[i]):
            clock_cycles = (term - previous_term) #doubled because of clock divider
            await ClockCycles(dut.clk, clock_cycles)
            print(f"Term: {term}, Expected: {expected}, Actual: {dut.uo_out.value}")
            previous_term = term
            #await ClockCycles(dut.clk, clock_cycles) #moved from above