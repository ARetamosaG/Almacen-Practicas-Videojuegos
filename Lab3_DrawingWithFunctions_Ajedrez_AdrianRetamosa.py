import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def tiles():
    arcade.draw_lrtb_rectangle_filled(0, 74, 74, 0, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(150, 224, 74, 0, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 374, 74, 0, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 524, 74, 0, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(75, 149, 149, 75, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(225, 299, 149, 75, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(375, 449, 149, 75, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(525, 600, 149, 75, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(0, 74, 224, 150, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(150, 224, 224, 150, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 374, 224, 150, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 524, 224, 150, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(75, 149, 299, 225, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(225, 299, 299, 225, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(375, 449, 299, 225, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(525, 600, 299, 225, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(0, 74, 374, 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(150, 224, 374, 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 374, 374, 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 524, 374, 300, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(75, 149, 449, 375, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(225, 299, 449, 375, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(375, 449, 449, 375, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(525, 600, 449, 375, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(0, 74, 524, 450, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(150, 224, 524, 450, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 374, 524, 450, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 524, 524, 450, arcade.csscolor.WHITE)

    arcade.draw_lrtb_rectangle_filled(75, 149, 599, 525, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(225, 299, 599, 525, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(375, 449, 599, 525, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(525, 600, 599, 525, arcade.csscolor.WHITE)


def rooks():
    arcade.draw_lrtb_rectangle_filled(20, 55, 65, 10, arcade.csscolor.ROSY_BROWN)
    arcade.draw_lrtb_rectangle_filled(545, 580, 590, 535, arcade.csscolor.SANDY_BROWN)

    arcade.draw_lrtb_rectangle_filled(545, 580, 65, 10, arcade.csscolor.ROSY_BROWN)
    arcade.draw_lrtb_rectangle_filled(20, 55, 590, 535, arcade.csscolor.SANDY_BROWN)


def knights():
    arcade.draw_triangle_filled(95, 10, 130, 10, 112, 65, arcade.csscolor.ROSY_BROWN)
    arcade.draw_triangle_filled(470, 10, 505, 10, 487, 65, arcade.csscolor.ROSY_BROWN)

    arcade.draw_triangle_filled(95, 535, 130, 535, 112, 590, arcade.csscolor.SANDY_BROWN)
    arcade.draw_triangle_filled(470, 535, 505, 535, 487, 590, arcade.csscolor.SANDY_BROWN)


def bishops():
    arcade.draw_circle_filled(187, 37, 20, arcade.csscolor.ROSY_BROWN)
    arcade.draw_circle_filled(412, 37, 20, arcade.csscolor.ROSY_BROWN)

    arcade.draw_circle_filled(187, 563, 20, arcade.csscolor.SANDY_BROWN)
    arcade.draw_circle_filled(412, 563, 20, arcade.csscolor.SANDY_BROWN)


def queens():
    arcade.draw_ellipse_filled(262, 37, 30, 60, arcade.csscolor.ROSY_BROWN)
    arcade.draw_ellipse_filled(262, 562, 30, 60, arcade.csscolor.SANDY_BROWN)


def kings():
    arcade.draw_rectangle_filled(337, 37, 10, 60, arcade.csscolor.ROSY_BROWN)
    arcade.draw_rectangle_filled(337, 47, 40, 10, arcade.csscolor.ROSY_BROWN)

    arcade.draw_rectangle_filled(337, 562, 10, 60, arcade.csscolor.SANDY_BROWN)
    arcade.draw_rectangle_filled(337, 572, 40, 10, arcade.csscolor.SANDY_BROWN)


def pawns():
    x = 35
    for i in range(8):
        arcade.draw_rectangle_filled(x, 110, 30, 30, arcade.csscolor.ROSY_BROWN)
        arcade.draw_rectangle_filled(x, 490, 30, 30, arcade.csscolor.SANDY_BROWN)
        x += 75


def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing test")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()
    tiles()
    rooks()
    knights()
    bishops()
    queens()
    kings()
    pawns()
    arcade.finish_render()
    arcade.run()


main()

