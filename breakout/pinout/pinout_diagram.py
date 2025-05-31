from pinout.core import Group, Image
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend
from pinout.components.annotation import AnnotationLabel

# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram(1600, 1100, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group(650, -600))

# Add and embed an image
hardware = graphic.add(Image("NN2040-breakout-top.png", embed=True, width=250))

# Measure and record key locations with the hardware Image instance
hardware.add_coord("pin1", -10, 625)
hardware.add_coord("pin51", 645, 625)
hardware.add_coord("swclk", 260, 2240)
hardware.add_coord("usb", 635 / 2, 40)
hardware.add_coord("boot", 125, 130)
hardware.add_coord("reset", 530, 130)
hardware.add_coord("legend", -1620, -150)
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, 62)
hardware.add_coord("pin_pitch_h", 62, 0)

# USB annotation
graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 60, "content": ["USB-C", "port"]},
        x=hardware.coord("usb").x,
        y=hardware.coord("usb").y,
        scale=(1, -1),
        body={"width": 125},
    )
)

# reset annotation
graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 60, "content": ["Boot", "button"]},
        x=hardware.coord("boot").x,
        y=hardware.coord("boot").y,
        scale=(-1, -1),
        body={"width": 125},
    )
)

# boot annotation
graphic.add(
    AnnotationLabel(
        content={"x": 165, "y": 60, "content": ["Reset", "button"]},
        x=hardware.coord("reset").x,
        y=hardware.coord("reset").y,
        scale=(1, -1),
        body={"x": 100, "width": 125},
    )
)

# Create pinlabels on the right header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("pin51").x,
        y=hardware.coord("pin51").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(70, -145),
        label_pitch=(0, 30),
        labels=data.right_header,
    )
)

# Create pinlabels on the left header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("pin1").x,
        y=hardware.coord("pin1").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(70, -145),
        label_pitch=(0, 30),
        scale=(-1, 1),
        labels=data.left_header,
    )
)

# Create pinlabels on the lower header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("swclk").x,
        y=hardware.coord("swclk").y,
        scale=(-1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(70, 30),
        label_pitch=(0, 30),
        labels=data.lower_header,
        leaderline=lline.Curved(direction="vh"),
    )
)

graphic.add(
    Legend(
        data.legend,
        x=hardware.coord("legend").x,
        y=hardware.coord("legend").y,
        max_height=132,
    )
)

# # Create a title and description text-blocks
# title_block = diagram.panel_02.add(
#     TextBlock(
#         data.title,
#         x=20,
#         y=30,
#         line_height=18,
#         tag="panel title_block",
#     )
# )
# diagram.panel_02.add(
#     TextBlock(
#         data.description,
#         x=20,
#         y=60,
#         width=title_block.width,
#         height=diagram.panel_02.height - title_block.height,
#         line_height=18,
#         tag="panel text_block",
#     )
# )

# # Create a legend
# legend = diagram.panel_02.add(
#     Legend(
#         data.legend,
#         x=1000,
#         y=8,
#         max_height=132,
#     )
# )
