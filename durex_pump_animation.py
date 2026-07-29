from manim import *

class BanburyTroubleshooting(Scene):
    def construct(self):
        # Title
        title = Text("Banbury Mixer: Process Oil Pumping Issues", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # Scene 1: Pipeline & Viscosity Problem
        pipe_box = Rectangle(width=6, height=1.5, color=BLUE).shift(UP * 1.5)
        oil_label = Text("Durex Oil (High Viscosity)", font_size=20).next_to(pipe_box, UP)
        
        warning_icon = Text("⚠️ FLOW STALL", font_size=24, color=RED).next_to(pipe_box, DOWN)

        self.play(Create(pipe_box), Write(oil_label))
        self.play(FadeIn(warning_icon))
        self.wait(1)

        # Scene 2: Solution - Trace Heating
        heater_label = Text("Fix: Apply Trace Heating / Line Heaters", font_size=22, color=GREEN)
        heater_label.to_edge(DOWN)
        
        heat_waves = VGroup(*[
            Arc(radius=0.3, start_angle=0, angle=PI, color=YELLOW).shift(RIGHT * i + DOWN * 0.2)
            for i in range(-2, 3)
        ])

        self.play(Transform(warning_icon, heater_label), Create(heat_waves))
        
        # Animate smooth flow
        oil_stream = Rectangle(width=5.8, height=1.3, color=YELLOW, fill_opacity=0.4).shift(UP * 1.5)
        self.play(Transform(pipe_box, oil_stream), run_time=1.5)
        self.wait(2)
