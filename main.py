def on_a_pressed():
    global Rock
    Rock = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . b b b . . . . . . .
            . . . . . . b 1 b b b b b . . .
            . . . . . b b 1 c c b e b b b .
            . . . . b b 1 c e 1 b b b e b .
            . . . . b c 1 1 1 1 e e b b b .
            . . . . b b c c c 1 b b b b . .
            . . . . . b b b c b b e e b . .
            . . . . . . . b b b c b b b . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        car,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite, effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Bogey: Sprite = None
Rock: Sprite = None
car: Sprite = None
car = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . 6 6 6 6 6 6 6 6 . . . .
        . . . 6 9 6 6 6 6 6 6 c 6 . . .
        . . 6 c 9 6 6 6 6 6 6 c c 6 . .
        . 6 c c 9 9 9 9 9 9 6 c c 9 6 d
        . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6
        . 6 6 8 b b 8 b b b 8 8 b 9 6 6
        . 6 8 b b b 8 b b b b 8 6 6 6 6
        . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6
        . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d
        . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d
        . 8 8 8 8 8 8 f f f 8 8 8 8 8 8
        . 8 f f f f 8 8 8 8 f f f 8 8 8
        . . f f f f f 8 8 f f f f f 8 .
        . . . f f f . . . . f f f f . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
car.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(car, 200, 200)

def on_update_interval():
    global Bogey
    Bogey = sprites.create(img("""
            . . f f f . . . . . . . . . . .
            f f f c c . . . . . . . . f f f
            f f c c c . c c . . . f c b b c
            f f c 3 c c 3 c c f f b b b c .
            f f c 3 b c 3 b c f b b c c c .
            f c b b b b b b c f b c b c c .
            c c 1 b b b 1 b c b b c b b c .
            c b b b b b b b b b c c c b c .
            c b 1 f f 1 c b b c c c c c . .
            c f 1 f f 1 f b b b b f c . . .
            f f f f f f f b b b b f c . . .
            f f 2 2 2 2 f b b b b f c c . .
            . f 2 2 2 2 2 b b b c f . . . .
            . . f 2 2 2 b b b c f . . . . .
            . . . f f f f f f f . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    Bogey.set_velocity(-100, 0)
    Bogey.left = scene.screen_width()
    Bogey.y = randint(0, scene.screen_height())
    Bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
