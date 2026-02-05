from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class LabTest(Scene):
    def construct(self):
        # Problem Statement
        problem = Tex(r"Expand $(a + b)^2$")
        eq_group = (
            VGroup(
                MathTex(r"(a+b)^2"),
                MathTex(r"(a+b)(a+b)"),
                MathTex(r"a(a+b)+b(a+b)"),
                MathTex(r"a^2+ab+ab+b^2"),
                MathTex(r"a^2+2ab+b^2"),
            )
            .arrange(DOWN, buff=0.5, aligned_edge=RIGHT)
            .shift(LEFT * 2)
        )
        # arrow_1 = Arrow(start=eq_group[0].get_right(), end=eq_group[0].get_right(), buff=0.1)
        annot_1 = Text("Step 1", font_size=30, color=RED).next_to(
            eq_group[0], RIGHT * 6
        )
        annot_2 = Text("Step 2", font_size=30, color=RED).next_to(
            eq_group[1], RIGHT * 6
        )
        annot_3 = Text("Step 3", font_size=30, color=RED).next_to(
            eq_group[2], RIGHT * 6
        )
        annot_4 = Text("Step 4", font_size=30, color=RED).next_to(
            eq_group[3], RIGHT * 6
        )
        annot_5 = Text("Final answer", font_size=30, color=RED).next_to(
            eq_group[4], RIGHT * 6
        )
        annot_group = VGroup(annot_1, annot_2, annot_3, annot_4, annot_5)
        box = SurroundingRectangle(eq_group[4])
        self.play(Write(problem))
        self.wait()
        self.play(problem.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B))
        self.wait()
        self.add(annot_group)
        self.wait()
        self.play(Write(eq_group[0]))
        self.wait()
        self.play(TransformFromCopy(eq_group[0], eq_group[1]))
        self.wait()
        self.play(TransformFromCopy(eq_group[1], eq_group[2]))
        self.wait()
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait()
        self.play(TransformFromCopy(eq_group[3], eq_group[4]))
        self.wait()
        self.add(box)
        self.play(Indicate(VGroup(eq_group[4], box)))
        self.wait()
        self.play(ShrinkToCenter(VGroup(problem, eq_group, box)))
        self.wait()
