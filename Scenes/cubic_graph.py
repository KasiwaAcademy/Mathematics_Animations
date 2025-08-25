# Main Py
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

class CubicGraph(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Solving Simultaneous Equations Graphically.", color=YELLOW)
        institution = Tex(r"@Kasiwa Academy")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B), FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        sub_title_1 = Tex(r"Problem Statement:", color=YELLOW).to_edge(DOWN)
        statement_1 = Tex(r"Solve the following simultaneous equations graphically:")
        eq_group_1 = VGroup(
            MathTex(r"y = x^3 + 3x^2 + x -2"),
            MathTex(r"y = 2x + 1")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(statement_1, DOWN, buff=0.3)
        self.play(Write(sub_title_1))
        self.wait()
        self.play(FadeOut(title, institution, shift=UP), sub_title_1.animate.to_edge(UP).scale(1.3).set_color(WHITE), 
                  FadeIn(statement_1, eq_group_1, shift=UP))
        self.wait()
        self.play(statement_1.animate.scale(1.1))
        self.wait(2)

        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(Write(final_text), FadeOut(statement_1, sub_title_1, eq_group_1, shift=RIGHT))
        self.wait()
        self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                    final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3))
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        self.wait()

# Thumbnail for CubicGraph
class Thumbnail(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Images/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)
        
        # Title text
        title = Text(
            "Change", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "Subject of Formula", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)

        # Quadratic Formula
        formula = MathTex(
            r"x = \frac{b - k^3}{k^3}", color=WHITE
        ).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        self.add(title, subtitle, formula)
