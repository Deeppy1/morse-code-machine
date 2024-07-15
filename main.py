basic.clear_screen()
morse_variable = 0
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.clear_screen()
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            . . . . .
            """)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.clear_screen()
basic.forever(on_forever)
