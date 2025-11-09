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
            text_box_1 = Text(text_1, color=PURE_RED, font_size=30).move_to(
                LEFT * 4.3 + UP * 3.5
            )
            box = SurroundingRectangle(
                text_box_1, buff=0.1, color=GRAY_A, corner_radius=0.2
            ).set_stroke(width=0.3)
            box_group = VGroup(text_box_1, box)
            step_x_text = Tex(text_2).next_to(box, RIGHT, buff=0.5).set_color(YELLOW_C)
            return {"box_group": box_group, "step_x_text": step_x_text}

        step_1 = steps(r"Step 1", r"Arrange equations as equation (i) and (ii):")
        box_group_1 = step_1["box_group"]
        step_1_text = step_1["step_x_text"]
        eq_group_1 = VGroup(
            Tex(r"$xy = 15$ - - - (i)"),
            Tex(r"$y + 1 = 2x$ - - - (ii)"),
            Tex(r"$y + 1 - 1 = 2x -1$").set_color(BLUE),
            Tex(r"$y = 2x -1$ - - - (iii)").set_color(BLUE),
        ).arrange(DOWN, buff=0.5)
        self.play(FadeOut(problem_group[0]), FadeIn(box_group_1), Write(step_1_text))
        self.wait()
        self.play(Transform(problem_group[1], eq_group_1[0]))
        self.wait()
        self.play(Transform(problem_group[2], eq_group_1[1]))
        self.wait(2)

        # Step 2
        step_2 = steps(r"Step_2", r"Express $y$ interms of $x$ in equation (i):")
        box_group_2 = step_2["box_group"]
        step_2_text = step_2["step_x_text"]
        self.play(
            Transform(box_group_1, box_group_2), FadeTransform(step_1_text, step_2_text)
        )
        self.wait()
        self.play(Write(eq_group_1[2]))
        self.wait()
        self.play(TransformFromCopy(eq_group_1[2], eq_group_1[3]))
        self.wait(2)

        # Step 3
        step_3 = steps(r"Step_3", r"Substitute equation (iii) in equation (i) for $y$:")
        box_group_3 = step_3["box_group"]
        step_3_text = step_3["step_x_text"]
        eq_group_2 = VGroup(
            MathTex(r"xy = 15"),
            MathTex(r"x(2x - 1) = 15"),
            MathTex(r"2x^2 - x = 15"),
            MathTex(r"2x^2 -x - 15 = 0"),
        ).arrange(DOWN, buff=0.5)
        self.play(
            Transform(box_group_1, box_group_3),
            FadeTransform(step_2_text, step_3_text),
            eq_group_1.animate.move_to(LEFT * 5.5 + UP * 1).scale(0.5),
            FadeOut(problem_group[1:]),
        )
        box_eq_group_1 = SurroundingRectangle(
            eq_group_1, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_1, eq_group_2))
        self.wait(2)
        self.play(eq_group_2.animate.move_to(LEFT * 5.5 + DOWN * 2).scale(0.5))
        box_eq_group_2 = SurroundingRectangle(
            eq_group_2, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_2))
        self.wait(2)

        # Step 4
        step_4 = steps(r"Step_4", r"Solve the quadratic equation by factorization:")
        box_group_4 = step_4["box_group"]
        step_4_text = step_4["step_x_text"]
        eq_group_3 = (
            VGroup(
                MathTex(r"2x^2 - x - 15"),
                MathTex(r"2x^2 \quad \times \quad - 15"),
                MathTex(r"- 30x^2"),
                MathTex(r"- 6x \qquad 5x"),
                MathTex(r"2x^2 -6x + 5x -15 = 0"),
                MathTex(r"(2x^2 - 6x) + (5x - 15) = 0"),
                MathTex(r"2x(x - 3) + 5(x - 3) = 0"),
                MathTex(r"(2x + 5)(x - 3) = 0"),
                Tex(r"$2x + 5 = 0$ \quad or \quad $x - 3 = 0$"),
                Tex(r"$x = -\frac{5}{2}$ \quad or \quad $x = 3$"),
            )
            .arrange(DOWN, buff=0.3)
            .scale(0.75)
        )
        self.play(
            Transform(box_group_1, box_group_4),
            FadeOut(step_3_text),
            Write(step_4_text),
            FadeIn(eq_group_3),
        )
        self.wait()
        self.play(eq_group_3.animate.move_to(RIGHT * 5.5 + UP * 1).scale(0.5))
        box_eq_group_3 = SurroundingRectangle(
            eq_group_3, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_3))
        self.wait(2)

        # Step 5
        step_5 = steps(r"Step_5", r"Solve for $y$ when $x = - \frac{5}{2}$:")
        box_group_5 = step_5["box_group"]
        step_5_text = step_5["step_x_text"]
        eq_group_4 = VGroup(
            MathTex(r"y = 2x - 1"),
            MathTex(r"y = 2(-\frac{5}{2}) - 1"),
            MathTex(r"y = -\frac{10}{2} - 1"),
            MathTex(r"y = - 6"),
        ).arrange(DOWN, buff=0.5)
        self.play(
            Transform(box_group_1, box_group_5),
            FadeOut(step_4_text),
            Write(step_5_text),
            FadeIn(eq_group_4),
        )
        self.wait()
        self.play(eq_group_4.animate.move_to(RIGHT * 5.5 + DOWN * 2).scale(0.3))
        box_eq_group_4 = SurroundingRectangle(
            eq_group_4, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_4))
        self.wait(2)

        # Step 6
        step_6 = steps(r"Step_6", r"Solve for $y$ when $x = 3$:")
        box_group_6 = step_6["box_group"]
        step_6_text = step_6["step_x_text"]
        eq_group_5 = VGroup(
            MathTex(r"y = 2x - 1"),
            MathTex(r"y = 2(3) - 1"),
            MathTex(r"y = 6 - 1"),
            MathTex(r"y = 5"),
        ).arrange(DOWN, buff=0.5)
        self.play(
            Transform(box_group_1, box_group_6),
            FadeOut(step_5_text),
            Write(step_6_text),
            FadeIn(eq_group_5),
        )
        self.wait()
        self.play(eq_group_5.animate.move_to(RIGHT * 3 + DOWN * 2).scale(0.3))
        box_eq_group_5 = SurroundingRectangle(
            eq_group_5, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_5))
        self.wait(2)

        # Step 7
        step_7 = steps(r"Step_7", r"Final Solution:")
        box_group_7 = step_7["box_group"]
        step_7_text = step_7["step_x_text"]
        eq_group_6 = VGroup(
            MathTex(r"(x, y) = (3, 5)"),
            Tex(r"or"),
            MathTex(r"() = (- \frac{5}{2}, -6)"),
        ).arrange(DOWN, buff=0.5)
        self.play(
            Transform(box_group_1, box_group_7),
            FadeOut(step_6_text),
            Write(step_7_text),
            FadeIn(eq_group_6),
        )
        self.wait()
        self.play(eq_group_6.animate.move_to(LEFT * 3 + DOWN * 2).scale(0.3))
        box_eq_group_6 = SurroundingRectangle(
            eq_group_6, buff=0.3, color=PURE_BLUE, corner_radius=0.1
        ).set_stroke(width=0.5)
        self.play(FadeIn(box_eq_group_6))
        self.wait(2)
        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(
            box_eq_group_1,
            box_eq_group_2,
            eq_group_2,
            eq_group_3,
            eq_group_4,
            eq_group_5,
            eq_group_6,
            eq_group_1,
            box_group_1,
            step_7_text,
            box_eq_group_3,
            box_eq_group_4,
            box_eq_group_5,
            box_eq_group_6,
        )
        self.play(Write(final_text), ShrinkToCenter(final_solution_group))
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        self.wait()
