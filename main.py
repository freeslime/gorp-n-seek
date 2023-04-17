@namespace
class SpriteKind:
    Button = SpriteKind.create()
    soap = SpriteKind.create()
    water = SpriteKind.create()
    door = SpriteKind.create()
    bread = SpriteKind.create()
    bred = SpriteKind.create()
    melk = SpriteKind.create()
    letter = SpriteKind.create()
    rock = SpriteKind.create()
    wood = SpriteKind.create()
def levelThree():
    global AWater
    sprites.destroy(kitchen_door)
    sprites.destroy(knob)
    scene.set_background_image(img("""
        ccccccccccccccccccccccccccccccccbbbbccccccccccccccccccccccccccccccccccc888888888cccccccccccccccccccccccccccccccccbddbccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbbbbccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc8b888888b88ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc8bb88888888ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88b8888b888ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88bb8888b88ccccccccccccccccccccccccccccccccbbbcccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbbbcbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc8888888888ccccccccccccccccccccccccccccccccccbbbbdccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbcccccccccccccccccccccccccccccc44445555544445555555dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.bbbcccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4ddddddddddd4dddddd5dddddddddddddddddddddddddddddb.b66bbbcccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbdddddddddddddddddddddddddddddd44dd55555d4444445dd5ddddddddddddddddddddddddddddcbcc6666bbbcccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccbb.bbcddddddddddddddddddddddddddddd545ddd55555ddddd55d4ddddddddddddddddddddddddddddcbcc666666bbbcccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccbbb6cbbcddddddddddddddddddddddddddddd555d55d115555555d5d4ddddddddddddddddddedddddddddcbcc66666666bbbcccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccbbb666cbbcdddddddddddddddddddddddddddddd55d55551111dd55dd54ddddddddddddddddddebddddddddcb.c6666666666bbbcccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccbbb66666cbbcdddddddddddddddddddddddddddddd5555dd555551115dd44ddddddddddddddddddebddddddddcbbcc66666666666bbccccccccccccccccccccccccccccc
                ccccccccccccccccccccccbbb6666666cbbddddddddddddddddddddddddddddddd5114444dddddd55d54dddddddddddddddddddebddddddddcbbccc666666666666bbccccccccccccccccccccccccccc
                ccccccccccccccccccccbbb66666666ecbbddddddddddddddedddddddddddddddd55111dddd5555dd111dddddddddddddddddddebdddddddddbbccccc66666666666bbbccccccccccccccccccccccccc
                ccccccccccccccccccbbb6666666cccccbbdddddddddddddbeddddddddddddddddd55511d555d551115ddddddddddddddddddddebdddddddddbbcecccc666666666666bbbccccccccccccccccccccccc
                cccccccccccccccccbbd66666ccccbbbcbbdddddddddddddbeddddddddddddddddddd551111111115ddddddddddddddddddddddebdddddddddbbccbccccb666666666666bbbccccccccccccccccccccc
                cccccccccccccccbb6666666cccbbbbecbbdddddddddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddedddbbccbeecccb6666666666666bbcccccccccccccccccccc
                cccccccccccccbb6666666ccccbebbeecbbdddddddedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddedddbbccccccecccc6666666666666bbccdccccccccccccccc
                cccccccccccbb6666666ccccbeecceeecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccccecc.ccccc6666666666666bbcccccccccccccccc
                cccccccccbb666666666cbbccccceeeecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbceeecc.cccb66666666666666bbcccccccccccccc
                cccccccbb6666666666bbcceccceeeebcbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbccceeecccbbbb6666666666666bbbcccccccccccc
                cccccbb6666666666bbcceccceeeeebecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbcceeeeccccbeebbbbb6666666666666bbbcccccccccc
                cccbb6666666666cccccccceeeeccccecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbbeeeeeccceeeeebbb6666666666666bbccccccccc
                cbbd666666666cccccccceeeeecccccbcbbddddddbedddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbeddbbeeebbbbeeeebcceeccccbbb6666666666666bbccccccc
                bd666666666cceecccceeeeecccccbbbcbbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbceeeebbbbeebbcceeccecccbb6666666666666bbccccc
                666666666cceeccccceeeeeccecbbbeecbbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbceeeeeebbbbeeeccceeceeccbbb66cc666666666bbccc
                6666666ccccccccceccceccbbebbeeeccebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbeeeeeeeeebbbbeeeccccccecccccb.cccc66666666bbc
                66666ccc.eeccccccbcceebbbbeeeeecccbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4ee4eeeeebbbbebeeeeeeeeccccbbcccc666666666b
                666bccceeeccecceecbbbbbbeeeeee4eeebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eee44eeeeebbbbeeeeeeeeececccbccccc66666666
                6bccceeccceeeeeccbbbbbeeeeee44eeeebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeee44eeeeebbbbebeeeeeecceccebcccc6666666
                cccccccceeeeeccbbbbeeeeeee44eee4eebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeee44eeeeebbbbeeccccceccceeebccc666666
                cecceeeeeeccccbbbeeeeeee44eeeee4eebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeeeee4eeeeeebbbbeeecccccceeeeebbccc666
                ccceeeeeccbbbbbeeeeeee44eeeeeee4eebddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeeeeee44eeeeeebbbbeeeccceeeccccebcccc6
                ecceecccbbbbbe4eeeee44eeeeeeeee4eebbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eedeeeeeeeee44eeeee4bbbbeebcceeececeeecc.c
                ecceeebbbbeeee4eeee4eeeeeeeeeed4eebbdddddddddddddddddddddeeeeeddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eedeeeeeeeeeee44eee4eebbbbbeeceeeccceeeccc
                eccebbbbeeeeee4eeeeeeeeeeeeeeed4eebbdddddddddddddddddddee99eeeeeeeeeeeeeeeeeeeddddddddddddddddeeceeeddddbddddbeddbcee4eedeeeeeeeeeeeee4ed4eeeebbbbeecceeccceeccc
                ecbbbbeeeeee4e4deeeeeeeeeeeeeed4eebcdddddddddddddddddde9999999999999999111111eeeeeeeeeeeeeeeee99cddeddddbddddbeddbcee4eedeeeeeeeeeeeeeeed4eeeeeebbbbeccceecceccc
                bbbbeeeeee44ee4deeeeeeeeeeeeeed4eebcdddddddddddddddddde999111119999999111bbbb111119999999999999ccddeddddbddddbeddbcee4eeeeeeeeeeeeeeeeeed4eeeeeeeebbbbbcccccecec
                bbeeeeeee4eee4e4eeeeeeeeeeeeeed4eebcdddddddddddddddddee99911bbb19991111111111111111999999999999cdddeddddebdddbeddbcee4eeeeeeeeeeeeeeeeeed4eeeeeeeeeebbbbeeeeecec
                eeeeeee44eeeeee4eeeeeeeeeeeeeee4eebcddddddddddddddddde111111b1bb1991111111111111111999999999999cdddedddddedddbeddbce44eeeeeeeeeeeeeeeeeed4eeeeee4eeeeebbbbeeecec
                eeeee44eeeeeeee4eeeeeeeeeeeeeee4eebcddddddddddddddddde1111111111199111111111111111bb99999999999cdddedddddddddbeddbceee44eeeeeeeeeeeeeeeed4ee4eeee44eeeeebbbbecec
                eeee4eeeeeeeeee4deeeeeeeeeeeeee4eebcddddddddddddddddde111111111119991b111111111111b999999999999cdddedddddddddbeddbcbeeee44eeeeeeeeeeebbbd4ee4eeeeee4eeeeeebbbbcc
                ee44eeeeeeeeeee4ddebbeeeeeeeeee44ebcddddddddddddddddde111111111199999bbbbb1111b1111999911111199cdddedddddddddbeddcccbbeeee4eeeeeeeeee1cbd4ee4eeeeeee44eeeeeebbcc
                e4eeeeeeeee4444.4dbbbeeeeeeeee44eebcddddddddddddddddde11111bb1119999999911111bb9999111111111199cdddedddddddddbeddcbcccbbeee44eeeeeeebbc1d4be4eeeeeeeee4eeeeeebcc
                eeeeeeeeeee4..bb4dbbbeeeeeee44eee.bcdddddddddddddddddde11111bbb9999999999991bb999991111bbb11199cdddedddddddddbeddcc66cccbbeee44eeeeebcccc11bb4eeeeeeeee44eeeeecc
                eeeeeeeeeee4bbbb4cccbeeeeee4eeeebccbdddddddd8888dddddde111bbb993999999999999b999bbbbb1111111199bdddedddddddddbeddbc666bccebbeee44eeebbbccccbbbeeeeeeeeeee4eeeeec
                e4eeeeeeeeebbcb11cdcbbeee44eeebbccbbdddddddffffffddddde99999933b3939999999999999b1111111111199cbdddedddddddddbeddbc66666bcbebbeee4eeeebbdcccbbeeeeeeeeeeeeee4eec
                e4eeeeeeeeeeb1ccc4dbbeee4eeebbeccccbdddddddddbbddddddde9999933b3b339999999999999b1111111111199cbdddedddddddddbeddbc6666666bbbbbbeeeeeeeed4bcbbeeeeeeeeeeeeee4eee
                e4eeeeeeeeeebcccb4deeeeeeeebeccc66ccdddddddddbbddddddde999999b3b3333999999999999bb11111b111199cbdddedddddddddbeddbc666666666bbbbbbeeeeded4bbbeeeeeeeeeeeeeee4eee
                e4edeeeeeeeebcbbb4deeeeeebbbbc666cccdddddddddbbddddddde99999333793999997779999999111111b111199ccdddedddddddddbeddbb6cc66666666bbbbbeeeedd4e4beeeeeeeeeeeedee4eee
                e4edeeeeeeeebbbbe4deeeebbeb66666cc6cdddddddddbbddddddde999999997999999987899999999911bbb9999996cdddedddddddddbeddbb66c6666666666bbbbbee.d4e4eeeeeeeeeeeeedee4eee
                e4edeeeeeeeeebeee4ddeebebb666666c66bdddddddddbbddddddde6696666977999666666699999999666666666999cdddedddddddddbeddbb6bb666666666666bbbbbee4eeeeeeeeeeeeeeedee4eee
                e4edeeeeeeeeeeeeee4dbbbb66666666666bbddddddddbbddddddde777777cc77cc7777777766666677777777777777cdddedddddddddbeddbb66666666666666666bbbbb4eeee4eeeeeeeeeedee4eee
                e4edeeeeeeeeeeeeddbbbb6666666666666bbddddddddbbbbbdddde77777ceeeeeec777777777777777777777777777cdddedddddddddbeddbb6666666666666666666bbb4beeee44eeeeeeeedee4eee
                e4eeeeeeeee4eedddbeb6666666666666ccbbddddddbbbbbbbbddde777777cccccc7777777777777777777777777777cdddedddddddddbeddbb666666666666666666666bbbbbeeee44eeeeeedee4eee
                e4eeeeeeee4eeddbbbb6666666666666666bbdddddbddbbbbbbbdde7cccccbccccbbcccccbbbbbbbbbbbbbbbbccccccbdddedddddddddbeddbb66666666666666666666666bbbbbeeee44eeeeeee4eee
                e4eeeeee444eebbbb666666666666666666bbddddbdd1bbbbbbbbdeccddddbcdccbdddddccccccccccccccccccdddddccbdedddddddddbedcbb6c6666666666666666666666bbbbbeeeee44eeeee4eee
                e4eeeee4eeebbebe666666666666666666bbbdddbbdbbbccbbbbbdecdddddbcdccbdddddddddddddddddddddddddddddcccbdddddddddbedcbb6bb66666666666666666666666bbbbbeeeee44eee4eee
                e4eeee4eeebebb66666666666666666666bbbdddbddbbcccccbbbdeeddddddbbbbdddddddddddddddddddddddddddddddeeedddddddddbedcbb6666666666666666666666666666bbbbbeeeee44e4eee
                ee4e44eebbbb666666666666666666666666bdddb1bbbcbbbcbbbdddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddbedcbb666666666666666666666666666666bbbbbeeeee44eee
                eee4eebbbbe6666666666666666666666666bdddbdbbbcbbcbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddbedcbb66666666666666666666666666666666bbbbbeeeeeeee
                ee4eebebee66666666666666666666666666bdddbbbbbccccbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddbedcbb6666666666666666666666666666666666bbbbbeeeeee
                eeebbbbe6666666666666666666666666666bdddbbbbbbbb1dd1bdddddddddddddddddddcccccddddddddddddddddddddddddddddddddbedcbb666666666666666666666666666666666666bbbbbeeee
                ebbbbecc666666666666666666666666666bbdddcbbbbbbddbbbcddddddddddddddddddcbb1bccddddddddddddddddddddddddddddddbdeddbb66666666666666666666666666666666666666cbbbbee
                bbbe.cc6666666666666666666666666666bbbddccbbbbb1bbcccddddddddddddddddddccccb1ccddddddddddddddddddddddddccccccccccbbc66666666666666666666666666666666666666ccbbbe
                b..cc6666666666666666666666666666666bbcccccbbbbccccddddddddddddddddccddcbcdccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc66666666666666666666666666666666666666ccbe
                6ccc666666666666666666666666666666cbbbbbbbccccccbbbbbbbbbbbbbbbbbbccccccbcbbccdddddddddddddddddddddbddddddbdddedcbbcbbc66666666666666666666666666666666666666ccc
                666666666666666666666666666666666cbdbbdbddddbddddddddddbddddddddddccccdcbcdd91dddddddddddbdddddddddbddddddbddddecbbcddbc6666666666666666666666666666666666666666
                66666666666666666666666666666c6ccbdcbbcbbdddbbdddddddddbddddbbbbbbbbbcccbcdd99dbbbbb99bbdbddddddddddddddddbdddddcbbcdddbcc66666666666666666666666666666666666666
                66666666666666666666666666666ccbbddcbbcdddddddddddddddddddddb999999999ccccbb99bb99999bbbddddddddddddddddddddddddcbbcddddbb66666666666666666666666666666666666666
                6c666666666666666666666666666cbddddcbbcdddddddddddddddddd99db999991919999999999999999bcbddddddddddddddddddddddddcbbcddddddb6666666666666666666666666666666666666
                cc66666666666666666666666666cbdddddcbbcdddddddddddddddddd999bb99199999999999999999b9cccbddddddddddddddddddddddddcbbcdddddbdbcc6666666666666666666666666666666666
                c66666666666666666666666666cbddddddcbbcddddddddddddddddddd99999999999999999999999999cccbddddddddddddddddddddddddcbbcddddddddbbc666666666666666666666666666666666
                6666666666666666666666666ccbddddddddbbcddddddddddddddddddddd999999999999999999999999ccccddddddddddddddddddddddddcbbcddddddddddbcc6666666666666666666666666666666
                bb6666666666666666666666cbbdddddddddbbcddddddddddddddddddd99bd999999bbbbbbbbb99999b9ccdcdddddddddddddddddddddddddbbcdddddddddddbbc666666666666666666666666666b66
                b6666666666666666666666cbdbdddddddddbbcdddddddddddddddddddddbbbd99c9cccccccccc99999cccccddddddddddddddddddddddddbbbddddddddddddbdbc6c666666666666666666666666bb6
                6666666666666666666666ccddbdddddddddbbcdddddddddddddddddddddddbb9bb9bbbbbbbbbb9bb99ccccbdddddddddddddddddddddddddbbddddddddddddbddbccb66666666666666666666666cbb
                66666666666666666666bbccddddddddddddbbddddddddddddddddddddddddd99dd9dddddddddb99b99bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddbcc666666666666666666666666cc
                6666666666666666666cbbddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbb99bbbbbbbbbbbbbb9991bbbbbbbbbbbbbbbbbbbbbbbbbeeeebbcddddddddddddddddddbc6666666666666666666666666
                666666666666666666cbbdddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbb99bbbbbbbbbbbbbbb999bbbbbeeeeeeeeeeeeeeeeeeeeeeeeebcbddddddddddddddddddbcc66c66666666666666666666
                6b666666666666666cbdddddddddddddddddbbeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeebcbbddddddddddddddddddbbc6cbb666666666666666666
                bb6666666666666ccbddddddddddddddddbbbbeeeee444444444444eeeeeeee91eeeeeeeeeeeeeeee91eeeeeeeeeeeeeeeeeeeeeeeeeeeeebbcbbbdddddddddddddddddddbcccb666666666666666666
                bb666666666666ccbddddddddddddddddbbbcbee4444eeeeeeeeeeeeeedeee499444444444de44444994444eeee444444444444444eeeeeebbcebbbbddddddddddddddddddbbcb666666666666666666
                cb66666666666cbbddddddddddddddddbbebcbee4eeeeeeeeeeeeeeeeedeee9eeeeeeeeee4de4eeee99eeeeedeeeeeeeeeeeeeeeee444eebebceebbbbdddddddddddddddddddbc666666666666666b66
                c66666666666cbdddddddddddddddddbbebecbee4eeeeeeeeeeeeeeeeedeee9eeeeeeeeee4de4eeee999eeeedeeeeeeeeeeeeeeeeeee44eeebceeebbbbddddddddddddddddddbbcc6666666666666cb6
                6666666bc66cbdbbddddddddddddddbbbbeecbee4eeeeeeeeeeeeeeeeedee9eeeeeeeeeee4de4eeee999eeeedeeeeeeeeeeeeeeeeeeee44eebceeeebbbbdddddddddddddddddbdbbc666666666666cbb
                6666666bc6cbdddddddddddddddddbbbeeeecbee4eeeeeeeeeeeeeeeeedee99eeeeeeee444d44eeee999eeeedeeeeeeeeeeeeeeeeeeeee4ebbceeeeeebbbddddddddddddddddbdddbc666c6666666666
                666666bbccbdddddddddddddddddbbbeeeeecbeee4eeeeeeeeeeeeeeeedeeeee9eeeee44edd4eeeee99eeeeedeeeeeeeeeeeeeeeeeeeee4ebbceeeeeeebbbddddddddddddddddddddbcc6cbb66666666
                66666bbcbbdddddddddddddddddbbbeeeeeecbeee4eeeeeeeeeeeeeeeedeeeee9eeeeee4edddeeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeee4ebcceeeeeeeebbbbdddddddddddddddddddbbcccb66666666
                66666bcbddddddddddddddddddbbbeeeeeeecbeee4eeeeeebbbeeeeeeedeeee9eeeeeee4ede4eeeeeeeeeeeedeeeeeeeeebbbeeeeeeeee4ebcceeeeeeeeebbbbddddddddddddddddddddbccb66666666
                66666bbdbdddddddddddddddbbbeeeeeeeeecbeee4eeeeeebcbeeeeeeedeeee9eeeeeee44de4eeeeeeeeeeeedeeeeeeeeebcbeeeeeeee4eebceeeeeeeeeeebbbbddddddddddddddddddddbcc66666666
                6666cbdddddddddddddddddbbbbeeeeeeeeec.bee4eeeeeebbbeeeeeeedeeeeeeeeeeeee4bbbbbbbeeeeeeeedeeeeeeeeebbbeeeeeeee4eebceeeeeeeeeeeebbbbddddddddddddddddddbdcbc6666666
                66ccbdddddddddddddddddbbbbeeeeeeeeeeccbee4eeeeeeeeeeeeeeeedeeeeeeeeeeeee4ccccccbbe9eeeeedeeeeeeeeeeeeeeeeeeee4eebceeeeeeeeeeeeebbbbdddddddddddddddddddddbcc66666
                6cbbdddddddddddddddddbbbbeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4bbbbbbbbe9eeeeedeeeeeeeeeeeeeeeeeeee4eebcceeeeeeeeeeeeeebbbdddddddddddddddddddddbbc6666
                cbddddddddddddddddddb.cbeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4eeeeeeeee9eeeeddeeeeeeeeeeeeeeeeeeee4ebbcceeeeeeeeeeeeeeebbbbdddddddddddddddddddddbc666
                bddddddddddddddddddbccbeeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4deeeeeee99eeeedeeeeeeeeeeeeeeeeeeeee4ebbcceeeeeeeeeeeeeeeebbbbdddddddddddddddddddddbcc6
                dbddddddddddddddddbcbbeeeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeeeeddeeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeb44ebbcceeeeeeeeeeeeeeeeebbbbdddddddddddddddddddddbbc
                dbdddddddddddddddbbcbeeeeeeeeeeeeeeeecbeee44eeeeeeeeeeeeeedeeeeeeeeeeeeeeedeeeeeeeeeeeedeeeeeeeeeeeeeeeeeee44eebbcceeeeeeeeeeeeeeeeeebbbbddddddddddddddddddddbdb
                ddddddddddddddddbcceeeeeeeeeeeeeeeeeecbeeee44444444444444edeeeeeeeeeeeeeeedeeeeeeeeeee4deeeeeeeeeeeeeeee4444beebbceeeeeeeeeeeeeeeeeeeebbbbdddddddddddddddddddbdd
                dddddddddddddddbcceeeeeeeeeeeeeeeeeeecbeeeeeeeeeeeeeeeeeeedeee4444444444eedeeee4444444eeeeeeeeee444444444eeeebebbceeeeeeeeeeeeeeeeeeeeebcbbddddddddddddddddddbdd
                dddddddddddddddccbeeeeeeeeeeeeeeeeeeecbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedeebbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbceeeeeeeeeeeeeeeeeeeeeebcbbdddddddddddddddddddd
                ddddddddddddddccbeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccc.ceeeeeeeeeeeeeeeeeeeeeeeccbbddddddddddddddddddd
                dddddddddddddccbeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccc9ccccccccccccccccccccccccffff111111111111111cceeeeeeeeeeeeeeeeeeeeeeebcbbbdddddddddddddddddd
                ddddddddddddbceeeeeeeeeeeeeeeeeeeeeeeccfffffffffff11111111111fff9fff99999999999991111fffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbdddddddddddddddd
                dddddddddddccbeeeeeeeeeeeeeeeeeeeeeeccfffffffffff111111111111fff999999999999999999999999fffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbddddddddddddddd
                ddddddddddcceeeeeeeeeeeeeeeeeeeeeeeccfffffffffff1111111111111f991199f9999999991199999999ffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbdddddddddddddd
                dddddddddccbeeeeeeeeeeeeeeeeeeeeeec.bfffffffffffb11111111111f99999999ffff999111999999999fffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbddddddddddddd
                ddddddddccbeeeeeeeeeeeeeeeeeeeeeeccbfffffffffffb111111111111f99fffffffff999111999999999fffffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeecccbbbdddddddddddd
                dddddddcceeeeeeeeeeeeeeeeeeeeeeeccbfffffffffffb111111111111fb9ffffffffff9911111199999bfffffffffffffffbf1111111111111bccbeeeeeeeeeeeeeeeeeeeeeeebccbbbbdddddddddd
                ddddddcceeeeeeeeeeeeeeeeeeeeeecccbfffffffffffb1111111111111fbffffffffffffb11ffff9999ffbfffffffffffffffbfffffffffffffffccceeeeeeeeeeeeeeeeeeeeeeebbccbbbddddddddd
                dddddcceeeeeeeeeeeeeeeeeeeeeecccbfffffffffffbffffffffffffffbfffffffffffffbffffffffffffbf111111111111111bbfffffffffffffcccceeeeeeeeeeeeeeeeeeeeeeeebcccbbdddddddd
                ddddcceeeeeeeeeeeeeeeeeeeeeecccb11111111111bfffffffffffffffb1111111111111bfffffffffffffbf1111111111111111bfffffffffffffcccbeeeeeeeeeeeeeeeeeeeeeeeebbcccbddddddd
                dddccbeeeeeeeeeeeeeeeeeeeeecccbb1111111111bfffffffffffffffb11111111111111bffffffffffffffb11111111111111111bfffffffffffffcccceeeeeeeeeeeeeeeeeeeeeeeeebbcccdddddd
                ddcceeeeeeeeeeeeeeeeeeeeeccccbb1111111111bffffffffffffffffb11111111111111fffffffffffffffbf11111111111111111bbfffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbccbdbdd
                dbceeeeeeeeeeeeeeeeeeeeececcbb11111111111ffffffffffffffffb111111111111111ffffffffffffffffb1111111111111111111bfffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbcccdbb
                bbeeeeeeeeeeeeeeeeeeeeececcbb11111111111fffffffffffffffff1111111111111111ffffffffffffffffff1111111111111111111ffffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbbccdb
    """))
    AWater = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 9 9 9 . . . . . . . 
                    . . . . . . 9 9 9 9 . . . . . . 
                    . . . . b b 9 9 b b b b . . . . 
                    . . . . . b b b b . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.water)
    AWater.set_position(74, 73)
def level_six():
    global wood2
    sprites.destroy(rock2)
    scene.set_background_image(img("""
        99999999999999977777777777777777777777777777777777777777777777777777777776777777777777777777999999999999999999999998866ccccccccccccccccccccccccccccccccccccccccc
                999999999966667.6777777777776667777777776677777777777777777bb77777776666667777777777777777767999999999999999999988866cccccccccceeccccccccccccccccccccccccceccccc
                999999999967777667777777667777777777777667777777777777777777b777b777777777777777777777777777b799999999999999988886cceccccccccceccccccccccccccceeccccccceeecccccc
                9999999999967776bbbb76667777777777777667777777777777b77777777777b777777777777777777777777777bb799999999999988866cccecccccccccecccccccccccccceeccccccceecccccccce
                99999999997.6bbb666b667777777777777777777777777bbbbb77777777777777777777777777777777777777777b6999999999988866cccceccccccccceccccccccccccceeccccccccecccccccccec
                99999999977777777777b777777777777777777777bbbbb7777777777777777777777777777777777777777777777b67999999998866cccccecccccccceecccccccccccceecccccccceecccccccccecc
                9999999977777777777bb777766677777777777777777777777777777777777777777777777777b77777777777776667999999886ccccccceccccccccecccccccccceeeecccccccccecccccccccceccc
                999999997777b77777777777767777777777777777777777777777777777777777777777777777b7777777667776.6779999886cccccccceccccccccecccccccceeeccccccccccceeccccccccccecccc
                999999997777b777777777766777777777777bb77777777777777777777777777777777bbbbb77b777777667777776799988ccccccccceeecccccccceccccccceccccccccccccceccccccccccccccccc
                999999997777777777777767777777777777777b77777777777777777777777777777777777777b7777776777bbbbb99998ccccccccccecccccccccccccccccccccccccccccccccccccccccccccccccc
                9999999677777777777776677777777777777777bb7777777777777777777777777777777b7777b77777677777777796688ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                99999996777bb77777777777777666777777777777bb7777777776b77777777777777777bb777b77777667777777779968eddddddddddddddddddcccccccccccccccccdddddddddddddddddddddddddd
                9999999677777b777777777777777767777777777776bbb7777666777777777bbbb7777777777b77666777777777779968ebbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddbbbbbbbbbbbbbbbbbbbbdd
                999999966777777b7777777777777777777777777777666bbb66777777777777777bbbbbbbbbb777777777777777777968dddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddd
                999999996777777b77777777777777777777777777777777777777777777777777777777777777777777777777777b796edbdddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddd
                99999999677777bb77777777777777777777777777777777777777777777777777777777777777777777777777777b668edbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                9999999966777777777777777777777777777777777777777777777777777777777777777777777777777777777766698edbddddddddddddddddddddddddddddddddddddddbdddddddddddddddbddddd
                999999999667767777777777777777777777777767777777777777777777777777777777777777777777777666b6bb798edbddddddddddddddddddddddddddddddddddddddbdddddbdddddddddbddddd
                999999999777766bb777777777777777777b..666777777777777777777777777777777777777777777777767bbb77998edbdddddddddddddbbbbdddddbdddddddddddddddbdddddbdddddddddbddddd
                99999999997777667777777777777777776b66677777777777777777777777777777777777777777777b7776b77779998edbbdddddddddddddddddddddddddddddddddddddbdddddbdddddddddbddddd
                999999999977777667777777777777777bb777777777777777777777777777777777777777bb77b777bb7776b99999998eddbdddddddddddddddddddddddddddddddddddddbdddddbddddddddddddddd
                999999999777777766777777777777bbb6677777777777777777777777777777777777777b7777777777776b999999998eddbdddddddddddddddddddddddddddddddddddddbdddddbddddddddddddddd
                999999999b7777777667777bbbbbbb7776b77777777777767777777777777777777766777777777777777769999999998eddbdddddddddddddddddeeeeeeeeedddddddddddbdddddbddddddddddddddd
                999999999b7777777766677666777777bb77777777777b76777777777777777777776677777777777777bb67999999998eddbddddddddddddeeeeeeeeeeeeeeeeeddddddddbdddddbddddddddddddddd
                999999999b77777777776666776666bb67777777777777b677777777777777777777e6777777777777776667999999998eddbddddddddddeeeeeeeeeeeeeeeeeeeedddddddbddddddddddddddddddddd
                999999999b7777777777777bb77bbb777777777e777777b677777777777777777777e677777777b777777666999999988eddbddddddddee6666666666666666666eeddddddbddddddddddddddddddddd
                999999999bb77777777777777bb77777777766b6777777b67777777bbbb77b7677666677777777b777777776999999986eddbdddddddde6666666666666666666b6eddddddbddddddddddddddddddddd
                9999999999bb77777777777777777777777777b67777776b7777bb777777bb76667ee677777777b77777777699999bb86eddbdddddddde6666666666666666666bbeddddddbddddddddddddddddddddd
                99999999997777777777777777777777777777b67777b666b777b77777bb77667b7e7677777777b777777776999888886eddbddbddddde66666666666666666666beddddddbddddddddddddddddddddd
                99999999999977777777777777777777777677be7777b666777777777777776677bb767777b667b777777796998bb888beddbddbddddde66666666666666666666beddddddbddddddddddddddddddddd
                99999999999697777767777777777777776677be7777b6ee6777777777777666667ebb7766677b777777779698888887beddbddbddddde66666666666666666666beddddddddddddddddddddddddeeee
                99999999999699977777777777777777777777be7777b6ee667777777777667e777e77b77777b7777777766688b77b777bbdbddbddddde66666666666666666666bedddddddddddddddddddddddeeeee
                99999999999969997777777777777777777777be7777bee6667777776666677ee77e6667766b7777777668888777b7b77eddbdddbdddde66666666666666666666bedddddddddddddddddddddddebbbb
                9999999999999666b777777777777777777777be77bbeee666666777676667eeeee777.666bbbbbbb66886887777bb7b7eddbdddbddddde6666666666666666666bedddddddddddddddddddddddbbeee
                99999999999999966bb7777777777767777776bbbb77eee6e677777766677eeeeeeee97777778866688888888bb78bbb7eddbdddbddddde6666666666666666666bedddddddddddddddddddddddbeeee
                99999999999999999677777777777776776667be777eee6eee6777666777eeeeee4ee999998866b88b77777777bb78bb7eddbdddbddddde6666666666666666666beddddddddddddddddddbddddbeeee
                99999999999999999667777777777776667777be77eeee6eeee666777eeeeeeeee4ebb99986668877777.87bb77bb8b7beddbdddbddddde6666666666666666666beddddddddddddddddddbddddbeeee
                89999999999999999966666666777777667777b77eeeee6eeeeeeeeeeeeeeeeeee4eb998866888777777b8877bbbb78bbbddbddddddddde666666666666666bbbbeeddddddddddddddddddbddddbeeee
                899999999999999999999bb7776667776666776eeeeeeeeeeeeeeeeeeeeeeeeeeee4b988888b77777.7777b88b77b7777eddbdddddddddee66666666666bbbbeeeedddddddddddddddddddbddddbeeee
                899999999999999999999999777776997779666eeeeeeeeeeeeeeeeeeeeeeeeeeee4b88bb7777777777777bb788bbb777eddbddddddddddeebbbbbbbbbbeeeeeeeddddddddddddddbdddddbddddbeeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee4886b777777777777777bbb78bbbbbeddbddddddddddeeeeeeeeeeeeeeeedddddddddddddddddbdddddbddddbeeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee48bb7777766666666777777b88bbbbeddbddddddddddddddeeeeeeeeeeeedddddddddddddddddbddddbdddddebeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee4e7777776666777776666777777b77eddbdddddddddddddddddddddddddddddddddddddddddddbddddddddddebeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeee4eeeeeeeeeeeeb4777777777766677777666bb77777eedbddddddddddddddddddddddddddddddddddddddddddbdddddddddddebeee
                8999999999999999999999999999999999999cceeeeeeeeeeeeeee4eeeeeeeeeeeeb47777777777777667667777bbb87bbedbddddddddddddddddddddddddddddddddddddddddddddddddddddddebeee
                89999999999999999999999988888888888894ceeeeeeeeeeeeeee4eebeeeeeeeeeb477777777777776666666677777787edbddddddddddddddddddddddddddddddddddddddddddddddddddddddebeee
                89999999999999999999998888888778888997ceeeeeeeeeeeeeee4eebeeeeeeebebe77777777777776777777776666667edbdddddddbbbbbbbbbbdddddddddddddddddddddddddddddddddddddebeee
                8899999999999999998888886667767bbb7777ceeeeeeeeeeeeeee4eebeeeeeeebebe77777677777777777776666666667eebddddddddddddddddbbbbbbbbbbbbbbbbbbdddddddbbbbbbbbbbbddebeee
                8899999999999888888b8877777bbbbb6777.cceeeeeeeeeeeeeee4eebeeeeeeebebe77777677777777776666666677777eebeeeeeeeeddddddddddddddddddddddddddbbbbbbbdddddddddddddebeee
                889999999999886bbb8877777b6666667777cceeeeeeeeeeeeeeee4eebeeeeeeebebb7777767777766666777777776667777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                889999999888888887777776667777777777c4eeeeeeeeeeeeeeeee4ebeeeeeeebeeb77777677776777777777777766666677777777777777777777777777777777777777777777777777777777ddddd
                88999988666666677666666777777777777cb46eeeeeeeeeeeeeeee4e4eeeeeeeebeb777776777667777777777777766666666666666666666666777777777777777777777777777777777777ebddddd
                88988866b88777777777777777777777676666eeeeeeeeeeeeeeeeeee4eeeeeeeebeb777767776777777777777777777777777777777666666666666666666666666666666666666666666666ebbdddd
                8686666b777777777777777777777767777cbeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeb777666667777777777777777777777777777777777777777777776666666666666666666666677777777e7bdddd
                668666b8777777777777777777666677777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeebbb777777777777777777777777777777777777777777777777777777777777777666667777777777777777e7bdddd
                68668887777777777777777777666677777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeeebb777777777777777777777777777777777777777777777777777777777777777777777777777777777777eebdddd
                66686b77777777777777777777777767777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeb777777777777777777777777777777777777777777777777777777777777777777777777222222222277eebdddd
                666b7777777777777777777777777766777ceebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeb777777777777777777777777777777777777777777777777777777777777777777722222222222227277eebdddd
                8867777777766667766666666666666677cceebeeeeeee4beeeeeeeeeeeeeeeeeeeeb777777777777777777777777777777777777777777777777777777777777777777222222222d22222277eebdddd
                8667777766677767666667666666666667cbeeeeeeeeee4bbeeeeeeeeeeeeeeeeeeeb777777777777777777777777777777777777777777777777777777777777777777222222222d22222277eebdddd
                8677777766667667777776666777777777cbeeeeeeeeee4ebeeeeeeeeeebeeeeeeeeeb77777777777777777777777777777777777777777777777777777777777777777222222dddd22222277eebddde
                767777777776666666666666677777777ccbeeeeeeeeeee4beeeeeeeeeebeeeeeeeeeb777777777777777777777777777777777777777777777777777777777777777772222ddd22222222277eebdbeb
                677777766667777777777777777777777cbbeeeeeeeeeee4beeeeeeeeeebeeeee4eeeb77777777777777777777777777777777777777777777777777777777777777772222222222222222277eedeeed
                666666677777777777777777777777777cbebbeeeeeeeeeeeeeeeeeeeeebeeeee4eeeb77777777777777777777777777777777777777777777777776677777777777772222222222222222277eeedddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeb77777777777777777777777777777777777777777777776667777777777777772222222b22227777777ebddddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeb77777777777777777777777777777777777777777777776666777777777777777777777bccc77777777ebddddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe777777777777777777777777777777777777777777777777767777777777777777777bbccc77777777ebddddd
                777777777777777777777777777777777c4beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe777777777777777777777777766777777777777777777777666777777777777777777bbccc77777777e.ddddd
                77777777777777777777777777777777bcbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe777777776667777777777777766777777777777777777766666666666777777777777bbccc77777777edddddd
                77777777777777777777777777777777bcbeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebe777777667777777777777777776777777777777777777777777777777777777777777bbccc77777777edddddd
                77777777777777777777777777777777bceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebe777777777777777777777777777667777777777777777777777777777777777777777bbccc7777777eedddddd
                77777777777777777777777766677777bceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeebe77777777777777777777777777776777777777777777777777777777777777777777bbccc7777777ebdddddd
                77777777777777777777777777777777bceeeeeeeeeeeeee4eeeeeeeeeeeebeeeeeeeebb77777777777777777777777777777667777777777777777777777777777777776677bbccc7777777ebdddddd
                77777777777777777777777777777777cceeeeeeeeeeeeee4eeeeeeeeeeebbeeeeeeeeeb77777777777777777777777777666677777777777777777777777777777777767777bbccc7777777ebdddddd
                77777777777777777777777777777777c4eeeeeeeeeeeeee4eeeeeeeeeeeeeeeeeeeeeebb7777777777777777777777777777777777777777777777777777777777776667777bbccc777777ebdddddd.
                77777777777777777777777777777777ceeeeeeeeeeeeeee4eeeeeeeeeeeeeeeeeeeeeeeb7777777777777777777777777777777777777777777777777777777777777777777bbccc777777ebeeebbbb
                77777777777777777777777777777777ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeeeebb777777777777777777777777777777777777777777777777777777777777777777bbbcc77777e7edbbdddd
                777777777777777777777777777777ccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebceeeeb7777777777777777777777777777777777777777777777777777777777777777777bbcc77777ebeddddddd
                bbbbbbbbbbbb77777777777777777ccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4cceeb7777777777777777777777777777777777777777777777777777777777777777777bbcc7777eebeddddddd
                bb77ccccccccccb7777777777777cc7beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4cceb77777777777777777777777777777777777777777777777777777777777777777777bccc777ebbdddddddd
                77ccc777777777cccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4bccb77777777777777777777777777777777777777777777777777777777777777777777bccc777ebddddddddd
                77778888888888888888888888888bbeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44ecb77777777777777777777777777777777777777777777777766677777777777777777bccc77eebddddddddd
                77778bbbbbbbbbbbbbbbbbb7777777beecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4bcb77777777777777777777777777777777777777777777777777777777777777777777bccc7eebbddddddddd
                7bbbbbb7bbbbbbbb7777777bbb777bbecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc77777777777777777777777777777777777777777777777777777777777777777777bccb7ebbdddddddddd
                77777bbbbbbbbbbbbbbb777777777b.eceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeece7777777777777777777777777777777777777777777777777777777777777777777bccb7ebddddddddddd
                7777777777888777777bbbbbbbbbbbccceeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeece7777777777777777777777777777777777777777777777777777777777777777777bcbbebbddddddddddd
                bbbbbbbb88bbb77bbbbbbbbbb77bcceeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecbe777777777777777777777777777777777777777777777777777777777777777777bbbeebdddddddddddd
                77bbbb77777777bbbbbb7777cccccceeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecbe77777777777777777777777777777777777777777777777777777777777777777777eebddddddddddddd
                777777bbbbbbbb77777b7777eeeeeeceeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc.e7777777777777777777777777777777777777777777777777777777777777777777ebdddddddddddddd
                7777777777777788877b777beeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebeeeeeeeeeeecccce77777777777777777777777777777777777777777777777777777777777777777eebdddddddddddddd
                7777777bbbbbbbbbbbbbb7bbeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebb4eeeeeeeeeececb7777777777733777333377777777777777776677777777777777777777777777eebdddddddddddd...
                bbbbbbbbb77bbbbb77777bbee44eeeeeeeeeeeeebbeeeeeeeeeeeeeeeeeeebb4eeeeeeeeeeceecc777777777733333333777777777777777777667777777777777777777777777e7bddddddddbbbbbbb
                777777777788888bbb77bbe.4.4eeeeeeeeeeeeebeeeeeeeeeeeeebeeeeeeeb4eeeeeeeeeecb.cecc777773333bbbbbb333337777777777777766777777777777777777777777ee7bddd...bbbdddddd
                77777777777bb7788887be.444eeeeeeeeeeeee44ee4eeeeeeeeeebeeeeeeeb4eeeeeeeeeeececcec77777aabaaaabbabaa37777777777777776777777777777777777777777eebbddbbeeeddddddddd
                7bbbbbbbbbbb7777777be.44ceeeeeeeeeeeeee4bbe4eeeeeeeeeebeeeeeeeb4eeeeeeeeeeeececee7777773bbbaabbaaa337777777777777767777777777777777777777777e7beeeeeeddddddddddd
                777bbbbbbbbbbbbbb778eeeeceeeeeeeeeeeee4bbe4eeeeeeeeee4beeeeeeeb4eeeeeeeeeeeeecceee77777333aaaaaa3777777777777777767777777777777777777777777ee7bddddddddddddddddd
                b7777b8bbbbb7888888eeeeeeeeeee444444e4bee44eeeeeeeeee4beeeebccb4eeeeeeeeeeeeeeceeeb7777777aa3aa37777777777777777777777777777777777777777777e7bbddddddddddddddddd
                bbbbbbb88bb88bbb7eeeeeee444444ee4ee4e4be44eeeeeeeeee4beeeeeebcb4eeeeeeeeeeeeee.eeeb77777773333a37777777777777777767777777777777777777777777e7bdddddddddddddddddd
                77777777bbbbb777beeeeeeeccc444444eeee4beeeeeeeeeeeee4beeeeeeeb.4eeeeee.eeeeeeeeeeecb777777367333777777777777777776677777777777777777777777e7bbdddddddddddddddddd
                777777777777777bbeeeecceecc4.eccceeeeeeeeeeeeeeeeeee4beeeeeeebb4eeee4cccceeeeeeeeecb77777776733777777777777777777667777777777777777777777eebbddddddddddddddddddd
                7777777777777bbbeeeecceee444.eeeeeeeeeeeeeecee44eeee4eeeeeecccb4eee.cc77ceeeeeeeeecb77777776763777777777777777666777777777777777777777777e7bdddddddddddddddddddd
                77777777777bbbeeccccceeeeeeeeeeeeeeeeeeeeeeceeeeeee44ebeeeccccb4eeee7777ceeeeeeeeecb7777777616777777776666666677777777777777777777777777eebbdddddddddddddddddddd
                777777777eeebeecccccc7eeeeeeeeeeeeeeeeeeeecceee4eeec4eeeecc77cb4eeee77777ceeeeeeeeccb77777761677777766667777777777777777777777777777777eebbddddddddddddddddddddd
                77777777777ee7777777ccceeeeeeeeeeeeeee7ccccceeeeeee4beeecc777c7beeee77777cceeeeeeeecb7777776167777777777666667777777777777777777777777ee7bdddddddddddddddddddddd
                77777777777e77777777777cccceeeeeeeeeccc7777cceeecce4beeece777ccbbeee777777cc7eeeeeecb777777616777777777777777777777777777777777777777eebbddddddddddddddddddddddd
                77777777777777777777777777ceeeeeecccc7777777cccccc74bee7c777777bcbe77777777ec7eeeeecb77777761677777777777777777777777777777777776667eebbdddddddddddddddddddddddd
                7777777777777777777777777777bbeccce7777777777cccc774bee77777777bccce77777777cc777eecbb7777761677777777777777777777777777777777667677ebb.dddddddddddddddddddddddd
                777777777777777777777777777bcccceee777777777777c7777beee7777777bccce7777777777ccc7ee.b777776167777777777777777777777777777766676677ebb.ddddddddddddddddddddddddd
                77777777777777777777777777bbcbeeeee77777777777777777bbbe77777777bccb777777777777ccce.b777776767777777777777777777777777766677767777ebb.ddddddddddddddddddddddddd
                777777777777777777777777bbbcc7eee7777777777777777777bbee77777777bccb777777777777777cc.b777767667777777777777777777777666777766777eebbb.ddddddddddddddddddddddddd
                7777777777777777777777bbbb77777777777777777777777777bcbe777777777bcbe7777777777777777eb77776766777777777777777777777667777767777eebbdddddddddddddddddddddddddddd
                777777777777777777777bb77777777777777777777777777777bbb77777777777bbee777777777777777ee66666766677777777777777777766777776677777e7bdddddddddddddddddddddddddd.bb
                77777777777777777777777777777777777777777777777777777bb77777777777bb7777777777777777777bb6666677777777777777777666777666677777ee7bddddddddddddddddddddddbbbbbbbd
                666776666777777777777777777777777777777777777777777777777777777777bb777777777777777777777777766777777777777777677776666777777ee7bbdddddddddddddddddbbbbbdddddddd
                7666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777677777777777776677776667777777ee7bbdddddddddd.bbbbbbbbdddddddddddd
                777667766666677777777777777777777777777777777777777777776666666667777777777777777777777777777777777777777666777766677777777ee7bdddeeebbbbbbbbddddddddddddddddddd
                7777766777777667666666666666666777766666666667766666666667777777766667777777777777777777777777777777777777766766777777777eeebbbeeeebbddddddddddddddddddddddddddd
                776666666666666666677777777777766666666666666666666667666666777777777666777777777777777777777777777777777777667777777777eeeeeeeedddddddddddddddddddddddddddddddd
                777777777777777777766666666666666666666667766666677777777766666666667666666666666667777777777777777777766666666666666666ebbddddddddddddddddddddddddddddddddddddd
                7777777777777777777777777777777777777777776677777777777777777777777777777777777777776666666666666666666666677776666666666ddddddddddddddddddddddddddddddddddddddd
    """))
    wood2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . e e e e . . . . . . . . . 
                    . . . e e e e . . . e e . . . . 
                    . . . . . . e e e e e . . . . . 
                    . . . . . . e e e e e e e . . . 
                    . . . e e e e e e e e e . . . . 
                    . . e e e e e e e e e . . . . . 
                    . . . . e e e e e e e e . . . . 
                    . . . . e e e e e e e e e e e . 
                    . . . . e e e e e e . . . . e . 
                    . . . e e e e e e e . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.wood)
    wood2.set_position(54, 74)

def on_on_overlap(sprite, otherSprite):
    scene.set_background_image(img("""
        ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbddbccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbbbbccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888b88ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888b88ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88b88888888ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88bb8888888ccccccccccccccccccccccccccccccccbbbbbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc8888b888888ccccccccccccccccccccccccccccccccbbbcccccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc88888888888ccccccccccccccccccccccccccccccccbbbcbcccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbcccccccccccccccccccccccccccccccccc8888888888ccccccccccccccccccccccccccccccccccbbbbdccccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbcccccccccccccccccccccccccccccc44445555544445555555dbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.bbbcccccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4ddddddddddd4dddddd5dddddddddddddddddddddddddddddb.b66bbbcccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccccbbbdddddddddddddddddddddddddddddd44dd55555d4444445dd5ddddddddddddddddddddddddddddcbcc6666bbbcccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccccbb.bbcddddddddddddddddddddddddddddd545ddd55555ddddd55d4ddddddddddddddddddddddddddddcbcc666666bbbcccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccccbbb6cbbcddddddddddddddddddddddddddddd555d55d115555555d5d4ddddddddddddddddddedddddddddcbcc66666666bbbcccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccbbb666cbbcdddddddddddddddddddddddddddddd55d55551111dd55dd54ddddddddddddddddddebddddddddcb.c6666666666bbbcccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccbbb66666cbbcdddddddddddddddddddddddddddddd5555dd555551115dd44ddddddddddddddddddebddddddddcbbcc66666666666bbccccccccccccccccccccccccccccc
                ccccccccccccccccccccccbbb6666666cbbddddddddddddddddddddddddddddddd5114444dddddd55d54dddddddddddddddddddebddddddddcbbccc666666666666bbccccccccccccccccccccccccccc
                ccccccccccccccccccccbbb66666666ecbbddddddddddddddedddddddddddddddd55111dddd5555dd111dddddddddddddddddddebdddddddddbbccccc66666666666bbbccccccccccccccccccccccccc
                ccccccccccccccccccbbb6666666cccccbbdddddddddddddbeddddddddddddddddd55511d555d551115ddddddddddddddddddddebdddddddddbbcecccc666666666666bbbccccccccccccccccccccccc
                cccccccccccccccccbbd66666ccccbbbcbbdddddddddddddbeddddddddddddddddddd551111111115ddddddddddddddddddddddebdddddddddbbccbccccb666666666666bbbccccccccccccccccccccc
                cccccccccccccccbb6666666cccbbbbecbbdddddddddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddedddbbccbeecccb6666666666666bbcccccccccccccccccccc
                cccccccccccccbb6666666ccccbebbeecbbdddddddedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddedddbbccccccecccc6666666666666bbccdccccccccccccccc
                cccccccccccbb6666666ccccbeecceeecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccccecc.ccccc6666666666666bbcccccccccccccccc
                cccccccccbb666666666cbbccccceeeecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbceeecc.cccb66666666666666bbcccccccccccccc
                cccccccbb6666666666bbcceccceeeebcbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbccceeecccbbbb6666666666666bbbcccccccccccc
                cccccbb6666666666bbcceccceeeeebecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbcceeeeccccbeebbbbb6666666666666bbbcccccccccc
                cccbb6666666666cccccccceeeeccccecbbddddddbedddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbedddbbccbbeeeeeccceeeeebbb6666666666666bbccccccccc
                cbbd666666666cccccccceeeeecccccbcbbddddddbedddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebddddbeddbbeeebbbbeeeebcceeccccbbb6666666666666bbccccccc
                bd666666666cceecccceeeeecccccbbbcbbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbceeeebbbbeebbcceeccecccbb6666666666666bbccccc
                666666666cceeccccceeeeeccecbbbeecbbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbceeeeeebbbbeeeccceeceeccbbb66cc666666666bbccc
                6666666ccccccccceccceccbbebbeeeccebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbeeeeeeeeebbbbeeeccccccecccccb.cccc66666666bbc
                66666ccc.eeccccccbcceebbbbeeeeecccbddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4ee4eeeeebbbbebeeeeeeeeccccbbcccc666666666b
                666bccceeeccecceecbbbbbbeeeeee4eeebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eee44eeeeebbbbeeeeeeeeececccbccccc66666666
                6bccceeccceeeeeccbbbbbeeeeee44eeeebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeee44eeeeebbbbebeeeeeecceccebcccc6666666
                cccccccceeeeeccbbbbeeeeeee44eee4eebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeee44eeeeebbbbeeccccceccceeebccc666666
                cecceeeeeeccccbbbeeeeeee44eeeee4eebddddddbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeeeee4eeeeeebbbbeeecccccceeeeebbccc666
                ccceeeeeccbbbbbeeeeeee44eeeeeee4eebddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eeeeeeeeee44eeeeeebbbbeeeccceeeccccebcccc6
                ecceecccbbbbbe4eeeee44eeeeeeeee4eebbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eedeeeeeeeee44eeeee4bbbbeebcceeececeeecc.c
                ecceeebbbbeeee4eeee4eeeeeeeeeed4eebbdddddddddddddddddddddeeeeeddddddddddddddddddddddddddddddddddddddddddbddddbeddbbee4eedeeeeeeeeeee44eee4eebbbbbeeceeeccceeeccc
                eccebbbbeeeeee4eeeeeeeeeeeeeeed4eebbdddddddddddddddddddee99eeeeeeeeeeeeeeeeeeeddddddddddddddddeeceeeddddbddddbeddbcee4eedeeeeeeeeeeeee4ed4eeeebbbbeecceeccceeccc
                ecbbbbeeeeee4e4deeeeeeeeeeeeeed4eebcdddddddddddddddddde9999999999999999111111eeeeeeeeeeeeeeeee99cddeddddbddddbeddbcee4eedeeeeeeeeeeeeeeed4eeeeeebbbbeccceecceccc
                bbbbeeeeee44ee4deeeeeeeeeeeeeed4eebcdddddddddddddddddde999111119999999111bbbb111119999999999999ccddeddddbddddbeddbcee4eeeeeeeeeeeeeeeeeed4eeeeeeeebbbbbcccccecec
                bbeeeeeee4eee4e4eeeeeeeeeeeeeed4eebcdddddddddddddddddee99911bbb19991111111111111111999999999999cdddeddddebdddbeddbcee4eeeeeeeeeeeeeeeeeed4eeeeeeeeeebbbbeeeeecec
                eeeeeee44eeeeee4eeeeeeeeeeeeeee4eebcddddddddddddddddde111111b1bb1991111111111111111999999999999cdddedddddedddbeddbce44eeeeeeeeeeeeeeeeeed4eeeeee4eeeeebbbbeeecec
                eeeee44eeeeeeee4eeeeeeeeeeeeeee4eebcddddddddddddddddde1111111111199111111111111111bb99999999999cdddedddddddddbeddbceee44eeeeeeeeeeeeeeeed4ee4eeee44eeeeebbbbecec
                eeee4eeeeeeeeee4deeeeeeeeeeeeee4eebcddddddddddddddddde111111111119991b111111111111b999999999999cdddedddddddddbeddbcbeeee44eeeeeeeeeeebbbd4ee4eeeeee4eeeeeebbbbcc
                ee44eeeeeeeeeee4ddebbeeeeeeeeee44ebcddddddddddddddddde111111111199999bbbbb1111b1111999911111199cdddedddddddddbeddcccbbeeee4eeeeeeeeee1cbd4ee4eeeeeee44eeeeeebbcc
                e4eeeeeeeee4444.4dbbbeeeeeeeee44eebcddddddddddddddddde11111bb1119999999911111bb9999111111111199cdddedddddddddbeddcbcccbbeee44eeeeeeebbc1d4be4eeeeeeeee4eeeeeebcc
                eeeeeeeeeee4..bb4dbbbeeeeeee44eee.bcdddddddddddddddddde11111bbb9999999999991bb999991111bbb11199cdddedddddddddbeddcc66cccbbeee44eeeeebcccc11bb4eeeeeeeee44eeeeecc
                eeeeeeeeeee4bbbb4cccbeeeeee4eeeebccbdddddddd8888dddddde111bbb993999999999999b999bbbbb1111111199bdddedddddddddbeddbc666bccebbeee44eeebbbccccbbbeeeeeeeeeee4eeeeec
                e4eeeeeeeeebbcb11cdcbbeee44eeebbccbbdddddddffffffddddde99999933b3939999999999999b1111111111199cbdddedddddddddbeddbc66666bcbebbeee4eeeebbdcccbbeeeeeeeeeeeeee4eec
                e4eeeeeeeeeeb1ccc4dbbeee4eeebbeccccbdddddddddbbddddddde9999933b3b339999999999999b1111111111199cbdddedddddddddbeddbc6666666bbbbbbeeeeeeeed4bcbbeeeeeeeeeeeeee4eee
                e4eeeeeeeeeebcccb4deeeeeeeebeccc66ccdddddddddbbddddddde999999b3b3333999999999999bb11111b111199cbdddedddddddddbeddbc666666666bbbbbbeeeeded4bbbeeeeeeeeeeeeeee4eee
                e4edeeeeeeeebcbbb4deeeeeebbbbc666cccdddddddddbbddddddde99999333793999977779999999111111b111199ccdddedddddddddbeddbb6cc66666666bbbbbeeeedd4e4beeeeeeeeeeeedee4eee
                e4edeeeeeeeebbbbe4deeeebbeb66666cc6cdddddddddbbddddddde999999997999999787899999999911bbb9999996cdddedddddddddbeddbb66c6666666666bbbbbee.d4e4eeeeeeeeeeeeedee4eee
                e4edeeeeeeeeebeee4ddeebebb666666c66bdddddddddbbddddddde6696666977999666666699999999666666666999cdddedddddddddbeddbb6bb666666666666bbbbbee4eeeeeeeeeeeeeeedee4eee
                e4edeeeeeeeeeeeeee4dbbbb66666666666bbddddddddbbddddddde777777cc77cc7777777766666677777777777777cdddedddddddddbeddbb66666666666666666bbbbb4eeee4eeeeeeeeeedee4eee
                e4edeeeeeeeeeeeeddbbbb6666666666666bbddddddddbbbbbdddde77777ceeeeeec777777777777777777777777777cdddedddddddddbeddbb6666666666666666666bbb4beeee44eeeeeeeedee4eee
                e4eeeeeeeee4eedddbeb6666666666666ccbbddddddbbbbbbbbddde777777cccccc7777777777777777777777777777cdddedddddddddbeddbb666666666666666666666bbbbbeeee44eeeeeedee4eee
                e4eeeeeeee4eeddbbbb6666666666666666bbdddddbddbbbbbbbdde7cccccbccccbbcccccbbbbbbbbbbbbbbbbccccccbdddedddddddddbeddbb66666666666666666666666bbbbbeeee44eeeeeee4eee
                e4eeeeee444eebbbb666666666666666666bbddddbdd1bbbbbbbbdeccddddbcdccbdddddccccccccccccccccccdddddccbdedddddddddbedcbb6c6666666666666666666666bbbbbeeeee44eeeee4eee
                e4eeeee4eeebbebe666666666666666666bbbdddbbdbbbccbbbbbdecdddddbcdccbdddddddddddddddddddddddddddddcccbdddddddddbedcbb6bb66666666666666666666666bbbbbeeeee44eee4eee
                e4eeee4eeebebb66666666666666666666bbbdddbddbbcccccbbbdeeddddddbbbbdddddddddddddddddddddddddddddddeeedddddddddbedcbb6666666666666666666666666666bbbbbeeeee44e4eee
                ee4e44eebbbb666666666666666666666666bdddb1bbbcbbbcbbbdddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddbedcbb666666666666666666666666666666bbbbbeeeee44eee
                eee4eebbbbe6666666666666666666666666bdddbdbbbcbbcbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddbedcbb66666666666666666666666666666666bbbbbeeeeeeee
                ee4eebebee66666666666666666666666666bdddbbbbbccccbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddbedcbb6666666666666666666666666666666666bbbbbeeeeee
                eeebbbbe6666666666666666666666666666bdddbbbbbbbb1dd1bdddddddddddddddddddcccccddddddddddddddddddddddddddddddddbedcbb666666666666666666666666666666666666bbbbbeeee
                ebbbbecc666666666666666666666666666bbdddcbbbbbbddbbbcddddddddddddddddddcbb1bccddddddddddddddddddddddddddddddbdeddbb66666666666666666666666666666666666666cbbbbee
                bbbe.cc6666666666666666666666666666bbbddccbbbbb1bbcccddddddddddddddddddccccb1ccddddddddddddddddddddddddccccccccccbbc66666666666666666666666666666666666666ccbbbe
                b..cc6666666666666666666666666666666bbcccccbbbbccccddddddddddddddddccddcbcdccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc66666666666666666666666666666666666666ccbe
                6ccc666666666666666666666666666666cbbbbbbbccccccbbbbbbbbbbbbbbbbbbccccccbcbbccdddddddddddddddddddddbddddddbdddedcbbcbbc66666666666666666666666666666666666666ccc
                666666666666666666666666666666666cbdbbdbddddbddddddddddbddddddddddccccdcbcdddddddddddddddbdddddddddbddddddbddddecbbcddbc6666666666666666666666666666666666666666
                66666666666666666666666666666c6ccbdcbbcbbdddbbdddddddddbddddbbbbbbbbbcccbcdddddbbbbbbbbbdbddddddddddddddddbdddddcbbcdddbcc66666666666666666666666666666666666666
                66666666666666666666666666666ccbbddcbbcdddddddddddddddddddddb999999999ccccbbddbb99999bbbddddddddddddddddddddddddcbbcddddbb66666666666666666666666666666666666666
                6c666666666666666666666666666cbddddcbbcdddddddddddddddddddddb999991919999999999999999bcbddddddddddddddddddddddddcbbcddddddb6666666666666666666666666666666666666
                cc66666666666666666666666666cbdddddcbbcdddddddddddddddddddddbb99199999999999999999b9cccbddddddddddddddddddddddddcbbcdddddbdbcc6666666666666666666666666666666666
                c66666666666666666666666666cbddddddcbbcdddddddddddddddddddddb99999999999999999999999cccbddddddddddddddddddddddddcbbcddddddddbbc666666666666666666666666666666666
                6666666666666666666666666ccbddddddddbbcdddddddddddddddddddddb99999999999999999999999ccccddddddddddddddddddddddddcbbcddddddddddbcc6666666666666666666666666666666
                bb6666666666666666666666cbbdddddddddbbcdddddddddddddddddddddbd999999bbbbbbbbb99999b9ccdcdddddddddddddddddddddddddbbcdddddddddddbbc666666666666666666666666666b66
                b6666666666666666666666cbdbdddddddddbbcdddddddddddddddddddddbbbd99c9cccccccccc99999cccccddddddddddddddddddddddddbbbddddddddddddbdbc6c666666666666666666666666bb6
                6666666666666666666666ccddbdddddddddbbcdddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbccbdddddddddddddddddddddddddbbddddddddddddbddbccb66666666666666666666666cbb
                66666666666666666666bbccddddddddddddbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddbcc666666666666666666666666cc
                6666666666666666666cbbddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeebbcddddddddddddddddddbc6666666666666666666666666
                666666666666666666cbbdddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeebbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeebcbddddddddddddddddddbcc66c66666666666666666666
                6b666666666666666cbdddddddddddddddddbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebcbbddddddddddddddddddbbc6cbb666666666666666666
                bb6666666666666ccbddddddddddddddddbbbbeeeee444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbcbbbdddddddddddddddddddbcccb666666666666666666
                bb666666666666ccbddddddddddddddddbbbcbee4444eeeeeeeeeeeeeedeee444444444444de44444444444eeee444444444444444eeeeeebbcebbbbddddddddddddddddddbbcb666666666666666666
                cb66666666666cbbddddddddddddddddbbebcbee4eeeeeeeeeeeeeeeeedeeeeeeeeeeeeee4de4eeeeeeeeeeedeeeeeeeeeeeeeeeee444eebebceebbbbdddddddddddddddddddbc666666666666666b66
                c66666666666cbdddddddddddddddddbbebecbee4eeeeeeeeeeeeeeeeedeeeeeeeeeeeeee4de4eeeeeeeeeeedeeeeeeeeeeeeeeeeeee44eeebceeebbbbddddddddddddddddddbbcc6666666666666cb6
                6666666bc66cbdbbddddddddddddddbbbbeecbee4eeeeeeeeeeeeeeeeedeeeeeeeeeeeeee4de4eeeeeeeeeeedeeeeeeeeeeeeeeeeeeee44eebceeeebbbbdddddddddddddddddbdbbc666666666666cbb
                6666666bc6cbdddddddddddddddddbbbeeeecbee4eeeeeeeeeeeeeeeeedeeeeeeeeeeee444d44eeeeeeeeeeedeeeeeeeeeeeeeeeeeeeee4ebbceeeeeebbbddddddddddddddddbdddbc666c6666666666
                666666bbccbdddddddddddddddddbbbeeeeecbeee4eeeeeeeeeeeeeeeedeeeeeeeeeee44edd4eeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeee4ebbceeeeeeebbbddddddddddddddddddddbcc6cbb66666666
                66666bbcbbdddddddddddddddddbbbeeeeeecbeee4eeeeeeeeeeeeeeeedeeeeeeeeeeee4edddeeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeee4ebcceeeeeeeebbbbdddddddddddddddddddbbcccb66666666
                66666bcbddddddddddddddddddbbbeeeeeeecbeee4eeeeeebbbeeeeeeedeeeeeeeeeeee4ede4eeeeeeeeeeeedeeeeeeeeebbbeeeeeeeee4ebcceeeeeeeeebbbbddddddddddddddddddddbccb66666666
                66666bbdbdddddddddddddddbbbeeeeeeeeecbeee4eeeeeebcbeeeeeeedeeeeeeeeeeee44de4eeeeeeeeeeeedeeeeeeeeebcbeeeeeeee4eebceeeeeeeeeeebbbbddddddddddddddddddddbcc66666666
                6666cbdddddddddddddddddbbbbeeeeeeeeec.bee4eeeeeebbbeeeeeeedeeeeeeeeeeeee4bbbbbbbeeeeeeeedeeeeeeeeebbbeeeeeeee4eebceeeeeeeeeeeebbbbddddddddddddddddddbdcbc6666666
                66ccbdddddddddddddddddbbbbeeeeeeeeeeccbee4eeeeeeeeeeeeeeeedeeeeeeeeeeeee4ccccccbbeeeeeeedeeeeeeeeeeeeeeeeeeee4eebceeeeeeeeeeeeebbbbdddddddddddddddddddddbcc66666
                6cbbdddddddddddddddddbbbbeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4bbbbbbbbeeeeeeedeeeeeeeeeeeeeeeeeeee4eebcceeeeeeeeeeeeeebbbdddddddddddddddddddddbbc6666
                cbddddddddddddddddddb.cbeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4eeeeeeeeeeeeeeddeeeeeeeeeeeeeeeeeeee4ebbcceeeeeeeeeeeeeeebbbbdddddddddddddddddddddbc666
                bddddddddddddddddddbccbeeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeee4deeeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeee4ebbcceeeeeeeeeeeeeeeebbbbdddddddddddddddddddddbcc6
                dbddddddddddddddddbcbbeeeeeeeeeeeeeeccbeee4eeeeeeeeeeeeeeedeeeeeeeeeeeeeeddeeeeeeeeeeeedeeeeeeeeeeeeeeeeeeeb44ebbcceeeeeeeeeeeeeeeeebbbbdddddddddddddddddddddbbc
                dbdddddddddddddddbbcbeeeeeeeeeeeeeeeecbeee44eeeeeeeeeeeeeedeeeeeeeeeeeeeeedeeeeeeeeeeeedeeeeeeeeeeeeeeeeeee44eebbcceeeeeeeeeeeeeeeeeebbbbddddddddddddddddddddbdb
                ddddddddddddddddbcceeeeeeeeeeeeeeeeeecbeeee44444444444444edeeeeeeeeeeeeeeedeeeeeeeeeee4deeeeeeeeeeeeeeee4444beebbceeeeeeeeeeeeeeeeeeeebbbbdddddddddddddddddddbdd
                dddddddddddddddbcceeeeeeeeeeeeeeeeeeecbeeeeeeeeeeeeeeeeeeedeee4444444444eedeeee4444444eeeeeeeeee444444444eeeebebbceeeeeeeeeeeeeeeeeeeeebcbbddddddddddddddddddbdd
                dddddddddddddddccbeeeeeeeeeeeeeeeeeeecbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedeebbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbceeeeeeeeeeeeeeeeeeeeeebcbbdddddddddddddddddddd
                ddddddddddddddccbeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccc.ceeeeeeeeeeeeeeeeeeeeeeeccbbddddddddddddddddddd
                dddddddddddddccbeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccc9ccccccccccccccccccccccccffff111111111111111cceeeeeeeeeeeeeeeeeeeeeeebcbbbdddddddddddddddddd
                ddddddddddddbceeeeeeeeeeeeeeeeeeeeeeeccfffffffffff11111111111ffffffffffff991111111111fffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbdddddddddddddddd
                dddddddddddccbeeeeeeeeeeeeeeeeeeeeeeccfffffffffff111111111111ffffffffffff111111111111ffffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbddddddddddddddd
                ddddddddddcceeeeeeeeeeeeeeeeeeeeeeeccfffffffffff1111111111111ffffffffffff111111111111fffffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbdddddddddddddd
                dddddddddccbeeeeeeeeeeeeeeeeeeeeeec.bfffffffffffb11111111111fffffffffffff111111111111ffffffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeebcbbbbddddddddddddd
                ddddddddccbeeeeeeeeeeeeeeeeeeeeeeccbfffffffffffb111111111111ffffffffffff9111111111111fffffffffffffffff11111111111111ccbeeeeeeeeeeeeeeeeeeeeeeecccbbbdddddddddddd
                dddddddcceeeeeeeeeeeeeeeeeeeeeeeccbfffffffffffb111111111111fbfffffffffff9111111111111bfffffffffffffffbf1111111111111bccbeeeeeeeeeeeeeeeeeeeeeeebccbbbbdddddddddd
                ddddddcceeeeeeeeeeeeeeeeeeeeeecccbfffffffffffb1111111111111fbffffffffffffb11ffff9999ffbfffffffffffffffbfffffffffffffffccceeeeeeeeeeeeeeeeeeeeeeebbccbbbddddddddd
                dddddcceeeeeeeeeeeeeeeeeeeeeecccbfffffffffffbffffffffffffffbfffffffffffffbffffffffffffbf111111111111111bbfffffffffffffcccceeeeeeeeeeeeeeeeeeeeeeeebcccbbdddddddd
                ddddcceeeeeeeeeeeeeeeeeeeeeecccb11111111111bfffffffffffffffb1111111111111bfffffffffffffbf1111111111111111bfffffffffffffcccbeeeeeeeeeeeeeeeeeeeeeeeebbcccbddddddd
                dddccbeeeeeeeeeeeeeeeeeeeeecccbb1111111111bfffffffffffffffb11111111111111bffffffffffffffb11111111111111111bfffffffffffffcccceeeeeeeeeeeeeeeeeeeeeeeeebbcccdddddd
                ddcceeeeeeeeeeeeeeeeeeeeeccccbb1111111111bffffffffffffffffb11111111111111fffffffffffffffbf11111111111111111bbfffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbccbdbdd
                dbceeeeeeeeeeeeeeeeeeeeececcbb11111111111ffffffffffffffffb111111111111111ffffffffffffffffb1111111111111111111bfffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbcccdbb
                bbeeeeeeeeeeeeeeeeeeeeececcbb11111111111fffffffffffffffff1111111111111111ffffffffffffffffff1111111111111111111ffffffffffffbcccceeeeeeeeeeeeeeeeeeeeeeeeeebbbccdb
    """))
    sprites.destroy(soap2)
    game.show_long_text("That's better.", DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        game.show_long_text("He must be close.", DialogLayout.BOTTOM)
        game.show_long_text("Lets look in the fridge.", DialogLayout.BOTTOM)
        levelFour()
sprites.on_overlap(SpriteKind.player, SpriteKind.soap, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.show_long_text("Bread, huh? This is definitely a clue.",
        DialogLayout.BOTTOM)
    sprites.destroy(brad)
sprites.on_overlap(SpriteKind.player, SpriteKind.bred, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(wood2)
    scene.set_background_image(img("""
        99999999999999977777777777777777777777777777777777777777777777777777777776777777777777777777999999999999999999999998866ccccccccccccccccccccccccccccccccccccccccc
                999999999966667.6777777777776667777777776677777777777777777bb77777776666667777777777777777767999999999999999999988866cccccccccceeccccccccccccccccccccccccceccccc
                999999999967777667777777667777777777777667777777777777777777b777b777777777777777777777777777b799999999999999988886cceccccccccceccccccccccccccceeccccccceeecccccc
                9999999999967776bbbb76667777777777777667777777777777b77777777777b777777777777777777777777777bb799999999999988866cccecccccccccecccccccccccccceeccccccceecccccccce
                99999999997.6bbb666b667777777777777777777777777bbbbb77777777777777777777777777777777777777777b6999999999988866cccceccccccccceccccccccccccceeccccccccecccccccccec
                99999999977777777777b777777777777777777777bbbbb7777777777777777777777777777777777777777777777b67999999998866cccccecccccccceecccccccccccceecccccccceecccccccccecc
                9999999977777777777bb777766677777777777777777777777777777777777777777777777777b77777777777776667999999886ccccccceccccccccecccccccccceeeecccccccccecccccccccceccc
                999999997777b77777777777767777777777777777777777777777777777777777777777777777b7777777667776.6779999886cccccccceccccccccecccccccceeeccccccccccceeccccccccccecccc
                999999997777b777777777766777777777777bb77777777777777777777777777777777bbbbb77b777777667777776799988ccccccccceeecccccccceccccccceccccccccccccceccccccccccccccccc
                999999997777777777777767777777777777777b77777777777777777777777777777777777777b7777776777bbbbb99998ccccccccccecccccccccccccccccccccccccccccccccccccccccccccccccc
                9999999677777777777776677777777777777777bb7777777777777777777777777777777b7777b77777677777777796688ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                99999996777bb77777777777777666777777777777bb7777777776b77777777777777777bb777b77777667777777779968eddddddddddddddddddcccccccccccccccccdddddddddddddddddddddddddd
                9999999677777b777777777777777767777777777776bbb7777666777777777bbbb7777777777b77666777777777779968ebbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddbbbbbbbbbbbbbbbbbbbbdd
                999999966777777b7777777777777777777777777777666bbb66777777777777777bbbbbbbbbb777777777777777777968dddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddd
                999999996777777b77777777777777777777777777777777777777777777777777777777777777777777777777777b796edbdddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddd
                99999999677777bb77777777777777777777777777777777777777777777777777777777777777777777777777777b668edbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                9999999966777777777777777777777777777777777777777777777777777777777777777777777777777777777766698edbddddddddddddddddddddddddddddddddddddddbdddddddddddddddbddddd
                999999999667767777777777777777777777777767777777777777777777777777777777777777777777777666b6bb798edbddddddddddddddddddddddddddddddddddddddbdddddbdddddddddbddddd
                999999999777766bb777777777777777777b..666777777777777777777777777777777777777777777777767bbb77998edbdddddddddddddbbbbdddddbdddddddddddddddbdddddbdddddddddbddddd
                99999999997777667777777777777777776b66677777777777777777777777777777777777777777777b7776b77779998edbbdddddddddddddddddddddddddddddddddddddbdddddbdddddddddbddddd
                999999999977777667777777777777777bb777777777777777777777777777777777777777bb77b777bb7776b99999998eddbdddddddddddddddddddddddddddddddddddddbdddddbddddddddddddddd
                999999999777777766777777777777bbb6677777777777777777777777777777777777777b7777777777776b999999998eddbdddddddddddddddddddddddddddddddddddddbdddddbddddddddddddddd
                999999999b7777777667777bbbbbbb7776b77777777777767777777777777777777766777777777777777769999999998eddbdddddddddddddddddeeeeeeeeedddddddddddbdddddbddddddddddddddd
                999999999b7777777766677666777777bb77777777777b76777777777777777777776677777777777777bb67999999998eddbddddddddddddeeeeeeeeeeeeeeeeeddddddddbdddddbddddddddddddddd
                999999999b77777777776666776666bb67777777777777b677777777777777777777e6777777777777776667999999998eddbddddddddddeeeeeeeeeeeeeeeeeeeedddddddbddddddddddddddddddddd
                999999999b7777777777777bb77bbb777777777e777777b677777777777777777777e677777777b777777666999999988eddbddddddddee6666666666666666666eeddddddbddddddddddddddddddddd
                999999999bb77777777777777bb77777777766b6777777b67777777bbbb77b7677666677777777b777777776999999986eddbdddddddde6666666666666666666b6eddddddbddddddddddddddddddddd
                9999999999bb77777777777777777777777777b67777776b7777bb777777bb76667ee677777777b77777777699999bb86eddbdddddddde6666666666666666666bbeddddddbddddddddddddddddddddd
                99999999997777777777777777777777777777b67777b666b777b77777bb77667b7e7677777777b777777776999888886eddbddbddddde66666666666666666666beddddddbddddddddddddddddddddd
                99999999999977777777777777777777777677be7777b666777777777777776677bb767777b667b777777796998bb888beddbddbddddde66666666666666666666beddddddbddddddddddddddddddddd
                99999999999697777767777777777777776677be7777b6ee6777777777777666667ebb7766677b777777779698888887beddbddbddddde66666666666666666666beddddddddddddddddddddddddeeee
                99999999999699977777777777777777777777be7777b6ee667777777777667e777e77b77777b7777777766688b77b777bbdbddbddddde66666666666666666666bedddddddddddddddddddddddeeeee
                99999999999969997777777777777777777777be7777bee6667777776666677ee77e6667766b7777777668888777b7b77eddbdddbdddde66666666666666666666bedddddddddddddddddddddddebbbb
                9999999999999666b777777777777777777777be77bbeee666666777676667eeeee777.666bbbbbbb66886887777bb7b7eddbdddbddddde6666666666666666666bedddddddddddddddddddddddbbeee
                99999999999999966bb7777777777767777776bbbb77eee6e677777766677eeeeeeee97777778866688888888bb78bbb7eddbdddbddddde6666666666666666666bedddddddddddddddddddddddbeeee
                99999999999999999677777777777776776667be777eee6eee6777666777eeeeee4ee999998866b88b77777777bb78bb7eddbdddbddddde6666666666666666666beddddddddddddddddddbddddbeeee
                99999999999999999667777777777776667777be77eeee6eeee666777eeeeeeeee4ebb99986668877777.87bb77bb8b7beddbdddbddddde6666666666666666666beddddddddddddddddddbddddbeeee
                89999999999999999966666666777777667777b77eeeee6eeeeeeeeeeeeeeeeeee4eb998866888777777b8877bbbb78bbbddbddddddddde666666666666666bbbbeeddddddddddddddddddbddddbeeee
                899999999999999999999bb7776667776666776eeeeeeeeeeeeeeeeeeeeeeeeeeee4b988888b77777.7777b88b77b7777eddbdddddddddee66666666666bbbbeeeedddddddddddddddddddbddddbeeee
                899999999999999999999999777776997779666eeeeeeeeeeeeeeeeeeeeeeeeeeee4b88bb7777777777777bb788bbb777eddbddddddddddeebbbbbbbbbbeeeeeeeddddddddddddddbdddddbddddbeeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee4886b777777777777777bbb78bbbbbeddbddddddddddeeeeeeeeeeeeeeeedddddddddddddddddbdddddbddddbeeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee48bb7777766666666777777b88bbbbeddbddddddddddddddeeeeeeeeeeeedddddddddddddddddbddddbdddddebeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeeeeeeeeeeeeeeee4e7777776666777776666777777b77eddbdddddddddddddddddddddddddddddddddddddddddddbddddddddddebeee
                8999999999999999999999999999999999999cbeeeeeeeeeeeeeee4eeeeeeeeeeeeb4777777777766677777666bb77777eedbddddddddddddddddddddddddddddddddddddddddddbdddddddddddebeee
                8999999999999999999999999999999999999cceeeeeeeeeeeeeee4eeeeeeeeeeeeb47777777777777667667777bbb87bbedbddddddddddddddddddddddddddddddddddddddddddddddddddddddebeee
                89999999999999999999999988888888888894ceeeeeeeeeeeeeee4eebeeeeeeeeeb477777777777776666666677777787edbddddddddddddddddddddddddddddddddddddddddddddddddddddddebeee
                89999999999999999999998888888778888997ceeeeeeeeeeeeeee4eebeeeeeeebebe77777777777776777777776666667edbdddddddbbbbbbbbbbdddddddddddddddddddddddddddddddddddddebeee
                8899999999999999998888886667767bbb7777ceeeeeeeeeeeeeee4eebeeeeeeebebe77777677777777777776666666667eebddddddddddddddddbbbbbbbbbbbbbbbbbbdddddddbbbbbbbbbbbddebeee
                8899999999999888888b8877777bbbbb6777.cceeeeeeeeeeeeeee4eebeeeeeeebebe77777677777777776666666677777eebeeeeeeeeddddddddddddddddddddddddddbbbbbbbdddddddddddddebeee
                889999999999886bbb8877777b6666667777cceeeeeeeeeeeeeeee4eebeeeeeeebebb7777767777766666777777776667777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                889999999888888887777776667777777777c4eeeeeeeeeeeeeeeee4ebeeeeeeebeeb77777677776777777777777766666677777777777777777777777777777777777777777777777777777777ddddd
                88999988666666677666666777777777777cb46eeeeeeeeeeeeeeee4e4eeeeeeeebeb777776777667777bbbb77777766666666666666666666666777777777777777777777777777777777777ebddddd
                88988866b88777777777777777777777676666eeeeeeeeeeeeeeeeeee4eeeeeeeebeb7777677767bbbbbbbbb77777777777777777777666666666666666666666666666666666666666666666ebbdddd
                8686666b777777777777777777777767777cbeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeb77766666bbbbb8888bbbb777777777777777777777777777777776666666666666666666666677777777e7bdddd
                668666b8777777777777777777666677777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeebbb777777bbbbbb86666888b777777777777777777777777777777777777777777666667777777777777777e7bdddd
                68668887777777777777777777666677777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeeebb777bbbb8886667777668bb77777777777777777777777777777777777777777777777777777777777777eebdddd
                66686b77777777777777777777777767777cbeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeb77bb88666777777777688bb7777777777777777777777777777777777777777777777777222222222277eebdddd
                666b7777777777777777777777777766777ceebeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbb8867777777777777688bb777777777777777777777777777777777777777777722222222222227277eebdddd
                8867777777766667766666666666666677cceebeeeeeee4beeeeeeeeeeeeeeeeeeeebbb887777777777777777688b777777777777777777777777777777777777777777222222222d22222277eebdddd
                8667777766677767666667666666666667cbeeeeeeeeee4bbeeeeeeeeeeeeeeeeeeeb88877777777777777777678bb77777777777777777777777777777777777777777222222222d22222277eebdddd
                8677777766667667777776666777777777cbeeeeeeeeee4ebeeeeeeeeeebeeeeeeeeeb7677777777777777777678bb77777777777777777777777777777777777777777222222dddd22222277eebddde
                767777777776666666666666677777777ccbeeeeeeeeeee4beeeeeeeeeebeeeeeeeeeb6777777777777777777768bb777777777777777777777777777777777777777772222ddd22222222277eebdbeb
                677777766667777777777777777777777cbbeeeeeeeeeee4beeeeeeeeeebeeeee4eeeb88888777777777888877688b77777777777777777777777777777777777777772222222222222222277eedeeed
                666666677777777777777777777777777cbebbeeeeeeeeeeeeeeeeeeeeebeeeee4eeeb88888888877888888888868b77777777777777777777777776677777777777772222222222222222277eeedddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeb76666677877876666677868b77777777777777777777776667777777777777772222222b22227777777ebddddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeb76166677877876166677868bb7777777777777777777776666777777777777777777777bccc77777777ebddddd
                777777777777777777777777777777777c4ebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe6666677877876666677868bb777777777777777777777777767777777777777777777bbccc77777777ebddddd
                777777777777777777777777777777777c4beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe66666888778766666778868b766777777777777777777777666777777777777777777bbccc77777777e.ddddd
                77777777777777777777777777777777bcbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebe66666888668866666788868b766777777777777777777766666666666777777777777bbccc77777777edddddd
                77777777777777777777777777777777bcbeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeb888888886777888888888768b776777777777777777777777777777777777777777777bbccc77777777edddddd
                77777777777777777777777777777777bceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebe88888777777778888777768b777667777777777777777777777777777777777777777bbccc7777777eedddddd
                77777777777777777777777766677777bceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeebe7777777777777777777768bb77776777777777777777777777777777777777777777bbccc7777777ebdddddd
                77777777777777777777777777777777bceeeeeeeeeeeeee4eeeeeeeeeeeebeeeeeeeebb77777777777777777777688b77777667777777777777777777777777777777776677bbccc7777777ebdddddd
                77777777777777777777777777777777cceeeeeeeeeeeeee4eeeeeeeeeeebbeeeeeeeeeb77777777777777777777768bb7666677777777777777777777777777777777767777bbccc7777777ebdddddd
                77777777777777777777777777777777c4eeeeeeeeeeeeee4eeeeeeeeeeeeeeeeeeeeeebb777877777877777777776bbb7777777777777777777777777777777777776667777bbccc777777ebdddddd.
                77777777777777777777777777777777ceeeeeeeeeeeeeee4eeeeeeeeeeeeeeeeeeeeeeeb7778888888777777777768bb7777777777777777777777777777777777777777777bbccc777777ebeeebbbb
                77777777777777777777777777777777ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeeeebb7777777777777777777688b7777777777777777777777777777777777777777777bbbcc77777e7edbbdddd
                777777777777777777777777777777ccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebceeeeb7777777777777777777678b77777777777777777777777777777777777777777777bbcc77777ebeddddddd
                bbbbbbbbbbbb77777777777777777ccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4cceeb7777777777777777777668b77777777777777777777777777777777777777777777bbcc7777eebeddddddd
                bb77ccccccccccb7777777777777cc7beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4cceb7777777777777777777768b777777777777777777777777777777777777777777777bccc777ebbdddddddd
                77ccc777777777cccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4bccb7777777777777777777768bbb7777777777777777777777777777777777777777777bccc777ebddddddddd
                77778888888888888888888888888bbeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44ecb77777777777777777777688bb7777777777777777777777766677777777777777777bccc77eebddddddddd
                77778bbbbbbbbbbbbbbbbbb7777777beecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4bcb77777777777777777777678bb7777777777777777777777777777777777777777777bccc7eebbddddddddd
                7bbbbbb7bbbbbbbb7777777bbb777bbecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc77777777777777777777668bb7777777777777777777777777777777777777777777bccb7ebbdddddddddd
                77777bbbbbbbbbbbbbbb777777777b.eceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeece7777777777777777777768bb7777777777777777777777777777777777777777777bccb7ebddddddddddd
                7777777777888777777bbbbbbbbbbbccceeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeece77777778877777877777688b7777777777777777777777777777777777777777777bcbbebbddddddddddd
                bbbbbbbb88bbb77bbbbbbbbbb77bcceeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecbe7766888886667888766678b7777777777777777777777777777777777777777777bbbeebdddddddddddd
                77bbbb77777777bbbbbb7777cccccceeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecbe688bbbbbbbb8668888bbbbb777777777777777777777777777777777777777777777eebddddddddddddd
                777777bbbbbbbb77777b7777eeeeeeceeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc6bbbb777777bbbbbbbbb7777777777777777777777777777777777777777777777777ebdddddddddddddd
                7777777777777788877b777beeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebeeeeeeeeeeecccce77777777777777777777777777777777777777777777777777777777777777777eebdddddddddddddd
                7777777bbbbbbbbbbbbbb7bbeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeebb4eeeeeeeeeececb7777777777733777333377777777777777776677777777777777777777777777eebdddddddddddd...
                bbbbbbbbb77bbbbb77777bbee44eeeeeeeeeeeeebbeeeeeeeeeeeeeeeeeeebb4eeeeeeeeeeceecc777777777733333333777777777777777777667777777777777777777777777e7bddddddddbbbbbbb
                777777777788888bbb77bbe.4.4eeeeeeeeeeeeebeeeeeeeeeeeeebeeeeeeeb4eeeeeeeeeecb.cecc777773333bbbbbb333337777777777777766777777777777777777777777ee7bddd...bbbdddddd
                77777777777bb7788887be.444eeeeeeeeeeeee44ee4eeeeeeeeeebeeeeeeeb4eeeeeeeeeeececcec77777aabaaaabbabaa37777777777777776777777777777777777777777eebbddbbeeeddddddddd
                7bbbbbbbbbbb7777777be.44ceeeeeeeeeeeeee4bbe4eeeeeeeeeebeeeeeeeb4eeeeeeeeeeeececee7777773bbbaabbaaa337777777777777767777777777777777777777777e7beeeeeeddddddddddd
                777bbbbbbbbbbbbbb778eeeeceeeeeeeeeeeee4bbe4eeeeeeeeee4beeeeeeeb4eeeeeeeeeeeeecceee77777333aaaaaa3777777777777777767777777777777777777777777ee7bddddddddddddddddd
                b7777b8bbbbb7888888eeeeeeeeeee444444e4bee44eeeeeeeeee4beeeebccb4eeeeeeeeeeeeeeceeeb7777777aa3aa37777777777777777777777777777777777777777777e7bbddddddddddddddddd
                bbbbbbb88bb88bbb7eeeeeee444444ee4ee4e4be44eeeeeeeeee4beeeeeebcb4eeeeeeeeeeeeee.eeeb77777773333a37777777777777777767777777777777777777777777e7bdddddddddddddddddd
                77777777bbbbb777beeeeeeeccc444444eeee4beeeeeeeeeeeee4beeeeeeeb.4eeeeee.eeeeeeeeeeecb777777367333777777777777777776677777777777777777777777e7bbdddddddddddddddddd
                777777777777777bbeeeecceecc4.eccceeeeeeeeeeeeeeeeeee4beeeeeeebb4eeee4cccceeeeeeeeecb77777776733777777777777777777667777777777777777777777eebbddddddddddddddddddd
                7777777777777bbbeeeecceee444.eeeeeeeeeeeeeecee44eeee4eeeeeecccb4eee.cc77ceeeeeeeeecb77777776763777777777777777666777777777777777777777777e7bdddddddddddddddddddd
                77777777777bbbeeccccceeeeeeeeeeeeeeeeeeeeeeceeeeeee44ebeeeccccb4eeee7777ceeeeeeeeecb7777777616777777776666666677777777777777777777777777eebbdddddddddddddddddddd
                777777777eeebeecccccc7eeeeeeeeeeeeeeeeeeeecceee4eeec4eeeecc77cb4eeee77777ceeeeeeeeccb77777761677777766667777777777777777777777777777777eebbddddddddddddddddddddd
                77777777777ee7777777ccceeeeeeeeeeeeeee7ccccceeeeeee4beeecc777c7beeee77777cceeeeeeeecb7777776167777777777666667777777777777777777777777ee7bdddddddddddddddddddddd
                77777777777e77777777777cccceeeeeeeeeccc7777cceeecce4beeece777ccbbeee777777cc7eeeeeecb777777616777777777777777777777777777777777777777eebbddddddddddddddddddddddd
                77777777777777777777777777ceeeeeecccc7777777cccccc74bee7c777777bcbe77777777ec7eeeeecb77777761677777777777777777777777777777777776667eebbdddddddddddddddddddddddd
                7777777777777777777777777777bbeccce7777777777cccc774bee77777777bccce77777777cc777eecbb7777761677777777777777777777777777777777667677ebb.dddddddddddddddddddddddd
                777777777777777777777777777bcccceee777777777777c7777beee7777777bccce7777777777ccc7ee.b777776167777777777777777777777777777766676677ebb.ddddddddddddddddddddddddd
                77777777777777777777777777bbcbeeeee77777777777777777bbbe77777777bccb777777777777ccce.b777776767777777777777777777777777766677767777ebb.ddddddddddddddddddddddddd
                777777777777777777777777bbbcc7eee7777777777777777777bbee77777777bccb777777777777777cc.b777767667777777777777777777777666777766777eebbb.ddddddddddddddddddddddddd
                7777777777777777777777bbbb77777777777777777777777777bcbe777777777bcbe7777777777777777eb77776766777777777777777777777667777767777eebbdddddddddddddddddddddddddddd
                777777777777777777777bb77777777777777777777777777777bbb77777777777bbee777777777777777ee66666766677777777777777777766777776677777e7bdddddddddddddddddddddddddd.bb
                77777777777777777777777777777777777777777777777777777bb77777777777bb7777777777777777777bb6666677777777777777777666777666677777ee7bddddddddddddddddddddddbbbbbbbd
                666776666777777777777777777777777777777777777777777777777777777777bb777777777777777777777777766777777777777777677776666777777ee7bbdddddddddddddddddbbbbbdddddddd
                7666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777677777777777776677776667777777ee7bbdddddddddd.bbbbbbbbdddddddddddd
                777667766666677777777777777777777777777777777777777777776666666667777777777777777777777777777777777777777666777766677777777ee7bdddeeebbbbbbbbddddddddddddddddddd
                7777766777777667666666666666666777766666666667766666666667777777766667777777777777777777777777777777777777766766777777777eeebbbeeeebbddddddddddddddddddddddddddd
                776666666666666666677777777777766666666666666666666667666666777777777666777777777777777777777777777777777777667777777777eeeeeeeedddddddddddddddddddddddddddddddd
                777777777777777777766666666666666666666667766666677777777766666666667666666666666667777777777777777777766666666666666666ebbddddddddddddddddddddddddddddddddddddd
                7777777777777777777777777777777777777777776677777777777777777777777777777777777777776666666666666666666666677776666666666ddddddddddddddddddddddddddddddddddddddd
    """))
    game.show_long_text("Gorp?", DialogLayout.BOTTOM)
    game.set_dialog_text_color(6)
    game.show_long_text("Yes, it's Me. Gorp.", DialogLayout.BOTTOM)
    game.show_long_text("I know that you've been looking for me.",
        DialogLayout.BOTTOM)
    game.show_long_text("Though I'm not entirely sure why.", DialogLayout.BOTTOM)
    game.show_long_text("A secret, you say? Yeah, I know a few things.",
        DialogLayout.BOTTOM)
    game.show_long_text("The secret I will share for you, is one that's very special.",
        DialogLayout.BOTTOM)
    game.show_long_text("You are exactly where you are supposed to be. ",
        DialogLayout.BOTTOM)
    game.show_long_text("You are doing so well. And I'm so very proud of you.",
        DialogLayout.BOTTOM)
    finallevel()
sprites.on_overlap(SpriteKind.player, SpriteKind.wood, on_on_overlap3)

def levelOne():
    scene.set_background_image(img("""
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7766666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8866667666777777777666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb886666677777771177777777668888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88666771111111117777777777776688bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88666677117777777777777777777776688bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88666771177777777777777777777777766888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8666111177777777777777777777777777677888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb866667777777777777777777777777777777677788bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb886667777777777777777777777777777777776677788bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb866667777777777777777777777777777777777666778bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb86667777777777777777777777777777777777777766678bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88666777777777777777777777777777777777777777766788bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb866677777777777777777777777777777777777777777776678bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8667777777777777777777777777777777777777777777777767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb886677777777777777777777777777777777777777777777777767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb86667777777777777777777777777777777777777777777777777767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8666777777777777777777777777777777777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb886677777777777777777777777777777777777777777777777777776677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88667777777777777777777777777777777777777777777777777777776677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb886677777777777777777777777777777777777777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88666777777777777777777777777777777777777777777777777777777777667bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8666677777777777777777777777777777777777777777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb86666777777788888888888887777777777777777777777777777777777777776677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8.6667777777788888888888888877777788888888888887777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb866677777777788888666668888877777888888888888887777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb866777777777777777777776668877777888888888888887777777777777777777767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8667777777777777777777777777777778888666666677777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb68677777777777777777777777777777777777777777777777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb68677777777777777777777777777777777777777777777777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb68777788888888111111111777777777777777777777777777777777777777777777767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6677778888888888888888888877777777777111177777777778888888888777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6677778888888866688888888877777777778888118888888888888888888777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6677778888777766688888888877777777778888888888888888888888888777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66677777777777766666667788877777777778888888666888888877777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66677777777777661166667788877777777778887766666667777777777777777777777677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb667777777777776616666677888777777777788877611666677777777777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7667777777777776666666677888777777777788877616666677777777777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6677777777777776666666677888777777777788877666666677777777777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6677777777777776666666777888777777777788887666666677777777777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777888888666667777888777777777788887666666677777777777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66777777777888888888888777888777777777788888666666688888887777777777777676777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66777777777888888888888888666777777777778888776668888888888777777777777766777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66777777777777776666666666677777777777778888888888888888888777777777777776777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb667777777777777777777777777777777777777777888888888887778888777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb677777777777777777777777777777777777777777766666886667777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777777777777777777666777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777677777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb67777777777777777777777777777777776666667777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb67777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb677777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb677777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb677777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb677777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777777117777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777788811111888887777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777777888888888888888777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777788888888888888888777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777788886666666666888777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6777777777777777777777777777777788866777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb76777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb76777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb76777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66677777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666677777777777777777777777777777777777777777777777777777777777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6666777777777777777777777777777777777777777777777777777777777777777777777777777777776667bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66677777777777777777777777777777777777777777777777777777777777777777777777777777777766677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66677777777777777777777777777777777777777777777777777777777777777777777777777777777666677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666677777777777777777777777766677777777777777777777777777666777777777777777777777777666677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666677777777777777777777777666677777777777777777777777776666777777777777777777777777666777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666677777777777777777777776666666666777777777777777777776666777777777777777777777777666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66667777777777777777777776666666666666717777777777777777666667111111111111177777777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66667777777777777777777776668888888666671111177777777777666666666666666666611177777776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666777777766666666666666668886666b88866677771177777777116666888888886866666666111666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6667777111166666666666688866666bbbbb886667777177777771166668866666668866666666666116666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb7666777116666688888888888666bbbbbbbbbb88666666717777711666888bbbbbbbbbbbbbb6666666666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb76667111666668877777bbbbbbbbbbbbbbbbbbb68888866611111666688bbbbbbbbbbbbbbbbbbbbbbbbb7776666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb76667166666888bbbbbbbbbbbbbbbbbbbbbbbbb6666688888666666888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb766666666688bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666668888886bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666688888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6666667bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    """))
    game.show_long_text("This is Gorp. He holds Secrets.", DialogLayout.BOTTOM)
    game.show_long_text("You must find him. And figure out what he knows.",
        DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        scene.set_background_image(img("""
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        """))
        game.show_long_text("Wait, where did Gorp go?", DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        levelTwo()

def on_on_overlap4(sprite4, otherSprite4):
    game.show_long_text("Pink milk? That cannot be good.", DialogLayout.BOTTOM)
    sprites.destroy(milk)
sprites.on_overlap(SpriteKind.player, SpriteKind.melk, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    global soap2
    game.show_long_text("Oh no. They must've left the sink running.",
        DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        game.show_long_text("Maybe you should turn it off?", DialogLayout.BOTTOM)
        sprites.destroy(AWater)
    soap2 = sprites.create(img("""
            . . . . . . . 
                    . 3 3 3 3 3 . 
                    3 3 d d 1 3 3 
                    3 d 3 3 3 3 3 
                    b 3 3 3 3 3 b 
                    . b b b b b .
        """),
        SpriteKind.soap)
    soap2.set_position(84, 69)
sprites.on_overlap(SpriteKind.player, SpriteKind.water, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    game.show_long_text("A letter? In the fridge? LOL", DialogLayout.BOTTOM)
    game.show_long_text("What does it say?", DialogLayout.BOTTOM)
    levelFive()
sprites.on_overlap(SpriteKind.player, SpriteKind.letter, on_on_overlap6)

def finallevel():
    scene.set_background_image(img("""
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb7777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbb777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbb7777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbb77777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbb77777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb777bbbbbbbb77777bbbbbbbbb77777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb7777777777777777bbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbb7777777777777777bbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777bbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb777bbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb7777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb7777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbb777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbb777777777777777777777bbbbbbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbb77777777777777bbbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbb77777777bbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbb7777777777bbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbb7777777777777bbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbb777777bbbbb777777bbb7777bbbbbbbbbbbbbb7777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbb77777777bbbbb7777bbbbbb777bbbbbbbbbbbb777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777777777bbbbb7777bbbbbb777bbbbbbbbbbb7777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777777777bbbbbbbb7777bbbbbbb777bbbbbbbbbb777777bb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777777777bbbbbbbbbb7777bbbbbbb7777bbbbbbbbb7777bbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbb77777bbbbbbb7777bbbbbbbb7777bbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbb77777bbbbbbbb777bbbbbbbb7777bbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbb77777bbbbbbbb777bbbbbbb7777bbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbb777bbbbbbb7777bbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbb777bbbbbb7777bbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbb777bbbbbb7777bbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbb77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbb777bbbbbb777bbbbbbbbb7777777bbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbb77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbb777bbbbbb777bbbbbbbbb777777777777777777bbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbb777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbb777bbbbbb777bbbbbbbb7777777777777777777bbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbb77777777777777777bbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbb777bbbbbb777bbbbbbb77777bb77777777777bbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbb7777777777777777777bbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbb777bbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbb77777777777777777777bbbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbb7777777777777777777777bbbbbbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777bbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbb77777777777777777777777bbbbbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbb7777777777777777777777777bbbbbbbbbbbbbbbbbbbbbb777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbb777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbb77777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbb7777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbb777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbb7777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb7777777788868887777776668887777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb777777778886888777788888888b7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb77777888888688877778888888887777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb77777888666666677778888868887777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb7777778886616666777777616688877777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb7777777766666667777777666666777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77777777766666667777777666666777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb777777777777777777777777766677777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb7777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb7777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77777777777777777777766677777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77777777777766667777766677777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77777777777766666776666677777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb777777777777666666666666777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb777777777777766666666667777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb777777777777776666666677777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb7777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb7777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb7777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb77777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb77777777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb777777777777777777777bbb7777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb777777777777777777bbbbbbbbbb77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb777777777777777bbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    """))

def on_on_overlap7(sprite7, otherSprite7):
    game.show_long_text("Tree huh? Is this a classic Gorp trick?",
        DialogLayout.BOTTOM)
    game.show_long_text("Only one way to find out I guess...", DialogLayout.BOTTOM)
    level_six()
sprites.on_overlap(SpriteKind.player, SpriteKind.rock, on_on_overlap7)

def levelFive():
    global rock2
    sprites.destroy(brad)
    sprites.destroy(milk)
    sprites.destroy(letter2)
    scene.set_background_image(img("""
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeedddddddddddddeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeedddddddddddeeededdddddddddddddddddddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddeeeddeedeeedddddddddddddddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeedddddddddeeddddeedeeeddddddddddddddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddeeddddeeddeeddddddddddddddddddddeddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeedddddddddeeddddeeddeedddeeeeddddddeeeedddedddddddddddddeedddddddddddeeeeddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeedddddddddeedddddeddeedddeddedddddeeddeddddeeeddddddddddededdeeeeddddedeeddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeedddddddddeedddddeddeedddeeeedddddeeededdeeeddddddddddeeddedeeddeddddeeedddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddeedddddeddeedddeddddddddeddeeddddeddddddddddeedddeedddedddeeeddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeddddddddeedddddedddedddeeddeedddeddddddddeddddddddddeddddeddddeedddedddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeedddddddddedddddedddedddddeedddddeddddddddeddddddddddeddddddddddedddedddddedddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeddddddddddddddddddddddddddddddddeeeeeddddedddddddddddddddddddddddddeeddeeedddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeedddddddddddddddddddddddddddddddddddddddddedddddddddddddddddddddddddddeeedddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeedddddddddddddddeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeedddddddddddddddeedddddddddddddddddddddddddeeedeeeeeeeeeeddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeedddddddddddddddeedddddddddddddddddddddddddeeeeeeeeeededdddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddedddddddddddddddddddddddddddddedddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddeddeeeeeddddddddddddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddededddeedddeddddddddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddeeedddeedddedddeddddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddeeddddeedddedddeddddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddeedddeeedddedddeedddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddeeedeeeeddddeddeedddddddddddddeeddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddeeeeeddddddedeeedddddddddddddeeedddeeeeddddddeeeeddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddeeeeedddddddddddddeeedddeddedddddedddedddddddeeeddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddeeddddddddddddededddeededdddeeddeeddddddeedeedddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddedddddddddddeeedddeeddddddedeedddddddeeeeeedddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddeddddddddddddeedddeeddddddeddddddddddeddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddeeddddddddddddeedddeeddddddeeeddeeddddeeeeeddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddeeedddddddddddddddddddeddddddddeeeedddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddd77777777ddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddd777777777777dddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddd7ddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddd7ddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd77ddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd77ddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd7dddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddd77dddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddeeeeeeeeeedddd77ddddd77777777dd777ddddddddddddd7777ddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddd77dddddd7777777d77d777dd7d777ddd7777777ddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd77dddddddddd77d7dddd7dd777dddd7dddddd7ddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd777ddddddddd77d7dddd7dd77ddddd77dddd77ddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddd77777dddddd777d77ddd7dd77ddddd77ddd7ddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddd7777777777777dd77dd7dd7dddddd77d77dddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddd7777777d7ddddd777dd7ddddddd77dddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddddddddddddddddddddddddddddd7ddddddddddddddddd777dddddddddddddddddddddddddebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd7ddddddddddddddddddddddddddcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd7ddddddddddddddddddddddddddccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddddddddddddddddddddd77dddddddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccceeeddddddddddddddddddddddddddddd777777dddddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccceeedddddddddddddddddddddddddddd6777777d77ddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccceeeddddddddddddddddddddddddddd66767777777ddddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccceeedddddddddddddddddddddddddd7777777666777dddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddddddddd2dddddddddddd7777777677777dddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeddddddddddddd22222ddddddddd7777777777777ddddddddddddddddddddddddddddddddddddddddddddddddddeccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeedddddddddddddd222222ddddddd7777e777e7777ddddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeddddddddddddddddd2222dddddd67766777677777dddddddddddddddddddddddddddddddddddddddddddddddddeeccbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddd222ddddd6666d77d76677ddddd3dddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeedddddddddddddd222222222dddddddeeeeed7ddddd3333dddddddddddddddddddddddddddddddddddddddddddddeeccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeddddddd222222222222222222ddddddeeeeeeddddddd337333ddddddddddddddddddddddddddddddddddddddddddeeecbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeddddddd222222222222222222dddddddeeeeedddddddd333dddddddddddddddddddddddddddddddddddddddddddddeeccbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeeddddddd22222222222dd2222ddddddbeeebbeddddddddd7ddddddddddddddddddddddddddddddddddddddddddddddeebcbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeedddddddddddddddddddd2222ddddddddeeeeebddddddddd7ddddddddddddddddddddddddddddddddddddddddddddddeeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeddddddddddddddddddd2222ddddddddebeeeebedddddddd7dddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeedddddddddddddddddd222ddddddddddbeeeeeebedddddddddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbcceeeedddddddddddddddd222ddddddddddeeeeebeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbceeeeeddddddddddddddddd2ddddddddddeeededeedeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeedddddddddddddddddddddddddddddddddddedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccceeeeeeeeeeeeecbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeedddddddddddddddddccccccddddeecccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbcccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeccccccccccccccccceeeeccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    """))
    rock2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . b c c c . . . . 
                    . . . . . . . b b b b c b . . . 
                    . . . . . . b b b b b b c . . . 
                    . . . . b b b b b b b b c b . . 
                    . . c b d d d b b b b b b b b . 
                    . c b d b b b b b b b b b b b . 
                    . b b b b b b b b b b b b b b b 
                    . b b b b b b b b d d d d b b b 
                    . c c b b b b b b b b b b b b b 
                    . . c c c c c c c b b b b b c c 
                    . . . . . . . . c c c c c c c . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.rock)
    rock2.set_position(90, 103)

def on_on_overlap8(sprite8, otherSprite8):
    game.show_long_text("This must be the door to the kitchen.", DialogLayout.BOTTOM)
    game.show_long_text("I wonder if Gorp is in there.", DialogLayout.BOTTOM)
    levelThree()
sprites.on_overlap(SpriteKind.player, SpriteKind.Button, on_on_overlap8)

def levelFour():
    global brad, milk, letter2
    scene.set_background_image(img("""
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeebbbbbbeeeeeeee
                eebbbbbbbbbbbbbbbbeeebeeeeebbbbbbeeeeeeebeeeeeeeebbbbeeeeeebeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbeeeeebbbbbbbe
                eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeebeeeeeeeeeeeebbbeeebeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eeeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeebeeebeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                ebeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeebbbbbbeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                ebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccce
                ebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccceeeeeeccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe
                ebbeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccce
                ebbeebeeeeeeebbeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbce
                ebeeebbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbbbbbbbbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbce
                ebeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbbbbbbbbbbbbccccbbbdddddddddddddbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbce
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbbbbbbbbbbccccccdddccbcddddddddddddcbdddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeeeeeeeeeeeeeeeeeeeeeeeeccccbbbbbbbbbbbbcccccdddddddddcbbcdddbbbbbbbdddcdddddbdddbddddddbdddddddddddddddddddddddddddddddddddddddbddddbddddddbddcbcbbbbbbbbbbbce
                eeeeeeeeeeeeeeeeeeeccccccbbbbbbbbbbccccccddddddddddddddcbbcdddddddddddddcddddbbddddddddddbdddddddddddddddddddddddddddddddddddddddbddddbddddddbddcbcbbbbbbbbbbbce
                eeeeeeeeeeeeecccccccbbbbbbbbbccccccddddddddddddddddddddccbcdddddddddddddcdddddddddddddddddbddddddddddddddddddddddddddddddddddddddbddddbdddddbbddcbcbbbbbbbbbbbce
                eeeeeeecccccccccbbbbbbbbcccccddddddddddddddddddddddddddcbccdddddddddddddcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddcbcbbbbbbbbbbbce
                eeeecccccccbbbbbbbccccccdddddddddddddddddddddddbbbdddddcbbbdddddddddddddcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdbdddcbcbbbbbbbbbbbce
                eeeccccbbbbbbcccccddddddddddddddddddddddddbbbbbdddbddddcbbbdddddddddddddcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbcbbbbbbbbbbbce
                eeecbbbccccccddddddddddddddddddddddddbbbbcccccccccbddddcbbbddddddddddddccdbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbcbbbbbbbbbbbce
                eeeccccdddddddddddddddddddddddddbccccccccddddddddcbddddcbbbdbddddddddddcbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbcbbbbbbbbbbbce
                eeecbddddddddddddddddddddddbbbbbdddddddddddddddddcbddddcbbbdbddddddddddcbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbddddcbcbbbbbbbbbbbce
                eeecbdddddddddddddddddddbbbddddddddddddddddddddddcbddddcccbddbddddddddccbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcbcbbbbbbbbbbbce
                eeecbddddddddddddddddddddddddddddddddddddddddddddcbdddcdcbbddbddddddddcdbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccbcbbbbbbbbbbbce
                eeecbddddddddddddddddddddddddddddddddddddddddddddcbddddccbbddbddddddddcdbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcdbcbbbbbbbbbbbce
                eeecbddddddddddddddddddddddddddddddddddddddddddddcbddddcbbbddbddddddddcdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddddddddddddddddddddddddddddddddddddddddddddbddddcbbbddbddddddddcdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddddddddddddddddddddddddddddddddddbddddcbbbddbddddddddcdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddddddddddddddddddddddddddddddddddbddddccbcddbddddddddcdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddddddddddddddddddddddddddddddddddbdddddccbddbddddddddcdbdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddddddddddddddddddddddddddddddddddbdddddcbbdddddddddddccbdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddddddddddddddddddddddddddddddddddbdddddcbbddddddddddddcbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddddddde5edddddddddddddddddddddddddbdddddcbbddddddddddddcbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddbbbd5e5dddddddddddddddddddddddbbbdddddcbbddddddddddddcbdddddddddddddddddddddddddddddddddddddddddddddddddddddd7ddd7dddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddddb444554bbbdddddddddddddddddbbbddbdddddcbbddddddddddddcbdddddddddddddddddddddddddddddddddddddddddddddddddddddddd7dddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddbb45555444bddddddddddddddbbbdddddbdddddcbbddddddddddddcbdddddddddddddddddddddddddddddddddddddddddddddddddddd22227ddbbdddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddb455555555bdddddddddddbbbddbbbbbbbdddddcbbddddddddddddcbddddddddddddddddddddddddddddddddddddddddddddddddddd222262622bbddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddb455555544bddddddddbbbdddbbbbbbbbbdddddcbbddddddddddddcbdddbbbbbbbbddddddddddddddddddddddddddddddddddddddddd222266222bddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddb455444445bdddddbbbdddbbbbbbbbbbbbdddddcccddddddddddddcbdbbb333d33bbbddddddddddddddddddddddddddd7d7ddddddddd22d222222bbbbbbbbbbdbcbbbbbbbbbbbce
                eeecbdddbddddddddb454455554bddbbbdddbbbbbbbbbbbbbbbdddddcbbddddddddddddccbb33333d3333bbbddddbbbbbbbbbbbbbbbbbbbb2267bbbbbbbbb222d22222bbbbbbbbbbbbcbbbbbbbbbbbce
                eeecbdddbddddddddb455544444bbbddddbbbbbbbbbbbbbbbbbdddddcbbdddddddddddddbb3333dddddd333bbbbbbbbbbbbbbbbbbbbbbb22226722bbddddbb22222222bbdddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddb544445bbbddddbbbbbbbbbbbbbbbbccbbdddddbbbddddddddddccdd33dddd3333ddd333bddddddddddddddddddb222222622bbdddddbb222222bbddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddbb555bbbbddccbbbbbbbbbbbbbbbcccbddbdddddbbbdddddddddccbd333dbbddddddbbdddbdddddddddddddddddd222d2222222bddddddbbb222bbdddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddbd444bbddccbbbbbbbbbbbbbbbccbdddddbdddddbbbddddddddccb.63bbd3333d33333bbdb666ddddddddddddddd22222d22222bddddddddbbbbdddddddddddddbcbbbbbbbbbbbce
                eeecbdddbdddddddb44bbddccbbbbbbbbbbbbbbcccbdddddddbdddddbbbddddddcccbd66bb3d333d33333333d3b66ddddddddddddddd22dd2222222bdddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddddbbddccbbbbbbbbbbbbbcccbddddddddddddddddbbcddddcccbddb66333d3333d3333333ddb66ddddddddddddddb22222222222bdddddddddddddddddddddddddbcbbbbbbbbbbbce
                eeecbdddbddddddbbdbccbbbbbbbbbbbbcccbdddddddddddddddddddbbcddcccbbdddb6633ddd333d3333333ddb66dddddddddddddbb22222222222ddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeecbdddbdddddddbbbbbbbbbbbbbbbccbddddddddddddddddddddddbbbdccdbdddddb6d333333333dddd333d666bddddddddddddddbb22222222bbddddddddddddddddddddddddbbbcbbbbbbbbbbcee
                eeecbdddbdddddbbbbbbbbbbbbbbcccbddddddddddddddddddddddddbbbcddbddddddb66dd3333ddddd33366666bbdddddddddddddddbbbbbbbbbbdddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeecbdddbdddddbbbbbbbbbbbcccbddddddddddddddddddbbdddddddbbccbbdddddddb666666666663666666bbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeecbdddbdddddbbbbbbbbbccbddddddddddddddddddbcccbdddddddbbbbdddddddddbb666666666666bbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeecbddddbddddbbbbbbcccddddddddddddddddddbbccddcbdddddddbbcbbbbbbbbbbbbbbbb6666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbcee
                eeecbdddddddddbbbbccbdddddddddddddddddbbcccddddcbdddddddbccddddddddddddcccbbccccbbbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeecbdddddddddddbbdddddddddddddddddbbbccdddddddcbdddddddbccdddddddddddddbccdcbcbcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                eeeccbddddddddddddddddddddddddddbbbddddddddddddcbdddddddbccdddddddddddddbcddddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                beeccbddddddddddddddddddddddddbbdddddddddddddddcbdddddddbccdddddddddddddbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                beeccbdddddddddddddddddddddddddddddddddddddddddcbdddddddbbcdddddddddddddbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddddddddddddddddddddddddddddddddddddddddcbdddddddbbcdddddddddddddbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddddddddddddddddddddddddddddddddddddddddcbdddddddcbcdddddddddddddbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbddddddddddddddddddddddddddddddddddddddddddbdddddddbccdddddddddddddbcdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbddddddddddddddddddddddddddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbddddddddddddddddddddbbbdddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbddddddddddddddddbeeeddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddddddbbeeeddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddddddbe2eeddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddddddbe22eebbdddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddddbbbe2222ebdddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddbbbee22222ebbddddddddddddbbbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeccbdddbdddddddddddbbee2222eeeebdddddddddbbbddbdddddddbccdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                ebeecbdddbdddddddddddbbe222eee24ebddddddbbbdddddbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                bbeecbdddbdddddddddddbbeeee44442ebdddbbbddddddddbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                beeecbdddbdddddddddddbbee4442222edbbbdddbbbbbbbdbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbbcee
                beeecbdddbdddddddddddbbe4422222ccbddddbbbbbbbbbbbdddddddbbbdddddddddddddbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd55ddddddddddddbcbbbbbbbbbbcee
                beeecbdddbddddddddddddbe2222bccddddbbbbbbbbbbbbbbdddddddcbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddd4e5ddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddddbe2bcccddbbbbbbbbbbbbbbbbbbdddddddcbbdddddddddddddbdddddddddddddddddddddddddddddddddddddddddddddddddddddddd44eeddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddddbbccdddbbbbbbbbbbbbbbbbbbbbdddddddcbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddd44555bdddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbddddddbbbbbbbbbbbbbbbbbbbbbdddddddcbbddddddddddcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4bbbbbbbbbbbb445555bbbbbbbbbbbbbcbbbbbbbbbbcee
                beeecbddddbdddddddddddddddbbbbbbbbbbbbbbbbbbbbdbbdddddddcbbdddddddddccdddddddddddddddddddddddddddddddddddddddddddd44444ddddd44e455555bdddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddddddbbbbbbbbbbbbbbbbbbbbbbbdbdddddddccbddddddccccddddddddddddddddddddddddddddddddddddddddddddd454444444444555555bbdddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbbbbbbbbbbbbbbbbbbbbbbbdccdbdddddddccbdddcccdbbdddddddddddddddddddddddddddddddddddddddddddddd4555555eeeee55555bbddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbbbbbbbbbbbbbbbbbbbbbcccdddbdddddddcbbddccddbdddddddddddddddddddddddddddddddddddddddddddddddddb555e55555555555bdddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbbbbbbbbbbbbbbbbbbcccdddddbddddddddcbbdcccbbddddddddddddddddddddddddddddddddddddddddddddddddddbbb555e555e5555bbdddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbbbbbbbbbbbbbbbcccdddddddddddddddddcbbcccbdddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbb555e555bbbddddddddddddddbcbbbbbbbbbbcee
                beeecbddddbdddddddddbbbbbbbbbbbbbbccddddddddddddddddddddcbbccbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbdddddddddddddddbcbbbbbbbbbceee
                beeecbddddbdddddddddbbbbbbbbbbbcccddddddddddddddddddddddcbccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbddddddddddddddddddbcbbbbbbbbbceee
                beeecbdddddbddddddddbbbbbbbbcccddddddddddddddddddddddddccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbceee
                beeecbdddddbddddddddbbbbbcccdddddddddddddddddddddddddddcbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbdddddddddbbccddddddddddddddddddddddbbddddddcbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbdddddddddddddddddddddddddddddddddbccbddddddcbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddbbccdcbddddddcbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddbcccdddcbddddddccbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbdddddddddddddddddddddddddbbccddddddcbdddddddcbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbdddddddddddddddddddddddbbccddddddddcbdddddddcbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                bbeeccbddddbddddddddddddddddddddbbbddddddddddddcbdddddddcbbcddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbddddddddddddddddddbbdddddddddddddddcbdddddddcbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbddddddddddddddddbbdddddddddddddddddcbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbdddddddddddddddddddddddddddddddddddcbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbdddddbddddddddddddddddddddddddddddddddddcbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddddddddddddddddddddddddddddddddddddddcbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddddddddddddddddddddddddddddddddddddddcbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbcbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddddbdddddddbbcdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddddddddddddddddddddbbbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                bbeeccbddddbdddddddddddddddddddddddddddddddbbbddbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbddddddddddddddddddddddddddddbbbdddddbdddddddbbbdddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbdddddddddddddddddddddddddbbbdddbbbbbbdddddddbbbddddddddddddcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbceee
                ebeeccbddddbddddddddddddddddddddddbbbdddddbbbbbbbdddddddbbbddddddddddcccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                ebeeccbddddbdddddddddddddddddddbbbddddddbbbbbbbbbdddddddbbbddddddddddcbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddddbbbddddddbbbbbbbbbbbbdddddddbbbdddddddddcbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbdddddddddddddbbbdddbbbbbbbbbbbbbbbbbbdddddddbbbddddddddccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddbbbddbbbbbbbbbbbbbbbbbbbbbbdddddddbbbdddddddccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddbbddddbbbbbbbbbbbbbbbbbbbbbbbdddddddbbbdddddcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                beeeccbddddbddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbdddddddbbbdccccbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                eeeeccbddddbdddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddbbbccbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                eeeeccbddddbddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbccddddddddbccbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                eeeeccbddddbddddddbbbbbbbbbbbbbbbbbbbbbbbbccccddddddddddbcbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcbbbbbbbbbceee
                eeeeec.bdddbddddddbbbbbbbbbbbbbbbbbbbbbbccdddddddbddddddbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddb.cbbbbbbbceeee
    """))
    brad = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 4 4 4 4 4 4 4 4 . . . 
                    . . . 4 4 4 e e e e e e 4 4 4 . 
                    . . 4 4 e d d d e e d e e e 4 4 
                    . 4 4 e e e e d d e e d e e e 4 
                    4 4 e e d e e e d e e d d e e e 
                    e e e e d d e e d d e e d e e e 
                    e e e e e d e e e d e e 4 e e e 
                    e e e e e d e e e 4 e e e e e e 
                    e e e e e 4 e e e e e e e e b b 
                    b e e e e e e e e e e e b b b . 
                    b b b b b b b b b b b b c c c . 
                    . c c c c c c c c c c c . . . .
        """),
        SpriteKind.bred)
    brad.set_position(78, 108)
    milk = sprites.create(img("""
            ..............................
                    ..............................
                    ..............................
                    ..............................
                    ..............................
                    .............111..............
                    .............eee..............
                    ............bb3bb.............
                    .........bbbb333bbbbbb........
                    ........b333333333333b........
                    .......bb333333333333bccc.....
                    .......b3331333333333bbbccc...
                    ......bb3113333333bbbbc.bbc...
                    ......b33333aa3bbaa33bbc.bc...
                    .....bb3333a33aba33a33bc.bc...
                    .....b33bbbabbba333a33bc.bc...
                    .....bbbb33a3333333a33bc.bc...
                    .....bb3333a3333333abbcc.bc...
                    .....b33333a3333bb3ab3c..bc...
                    .....b33333a3bbbb3ba33c..bc...
                    .....b33333abb33333a33c..bc...
                    .....b33bbbb3333333333bbbcc...
                    .....bbbb333333333333bbccc....
                    .....b333133333333333bcc......
                    .....bb3331333333333bb........
                    .....cbbbb33333333bbbc........
                    .....ccccbbbbbbbbbbccc........
                    .......ccccccccccccc..........
                    ..............................
                    ..............................
        """),
        SpriteKind.melk)
    milk.set_position(108, 71)
    letter2 = sprites.create(img("""
            ..........................
                    ..........................
                    ..........................
                    ..........................
                    ..........................
                    ..........................
                    ....................8888..
                    ..............8888888666..
                    .........8888886666669996.
                    ...8888888866666999999996.
                    ..886666666699999999999966
                    ..669999999999999999996996
                    ..669999999999999999666996
                    ...69999999999999996699996
                    ...69999669999999666999996
                    ...69999966666996889999996
                    ...66999999988688899999996
                    ....6999999998889999999996
                    ....6999999999999999999996
                    ....6999999999999999996666
                    ....6699999999999666666888
                    .....699999966666ccccccc..
                    .....69966666ccccccc......
                    ......666ccccc............
                    ......8888................
                    ..........................
        """),
        SpriteKind.letter)
    letter2.set_position(120, 108)
def levelTwo():
    global kitchen_door, knob, mySprite
    scene.set_background_image(img("""
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                bbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebb
                ddbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdd
                ddddddbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbddddd
                dddddddddbbbbeeeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdddddddd
                dddddddddddddbbeeeeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbddddddddddd
                ddddddddddddddddbbeeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbdddddddddddddd
                dddddddddddddddddddbbbbeeeeeebeeebeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdddddddddddddddddd
                eedddddddddddddddddddddbbbeeebbbebeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbebeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbeeeeeeeeebeeeeeeeeebbbddddddddddddddddddddd
                bbbeeeddddddddddddddddddddbbbbebbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeebbbbeeeeebeeeeeebbbdddddddddddddddddddddddd
                dddbbbbeeeddddddddddddddddddddbbbedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbddebbbddddddddddddddddddddddddddd
                dddddddbbbbeeeddddddddddddddddddbeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebbbdddddddddddddddddddddddddddddd
                dddddddddddbbbbeeeddddddddddddddbeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddddddddddddbbbbeeeddddddddddbeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddddddddddddddddbbbbeeeddddddbedddddddddddddfddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddbbbbeeeddbeddddddddddddfbfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddbbbbebedddddddddddfbbdfddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                eedddddddddddddddddddddddddddddbbedddddddddddfbdddfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                bbeeedddddddddddddddddddddddddddbeddddddddddfbbddddfddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                ddbbbeeeddddddddddddddddddddddddbedddddddddfbbddddddfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddbbbeeddddddddddddddddddddddbedddddddddfdddddddddfddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                ddddddddbbbeedddddddddddddddddddbedddddeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                dddddddddddbbbeeddddddddddddddddbedddddbbbbbbeeeeeeeebbbbbeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebdddddddddddddddddddddddddddddddd
                ddddddddddddddbbbeedddddddddddddbbeddde.eeeeeeeeeeeeeeeeee.edddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                dddddddddddddddddbbbeeddddddddddbbedddebdddddddddddddddd.eeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                ddddddddddddddddddddbbbeddddddddbbeddeebdddddddddddddddddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                dddddddbbbdddddddddddddbbbedddddbbeddeeddddddddddddddddddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                ddddddeeeebbbbbbddddddddddbbbeddbbeddeeddddddddddddddddddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                ddddbeeeeeeeeeeebbbbbbdddddddbbbbbeddeeddd77dddddddddddddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddddddddddddddddddd
                ddddbeeee99eeeeeeeeeeebbbbbbbbbbbbeddbedd7887dbb7ddddddddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                deddbeeeeddddd999eeeeeeeeeeeebbbbbedebeddb777d878ddb87dddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee9999ddddd97ddeeeeeeeeeebbeddeeddb777d787ddb77dddeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee999999667777dedeeeeeeebbbeddeeddddddddddddddddddededddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee99999767677777777ddddeebbeddeeddddddddddddddddddebedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                bbbebeeee777996776767767767eddeebbeddeeddddddddddddddddddebedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                bbbdbeeee7776967677766677767ddebbbeddee.dddddddd.ddddddd.ebedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee7776967677777777667ddeebbeddeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee7776966667777776676ddeebbeddedbbbbbbbbbbdeeeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee977699966666e766776ddeebbeddddeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee9eee99966666e666776ddeebbeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee9ee699667776bee6669ddeebbeddddddddddddddddddbbbbbbbbbbbddddddddddddddbbbbbbddddddbbbbbbbbbbbbbbbbdddddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeeeeeeee9677777beee999ddeebbedddddddddddddddddbbaaaaaaaaabbddbdddbbbbbbbbaaaabbbddddb.bbaaaaaaaaaaabbbdddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeeeee6ee667887bbeee999ddeebbedddddddddddddddbbbabbaaaaaacaabbbbdbbbaaaaaaaabaaabbbbbbbaddaaaaaaaaaadaaaddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddbeeee96999677767beeeee99ddeebeddddddddddddddddaaabddaaaaaaaaaacabbbbaaaaaaaaaadbaaccacbbddaaaaaaaaaaadbacddddddddddddddddddebddddddddddddddddddddddddddddddd
                ddddb.eee99999677778beeeee99ddeebeddddddddddddddddccbbdaaaaaaabdbdaccbbaaaaaaaaaaaaadbaaccbaaaaaaaaaaaaaaadbbcdddddddddddddddddebddddddddddddddddddddddddddddddd
                dddddbeee9999967777be6ee6ee9ddeebedddddddddddddddddcbaaaaaaaaaaaaaaccbaaaaaaaaaaaaaadbbccbbaaaaaaaaaaaaaaadcbddddddddddddddddddebddddddddddddddddddddddddddddddd
                dddddbeee9999966676e66eee6eeddeebeddddddddddddddddddbaaaaaaaaaaaaaaccbaaaaaaaaaaaaaaaaaccbaaaaaaaaaaaaaaaacddddddddddddddddddddedbdddddddddddddddddddddddddddddd
                dddddbeee9999966bb4669ebbbb4ddeebeddddddddddddddddddbaaaaaaaaaaaaaaccbaaaaaaaaaaaaaaaaacbbaaaaaaaaaaaaaaaaccdddddddddddddddddddebbdddddddddddddddddddddddddddddd
                eeeeebeee9999bbbbbbbbbb44444ddeebeddddddddddddddddddcaaaaaaaaaaaaaaccbaaaaaaaaaaaaaaaaacbcaaaaaaaaaaaaaaaccddddddddddddddddddddebbdddddddddddddddddddddddddddddd
                bbbbbbeee99bbb4444444444444dddeebdddddddddddddddddddccaaaaaaaaaaaaaccaaaaaaaaaaaaaaaaaac.caaaaaaaaaaaaaaacdddddddddddddddddddddebbdddddddddddddddddddddddddddddd
                bbbddbeee9bb444444444444edddeeeebeddddddddddddddddddacaaaaaaaaaaaaacbaaaaaaaaaaaaaaaaaaacdaaaaaaaaaaaaaaacbddddddddddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeeebb444444444444ddeeeeebbbedddddddddddddbbbccccaaaaaaaaaaaaacbcaaaaaaaaaaaaaaaaaabdaaaaaaaaaaaaaaacbdcbbbdddddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeeeb44444444ddddddeeeebbddbeddddddddddddbbabccccaaaaaaaaaaaaacbccaaaaaaaaaaaaaaaacbdcaaaaaaaaaaaaaabbcbbcbbddddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeee44444ddddddeeeeebbbddddbedddddddddddbbaaaacbaaaaaaaaaaaaabbbcbaaaaaaaaaaaaaaaacbdcaaaaaaaaaaaaabcbcccbcbbdddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeee4dddddeeeeeeebbbdddddddbeddddddddddbaaaaacccaaaaaaaaaaaaccbbacaaaaaaaaaaaaaaacabccaaaaaaaaaaaabacbcaaaccbdddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeeedddeeeeeeeebbddddddddddbedddddddddddaaaaaccbbabaaaaaaccbcbdbacccaaaaaaaaaaaaaccbbaaaaaaaaaaabbaabbcaaaaabdddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeeeeeeeeeeebbbddddddddddeebedddddddddddaaaaacccbccccccccabcabddccaaccaaaaaaaaaacabcdbaaaaaaaacbbccbbcccaaaaccddddddddddddebbdddddddddddddddddddddddddddddd
                dddddbeeeeeeeebbbdddddddddddeebbbeddddddddddaaaaaacccacccccccccccbbbbbbbcbccbcccccccccccccccccccccccaaaaaacccaaaaaacdb66667777debbdddddddddddddddddddddddddddddd
                dddddbeeeeebbbddddddddddddeebbbdbeddddddddddcaaaacccaaacaaaacacaacacacaacaaacaaaacacccaaccacaacaaacccaacaaccacaaaaabb6677777777ebbdddddddddddddddddddddddddddddd
                dddddbeeebbbdddddddddddeeebbbdddbeddddddddddcaabacccaaaaaaacaacacaaccaaaaaaaaaaaaaaaaaaaccacacaaaaaaaaaaaaccccaaaabb667777777777bbdddddddddddddddddddddddddddddd
                dddddbbbbddddddddddddeebbbddddddbeddddddddddcbaabcccaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaacaaaaaaaaaacaaaaaaccccaaaab6678888888777bbdddddddddddddddddddddddddddddd
                ddddddbdddddddddddeeebbbddddddddbeddddddddddccccaccaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaccaaaaaaaaaaaaaaaaaacbaaaaab67787666d8777bbdddddddddddddddddddddddddddddd
                ddddddddddddddddeebbbddddddddddebeddddddddddddddbccabaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaacbaaaaaaaaaaaaaaaaaaacbccccb77787666687777bdddddddddddddddddddddddddddddd
                ddddddddddddddeebbbdddddddddddddbeddddddddddddddbccaabbaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaabdbbbbaaaaaaaaaaaacaacbddeeeeeeeeeeeeeee77bdddddddddddddddddddddddddddddd
                dddddddddddeeebbbddddddddddddddbbeddddddddddddddbcacccbbbbaaaaaaaaacbbaaaaaaaaaaaaaaabbcaaaabbbbaaaaaaaaaacacbdeecccccccccccccc77bbddddddddddddddddddddddddddddd
                dddddddddeebbbddddddddddddddddbdbeddddddddddddddbaccccccccbdddbbbbdddccbbbbbbbbaaabbbbadadaaaaaabbbbaaacccccccdebbbbbebbbbbbbbc77bdddddddddddddddddddddddddddddd
                ddddddeeebbbdddddddddddddddddbddbeddddddddddddddddccccccccccccccccccccccccccccabbbbccccccccccccccccbbbbbdddddddebbbb555bbbbbbcc777bddddddddddddddddddddddddddddd
                ddddeebbbdddddddddddddddddddbdddbeddddddddbbbbbbbdddacacaaaacaaaaaaaaaaaaaccccccccccccccaaaaaaaaaaaaaaacaacadddebbbb5e55bbbbccce77bbdddddddddddddddddddddddddddd
                ddeebbbddddddddddddddddddddbddddbddbbbbbbbeeeeeeedaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacadddeecb5ebbcccccc.ee77bddddddddddddddddddddddddddddd
                eebbddddddddddddddddddddddbdddddbeeeeeeeeeeeeeeeddcacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadbeceeeeeeeceeeeeeee77bddddddddddddddddddddddddddddd
                bbdddddddddddddddddddddddbdddddbbeeeeeeeeeeeeeeeebcaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacdbeccccccccccccccece77bddddddddddddddddddddddddddddd
                ddddddddddddddddddddddddbddddddbeeeeeeeeeeeeeeeebbccaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccabeeeeccccccccccccc667bddddddddddddddddddddddddddddd
                ddddddddddddddddddddddebddddddbeeeeeeeeeeeeeeeeebaaccaccaaababbabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccaabeeceecccccccccee6667bddddddddddddddddddddddddddddd
                dddddddddddddddddddddebddddddbeeeeeeeeeeeeeeeeeebaaacccccaaadadaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaacccaccaaadeecccceeeccccce7677ebddddddddddddddddddddddddddddd
                ddddddddddddddddddddebdddddddbeeeeeeeeeeeeeeeeeebbddaaacccaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbabadaaaaaaaaaccaaaabbeecccccceccccce7777ebddddddddddddddddddddddddddddd
                dddddddddddddddddddebdddddddbeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbdeeecccccecccccc7777eebdddddddddddddddddddddddddddd
                ddddddddddddddddddebdddddddbeeeeeeeeeeeeeeeeeeeeeebccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebcccccceeeeeecccccccccccc6666eebdddddddddddddddddddddddddddd
                dddddddddddddddddebddddddddbeeeeeeeeeeeeeeeeeeeeeebdcccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbdcccceeeeeeeccccccccccceeeeeeebddddddddddddddddddddddddddd
                ddddddddddddddddebddddddddbeeeeeeeeeeeeeeeeeeeeeeebccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccceeeeeeeecccccbbbbceeeeeeeebdddddddddddddddddddddddddd
                dddddddddddddddebddddddddbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccebbeeeeeeeeeeeebdddddddddddddddddddddddddd
                ddddddddddddddebdddddddddbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddd
                dddddddddddddebdddddddddbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddd
                ddddddddddddebdddddddddbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddd
                dddddddddddebdddddddddbeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeebddddddddddddddddddddddd
                ddddddddddebddddddddddbeeeeeeeeeeeeeeeeeeb22e2222e222222e22222e2222222e222222e22222e22222e22222e2222e222222e222222e2222eeeeeeeeeeeeeeeeeebdddddddddddddddddddddd
                dddddddddebddddddddddbeeeeeeeeeeeeeeeeeebbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeeeeeebdddddddddddddddddddddd
                dddddddeebddddddddddbeeeeeeeeeeeeeeeeeebb2e22222222222222222222222222222222222222222222222222222222222222222222222222e2beeeeeeeeeeeeeeeeeebddddddddddddddddddddd
                ddddddbbbdddddddddddbeeeeeeeeeeeeeeeeeebbe222222222222222222222222222222222222222222222222222222222222222222222222222e2b2eeeeeeeeeeeeeeeeeebdddddddddddddddddddd
                dddddbbbdddddddddddbeeeeeeeeeeeeeeeeeebb2e222222222222222222222222222222222222222222222222222222222222222222222222222e2b2eeeeeeeeeeeeeeeeeebdddddddddddddddddddd
                ddddebbdddddddddddbeeeeeeeeeeeeeeeeeeeb2e22222222222222222222222222222222222222222222222222222222222222222222222222222e2beeeeeeeeeeeeeeeeeeebddddddddddddddddddd
                dddebbddddddddddddbeeeeeeeeeeeeeeeeeeb22ee22224eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee222222222eebbeeeeeeeeeeeeeeeeeeebdddddddddddddddddd
                ddebbddddddddddddbeeeeeeeeeeeeeeeeeebb2ee2222ee44444444444444444444444444444444444444444444444444444444444444e222222222eebbeeeeeeeeeeeeeeeeeebdddddddddddddddddd
                debbddddddddddddbeeeeeeeeeeeeeeeeeeebeeee2222e444222222222222222222222222222222222222222222222222222222222224e4222222222e2beeeeeeeeeeeeeeeeeeebddddddddddddddddd
                ebbddddddddddddbbeeeeeeeeeeeeeeeeeebb2ee2222e4442e222222222222222222222222222555522222222222222222222222222244e222222222eebbeeeeeeeeeeeeeeeeeeebdddddddddddddddd
                bbdddddddddddddbeeeeeeeeeeeeeeeeeeeb2ee2222ee444222444444442222244444442222555ddd522222224422222222222222222244e222222222e2bbeeeeeeeeeeeeeeeeeebdddddddddddddddd
                bdddddddddddddbeeeeeeeeeeeeeeeeeeebb2e2222ee4442224422222224444422222224445dddd2d522222dddd44224444442222422224e422222222ee2beeeeeeeeeeeeeeeeeeebddddddddddddddd
                dddddddddddddbbeeeeeeeeeeeeeeeeeeebeee2222e4442222424422225524222222222225dd2244452224d4222444555522244444222244e222222222e2bbeeeeeeeeeeeeeeeeeeebdddddddddddddd
                dddddddddddddbeeeeeeeeeeeeeeeeeeebb2e22222e444222242422255222242222222255dd2255555424d222242245225555524422222244e222222222e2beeeeeeeeeeeeeeeeeeebdddddddddddddd
                ddddddddddddbeeeeeeeeeeeeeeeeeeeeb22e2222e2442222244422452ddddd422222255dd22222222244d222242225422222244242222244e222222222eebbeeeeeeeeeeeeeeeeeeebddddddddddddd
                dddddddddddbbeeeeeeeeeeeeeeeeeeeeb2e22222e4442222222224552d222dd42222252d222222222222d4422422255444444422244444244e222222222e2beeeeeeeeeeeeeeeeeeeebdddddddddddd
                dddddddddddbeeeeeeeeeeeeeeeeeeeebe2e22222e4422222222245522d222dd242225dd2224442222222d4444224422222442222244222444e222222222eebbeeeeeeeeeeeeeeeeeeebdddddddddddd
                ddddddddddbeeeeeeeeeeeeeeeeeeeeeb22e2222ee4422222222455222d22d2d244225d22224244222222dd2222422222222422224242222444e222222222e2beeeeeeeeeeeeeeeeeeeebddddddddddd
                dddddddddbbeeeeeeeeeeeeeeeeeeeeeb2ee2222e44222222224522222d22d2d22442222224555422222222dddd22222222242ddd44422224244e222222222e2beeeeeeeeeeeeeeeeeeeebdddddddddd
                dddddddddbeeeeeeeeeeeeeeeeeeeeebe2e2222ee44222222225522222d22ddd2224222224452224222222242442222222224dd2222222222444e222222222eebbeeeeeeeeeeeeeeeeeeebdddddddddd
                ddddddddbeeeeeeeeeeeeeeeeeeeeeeb2e22222e442222222245244444d444422224222224552224222222224222222222224d222222222224244e222222222e2beeeeeeeeeeeeeeeeeeeebddddddddd
                dddddddbbeeeeeeeeeeeeeeeeeeeeebb2e2222ee44222222224542222422244422222222245222242ddd22224422255dddd24d2222555222242444e22222222eebbeeeeeeeeeeeeeeeeeeeebdddddddd
                ddddddbbbeeeeeeeeeeeeeeeeeeeeeb2e22222e4422222222442222244222224422222224252222dd222d24422425ddd44d5422222522552422244e222222222e2beeeeeeeeeeeeeeeeeeeebdddddddd
                ddddddbbeeeeeeeeeeeeeeeeeeeeeeb2e22222e442222224555222224222222242222224425222242222d2422255dd4224dd4222225522254222444e22222222e22beeeeeeeeeeeeeeeeeeeebddddddd
                dddddbbeeeeeeeeeeeeeeeeeeeeeeb2e22222ee422222245542222224222222224222244552222244ddd2422225dd222224d22222225552542222444e2222222ee2beeeeeeeeeeeeeeeeeeeeebdddddd
                ddddbbeeeeeeeeeeeeeeeeeeeeeebbe222222e442222245ddd2222224225552224444425522222222ddd4222255d2444444222222222244544222244e22222222ee2beeeeeeeeeeeeeeeeeeeebdddddd
                ddddbbeeeeeeeeeeeeeeeeeeeeeebee22222ee42222245dd2422222245522522224225552225555442222222252422222224222222224425244222444e22222222e2beeeeeeeeeeeeeeeeeeeeebddddd
                dddbbeeeeeeeeeeeeeeeeeeeeeebbe222222e442222425d224444422452225222245552222255222442222255542222222242222222242452d4422244e22222222e2bbeeeeeeeeeeeeeeeeeeeeebdddd
                ddbbeeeeeeeeeeeeeeeeeeeeeeebee22222ee422222425d2242222445425552222242225555254222422255524222222222422222224224522d4222444e2222222ee2bbeeeeeeeeeeeeeeeeeeeebdddd
                ddbeeeeeeeeeeeeeeeeeeeeeeeebe22222ee4422d24225d24442ddddd442222222224252225255555555552242222222444444222224242522dd4222444e2222222e22beeeeeeeeeeeeeeeeeeeeebddd
                dbbbeeeeeeeeeeeeeeeeeeeeeeb2e2222ee44222d24225ddd2dd2552dd442222252224522252222244444444222222245555224425555555222d4222444e2222222ee2bbeeeeeeeeeeeeeeeeeeeeebdd
                bbbeeeeeeeeeeeeeeeeeeeeeebbe22222e444222d22422555dd552222d244422252224222252222242222222222222455224222555444422222d24222444e2222222ee2bbeeeeeeeeeeeeeeeeeeeebdd
                bbeeeeeeeeeeeeeeeeeeeeeebbe22222ee442222dd224444dd2244422dd222422552224225522222422222222222242522242555222222dd2ddd222222444e2222222e22beeeeeeeeeeeeeeeeeeeeebd
                beeeeeeeeeeeeeeeeeeeeeeeb2e22222ee4422222dddddddd222222442d222222255555555222224222222222222422555555522222222dddd22222222444e2222222ee2bbeeeeeeeeeeeeeeeeeeeeeb
                beeeeeeeeeeeeeeeeeeeeeeb2e222222e442222222222222222222222222222222222222444444422222222222224444444222222222222222222222222444e2222222e22beeeeeeeeeeeeeeeeeeeeee
    """))
    kitchen_door = sprites.create(img("""
            ..........................dbbbbbee......
                    ......................bbdddbeeeee.......
                    .............ddddddddddddeeeeeb.c.......
                    ............dd.bbbbbeeeeeeeeeebcc.......
                    ...........ddbbbbeeeeeeeee44eebc........
                    ..........bbbeeeeeee4444444eeebc........
                    ..........bceee44eeeeeeeeeeeeebc........
                    ..........bc4444eeeeeeeeeeeeeebc........
                    ..........bceeeeeeeeeeeeeeeeeebc........
                    ..........bceeeeeeeeeeee4eeeeebc........
                    ..........bceeeeeeb4eeee4eeeeebc........
                    ..........bce4eeeeb4eeee4eeeeebb........
                    ..........bce4eeeeb4eeee4eeeeeb.........
                    ..........bce4eeeeb4eeee4eeeeebc........
                    ..........bce4eeeeb44eee4eeeeebc........
                    ..........bce4ebeebb4eee4eeeeebc........
                    ..........bce4eebeee4eee4eeeeebc........
                    ..........bceeeeebeeeeee4eeeeebc........
                    ..........bceeeeebbeeeee4eeeeebc........
                    ..........bce4eeeebbeeee4eeeeebc........
                    ..........bce4eeeeebbeee4eeeeebc........
                    ..........bce4e4eeeeeeee4eeeeebc........
                    ..........bce4ee4eeeeeee4eeeeebc........
                    ..........bce4ee4eeeeeee4eeeeebc........
                    ..........bce4eeeeeeeeee4eeeebbc........
                    ..........bce4eeeeeeeeee4eeeebcc........
                    ..........bce4eeb4eeeeee4eeeebbc........
                    ..........bce4eeb4eeeeee4eeeeebc........
                    ..........bce4eeb4eeeeee4eeeeeb.........
                    ..........bce4eeb4eeeeee4eeeeeb.........
                    ..........bce4eeb4eeeeee4eeeeeb.........
                    ..........bce4eeb4eeeeeee4eeeeb.........
                    ..........bce4eee4eeeeeee4eeebb.........
                    ..........bce4eeeeeeeeeee4eeebb.........
                    ..........bceeeeeeeeeeeee4eeebb.........
                    ..........bceeeeeeeeeeeeeeeeecb.........
                    ..........bcee4444444eeeeeeeecb.........
                    ..........bceebbbeeeeeeebbbbbcb.........
                    ..........bceeeebbbbeeeebdbbbcb.........
                    ..........bceeebbeebbeeedbbbbcc.........
                    ..........bceeeebbeeebeecbbbcbc.........
                    ..........bceeeeeebeeeeebbbbcbc.........
                    ..........bceeeeeeeeeeeeccccebc.........
                    ..........bceeeeeeeeeeeeb4eeebc.........
                    ..........bcee444eeeeeeeb4eeebc.........
                    ..........bcebbb4444eeeeb4eeebc.........
                    ..........bceeeeeee444eeb4eeebc.........
                    ..........bce4eeeeeeeeeeb4eeebc.........
                    ..........bce4eeeeeeeeeee4eeebc.........
                    ..........bce4eeeeeeeeeeeeeeebc.........
                    ..........bce4eeeee4eeeeeeeeebc.........
                    ..........bceeeeeee4eeeeeeeeebc.........
                    ..........bceeeeeee4eeee4eeebbc.........
                    ..........bceeeeeee4eeee4eeeebc.........
                    ..........bcee4eeee4eeee4eeeebc.........
                    ..........bcee44eee4eeee4eeeebc.........
                    ..........bceeb44ee4eeee4eeeebc.........
                    .........b.beebbb4eeeeee4eeeebc.........
                    ...........cbeeebb4eeeee4eeeebc.........
                    ............cbeeeb4eeeee4eeeebc.........
                    .............cbeeeeeeeee4eeeebc.........
                    .............cbbeeeeeeeeeeeeebc.........
                    ..............cbbeeeeeeeeeeeebc.........
                    ...............cbeeeeeeeeeeeebc.........
                    ...............bcbeee4eeeeeeebc.........
                    ...............cbcbeeb4eeeeebbc.........
                    ................bbceeb44eeeebcc.........
                    ................cbbcebb44eeebcc.........
                    ................cbbcbebb44eecb..........
                    .................bbbceebb44eeb..........
                    .................cbbbceeee4eeb..........
                    ..................cbbbceeeeeeb..........
                    ...................cbbbceeeeeb..........
                    ....................cbbbceeeeb..........
                    .....................cbbbceeeb..........
                    ......................ccbceeeb..........
                    ........................cbcbeb..........
                    .........................cbceb..........
                    ..........................cbcb..........
                    ...........................cbc..........
                    ............................c...........
                    ........................................
                    ........................................
                    ........................................
                    ........................................
                    ........................................
                    ........................................
                    ........................................
                    ........................................
                    ........................................
        """),
        SpriteKind.door)
    kitchen_door.set_position(148, 75)
    knob = sprites.create(img("""
            e b b b b b c 
                    e b d b b b c 
                    e d b b b b c 
                    e c b b b c b 
                    e b b b b c b 
                    e c c c c e b
        """),
        SpriteKind.Button)
    knob.set_position(155, 70)
    game.show_long_text("This must be his family's home.", DialogLayout.BOTTOM)
    game.show_long_text("Find Gorp.", DialogLayout.BOTTOM)
    mySprite = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    .........5..........
                    ........585.........
                    .......54445........
                    ......5444445.......
                    ......4444444.......
                    .....544444445......
                    .....844444448......
                    ........444.........
                    ........444.........
                    ........444.........
                    ........888.........
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.player)
    controller.move_sprite(mySprite)
mySprite: Sprite = None
letter2: Sprite = None
milk: Sprite = None
brad: Sprite = None
soap2: Sprite = None
wood2: Sprite = None
rock2: Sprite = None
AWater: Sprite = None
knob: Sprite = None
kitchen_door: Sprite = None
scene.set_background_image(img("""
    bbbbbb77777777777766777777776677777777777677777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbb77777777777766777777776677777777777677777777777777777776bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbb6677777777776767777777767777777777767777777777777777677766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbb66777777777676777777776777777777767777777776677777667776677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbb6bb7777766767777777767777777776777777667777776667777766777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbb777bb666666b776777776777677777777677777777667777767777777766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbb7777777777776666666777677777776777777677766777767777777766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbb77777777777767777bb77767666666777777767b77767776777777b66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbb77777777777667777776666766666677777777677777667777777b66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbb7777777776677777777777667777767777766677777666777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbb6667777777666777777777767777777766666677666666666666777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbb77bb776666666777777777767777777777777777767777776666677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbb666777777766666677777777777777777776777777777777b77bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbb6677777777677777777777777777777777666777777777767b677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbb6777777776677777777666677777bb666667777777777666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbb7677777777777777777667b7777777b6777777777777766677b77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbb76777777777777b677767bb777777b67777777777777767777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbb6777777777777b6667666bb7777bb667777766677777677b7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbb6b77777777777b6b6666b666466776677666666b766667bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbb6777777777777b66666b7bbe66666666666bb666bbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbb766b66666b777766bbbbbbbe4eeeeeee7766667ebbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbb66bbbbb6666667bbbbbbbe44beeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbb66bbbbbbbbee4eeeeeeeeee444e4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee4eeeeeee44eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe44eeebeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd66ddddd666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4beeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddee6666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddeedeeeeeeeee666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddd6dbb6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddd6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbb77777bbeeeee4eeeee4eeee44bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6edddddddddddddddddddd6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbb777777beeeee4eeeee4eeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd66edddddddddddddddddddd6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbb777777777eeeee4eeeee4eeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd66eeedddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbb7777777777eeeee4eeeee4eeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddd66bbddddddddd6dddddddddd66ddd6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb78887778887eeeee4eeeee4eeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd6666bbdddddddddddddddddddddd66ddd6bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb7877777877eeeeee4eeee4beeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd6ddbbbdddddddddd6deededdddddd6bddd6dbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb78888788888eeeee4eeee4beeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbdddddddd666eeeeddeddddddd6bbddd666bbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb8666878666eeeeee4eeee4beeeeebebbbbbbbbbbbb3bbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddd6eedddddddddddddd6bbddddd666bbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb8888778888eeeeee4eeee4beeeeeeebbbbbbbbbbba3babbbbbbbbbbbbbbbbbbbbbbbbbbddd666ddddddddddddeddddddddddddddd6bbddddddd66bbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb7887777777eeeee4eeeee4beeeeeeebbbbbbbbbb33aabbbbbbbbbbbbbbbbbbbbbbbbbdddd6ddddddddddddddddddddddddddddddd6dddddddddddddbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb7777777777eeeee4eeeee4beeee4eebbbbbbbbbb3ca3bbbbbbbbbbbbbbbbbbbbbbbb66666dddddddddddddddddddddddddddddddd6ddddddddddddddbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb7777788777eeeeeeeeeeeebebee4bebbbbbbbbbbb33b7bbbbbbbbbbbbbbbbbbbbb66ddddddddddddddddddddddddddddddddddddd66ddddddddddddddbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb777777777eeeeeeeeeeeeebe4ee4e66bbbbbbbb7bb777bbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddd66dddd6666dddddbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb777777777eeeeeeeee4eeeee4ee4e66bbbbbbbb77776bbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddeeeeeeeedd666bbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb777777777eeeeeeeee4eeeee4ee446bbbbbbbbbb767bbbbbbbbbbbbbbbbbbbbbbddddddddddddddd666666666dddddddddddddddddddddddddddeeeeee6bbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb777b77766ebebeeeee4eeeeee4ee46ebbbbbbbbbb67bbbbbbbbbbbbbbbbbbbbbbddddddddddbbb66dddddddd6dddddddddddddddddddddddddddddddded6bbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbb777b7b66eeeebeeeee4eeeeee4ee66ebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbbedddddddbbb6ddddddddddd666666ddddddddddddddddddddddddddddd6bbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbb7bbbbbbbeebebee4eee4eeeeeee4ebeebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbeeddddddbbd66dddddddddddddddd666ddddddddddddddddddddddddddd6bbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbe4eeebe4eeeeeee4beeee44eebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbeeebbbbbeed6ddeeeeeeeeeeeeeeeddd66bbddddddddddddddddddddddddbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbee4eeeee4eeeeeee4beeeee44ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeedeee6666eeddddd666666d6eeddd666bbbbdddddddddddddddddddddbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbe4eeeeee4eeeeeee4eeeeeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6edeee6666bbbee6666666666666666dddd666bbdeeeeedddddddddddddbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbe4eeeeeee4eeeeee44e66eeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6ed66bbbbbbbbbb66666bbbbb66666bbeeeeeeeeeebddeee666dddddddddbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbb44e666be44eeb66e4e6beeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666bbbbbbbbbbbbbbbbbbbbbbbbb66666666666666bb6666bb666666bd66bbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbb44e66bbb44eebbb6e4e6666ebeebbeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66db666bbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbb4e66bbbe4eeebbb6e4ebbb66ebbbbbeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbeebbbbbebbebbbb6eeeebbb6ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbebbebbbb66eeebbb66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbebbbbbeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
game.show_long_text("Welcome to Gorp N Seek. In this game, you will be asked to find something.",
    DialogLayout.BOTTOM)
if controller.A.is_pressed():
    scene.set_background_image(img("""
        bbbbbb77777777777766777777776677777777777677777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb77777777777766777777776677777777777677777777777777777776bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb6677777777776767777777767777777777767777777777777777677766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb66777777777676777777776777777777767777777776677777667776677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb6bb7777766767777777767777777776777777667777776667777766777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbb777bb666666b776777776777677777777677777777667777767777777766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb7777777777776666666777677777776777777677766777767777777766bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb77777777777767777bb77767666666777777767b77767776777777b66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbb77777777777667777776666766666677777777677777667777777b66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb7777777776677777777777667777767777766677777666777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb6667777777666777777777767777777766666677666666666666777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbb77bb776666666777777777767777777777777777767777776666677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbb666777777766666677777777777777777776777777777777b77bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbb6677777777677777777777777777777777666777777777767b677bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbb6777777776677777777666677777bb666667777777777666666666bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb7677777777777777777667b7777777b6777777777777766677b77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb76777777777777b677767bb777777b67777777777777767777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb6777777777777b6667666bb7777bb667777766677777677b7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbb6b77777777777b6b6666b666466776677666666b766667bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb6777777777777b66666b7bbe66666666666bb666bbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbb766b66666b777766bbbbbbbe4eeeeeee7766667ebbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbb66bbbbb6666667bbbbbbbe44beeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbb66bbbbbbbbee4eeeeeeeeee444e4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee4eeeeeee44eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd66ddddd666bbbbbbbbbbbb777777bbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe44eeebeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddee6666666666bbbbbbbb6777777777bbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4beeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddeedeeeeeeeee666bbbbb6677777777776bbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddd6dbb6677777777777776bbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe4eee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddd67777777777777766bbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee4eeeee4eeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6edddddddddddddddddddd67888877777886776bbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee4eeeee4eeee44bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd66edddddddddddddddddddd67777777777777776bbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee4eeeee4eeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd66eeedddddddddddddddddddd678888877788887776bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeeee4eeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddd66bbddddddddd6dddddddddd66dd7868777886777776bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeeee4eeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd6666bbdddddddddddddddddddddd66d67868777876677776bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeeee4eeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd6ddbbbdddddddddd6deededdddddd6bd6d788777888887766bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeee4beeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbdddddddd666eeeeddeddddddd6bb66777777777777766bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeee4beeeeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddd6eedddddddddddddd6bbd6667777777777766bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeee4beeeeebebbbbbbbbbbbb3bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddd666ddddddddddddeddddddddddddddd6bbdd66d667777777776bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeee4eeee4beeeeeeebbbbbbbbbbba3babbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddd6ddddddddddddddddddddddddddddddd6ddddd666688877777766bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeee4eeeee4beeeeeeebbbbbbbbbb33aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66666dddddddddddddddddddddddddddddddd6ddddddd66d6777777776bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeee4eeeee4beeee4eebbbbbbbbbb3ca3bbbbbbbbbbbbbbbbbbbbbbbbbbbbb66ddddddddddddddddddddddddddddddddddddd66ddddddddddd77777776bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbb44eeeeeeeeeeebebee4bebbbbbbbbbbb33b7bbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddd66dddd66666666777776bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbb4eeeeeeeeeeeebe4ee4e66bbbbbbbb7bb777bbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddeeeeeeeedd6666776bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeee4eeeee4ee4e66bbbbbbbb77776bbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddd666666666dddddddddddddddddddddddddddeeeeee6676bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeee4eeeee4ee446bbbbbbbbbb767bbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddbbb66dddddddd6dddddddddddddddddddddddddddddddded676bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbb6ebebeeeee4eeeeee4ee46ebbbbbbbbbb67bbbbbbbbbbbbbbbbbbbbbbbbbbbbbedddddddbbb6ddddddddddd666666ddddddddddddddddddddddddddddd676bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbb66eeeebeeeee4eeeeee4ee66ebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeddddddbbd66dddddddddddddddd666ddddddddddddddddddddddddddd676bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbeebebee4eee4eeeeeee4ebeebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeebbbbbeed6ddeeeeeeeeeeeeeeeddd66bbdddddddddddddddddddddddd67bbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbe4eeebe4eeeeeee4beeee44eebbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeedeee6666eeddddd666666d6eeddd666bbbbdddddddddddddddddddddbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbee4eeeee4eeeeeee4beeeee44ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6edeee6666bbbee6666666666666666dddd666bbdeeeeedddddddddddddbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbe4eeeeee4eeeeeee4eeeeeeee4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb6ed66bbbbbbbbbb66666bbbbb66666bbeeeeeeeeeebddeee666dddddddddbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbe4eeeeeee4eeeeee44e66eeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666bbbbbbbbbbbbbbbbbbbbbbbbb66666666666666bb6666bb666666bd66bbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbb44e666be44eeb66e4e6beeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66db666bbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbb44e66bbb44eebbb6e4e6666ebeebbeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbb4e66bbbe4eeebbb6e4ebbb66ebbbbbeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbeebbbbbebbebbbb6eeeebbb6ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbebbebbbb66eeebbb66bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbebbbbbeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeebebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    """))
    game.show_long_text("Can you do it?", DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        levelOne()