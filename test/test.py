import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    print("hello world!")
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
    [(1, 0), (2, 1), (3, 4), (4, 9), (5, 16)],#(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0)], #last ones don't have expected values
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
    clock_settings = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
    for n in range (1,5):
        print(f"******* n = {n}*******")
        for i in range(0, 7):
            print(f"-----i = {i}-----")
            dut.ui_in.value = 8*n+i
            #await ClockCycles(dut.clk,1)
            dut.rst_n.value = 0
            await ClockCycles(dut.clk, 100)
            dut.rst_n.value=1
            previous_term = 0
            for j, (term, expected) in enumerate(expected_values[i]):
                if j==0:
                    clock_cycles = (term - previous_term)*clock_settings[n] #doubled because of clock divider
                else:
                    clock_cycles = 2*(term - previous_term)*clock_settings[n] #doubled because of clock divider
                for q in range(clock_cycles):
                    await ClockCycles(dut.clk, 1)
                    actual=dut.uo_out.value
                    print(f"Term: {term}, Expected: {expected}, Actual: {actual}")
                    assert expected==actual
                previous_term = term
                #await ClockCycles(dut.clk, clock_cycles) #moved from above

    dut.ena.value = 0
    for n in range (1,5):
        print(f"******* n = {n}*******")
        for i in range(0, 7):
            print(f"-----i = {i}-----")
            dut.ui_in.value = 8*n+i
            #await ClockCycles(dut.clk,1)
            dut.rst_n.value = 0
            await ClockCycles(dut.clk, 100)
            dut.rst_n.value=1
            previous_term = 0
            for j, (term, expected) in enumerate(expected_values[i]):
                if j==0:
                    clock_cycles = (term - previous_term)*clock_settings[n] #doubled because of clock divider
                else:
                    clock_cycles = 2*(term - previous_term)*clock_settings[n] #doubled because of clock divider
                for q in range(clock_cycles):
                    await ClockCycles(dut.clk, 1)
                    actual=dut.uo_out.value
                    expected = expected_values[i][0][1]
                    print(f"Term: {term}, Expected: {expected}, Actual: {actual}")
                    assert expected==actual
                previous_term = term