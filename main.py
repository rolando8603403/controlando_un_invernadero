def on_button_pressed_a():
    basic.show_number(input.temperature())
    while input.temperature() < 8:
        music.start_melody(music.built_in_melody(Melodies.JUMP_DOWN),
            MelodyOptions.ONCE_IN_BACKGROUND)
        basic.show_string("T.baja")
        basic.show_arrow(ArrowNames.SOUTH)
    while input.temperature() > 30:
        music.start_melody(music.built_in_melody(Melodies.JUMP_UP),
            MelodyOptions.ONCE_IN_BACKGROUND)
        basic.show_string("T.Alta")
        basic.show_arrow(ArrowNames.NORTH)
    if input.temperature() >= 8 and input.temperature() <= 30:
        music.stop_melody(MelodyStopOptions.ALL)
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_string("T.OK")
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    while pins.analog_read_pin(AnalogPin.P0) < 200:
        music.start_melody(music.built_in_melody(Melodies.JUMP_DOWN),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_string("H.baja")
        basic.show_arrow(ArrowNames.SOUTH)
    while pins.analog_read_pin(AnalogPin.P0) > 600:
        music.start_melody(music.built_in_melody(Melodies.JUMP_DOWN),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_string("H.Alta")
        basic.show_arrow(ArrowNames.NORTH)
    if pins.analog_read_pin(AnalogPin.P0) >= 200 and pins.analog_read_pin(AnalogPin.P0) <= 600:
        music.stop_melody(MelodyStopOptions.ALL)
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_string("H.OK")
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)
