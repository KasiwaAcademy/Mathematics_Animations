from manim import *
from manim_voiceover import VoiceoverScene

# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class QuadraticEquation1(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        self.set_speech_service(
            RecorderService(transcription_model=None, use_pyaudio=False)
        )

        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Solving Simultaneous Equations Graphically.", color=YELLOW).shift(
            UP
        )
        self.wait()
        institution = Tex(r"@Kasiwa Academy")
        intro_group = VGroup(title, institution)
        self.play(Write(intro_group[0]))
        self.wait()
        self.play(FadeIn(intro_group[1], shift=UP))
        self.wait(2)

        # Voice_over code:
        text = "The circle is drawn as I speak"
        circle = Circle()
        self.play(intro_group.animate.to_edge(UP))
        self.wait()
        with self.voiceover(text=text) as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            self.wait(2)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(Write(final_text), FadeOut(intro_group, circle, shift=UP))
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
            Text("Change", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )

        subtitle = (
            Text("Subject of Formula", font="Roboto", weight=BOLD, color=WHITE)
            .scale(1.5)
            .next_to(title, DOWN, buff=0.3)
        )

        # Quadratic Formula
        formula = (
            MathTex(r"x = \frac{b - k^3}{k^3}", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
