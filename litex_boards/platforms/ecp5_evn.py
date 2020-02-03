# This file is Copyright (c) 2019 Arnaud Durand <arnaud.durand@unifr.ch>
# License: BSD

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("clk12", 0, Pins("A10"), IOStandard("LVCMOS33")),
    ("rst_n", 0, Pins("G2"), IOStandard("LVCMOS33")),

    ("user_led", 0, Pins("A13"), IOStandard("LVCMOS25")),
    ("user_led", 1, Pins("A12"), IOStandard("LVCMOS25")),
    ("user_led", 2, Pins("B19"), IOStandard("LVCMOS25")),
    ("user_led", 3, Pins("A18"), IOStandard("LVCMOS25")),
    ("user_led", 4, Pins("B18"), IOStandard("LVCMOS25")),
    ("user_led", 5, Pins("C17"), IOStandard("LVCMOS25")),
    ("user_led", 6, Pins("A17"), IOStandard("LVCMOS25")),
    ("user_led", 7, Pins("B17"), IOStandard("LVCMOS25")),

    ("user_dip_btn", 1, Pins("J1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 2, Pins("H1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 3, Pins("K1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 4, Pins("E15"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 5, Pins("D16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 6, Pins("B16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 7, Pins("C16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 8, Pins("A16"), IOStandard("LVCMOS25")),

    ("serial", 0,
        Subsignal("rx", Pins("P2"), IOStandard("LVCMOS33")),
        Subsignal("tx", Pins("P3"), IOStandard("LVCMOS33")),
    ),

    ("clk200", 0,
        Subsignal("p", Pins("Y19")),
        Subsignal("n", Pins("W20")),
        IOStandard("LVDS")
    ),
    ("ext_clk50", 0, Pins("B11"), IOStandard("LVCMOS33")),
    ("ext_clk50_en", 0, Pins("C11"), IOStandard("LVCMOS33")),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    ("RASP",
        "None",  # (no pin 0)
        "None",  #  1 3.3V
        "None",  #  2 5V
        "T17",   #  3 RASP_IO02
        "None",  #  4 5V
        "U16",   #  5 RASP_IO03
        "None",  #  6 GND
        "U17",   #  7 RASP_IO04
        "P18",   #  8 RASP_IO14
        "None",  #  9 GND
        "N20",   # 10 RASP_IO15
        "N19",   # 11 RASP_IO17
        "T16",   # 12 RASP_IO18
        "M18",   # 13 RASP_IO27
        "None",  # 14 GND
        "N17",   # 15 RASP_IO22
        "P17",   # 16 RASP_IO23
        "None",  # 17 3.3V
        "M17",   # 18 RASP_IO24
        "U20",   # 19 RASP_IO10
        "None",  # 20 GND
        "T19",   # 21 RASP_IO09
        "N18",   # 22 RASP_IO25
        "R20",   # 23 RASP_IO11
        "U19",   # 24 RASP_IO08
        "None",  # 25 GND
        "R18",   # 26 RASP_IO07
        "L18",   # 27 RASP_ID_SD
        "L17",   # 28 RASP_ID_SC
        "U18",   # 29 RASP_IO05
        "None",  # 30 GND
        "T18",   # 31 RASP_IO06
        "T20",   # 32 RASP_IO12
        "P20",   # 33 RASP_IO13
        "None",  # 34 GND
        "R17",   # 35 RASP_IO19
        "P19",   # 36 RASP_IO16
        "N16",   # 37 RASP_IO26
        "P16",   # 38 RASP_IO20
        "None",  # 39 GND
        "R16",   # 40 RASP_IO21
    ),

    ("PMOD",
        "None",  # (no pin 0)
        "C6",    #  1
        "C7",    #  2
        "E8",    #  3
        "D8",    #  4
        "None",  #  5 GND
        "None",  #  6 VCCIO0
        "C8",    #  7 EXPCON_IO32
        "B8",    #  8 EXPCON_IO33
        "A7",    #  9 EXPCON_IO34
        "A8",    # 10 EXPCON_IO35
        "None",  # 11 GND
        "None",  # 12 VCCIO0
    ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name = "clk12"
    default_clk_period = 1e9/12e6

    def __init__(self, **kwargs):
        LatticePlatform.__init__(self, "LFE5UM5G-85F-8BG381", _io, _connectors, **kwargs)

    def request(self, *args, **kwargs):
        if "serial" in args:
            print("R22 and R23 should be removed, two 0 Ω resistors shoud be "
            "populated on R34 and R35 and the FT2232H should be configured to "
            "UART with virtual COM on port B")
        if "ext_clk50" in args:
            print("an oscillator must be populated on X5")

        return LatticePlatform.request(self, *args, **kwargs)

    def create_programmer(self):
        pass
        # fdir = os.path.join(
        #     os.path.abspath(os.path.dirname(__file__)), "prog")
        # return OpenOCD(os.path.join(fdir, "ecp5-evn.cfg"))