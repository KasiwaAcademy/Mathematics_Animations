from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class SimplifyQuadraticExpressions(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")  # ✅ REQUIRED
        my_template.add_to_preamble(r"\usepackage{cancel}")
        my_template.add_to_preamble(r"\renewcommand{\CancelColor}{\color{red}}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Problem Statement
        problem = (
            Tex(r"Simplify $\frac{a^2 + 2ab + b^2}{a^2 - b^2}$").to_edge(UP).scale(1.5)
        )
        eq_group_1 = VGroup(
            MathTex(r"\frac{a^2 + 2ab + b^2}{a^2 - b^2}"),
            MathTex(r"\frac{(a + b)^2}{(a + b)(a - b)}"),
        ).arrange(DOWN, buff=0.5)
        box_1 = SurroundingRectangle(
            eq_group_1, color=BLUE_B, buff=0.5, corner_radius=0.1
        ).set_stroke(width=1)
        box_1_group = VGroup(eq_group_1, box_1)

        eq_group_2 = VGroup(
            MathTex(r"\frac{(a + b)(a + b)}{(a + b)(a - b)}"),
            MathTex(
                r"\frac{\cancel{(a + b)}(a + b)}{\cancel{(a +b)}(a - b)}",
                tex_template=my_template,
            ),
        ).arrange(DOWN, buff=0.5)
        box_2 = SurroundingRectangle(
            eq_group_2, color=BLUE_B, buff=0.5, corner_radius=0.1
        ).set_stroke(width=1)
        box_2_group = VGroup(eq_group_2, box_2)

        solution = MathTex(r"\frac{a + b}{a - b}")
        solution_box = SurroundingRectangle(
            solution, color=BLUE_B, buff=0.5, corner_radius=0.1
        ).set_stroke(width=1)
        solution_group = VGroup(solution, solution_box)

        self.play(Write(problem), run_time=2)
        self.wait(4)
        self.play(Write(box_1_group[0][0]), run_time=2)
        self.wait(11)
        self.play(TransformFromCopy(box_1_group[0][0], box_1_group[0][1]), run_time=2)
        self.wait(13)
        self.play(FadeIn(box_1_group[1]), box_1_group.animate.to_edge(LEFT))
        # self.wait(13)

        self.play(Write(box_2_group[0][0]), run_time=2)
        self.wait(13)
        self.play(TransformFromCopy(box_2_group[0][0], box_2_group[0][1]), run_time=2)
        self.wait(7)
        self.play(Write(box_2_group[1]), box_2_group.animate.to_edge(RIGHT))
        # self.wait(3)

        self.play(Write(solution_group[0]), run_time=2)
        self.wait()
        self.play(FadeIn(solution_group[1]), solution_group.animate.to_edge(DOWN))
        self.wait()
        self.play(Indicate(solution_group))
        self.wait(3)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem, box_1_group, box_2_group, solution_group)),
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
            MathTex(r"\frac{a^2 + 2ab + b^2}{a^2 - b^2}", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
