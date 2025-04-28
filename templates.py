# coding: utf8
from __future__ import unicode_literals


# setting explicit height and max-width: none on the SVG is required for
# Jupyter to render it properly in a cell

TPL_HTML = """
<!DOCTYPE html>
<html lang="ar">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {style1}
</head>
<body>
    <div class="container">
        {content}
        {style2}
    </div>
</body>
</html>
"""

TPL_SVGS = """
        <div class="svg-container">
         {svgs}
        </div>
"""




TPL_DEP_SVG = """
        <div class="svg-container">
            <!-- الـ viewBox تحدد منطقة العرض المرادة داخل الصورة SVG -->
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="l1{id}" 
                class="treebank" width="{width}" height="{height}" viewBox="{viewBox}"
                style="color: {color}; background: {bg}; font-family: {font}">
                    {svg}
            </svg>
        </div>
"""

TPL_DEP_AYAH = """
            <g class="displacy-word">
                <text class="displacy-token" fill="currentColor" font-family="hafs" text-anchor="middle" direction="rtl" y="{y}">
                    <tspan class="displacy-ayah" dy="1em" fill="{tcolor}" font-size="1.50em" x="{x}">{text}</tspan>
                    <tspan class="displacy-line" fill="{tcolor}" font-size="2em" dy=".25em" x="{x}">{tline}</tspan>
                    <tspan class="displacy-tag" dy="2em" fill="{tcolor}" font-size="1em" x="{x}">{tag}</tspan>
                    <tspan class="displacy-circle" dy=".21em" fill="{tcolor}" font-size="4em" x="{x}">.</tspan>
                </text>
            </g>
"""


TPL_DEP_WORDS = """
            <g class="displacy-word">
                <text class="displacy-token" fill="currentColor" font-family="hafs" text-anchor="middle" direction="rtl" y="{y}">
                    <tspan class="displacy-word" fill="{tcolor}" font-size="4em" x="{x}">.</tspan>
                    <tspan class="displacy-word" dy="1em" fill="{tcolor}" font-size="1.50em" x="{x}">{text}</tspan>
                    <tspan class="displacy-word" fill="{tcolor}" font-size="2em" dy=".25em" x="{x}">{tline}</tspan>
                    <tspan class="displacy-tag" dy="2em" fill="{tcolor}" font-size="1em" x="{x}">{tag}</tspan>
                </text>
            </g>
"""


TPL_DEP_ARCS = """
            <g class="displacy-arrow">
                <path class="displacy-arc" id="arrow-{id}-{i}" stroke-width="{stroke}px" d="{arc}" fill="none" stroke="{acolor}"/>
                <path class="displacy-arrowhead" d="{head}" fill="{acolor}"/>
                <text dy="1.25em" style="font-size: 1em"  fill="{acolor}" text-anchor="middle" x="{x_curve}" y="{y_curve}"> {label} </text>
            </g>

"""

TPL_CON_PATH = """
            <path class="displacy-const" d="{constituent}" stroke="#4472C4" stroke-width="0.6" stroke-miterlimit="8" stroke-dasharray="2.6 2" fill="none" fill-rule="evenodd" />

"""



