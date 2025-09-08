# L-O-G-A-R-I-T-H-M-S

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
        self.wait(5)

        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(title, sub_title)
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
            "Using Tangents", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "to Solve Triangles", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)

        # Formula
        # formula = MathTex(r"x = \frac{b - k^3}{k^3}", color=WHITE).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        figure = make_figure()
        figure = figure.shift(DOWN).scale(0.85)
        line_AM = figure[-1].set_opacity(1) 
        angle_BAM = figure[3][2].set_opacity(1)
        angle_MAC = figure[3][4].set_opacity(1)
        self.add(title, subtitle, figure, line_AM, angle_BAM, angle_MAC)
