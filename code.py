import time
import board
import neopixel
import adafruit_sht4x

# ----------------------------
# NeoPixel settings (GRBW strip)
# ----------------------------
NUM_PIXELS = 8
PIXEL_PIN = board.D5
BRIGHTNESS = 0.03   # keep low for stability
UPDATE_SEC = 2.0

# ----------------------------
# Temperature → Color Scale (°F)
# ----------------------------
TEMP_COLOR_SCALE = [
    # 60–70°F: dark blue -> light blue
    (60.0,  (0,   0,  80, 0)),
    (70.0,  (0,   0, 255, 0)),

    # 70–80°F: dark green -> light green
    (70.0,  (0,  60,   0, 0)),
    (80.0,  (0, 255,   0, 0)),

    # 80–100°F: light red -> dark red
    (80.0,  (255,  80, 80, 0)),
    (100.0, (255,   0,  0, 0)),
]

# ----------------------------
# Utility functions
# ----------------------------
def lerp(a, b, t):
    return a + (b - a) * t

def lerp_color(c1, c2, t):
    return tuple(int(lerp(c1[i], c2[i], t)) for i in range(4))

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def color_for_temp_f(temp_f):
    if temp_f <= TEMP_COLOR_SCALE[0][0]:
        return TEMP_COLOR_SCALE[0][1]

    if temp_f >= TEMP_COLOR_SCALE[-1][0]:
        return TEMP_COLOR_SCALE[-1][1]

    for i in range(len(TEMP_COLOR_SCALE) - 1):
        t0, c0 = TEMP_COLOR_SCALE[i]
        t1, c1 = TEMP_COLOR_SCALE[i + 1]

        if t0 <= temp_f <= t1:
            t = (temp_f - t0) / (t1 - t0)
            return lerp_color(c0, c1, t)

    return TEMP_COLOR_SCALE[-1][1]

# ----------------------------
# Init
# ----------------------------
print("Booting...")

# ---- SHT41 ----
i2c = board.I2C()
sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
print("SHT41 initialized")

# ---- NeoPixels ----
pixels = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRBW,
)
pixels.fill((0, 0, 0, 0))
pixels.show()
print("NeoPixels ready")

last_color = None
print("Entering main loop...")

# ----------------------------
# Main Loop
# ----------------------------
while True:
    try:
        temp_c, rh = sht.measurements
        temp_f = c_to_f(temp_c)

        color = color_for_temp_f(temp_f)

        if color != last_color:
            pixels.fill(color)
            pixels.show()
            last_color = color

        print(
            f"Temp: {temp_f:.2f}F  "
            f"RH: {rh:.1f}%  "
            f"Color: {color}"
        )

    except Exception as e:
        print("Sensor error:", e)

    time.sleep(UPDATE_SEC)
