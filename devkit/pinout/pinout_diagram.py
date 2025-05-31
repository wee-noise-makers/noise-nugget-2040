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
graphic = diagram.add(Group(650, -400))

# Add and embed an image
hardware = graphic.add(Image("NN2040-devkit-top.png", embed=True, width=500))

# Measure and record key locations with the hardware Image instance
hardware.add_coord("pin_pitch_v", 0, 59)
hardware.add_coord("pin_pitch_h", 59, 0)

hardware.add_coord("pin1", 180, 580)
hardware.add_coord("pin51", 1670, 580)
hardware.add_coord("gpio16", 422, 1440)
hardware.add_coord("gpio4", 422 + 60 * 18, 1440)
hardware.add_coord("nc20", 422, 540)
hardware.add_coord("spklp", 422 + 60 * 18, 540)
hardware.add_coord("usb", 635 / 2, 40)
hardware.add_coord("boot", 125, 130)
hardware.add_coord("reset", 530, 130)
hardware.add_coord("legend", -2720, -1300)

# Create pinlabels on the right header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("pin51").x,
        y=hardware.coord("pin51").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(150, -145),
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
        x=hardware.coord("gpio16").x,
        y=hardware.coord("gpio16").y,
        scale=(-1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(0, 120),
        label_pitch=(0, 30),
        labels=data.lower_header_left,
        leaderline=lline.Curved(direction="vh"),
    )
)
graphic.add(
    PinLabelGroup(
        x=hardware.coord("gpio4").x,
        y=hardware.coord("gpio4").y,
        scale=(1, 1),
        pin_pitch=(-hardware.coord("pin_pitch_h", raw=True).x, 0),
        label_start=(0, 120),
        label_pitch=(0, 30),
        labels=data.lower_header_right[::-1],
        leaderline=lline.Curved(direction="vh"),
    )
)

# Create pinlabels on the upper header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("nc20").x,
        y=hardware.coord("nc20").y,
        scale=(-1, -1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(0, 170),
        label_pitch=(0, 30),
        labels=data.upper_header_left[::-1],
        leaderline=lline.Curved(direction="vh"),
    )
)
graphic.add(
    PinLabelGroup(
        x=hardware.coord("spklp").x,
        y=hardware.coord("spklp").y,
        scale=(1, -1),
        pin_pitch=(-hardware.coord("pin_pitch_h", raw=True).x, 0),
        label_start=(0, 170),
        label_pitch=(0, 30),
        labels=data.upper_header_right,
        leaderline=lline.Curved(direction="vh"),
    )
)

graphic.add(
    Legend(
        data.legend,
        x=hardware.coord("legend").x,
        y=hardware.coord("legend").y,
        max_height=200,
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
