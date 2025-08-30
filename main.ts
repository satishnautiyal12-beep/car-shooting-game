controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Rock = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . c c b b b a c a a a c c . . 
        . c c a b a c b a a a b a c c . 
        . c a b c f f f b a b b b a c . 
        . c a c f f f 5 a b b b b b a . 
        . c a 8 f f 8 c a b b b b b a . 
        . c c a c c c c a b c f a b c . 
        . c a a a c c c a c f f c b b . 
        . c a b 6 a c c a f f c c b b . 
        . a b c 8 6 c c a a a b b c b . 
        . a c f f a c c a f a c c c b . 
        . a 8 f c c b a f f c b c c c . 
        . c b c c c c b f c a b b a c . 
        . . . b b b b b b b b b b . . . 
        . . . c c c c b b b b b c . . . 
        . . . . . . . . . . . . . . . . 
        `, car, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    sprites.destroy(sprite, effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeLifeBy(-1)
})
let Bogey: Sprite = null
let Rock: Sprite = null
let car: Sprite = null
car = sprites.create(img`
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
    `, SpriteKind.Player)
car.setStayInScreen(true)
info.setLife(3)
controller.moveSprite(car, 200, 200)
game.onUpdateInterval(500, function () {
    Bogey = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Bogey.setVelocity(-100, 0)
    Bogey.left = scene.screenWidth()
    Bogey.y = randint(0, scene.screenHeight())
    Bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
