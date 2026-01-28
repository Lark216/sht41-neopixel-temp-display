# Wiring Guide

This project uses I2C for the SHT41 sensor and one digital pin for the NeoPixel data line.

## SHT41 (I2C)
Typical connections:
- VIN → 3V (or 5V if your board supports it; check your SHT41 breakout)
- GND → GND
- SDA → SDA
- SCL → SCL

## NeoPixel Strip (GRBW)
- DIN → `D5` (default, change `PIXEL_PIN` in `code.py` if needed)
- GND → GND (common ground is required)
- V+ → appropriate power for your strip (often 5V)

## Power notes
- NeoPixels can draw significant current at high brightness.
- This project defaults to low brightness (`0.03`) to reduce power issues.
- If using an external 5V supply for the strip, tie strip GND to board GND.
