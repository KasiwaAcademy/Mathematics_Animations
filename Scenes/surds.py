from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class RationalisingSurds(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")
        my_template.add_to_preamble(r"\usepackage{cancel}")
        my_template.add_to_preamble(r"\renewcommand{\CancelColor}{\color{red}}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Problem Statement
        problem = Tex(
            r"Simplify $\frac{\sqrt{5}-3\sqrt{3}}{2\sqrt{3} + \sqrt{5}}$,  leaving",
            r"your answer with a rational denominator.",
        ).arrange(DOWN, buff=0.4)
        title = Text(r"Rationalising the Denominator", font_size=48).to_edge(UP)
        underline = Underline(title, buff=0.1)
        title_group = VGroup(title, underline)

        # Equation Group 1
        eq_group_1 = (
            VGroup(
                MathTex(r"\frac{\sqrt{5} - 3\sqrt{3}}{2\sqrt{3} - \sqrt{5}}"),
                MathTex(
                    r"\frac{(\sqrt{5}-3\sqrt{3})(2\sqrt{3}-\sqrt{5})}"
                    r"{(2\sqrt{3}+\sqrt{5})(2\sqrt{3}-\sqrt{5})}"
                ),
                MathTex(r"\frac{5\sqrt{15} - 23}{7}"),
            )
            .arrange(DOWN, buff=0.5)
            .scale(0.7)
        )

        # Equation Group 2
        eq_group_2 = (
            VGroup(
                Text(r"Expand Numerator", color=PURE_RED, font_size=30),
                MathTex(r"(\sqrt{5}-3\sqrt{3})(2\sqrt{3}-\sqrt{5})"),
                MathTex(r"2\sqrt{15} - \sqrt{25} - 6\sqrt{9} - 3\sqrt{15}"),
                MathTex(r"2\sqrt{15} - 5 - 18 + 3\sqrt{15}"),
                MathTex(r"5\sqrt{15} - 23"),
            )
            .arrange(DOWN, buff=0.5)
            .scale(0.7)
        )

        # Equation Group 3
        eq_group_3 = (
            VGroup(
                Text(r"Expand Denominator", color=PURE_RED, font_size=30),
                MathTex(r"(2\sqrt{3}-\sqrt{5})(2\sqrt{3}-\sqrt{5})"),
                MathTex(r"4\sqrt{9} - 2\sqrt{15} + 2\sqrt{15} + \sqrt{25}"),
                MathTex(r"12 - 5"),
                MathTex(r"7"),
            )
            .arrange(DOWN, buff=0.5)
            .scale(0.7)
        )

        columns = VGroup(eq_group_2, eq_group_1, eq_group_3).arrange(
            RIGHT, buff=1, aligned_edge=UP
        )
        arrow_1 = Arrow(
            start=columns[1][1][0][0].get_left(),
            end=columns[0][1].get_right(),
            buff=0.1,
            stroke_width=3,
            color=BLUE,
        )
        arrow_2 = Arrow(
            start=columns[1][1][0][-1].get_right(),
            end=columns[2][1].get_left(),
            buff=0.1,
            stroke_width=3,
            color=BLUE,
        )

        self.play(Write(problem), run_time=3)
        self.wait(2)
        self.play(Transform(problem, title_group), Write(columns[1]))
        self.wait(2)
        self.play(FadeIn(columns[0], columns[2], arrow_1, arrow_2))
        self.wait(3)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem, columns, arrow_1, arrow_2)),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        # self.wait()


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
        title = (
            Text("Simplify", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )

        subtitle = (
            Text("the following", font="Roboto", weight=BOLD, color=WHITE)
            .scale(1.5)
            .next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(r"\frac{\sqrt{5}-3\sqrt{3}}{2\sqrt{3} + \sqrt{5}}", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
