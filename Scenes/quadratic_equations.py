from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class SimplifyQuadraticExpressions(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Problem Statement
        problem = (
            Tex(r"Simplify $\frac{a^2 + 2ab + b^2}{a^2 - b^2}$").to_edge(UP).scale(1.5)
        )
        eq_group_1 = (
            VGroup(
                MathTex(r"\frac{a^2 + 2ab + b^2}{a^2 - b^2}"),
                MathTex(r"\frac{(a + b)^2}{(a + b)(a - b)}"),
            )
            .arrange(DOWN, buff=0.5)
            .to_edge(LEFT)
        )
        eq_group_2 = (
            VGroup(
                MathTex(r"\frac{(a + b)(a + b)}{(a + b)(a - b)}"),
                MathTex(r"\frac{(a + b)(a + b)}{(a +b)(a - b)}"),
            )
            .arrange(DOWN, buff=0.5)
            .to_edge(RIGHT)
        )
        solution = MathTex(r"\frac{a + b}{a - b}").to_edge(DOWN)

        self.play(Write(problem))
        self.wait(3)
        self.play(Write(eq_group_1))
        self.wait(3)
        self.play(Write(eq_group_2))
        self.wait()
        self.play(Write(solution))
        self.wait(3)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            Write(final_text),
            FadeOut(problem, eq_group_1, eq_group_2, solution, shift=UP),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
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
            MathTex(r"\frac{a^2 + 2ab + b^2}{a^2 - b^2}", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
