# L-O-G-A-R-I-T-H-M-S

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

# 1.0 Introduction to Logarithms


class IntroductionLogarithm(VoiceoverScene):
    def construct(self):
        # Voiceover Instant
        self.set_speech_service(GTTSService(lang="en", transcription_model="base"))

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
        text = """
                Welcome to this lesson on logarithms.
                Logarithms may sound complicated at first, but they are simply another way of talking about exponents.
                By the end of this lesson, you will understand what logarithms mean, why we use them, and how to work with their rules.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(title))
            self.wait()
            self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B))
            self.wait()
            self.play(FadeIn(sub_title, shift=UP))
        self.wait(2)

        # Introduction
        sub_title_1 = Tex(r"Introduction.", color=YELLOW).to_edge(DOWN)
        eq_group_1 = (
            VGroup(
                MathTex(r"2^x = 8"),
                MathTex(r"2^", "x", "=", "2^", "3"),
                MathTex(r"x", "=", "3"),
            )
            .arrange(DOWN, buff=1)
            .scale(1)
        )
        eq_group_1[2][0].set_color(PURE_GREEN)
        eq_group_1[2][2].set_color(PURE_BLUE)
        text = """
                Let’s start with a basic example. Have you ever wondered how we can solve an equation of the form
                two raised to the power of x equals eight. If we ask ourselves, what power of two gives eight, 
                the answer is three, because two times two times two equals eight.
                So, in this case, x equals three. That is where logarithms come in. They help us undo exponents.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_1))
            self.wait()
            self.play(
                FadeOut(title, sub_title, shift=UP),
                sub_title_1.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_1[0]),
            )
            self.wait()
            self.play(TransformFromCopy(eq_group_1[0], eq_group_1[1]))
            self.wait()
            self.play(
                eq_group_1[1][1].animate.set_color(PURE_GREEN),
                eq_group_1[1][4].animate.set_color(PURE_BLUE),
            )
            self.wait()
            self.play(
                TransformFromCopy(eq_group_1[1][1], eq_group_1[2][0]),
                TransformFromCopy(eq_group_1[1][4], eq_group_1[2][2]),
                FadeIn(eq_group_1[2][1]),
            )
        self.wait(2)

        # Definition of Logarithms
        sub_title_2 = Tex(r"Definition of Logarithm.", color=YELLOW).to_edge(DOWN)
        eq_group_2 = (
            VGroup(
                Tex(r"A Logarithm is an inverse of an exponent."),
                MathTex(r"a^", "x", "=", "b"),
                MathTex(r"\log_", "a", "b", "=", "x"),
                MathTex(
                    r"a^x = b \qquad", r"\Longleftrightarrow", r"\qquad \log_a b = x"
                ),
                MathTex(r"2^3 = 8 \qquad \Longleftrightarrow \qquad \log_2 8 = 3"),
            )
            .arrange(DOWN, buff=0.75)
            .scale(1)
        )
        eq_group_2[2][1].set_color(PURE_GREEN)
        eq_group_2[2][4].set_color(PURE_RED)
        eq_group_2[2][2].set_color(PURE_BLUE)
        text = """
                A logarithm is defined as the inverse of an exponent.
                In other words, if a raised to the power of x equals b, then we can also say log base a of b equals x.

                Think of it like this:
                An exponent takes a base and tells us the result.
                A logarithm works backward — it takes the result and asks, what exponent on the base gives us this number?
                Logarithm asks the question 'What power must we raise a to inorder to get b?'
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_2))
            self.wait()
            self.play(
                FadeOut(sub_title_1, eq_group_1, shift=UP),
                sub_title_2.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_2[0]),
            )
            self.wait()
            self.play(Write(eq_group_2[1]))
            self.wait()
            self.play(
                eq_group_2[1][0].animate.set_color(PURE_GREEN),
                eq_group_2[1][1].animate.set_color(PURE_RED),
                eq_group_2[1][3].animate.set_color(PURE_BLUE),
            )
            self.play(
                TransformFromCopy(eq_group_2[1][0], eq_group_2[2][1]),
                TransformFromCopy(eq_group_2[1][1], eq_group_2[2][4]),
                TransformFromCopy(eq_group_2[1][3], eq_group_2[2][2]),
                FadeIn(eq_group_2[2][0], eq_group_2[2][3]),
            )
            self.wait()
            self.play(
                TransformFromCopy(eq_group_2[1], eq_group_2[3][0]),
                TransformFromCopy(eq_group_2[2], eq_group_2[3][2]),
                FadeIn(eq_group_2[3][1]),
            )
            self.wait()
            self.play(Write(eq_group_2[4]))
        self.wait(2)

        # Examples
        sub_title_3 = Tex(r"Examples:", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
            Tex(r"1. $log_2 8 = 3$"), MathTex(r"\Downarrow"), MathTex(r"2^3 = 8")
        ).arrange(DOWN, buff=1)
        eq_2 = VGroup(
            Tex(r"2. $log_{10} 1000 = 3$"),
            MathTex(r"\Downarrow"),
            MathTex(r"10^3 = 1000"),
        ).arrange(DOWN, buff=1)
        eq_3 = VGroup(
            Tex(r"3. $log_5 25 = 2$"), MathTex(r"\Downarrow"), MathTex(r"5^2 = 25")
        ).arrange(DOWN, buff=1)
        eq_group_3 = VGroup(eq_1, eq_2, eq_3).arrange(RIGHT, buff=1.5, aligned_edge=UP)
        text = """
                Here are some examples to make this clearer.

                Log base two of eight equals three, because two to the power of three is eight.
                Log base ten of one thousand equals three, because ten to the power of three is one thousand.
                Log base five of twenty-five equals two, because five squared is twenty-five.

                Notice that in every case, the logarithm is just answering the question: 
                ‘What power must I raise the base to, in order to get the number?
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_3))
            self.wait()
            self.play(
                FadeOut(sub_title_2, eq_group_2, shift=UP),
                sub_title_3.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_3[0][0]),
            )
            self.wait()
            self.play(TransformFromCopy(eq_group_3[0][0], eq_group_3[0][1:3]))
            self.wait(2)
            self.play(Write(eq_group_3[1][0]))
            self.wait()
            self.play(TransformFromCopy(eq_group_3[1][0], eq_group_3[1][1:3]))
            self.wait(2)
            self.play(Write(eq_group_3[2][0]))
            self.wait()
            self.play(TransformFromCopy(eq_group_3[2][0], eq_group_3[2][1:3]))
        self.wait(2)

        # Conditions of a Logarithm
        sub_title_4 = Tex(r"Conditions of Logarithm.", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
            Tex(
                r"1. The base $a$ must be positive and\\"
                r"not equal to 1 $(a > 0, a \neq 1)$"
            ),
            MathTex(r"\log_{\boxed{a}} b = x"),
            MathTex(r"\log_{", "2", "} 8", r"\qquad \text{Correct!}").set_color_by_tex(
                "2", PURE_GREEN
            ),
            MathTex(
                r"\log_{", "-2", "} 8", r"\qquad \text{Incorrect!}"
            ).set_color_by_tex("-2", PURE_RED),
            MathTex(
                r"\log_{", "1", "} 8", r"\qquad \text{Incorrect!}"
            ).set_color_by_tex("1", PURE_RED),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        eq_1[2][-1].set_color(PURE_GREEN)
        eq_1[3][-1].set_color(PURE_RED)
        eq_1[4][-1].set_color(PURE_RED)
        eq_2 = VGroup(
            Tex(r"2. The argument must be\\" r"positive $(b > 0)$"),
            MathTex(r"\log_a \boxed{b} = x"),
            MathTex(r"\log_2", "8", r"\qquad \text{Correct!}").set_color_by_tex(
                "8", PURE_GREEN
            ),
            MathTex(r"\log_2", "-8", r"\qquad \text{Incorrect!}").set_color_by_tex(
                "-8", PURE_RED
            ),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        eq_2[2][-1].set_color(PURE_GREEN)
        eq_2[3][-1].set_color(PURE_RED)
        eq_group_4 = (
            VGroup(eq_1, eq_2).arrange(RIGHT, buff=2, aligned_edge=UP).scale(0.75)
        )
        text = """
                Now, there are some important rules about when logarithms are valid.

                First, the base of a logarithm must always be positive, and it cannot be equal to one. Why?
                Because if the base is negative, powers don’t always make sense — for example, 
                what is negative two raised to the power of one-half?
                And if the base is one, then no matter what exponent you use, the result is always one, 
                so the logarithm would not be meaningful.

                Second, the argument — the number we take the log of — must also be positive.
                For example, log base two of eight is valid, but log base two of negative eight is not, 
                because no power of two will ever give a negative result.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_4))
            self.wait()
            self.play(
                FadeOut(sub_title_3, eq_group_3, shift=UP),
                sub_title_4.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_4[0][0]),
            )
            self.wait()
            self.play(Write(eq_group_4[0][1]))
            self.wait()
            self.play(Write(eq_group_4[0][2]))
            self.wait()
            self.play(Write(eq_group_4[0][3]))
            self.wait()
            self.play(Write(eq_group_4[0][4]))
            self.wait(2)
            self.play(Write(eq_group_4[1][0]))
            self.wait()
            self.play(Write(eq_group_4[1][1]))
            self.wait()
            self.play(Write(eq_group_4[1][2]))
            self.wait()
            self.play(Write(eq_group_4[1][3]))
        self.wait(2)

        # Common Types of Logarithms
        sub_title_5 = Tex(r"Common Types of Logarithms.", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
            Tex(r"1. Base $10$ Logarithms"),
            Tex(r"Written as $\log b$"),
            MathTex(r"\log_{10} 1000 = 3"),
            MathTex(r"\log 1000 = 3"),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)

        eq_2 = VGroup(
            Tex(r"2. Natural Logarithms (Base $e$)"),
            Tex(r"Written as $\ln$"),
            MathTex(r"\log_e 10 = 2.3"),
            Tex(r"where $e \approx 2.718$"),
            MathTex(r"\ln 10 = 2.3"),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        eq_group_5 = (
            VGroup(eq_1, eq_2).arrange(RIGHT, buff=2, aligned_edge=UP).scale(0.75)
        )
        text = """
                Two special logarithms are used so often that they have their own names.

                The first is the logarithm with base ten, called the common logarithm. 
                This is the one you often see on calculators, simply written as log.
                For example, log of one thousand means log base ten of one thousand, which equals three.

                The second is the logarithm with base e, where e is a special number approximately equal to two point seven one eight.
                This is called the natural logarithm, and it is written as ln. Natural logarithms are especially important in science,
                economics, and engineering, because they connect directly to continuous growth and decay.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_5))
            self.wait()
            self.play(
                FadeOut(sub_title_4, eq_group_4, shift=UP),
                sub_title_5.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_5[0][0]),
            )
            self.wait()
            self.play(Write(eq_group_5[0][1]))
            self.wait()
            self.play(Write(eq_group_5[0][2]))
            self.wait()
            self.play(Write(eq_group_5[0][3]))
            self.wait(2)
            self.play(Write(eq_group_5[1][0]))
            self.wait()
            self.play(Write(eq_group_5[1][1]))
            self.wait()
            self.play(Write(eq_group_5[1][2]))
            self.wait()
            self.play(Write(eq_group_5[1][3]))
            self.wait()
            self.play(Write(eq_group_5[1][4]))
        self.wait(2)

        # Laws of Logarithms
        sub_title_6 = Tex(r"Laws of Logarithms.", color=YELLOW).to_edge(DOWN)
        eq_group_6 = (
            VGroup(
                Tex(r"Logarithms follow special rules:"),
                Tex(r"1. $\log_a (MN) = \log_a M + \log_a N$"),
                Tex(r"2. $\log_a \left(\frac{M}{N}\right) = \log_a M - \log_a N$"),
                Tex(r"3. $\log_q (M^k) = k \log_a M$"),
            )
            .arrange(DOWN, buff=1, aligned_edge=LEFT)
            .scale(1)
        )
        text = """
                Logarithms follow some very useful rules, often called the laws of logarithms.

                The first law is the product rule: the log of a product is equal to the sum of the logs.
                This makes sense because multiplying inside the logarithm is the same as adding exponents.

                The second law is the quotient rule: the log of a quotient is equal to the difference of the logs.
                This comes from the fact that division of numbers corresponds to subtracting exponents.

                The third law is the power rule: the log of a number raised to a power is equal to that power 
                multiplied by the log of the base number.
                This is because exponents and logarithms are inverse operations.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_6))
            self.wait()
            self.play(
                FadeOut(sub_title_5, eq_group_5, shift=UP),
                sub_title_6.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_6[0]),
            )
            self.wait()
            self.play(Write(eq_group_6[1]))
            self.wait()
            self.play(Write(eq_group_6[2]))
            self.wait()
            self.play(Write(eq_group_6[3]))
        self.wait(2)

        # Use Cases
        sub_title_7 = Tex(r"Use Cases:", color=YELLOW).to_edge(DOWN)
        eq_1 = VGroup(
            Tex(r"1. $\log_a (MN) = \log_a M + \log_a N$"),
            MathTex(r"\log_{10} 8 + log_{10} 2"),
            MathTex(r"\Rightarrow \log_{10} (8 \times 2)"),
            MathTex(r"\Rightarrow \log_{10} 16"),
            MathTex(r"\Rightarrow \log 16"),
            MathTex(r"\Rightarrow \log (2^4)"),
            MathTex(r"\therefore \boxed{4 \log 2}"),
        ).arrange(DOWN, buff=0.75)
        eq_2 = VGroup(
            Tex(r"2. $\log_a \left(\frac{M}{N}\right) = \log_a M - \log_a N$"),
            MathTex(r"\log_{10} 40 - \log_{10} 5"),
            MathTex(r"\Rightarrow \log_{10} \left(\frac{40}{5}\right)"),
            MathTex(r"\Rightarrow \log_{10} 8"),
            MathTex(r"\Rightarrow \log 8"),
            MathTex(r"\Rightarrow \log (2^3)"),
            MathTex(r"\therefore \boxed{3 \log 2}"),
        ).arrange(DOWN, buff=0.75)
        eq_3 = VGroup(
            Tex(r"3. $\log_q (M^k) = k \log_a M$"),
            MathTex(r"\log_{10} (2^3)"),
            MathTex(r"\Rightarrow 3 \log_{10} 2"),
            MathTex(r"\therefore \boxed{3 \log 2}"),
        ).arrange(DOWN, buff=1.3)
        eq_group_7 = (
            VGroup(eq_1, eq_2, eq_3).arrange(RIGHT, buff=1, aligned_edge=UP).scale(0.5)
        )
        text = """
                Let’s see how these laws work in practice.

                Log base ten of eight plus log base ten of two equals log base ten of sixteen. 
                This shows the product rule, because eight times two equals sixteen.

                Log base ten of forty minus log base ten of five equals log base ten of eight. 
                This shows the quotient rule, because forty divided by five equals eight.

                Finally, log base ten of two cubed equals three times log base ten of two. This shows the power rule,
                because the exponent three comes down in front.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_7))
            self.wait()
            self.play(
                FadeOut(sub_title_6, eq_group_6, shift=UP),
                sub_title_7.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                Write(eq_group_7[0][0]),
            )
            self.wait()
            self.play(Write(eq_group_7[0][1]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[0][1], eq_group_7[0][2]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[0][2], eq_group_7[0][3]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[0][3], eq_group_7[0][4]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[0][4], eq_group_7[0][5]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[0][5], eq_group_7[0][6]))
            self.wait(2)
            self.play(Write(eq_group_7[1][0]))
            self.wait()
            self.play(Write(eq_group_7[1][1]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[1][1], eq_group_7[1][2]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[1][2], eq_group_7[1][3]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[1][3], eq_group_7[1][4]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[1][4], eq_group_7[1][5]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[1][5], eq_group_7[1][6]))
            self.wait(2)
            self.play(Write(eq_group_7[2][0]))
            self.wait()
            self.play(Write(eq_group_7[2][1]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[2][1], eq_group_7[2][2]))
            self.wait()
            self.play(TransformFromCopy(eq_group_7[2][2], eq_group_7[2][3]))
        self.wait(2)

        # Practice Questions
        sub_title_8 = Tex(r"Practice Questions.", color=YELLOW).to_edge(DOWN)
        eq_group_8 = VGroup(
            Tex(r"1. Evaluate $\log_3 81$"),
            Tex(r"2. Find $x$ if $10^x = 10000$"),
            Tex(r"3. Simplify $\log_2 16 + \log_2 4$"),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        text = """
                Now it’s your turn to try some practice problems.

                One: evaluate log base three of eighty-one. Remember, you are asking: three to what power equals eighty-one?

                Two: find x if ten to the power of x equals ten thousand. Here, you are just rewriting an exponential
                equation into logarithmic form.

                Three: simplify log base two of sixteen plus log base two of four, using the product rule.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_8))
            self.wait()
            self.play(
                FadeOut(sub_title_7, eq_group_7, shift=UP),
                sub_title_8.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                Write(eq_group_8[0]),
            )
            self.wait()
            self.play(Write(eq_group_8[1]))
            self.wait()
            self.play(Write(eq_group_8[2]))
        self.wait(2)

        # Summary
        sub_title_9 = Tex(r"Summary.", color=YELLOW).to_edge(DOWN)
        eq_group_9 = VGroup(
            Tex(r"$\bullet$ Logarithm is the inverse of an exponent."),
            Tex(
                r"$\bullet$ Definition: $a^x = b \quad \Longleftrightarrow \quad \log_a b = x$"
            ),
            Tex(r"$\bullet$ Rules: $a > 0$, $a \neq 1, b > 0$"),
            Tex(r"$\bullet$ Common logs: Base 10 logs and Natural logs (Base $e$)."),
        ).arrange(DOWN, buff=1, aligned_edge=LEFT)
        text = """
                Let’s summarize what we have learned.

                A logarithm is the inverse of an exponent.
                If a raised to the power of x equals b, then log base a of b equals x.

                The rules are:
                The base must be greater than zero, and not equal to one.
                The argument must be greater than zero.

                We also saw two special kinds of logarithms: the common logarithm with base ten, 
                and the natural logarithm with base e.

                Finally, we learned the three main laws of logarithms:
                The product rule, the quotient rule, and the power rule.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(sub_title_9))
            self.wait()
            self.play(
                FadeOut(sub_title_8, eq_group_8, shift=UP),
                sub_title_9.animate.to_edge(UP).scale(1.5).set_color(YELLOW_B),
                Write(eq_group_9[0]),
            )
            self.wait()
            self.play(Write(eq_group_9[1]))
            self.wait()
            self.play(Write(eq_group_9[2]))
            self.wait()
            self.play(Write(eq_group_9[3]))
        self.wait(2)
        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(sub_title_9, eq_group_9)
        text = """
                Congratulations! You now have a solid introduction to logarithms.
                As you continue, you will see logarithms appear in many areas, such as science, finance, and computer science.
                Thank you for watching, and see you in the next lesson.
               """
        with self.voiceover(text=text) as tracker:
            self.play(Write(final_text), ShrinkToCenter(final_solution_group))
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
            Text("Introduction", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )

        subtitle = (
            Text("to Logarithms", font="Roboto", weight=BOLD, color=WHITE)
            .scale(1.5)
            .next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(
                r"a^x = b \qquad \Longleftrightarrow \qquad \log_a b = x", color=WHITE
            )
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
