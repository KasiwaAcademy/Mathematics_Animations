from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class Reel(Scene):
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
            r"Solve for $p$ and $q$ in $\frac{32^4 \times 625^3}{8^6 \times 25^4} = 2^p5^q$"
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = (
            VGroup(
                MathTex(r"\frac{32^4 \times 625^3}{8^6 \times 25^4} = 2^p5^q"),
                MathTex(r"\frac{2^{20} \times 5^{12}}{2^{18} \times 5^8} = 2^p5^q"),
                MathTex(r"2", r"^2", r"\times 5", r"^4", r"= 2", r"^p", r"5", r"^q"),
                Tex(r"$p=2$", r" and ", r"$q=4$"),
            )
            .arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            .shift(RIGHT * 3)
        )
        eq_group[2][1].set_color(PURE_BLUE)
        eq_group[2][5].set_color(PURE_BLUE)
        eq_group[2][3].set_color(PURE_GREEN)
        eq_group[2][7].set_color(PURE_GREEN)
        eq_group[3][0].set_color(PURE_BLUE)
        eq_group[3][2].set_color(PURE_GREEN)

        box_1 = SurroundingRectangle(eq_group[3][0], color=PURE_BLUE, buff=0.1)
        box_2 = SurroundingRectangle(eq_group[3][2], color=PURE_GREEN, buff=0.1)
        annot_1 = (
            Tex(
                r"Write each element as a \\"
                r"power of $2$ and $5$."
            )
            .next_to(eq_group[0], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_2 = (
            Tex(
                r"Simplify the Left-Hand-Side\\"
                r"of the equation."
            )
            .next_to(eq_group[1], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_3 = (
            Tex(r"Equate the elements")
            .next_to(eq_group[2], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_group = VGroup(annot_1, annot_2, annot_3)
        self.play(Write(problem_group[0]))
        self.wait(2)
        self.play(problem_group.animate.to_edge(UP).scale(1.1).set_color(YELLOW_B))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Write(annot_group[0]))
        self.wait()
        self.play(TransformFromCopy(eq_group[0], eq_group[1]))
        self.wait(2)
        self.play(Write(annot_group[1]))
        self.wait()
        self.play(TransformFromCopy(eq_group[1], eq_group[2]))
        self.wait(2)
        self.play(Write(annot_group[2]))
        self.wait()
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(
            Indicate(eq_group[3][0], color=PURE_BLUE),
            Indicate(eq_group[3][2], color=PURE_GREEN),
            FadeIn(box_1, box_2),
        )
        self.wait(3)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem_group, eq_group, annot_group, box_1, box_2)),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        # self.wait()


# Thumbnail
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
            Text("Find the values", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )

        subtitle = (
            Tex(r"\textbf{of} $p$ \textbf{and} $q$")
            .set_color(WHITE)
            .scale(2)
            .next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(r"\frac{32^4 \times 625^3}{8^6 \times 25^4} = 2^p5^q", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
