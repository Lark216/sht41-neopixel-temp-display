# SHT41 NeoPixel Temperature Display (CircuitPython)

Reads temperature + humidity from an Adafruit SHT41 sensor and displays temperature in real time using a GRBW NeoPixel strip.

The LED color smoothly transitions by temperature range:
- Blue (cool) → Green (comfortable) → Red (warm/hot)

## Features
- Fully offline (no WiFi, no web services, no secrets file)
- Smooth temperature-to-color interpolation
- GRBW NeoPixel support
- Low brightness default for stable power

## Hardware
- CircuitPython-compatible microcontroller
- Adafruit SHT41 (I2C)
- GRBW NeoPixel strip (8 pixels by default)

## Wiring (typical)
- SHT41:
  - VIN → 3V
  - GND → GND
  - SDA → SDA
  - SCL → SCL
- NeoPixels:
  - DIN → `D5` (default in `code.py`)
  - 5V/3V and GND as appropriate for your strip/board

See: `docs/wiring.md`

## Install / Run
1. Install CircuitPython on your board.
2. Copy required libraries into `CIRCUITPY/lib/` (see next section).
3. Copy `code.py` to the root of `CIRCUITPY/`.
4. Power the board—LEDs will update every 2 seconds.

## Required CircuitPython libraries
Copy these into `CIRCUITPY/lib/` from the Adafruit CircuitPython Library Bundle:
- `adafruit_sht4x.mpy`
- `neopixel.mpy`

## Configuration
Edit values at the top of `code.py`:
- `NUM_PIXELS` (default 8)
- `PIXEL_PIN` (default `board.D5`)
- `BRIGHTNESS` (default `0.03`)
- `UPDATE_SEC` (default `2.0`)
- `TEMP_COLOR_SCALE` (adjust ranges/colors)

## License
MIT — see `LICENSE`.
