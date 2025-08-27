# Main Py
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

class TangentTriangle(Scene):
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
        title = Tex(r"Using Tangents to Solve Triangles.", color=YELLOW)
        institution = Tex(r"@Kasiwa Academy")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B), FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        sub_title_1 = Tex(r"Problem Statement:", color=YELLOW).to_edge(DOWN)
        statement_1 = Tex(r"$ABC$ is a triangle such that $AB = 8cm$, $\angle B = 90^\circ$ \\"
                r"and $BC = 6cm$. $M$ is the midpoint of BC. Calculate:")
        eq_group_1 = VGroup(
            Tex(r"(a) $\angle BAM$"),
            Tex(r"(b) $\angle MAC$")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(statement_1, DOWN, buff=0.3)
        self.play(Write(sub_title_1))
        self.wait()
        self.play(FadeOut(title, institution, shift=UP), sub_title_1.animate.to_edge(UP).scale(1.3).set_color(WHITE), 
                  FadeIn(statement_1, eq_group_1, shift=UP))
        self.wait()
        self.play(statement_1.animate.scale(1.1))
        self.wait(2)

        # Draw a sketch of the Triangle
        sub_title_2 = Tex(r"Draw a sketch of the triangle $ABC$.", color=YELLOW).to_edge(DOWN)

        ## ===== Define coordinates of the points
        A = 2*DOWN + 3*LEFT
        B = 2*DOWN + 2*RIGHT
        C = 2*UP + 2*RIGHT
        M = 2*RIGHT

        ## ===== Define the sides of a triangle
        AB = Line(A, B)
        AC = Line(A, C)
        BC = Line(B, C)
        AM = Line(A, M, stroke_width=2).set_opacity(opacity=0) 
        triangle = Polygon(A, B, C, stroke_width=2, color=WHITE) 

        ## ===== Define the dots and labels
        dot_A, dot_B, dot_C, dot_M = Dot(A, radius=0.025), Dot(B, radius=0.025), Dot(C, radius=0.025), Dot(M, radius=0.05)
        labA = MathTex("A").next_to(dot_A, UL, buff=0.12).scale(0.5)
        labB = MathTex("B").next_to(dot_B, DR, buff=0.12).scale(0.5) 
        labC = MathTex("C").next_to(dot_C, UR, buff=0.12).scale(0.5) 
        labM = MathTex("M").next_to(dot_M, UL, buff=0.12).scale(0.5) 
        dot_label_group = VGroup(dot_A, dot_B, dot_C, dot_M, labA, labB, labC, labM)

        ## Length annotations (nice for horizontal/vertical legs)
        braceAB = BraceBetweenPoints(A, B, direction=DOWN, buff=0.025, color=GRAY).set_fill(opacity=0) 
        textAB = braceAB.get_tex(r"8 cm", buff=0).scale(0.5)
        braceBC = BraceBetweenPoints(B, C, direction=RIGHT, color=GRAY).set_fill(opacity=0) 
        textBC = braceBC.get_tex(r"6 cm", buff=0).scale(0.5)
        braceBM = BraceBetweenPoints(B, M, direction=RIGHT, buff=0.025, color=GRAY_B).set_fill(opacity=0) 
        textBM = braceBM.get_tex(r"3 cm", buff=0).scale(0.5).set_fill(opacity=0) 
        brace_group = VGroup(braceAB, braceBC, braceBM, textAB, textBC, textBM)

        ## ==== Define Angles
        right_angle = RightAngle(AB, BC, length=0.5, stroke_width=2, quadrant=(-1, 1))
        angle_BAC = Angle(AC, AB, radius=1, stroke_width=2, other_angle=True).set_opacity(0)  
        angle_BAM = Angle(AB, AM, radius=0.9, stroke_width=2).set_opacity(0) 
        angle_BAM_label = MathTex(r"20.5^\circ").next_to(dot_A, UR, buff=0.75).shift(DOWN*0.75).scale(0.5).set_opacity(0)
        angle_MAC = Angle(AM, AC, radius=1.1, stroke_width=2).set_opacity(0)  
        angle_MAC_label = MathTex(r"16^\circ").next_to(dot_A, UR, buff=0.85).shift(DOWN*0.4).scale(0.5).set_opacity(0) 
        
        ## ===== Figure Group
        figure = VGroup(triangle, dot_label_group, brace_group, right_angle, angle_BAC, 
                        angle_BAM, angle_MAC,angle_BAM_label, angle_MAC_label, AM)

        self.play(Write(sub_title_2))
        self.wait()
        self.play(FadeOut(sub_title_1, statement_1, eq_group_1, shift=UP),
                  sub_title_2.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                  FadeIn(figure))
        self.wait(2)
        
        # Solutions
        sub_title_3 = Tex(r"Solutions:", color=YELLOW).to_edge(DOWN)

        ## ====== Solution to question (a)
        question_1 = Tex(r"(a) Calculate $\angle BAM$.").move_to([-4, 2, 0]).scale(1)
        solution_group_1 = VGroup(
                Tex(r"Join $A$ to $M$. Using $\triangle ABM$,"),
                Tex(r"$BM = 3cm$ (midpoint of $BC$)"),
                Tex(r"Since $\tan \theta = \frac{Opposite}{Adjacent}$"),
                MathTex(r"\Rightarrow \tan BAM = \frac{BM}{AB}"),
                MathTex(r"\Rightarrow \tan BAM = \frac{3}{8} = 0.375"),
                MathTex(r"\Rightarrow \tan^{-1} 0.375 = 20.5^\circ"),
                MathTex(r"\therefore \angle BAM = 20.5^\circ")
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.8).to_edge(RIGHT).scale(0.6).shift(DOWN*0.5)
        question_1_group = VGroup(question_1, solution_group_1)

        question_2 = Tex(r"(b) Calculate $\angle MAC$.").move_to([-4, 2, 0]).scale(1)
        solution_group_2 = VGroup(
                Tex(r"Using $\triangle ABC$, we can find $\angle BAC$"),
                MathTex(r"\Rightarrow \tan \angle BAC = \frac{BC}{AB} = \frac{6}{8} = 0.75"),
                MathTex(r"\Rightarrow \tan^{-1} 0.75 = 36.5^\circ"),
                Tex(r"$\angle MAC$ is $\between \angle BAC$ and $\angle BAM$"),
                MathTex(r"\Rightarrow \angle CAM = \angle BAC - \angle BAM"),
                MathTex(r"\Rightarrow \angle CAM = 36.5^\circ - 20.5^\circ"),
                MathTex(r"\therefore \angle CAM = 16^\circ")
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.8).to_edge(RIGHT).scale(0.6).shift(DOWN*0.5)

        self.play(Write(sub_title_3))
        self.wait()
        self.play(FadeOut(sub_title_2, shift=UP),
                 sub_title_3.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                 figure.animate.to_edge(LEFT),
                 Write(question_1))
        self.wait()
        self.play(Write(solution_group_1[0]))
        self.wait()
        self.play(figure[-1].animate.set_opacity(1))
        self.wait()
        self.play(Write(solution_group_1[1]))
        self.wait()
        self.play(figure[2][2].animate.set_opacity(1), figure[2][-1].animate.set_fill(opacity=1))
        self.wait()
        self.play(Write(solution_group_1[2]))
        self.wait()
        self.play(Write(solution_group_1[3]))
        self.wait()
        self.play(TransformFromCopy(solution_group_1[3], solution_group_1[4]))
        self.wait()
        self.play(TransformFromCopy(solution_group_1[4], solution_group_1[5]))
        self.wait()
        self.play(TransformFromCopy(solution_group_1[5], solution_group_1[6]))
        self.wait(3)
        self.play(ShrinkToCenter(question_1_group))
        
        self.play(Write(question_2))
        self.wait()
        self.play(Write(solution_group_2[0]))
        self.wait()
        self.play(Write(solution_group_2[1]))
        self.wait()
        self.play(TransformFromCopy(solution_group_2[1], solution_group_2[2]))
        self.wait()
        self.play(Write(solution_group_2[3]))
        self.wait()
        self.play(Write(solution_group_2[4]))
        self.wait()
        self.play(TransformFromCopy(solution_group_2[4], solution_group_2[5]))
        self.wait()
        self.play(TransformFromCopy(solution_group_2[5], solution_group_2[6]))
        self.wait(3)
        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
                Write(final_text),
                  FadeOut(sub_title_2, figure, solution_group_2, question_2, shift=UP))        
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
            "Using Tangents", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "to Solve Triangles", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)

        # Quadratic Formula
        formula = MathTex(
            r"x = \frac{b - k^3}{k^3}", color=WHITE
        ).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        self.add(title, subtitle, formula)
