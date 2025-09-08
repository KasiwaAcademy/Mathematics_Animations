# L-O-G-A-R-I-T-H-M-S

from re import M
from manim import *
#from manim_voiceover import VoiceoverScene
#from manim_voiceover.services.gtts import GTTSService

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

# 1.0 Introduction to Logarithms

class IntroductionLogarithm(Scene):
    def construct(self):
        # Voiceover Instant
        #self.set_speech_service(GTTSService(lang='en', transcription_model="base"))

        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Introduction to Logarithms.", color=YELLOW)
        sub_title = Tex(r"Understanding the inverse of exponents.")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B))
        self.wait()
        self.play(FadeIn(sub_title, shift=UP))
        self.wait(2)
        
        # Introduction
        sub_title_1 = Tex(r"Introduction", color=YELLOW).to_edge(DOWN)
        eq_group_1 = VGroup(
                MathTex(r"2^x = 8"),
                MathTex(r"2^x = 2^3"), 
                MathTex(r"x = 3")
                ).arrange(DOWN, buff=1).scale(1)
        self.play(Write(sub_title_1))
        self.wait()
        self.play(FadeOut(title, sub_title),
                  sub_title_1.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_1))
        self.wait(2)

        # Definition of Logarithms
        sub_title_2 = Tex(r"Definition of Logarithm.", color=YELLOW).to_edge(DOWN)
        eq_group_2 = VGroup(
                Tex(r"A Logarithm is an inverse of an exponent"),
                MathTex(r"a^x = b"), 
                MathTex(r"\log_a b = x"),
                MathTex(r"a^x = b \qquad \Longleftrightarrow \qquad \log_a b"),
                MathTex(r"2^3 = 8 \qquad \Longleftrightarrow \qquad \log_2 8 = 3")
                ).arrange(DOWN, buff=0.75).scale(1)
        self.play(Write(sub_title_2))
        self.wait()
        self.play(FadeOut(sub_title_1, eq_group_1),
                  sub_title_2.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_2))
        self.wait(2)

        # Examples
        sub_title_3 = Tex(r"Examples:", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
                Tex(r"1. $log_2 8 = 3$"),
                MathTex(r"\Downarrow"),
                MathTex(r"2^3 = 8")
                ).arrange(DOWN, buff=1)
        eq_2 = VGroup(
                Tex(r"2. $log_{10} 1000 = 3$"),
                MathTex(r"\Downarrow"),
                MathTex(r"10^3 = 1000")
                ).arrange(DOWN, buff=1)
        eq_3 = VGroup(
                Tex(r"3. $log_5 25 = 2$"),
                MathTex(r"\Downarrow"),
                MathTex(r"5^2 = 25")
                ).arrange(DOWN, buff=1)
        eq_group_3 = VGroup(eq_1, eq_2, eq_3).arrange(RIGHT, buff=1.5, aligned_edge=UP)
        self.play(Write(sub_title_3))
        self.wait()
        self.play(FadeOut(sub_title_2, eq_group_2),
                  sub_title_3.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_3))
        self.wait(2) 

        # Conditions of a Logarithm
        sub_title_4 = Tex(r"Conditions of Logarithm.", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
                Tex(r"1. The base $a$ must be positive and\\"
                r"not equal to 1 $(a > 0, a \neq 1)$"),
                MathTex(r"\log_a b = x"),
                Tex(r"$\log_2 8$ \qquad Correct!"),
                Tex(r"$\log_{-2} 8$ \qquad Incorrect!")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)

        eq_2 = VGroup(
                Tex(r"2. The argument must be\\"
                r"positive $(b > 0)$"),
                MathTex(r"\log_a b = x"),
                Tex(r"$\log_2 8$ \qquad Correct!"),
                Tex(r"$\log_2 -8$ \qquad Incorrect!")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        eq_group_4 = VGroup(eq_1, eq_2).arrange(RIGHT, buff=2, aligned_edge=UP).scale(0.75)
        self.play(Write(sub_title_4))
        self.wait()
        self.play(FadeOut(sub_title_3, eq_group_3),
                  sub_title_4.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_4))
        self.wait(2)

        # Common Types of Logarithms
        sub_title_5 = Tex(r"Common Types of Logarithms.", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
                Tex(r"1. Base $10$ Logarithms"),
                Tex(r"Written as $\log b$"),
                MathTex(r"\log_{10} 1000 = 3"),
                MathTex(r"\log 1000 = 3")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)

        eq_2 = VGroup(
                Tex(r"2. Natural Logarithms (Base $e$)"),
                Tex(r"Written as $\ln$"),
                MathTex(r"\log_e 10 = 2.3"),
                Tex(r"where $e \approx 2.718$"),
                MathTex(r"\ln 10 = 2.3")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        eq_group_5 = VGroup(eq_1, eq_2).arrange(RIGHT, buff=2, aligned_edge=UP).scale(0.75)
        self.play(Write(sub_title_5))
        self.wait()
        self.play(FadeOut(sub_title_4, eq_group_4),
                  sub_title_5.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_5))
        self.wait(2)

        # Laws of Logarithms
        sub_title_6 = Tex(r"Laws of Logarithms.", color=YELLOW).to_edge(DOWN)
        eq_group_6 = VGroup(
                Tex(r"Logarithms follow special rules:"),
                Tex(r"1. $\log_a (MN) = \log_a M + \log_a N$"), 
                Tex(r"2. $\log_a \left(\frac{M}{N}\right) = \log_a M - \log_a N$"),
                Tex(r"3. $\log_q (M^k) = k \log_a M$")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT).scale(1)
        self.play(Write(sub_title_6))
        self.wait()
        self.play(FadeOut(sub_title_5, eq_group_5),
                  sub_title_6.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_6))
        self.wait(2)

        # Examples
        sub_title_7 = Tex(r"Examples:", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
                Tex(r"1. $\log_a (MN) = \log_a M + \log_a N$"), 
                MathTex(r"\log_{10} 8 + log_{10} 2"),
                MathTex(r"\Rightarrow \log_{10} (8 \times 2)"),
                MathTex(r"\Rightarrow \log_{10} 16"),
                MathTex(r"\Rightarrow \log 16"),
                MathTex(r"\Rightarrow \log (2^4)"),
                MathTex(r"\therefore \boxed{4 \log 2}")
                ).arrange(DOWN, buff=0.75)
        eq_2 = VGroup(
                Tex(r"2. $\log_a \left(\frac{M}{N}\right) = \log_a M - \log_a N$"),
                MathTex(r"\log_{10} 40 - \log_{10} 5"),
                MathTex(r"\Rightarrow \log_{10} \left(\frac{40}{5}\right)"),
                MathTex(r"\Rightarrow \log_{10} 8"),
                MathTex(r"\Rightarrow \log 8"),
                MathTex(r"\Rightarrow \log (2^3)"),
                MathTex(r"\therefore \boxed{3 \log 2}")
                ).arrange(DOWN, buff=0.75)
        eq_3 = VGroup(
                Tex(r"3. $\log_q (M^k) = k \log_a M$"),
                MathTex(r"\log_{10} (2^3)"),
                MathTex(r"\Rightarrow 3 \log_{10} 2"),
                MathTex(r"\therefore \boxed{3 \log 2}")
                ).arrange(DOWN, buff=1.3) 
        eq_group_7 = VGroup(eq_1, eq_2, eq_3).arrange(RIGHT, buff=1, aligned_edge=UP).scale(0.5)
        self.play(Write(sub_title_7))
        self.wait()
        self.play(FadeOut(sub_title_6, eq_group_6),
                  sub_title_7.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                  Write(eq_group_7))
        self.wait(2) 

        # Practice Questions
        sub_title_8 = Tex(r"Practice Questions.", color=YELLOW).to_edge(DOWN)
        eq_group_8 = VGroup(
                        Tex(r"1. Evaluate $\log_3 81$"),
                        Tex(r"2. Find $x$ if $10^x = 10000$"),
                        Tex(r"3. Simplify $\log_2 16 + \log_2 4$")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        self.play(Write(sub_title_8))
        self.wait()
        self.play(FadeOut(sub_title_7, eq_group_7),
                  sub_title_8.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                  Write(eq_group_8))
        self.wait(2) 

        # Summary
        sub_title_9 = Tex(r"Summary.", color=YELLOW).to_edge(DOWN)
        eq_group_9 = VGroup(
                        Tex(r"$\bullet$ Logarithm is the inverse of an exponent."),
                        Tex(r"$\bullet$ Definition: $a^x = b \quad \Longleftrightarrow \quad \log_a b = x$"),
                        Tex(r"$\bullet$ Rules: $a > 0$, $a \neq 1, b > 0$"),
                        Tex(r"$\bullet$ Common logs: Base 10 logs and Natural logs (Base $e$).")
                ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        self.play(Write(sub_title_9))
        self.wait()
        self.play(FadeOut(sub_title_8, eq_group_8),
                  sub_title_9.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                  Write(eq_group_9))
        self.wait(2) 
        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(sub_title_9, eq_group_9)
        self.play(
                Write(final_text),
                  ShrinkToCenter(final_solution_group))        
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
            "Introduction", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "to Logarithms", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)

        # Formula
        formula = MathTex(r"a^x = b \qquad \Longleftrightarrow \qquad \log_a b = x", color=WHITE).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        self.add(title, subtitle, formula)
