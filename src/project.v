/*
*/
`default_nettype none

module tt_um_acrypticcode (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
  maindivider divmod (
    .clk(clk),
    .enable(ena),
    .reset(!rst_n),
    .divider_setting(divider_input),
    .divout(divider_value)
  );

  mainsqrs sqrsmod (
    .clk(divider_value),
    .reset(!rst_n),
    .counter(counter_value),
    .perfout(sqrs_output)
  );

  mainexp3 exp3mod (
    .clk(divider_value),
    .reset(!rst_n),
    .counter(counter_value),
    .expout(exp3_output)
  );
  
  maintri trimod (
    .clk(divider_value),
    .reset(!rst_n),
    .counter(counter_value),
    .triout(tri_output)
  );
  
  mainfib fibmod (
    .clk(divider_value),
    .reset(!rst_n),
    .fibout(fib_output)
  );
  
  mainpell pellmod (
    .clk(divider_value),
    .reset(!rst_n),
    .pellout(pell_output)
  );
  
  mainluc lucmod (
    .clk(divider_value),
    .reset(!rst_n),
    .lucout(luc_output)
  );

  mainpad padmod (
    .clk(divider_value),
    .reset(!rst_n),
    .padout(pad_output)
  );

  mainsylv sylvmod (
    .clk(divider_value),
    .reset(!rst_n),
    .sylvout(sylv_output)
  );
  
  maincounter counter_inst (
    .clk(divider_value),
    .reset(!rst_n),
    .countout(counter_value)
  );
  
  reg [7:0] sqrs_output, exp3_output, tri_output, fib_output, pell_output, luc_output, pad_output, sylv_output, counter_value,divider_input;
  reg reset_signal, divider_value;

  
  // All output pins must be assigned. If not used, assign to 0.
  assign divider_input[3:0] = ui_in[6:3];
  assign divider_input[7:4] = 4'b0000;
  assign reset_signal = !rst_n;
  //assign uio_out = 0;
  assign uio_oe  = 255;//arbitrary decision-pins will not beused for either input or output

  assign uio_out = 0;

  assign uo_out = 
    (ui_in[2:0] == 3'b000) ? sqrs_output :
    (ui_in[2:0] == 3'b001) ? exp3_output :
    (ui_in[2:0] == 3'b010) ? tri_output :
    (ui_in[2:0] == 3'b011) ? fib_output :
    (ui_in[2:0] == 3'b100) ? pell_output :
    (ui_in[2:0] == 3'b101) ? luc_output :
    (ui_in[2:0] == 3'b110) ? pad_output :
  sylv_output;
  
endmodule


module maindivider(
  input wire clk,
  input wire enable,
  input wire reset,
  input [7:0] divider_setting,
  output reg divout //failed when using wire but consider changing back and fixing
);
  reg [23:0] count;
  reg [23:0] divider_period;

  assign divider_period =
    (divider_setting[3:0] == 4'b0000) ? 1:
    (divider_setting[3:0] == 4'b0001) ? 2:
    (divider_setting[3:0] == 4'b0010) ? 5:
    (divider_setting[3:0] == 4'b0011) ? 10:
    (divider_setting[3:0] == 4'b0100) ? 20:
    (divider_setting[3:0] == 4'b0101) ? 50:
    (divider_setting[3:0] == 4'b0110) ? 100:
    (divider_setting[3:0] == 4'b0111) ? 200:
    (divider_setting[3:0] == 4'b1000) ? 500:
    (divider_setting[3:0] == 4'b1001) ? 1000:
    (divider_setting[3:0] == 4'b1010) ? 2000:
    (divider_setting[3:0] == 4'b1011) ? 5000:
    (divider_setting[3:0] == 4'b1100) ? 10000:
    (divider_setting[3:0] == 4'b1101) ? 20000:
    (divider_setting[3:0] == 4'b1110) ? 50000:
  100000;

  always@(posedge clk) begin
    if (enable) begin
      count <= count + 1;
      if (count==divider_period-1) begin
        count <= 0;
        divout <= !divout;
      end
    end
    if (reset) begin
      divout <= 0;
      count <= 0;
    end
  end
endmodule

module mainsqrs(
  input wire clk,
  input wire reset,
  input [7:0] counter,
  output reg [7:0] perfout
);
  always@(posedge clk or posedge reset) begin
    
    if (reset) begin
      perfout <= 8'b00000000;
    end
    else begin
      perfout <= counter*counter;
    end
  end
endmodule

module mainexp3(
  input wire clk,
  input wire reset,
  input [7:0] counter,
  output reg [7:0] expout
);
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      expout <= 8'b00000001;
    end
    else begin
      expout <= expout*3;
    end
  end
endmodule

module maintri(
  input wire clk,
  input wire reset,
  input [7:0] counter,
  output reg [7:0] triout
);
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      triout <= 8'b00000000;
    end
    else begin
      triout <= triout+counter;
    end
  end
endmodule


module mainfib(
  input wire clk,
  input wire reset,
  output reg [7:0] fibout
);
  reg [7:0] nextout;    
  always@(posedge clk or posedge reset) begin  
    if (reset) begin
      nextout <= 8'b00000001;
      fibout <= 8'b00000001;
    end
    else begin
      nextout <= nextout+fibout;
      fibout <= nextout;
    end
  end
endmodule


module mainpell(
  input wire clk,
  input wire reset,
  output reg [7:0] pellout
);  
  reg [7:0] nextout;
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      nextout <= 8'b00000001;
      pellout <= 8'b00000000;
    end
    else begin
      nextout <= 2*nextout+pellout;
      pellout <= nextout;
    end
  end
endmodule


module mainluc(
  input wire clk,
  input wire reset,
  output reg [7:0] lucout
);
  reg [7:0] nextout;
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      nextout <= 8'b00000001;
      lucout <= 8'b00000010;
    end 
    else begin
      nextout <= nextout+lucout;
      lucout <= nextout;
    end
  end  
endmodule


module mainpad(
  input wire clk,
  input wire reset,
  output reg [7:0] padout
);
  reg [7:0] next2;
  reg [7:0] next1;
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      next2 <= 8'b00000001;
      next1 <= 8'b00000001;
      padout <= 8'b00000001;
    end
    else begin
      next2 <= next1 + padout;
      next1 <= next2;
      padout <= next1;
    end
  end
endmodule


module mainsylv( 
  input wire clk,
  input wire reset,
  output reg [7:0] sylvout
);
  reg [7:0] nextout;
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      sylvout <= 8'b00000010;
      nextout <= 8'b00000011;
    end
    else begin
      nextout <= nextout*(nextout-1)+1;
      sylvout <= nextout;
    end
  end
endmodule


module maincounter(
  input wire clk,
  input wire reset,
  output reg [7:0] countout
);
  always@(posedge clk or posedge reset) begin
    if (reset) begin
      countout <= 8'b00000001;
    end
    else begin
      countout <= countout+8'b00000001;
    end
  end  
endmodule