# Main Py
from manim import *
from numpy import array

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

        # Complete the tables of values
        sub_title_2 = Tex(r"Complete the tables of values:", color=YELLOW).to_edge(DOWN)
        table_group_1 = Group(
                    MathTex(r"y = x^3 + 3x^2 + x - 2"),
                    MathTable(
                        [["-3", "-2", "-1", "0", "1", "2", "3"],
                         ["", "", "", "", "", "", ""]],
                        row_labels=[MathTex("x"), MathTex("y")],
                        include_outer_lines=True,
                        line_config={"stroke_width":1} 
                        ).scale(0.5)
                ).arrange(DOWN).scale(0.75).move_to([-4, 1, 0]) 
        table_group_2 = Group(
                    MathTex(r"y = 2x + 1"),
                    MathTable(
                        [["-3", "-2", "-1", "0", "1", "2", "3"],
                         ["", "", "", "", "", "", ""]],
                        row_labels=[MathTex("x"), MathTex("y")],
                        include_outer_lines=True,
                        line_config={"stroke_width":1} 
                        ).scale(0.5)
                ).arrange(DOWN).scale(0.75).move_to([-4, -1, 0])

        #================y values for y = x³ + 3x² + x - 2 ===========================#
        s_1 = VGroup(
            MathTex(r"y = x^3 + 3x^2 + x - 2"),
            MathTex(r"\Rightarrow f(x) = x^3 + 3x^2 + x - 2"),
            MathTex(r"\Rightarrow f(-3) = (-3)^3 + 3(-3)^2 + (-3) - 2"),
            MathTex(r"\Rightarrow f(-3) = -27 + 27 -3 - 2"),
            MathTex(r"\Rightarrow f(-3) = -5"),
            MathTex(r"\Rightarrow y = -5")
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT).scale(0.75)
        #================y values for y = 2x + 1 ===========================#
        s_2 = VGroup(
            MathTex(r"y = 2x + 1"),
            MathTex(r"\Rightarrow f(x) = 2x + 1"),
            MathTex(r"\Rightarrow f(-3) = 2(-3) + 1"),
            MathTex(r"\Rightarrow f(-3) = -6 + 1"),
            MathTex(r"\Rightarrow f(-3) = -5"),
            MathTex(r"\Rightarrow y = -5")
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT).scale(0.75)
        self.play(Write(sub_title_2))
        self.wait()
        self.play(FadeOut(statement_1, sub_title_1, eq_group_1, shift=UP),
                  sub_title_2.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                  FadeIn(table_group_1, table_group_2, s_1))
        self.wait(5)
        self.play(Transform(s_1, s_2))
        self.wait(5)
        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(Write(final_text), FadeOut(table_group_1, table_group_2, s_1, shift=UP))        
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
