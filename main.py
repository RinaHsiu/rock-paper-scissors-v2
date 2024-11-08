hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                4717,
                5000,
                255,
                0,
                50,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . # # # .
            . . . . .
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                198,
                1,
                255,
                0,
                75,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        basic.show_leds("""
            . . . . .
            # . . . #
            . # . # .
            . # # # .
            . # # # .
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                2793,
                3523,
                255,
                0,
                75,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
