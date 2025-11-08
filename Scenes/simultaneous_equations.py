# SIMULTANEOUS EQUATIONS
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class FirstSimultaneousEquation(Scene):
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
        problem_group = VGroup(
            Text(r"Solve the following equations Simultaneously:", font_size=32),
            MathTex(r"xy = 15"),
            MathTex(r"y + 1 = 2x"),
        ).arrange(DOWN, buff=0.5)
        self.play(Write(problem_group))
        self.wait(3)

        # Step 1: Arrange equations as equation (i) and (ii)
        # Define a function for dispalying steps
        def steps(text_1, text_2):
            text_box_1 = Text(text_1, color=PURE_RED, font_size=30).to_corner(UL)
            box = SurroundingRectangle(text_box_1, buff=0.3)
            box_group = VGroup(text_box_1, box)
            step_x_text = Text(
                text_2,
                color=YELLOW_B,
                font_size=34,
            ).next_to(box, RIGHT, buff=0.5)
            return {"box_group": box_group, "step_x_text": step_x_text}

        step_1 = steps(r"Step 1", r"Arrange equations as equation (1) and (ii):")
        box_group_1 = step_1["box_group"]
        step_1_text = step_1["step_x_text"]
        eq_group_1 = VGroup(
            Tex(r"$xy = 15$ - - - (i)"), Tex(r"$y + 1 = 2x$ - - - (ii)")
        ).arrange(DOWN, buff=0.5)
        self.play(FadeOut(problem_group[0]), FadeIn(box_group_1))
        self.wait()
        self.play(Write(step_1_text))
        self.wait()
        self.play(Transform(problem_group[1], eq_group_1[0]))
        self.wait()
        self.play(Transform(problem_group[2], eq_group_1[1]))
        self.wait(3)

        # Step 2
        step_2 = steps(r"Step_2", r"Express y interms of x in equation (i):")
        box_group_2 = step_2["box_group"]
        step_2_text = step_2["step_x_text"]
        self.play(Transform(box_group_1, box_group_2), FadeOut(step_1_text))
        self.wait()
        self.play(Write(step_2_text))
        self.wait()

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(problem_group[1:], box_group_1, step_2_text)
        self.play(Write(final_text), ShrinkToCenter(final_solution_group))
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        self.wait()
