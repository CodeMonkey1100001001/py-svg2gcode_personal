''' Configuration file for SVG to GCODE converter
    Date: 26 Oct 2016
    Author: Peter Scriven
'''


'''G-code emitted at the start of processing the SVG file'''
preamble = "G92 X0 Y0 Z0\nM280 P3 S123\nM282 P3\n"
# G28\nG1 Z0.0\nM05"

'''G-code emitted at the end of processing the SVG file'''
postamble = "M280 P3 S123\nG1 X0 Y0 F3000\nM18\n"

'''G-code emitted before processing a SVG shape'''
#shape_preamble = "G4 P0.2"
shape_preamble = "M280 P3 S20\nM282 P3\n"

'''G-code emitted after processing a SVG shape'''
shape_postamble = "M280 P3 S123\nM282 P3\n" #G4 P0.2\nM05"

feed_rate_rapid = 4000
feed_rate = 3000


# A4 area:               210mm x 297mm
# Printer Cutting Area: ~178mm x ~344mm
# Testing Area:          150mm x 150mm  (for now)
'''Print bed width in mm'''
bed_max_x = 200 
bed_min_x = -200

'''Print bed height in mm'''
bed_max_y = 200
bed_min_y = -200

''' Used to control the smoothness/sharpness of the curves.
    Smaller the value greater the sharpness. Make sure the
    value is greater than 0.1'''
smoothness = 0.1
