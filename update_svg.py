#!/usr/bin/env python3
"""
Update cabinet-layout-v10.svg:
1. Fix y-coordinates (base gap, wood panel thickness)
2. Add comprehensive dimension annotations
"""

FILE = '/Users/VN-287098/.qoderwork/workspace/mr6cc9n3665lissn/outputs/cabinet-layout-v10.svg'

with open(FILE, 'r') as f:
    lines = f.readlines()

new_lines = []

for i, line in enumerate(lines):
    orig = line

    # ---- BACKGROUND ----
    if 'height="920" fill="#fafafa"' in line:
        line = line.replace('height="920"', 'height="940"')

    # ---- BASE RECT ----
    elif 'y="576" width="476"' in line:
        line = line.replace('y="576"', 'y="590.4"').replace('height="16"', 'height="15.6"')

    # ---- TOP ZONE BG ----
    elif 'y="52" width="476" height="148"' in line:
        line = line.replace('y="52"', 'y="53.6"').replace('height="148"', 'height="146.4"')

    # ---- DOORS (3 lines) ----
    elif 'y="54"' in line and 'height="144"' in line and 'fill="#ffffff"' in line:
        line = line.replace('y="54"', 'y="55.6"').replace('height="144"', 'height="142.4"')

    # ---- GAS STRUTS (3 lines) ----
    elif 'gas strut' in line and 'y="70"' in line:
        line = line.replace('y="70"', 'y="71.6"')

    # ---- TOP ZONE TEXT 125 ----
    elif 'y="125"' in line and 'CHAN' in line:
        line = line.replace('y="125"', 'y="126.6"')

    # ---- TOP ZONE TEXT 140 ----
    elif 'y="140"' in line and '3 canh' in line:
        line = line.replace('y="140"', 'y="141.6"')

    # ---- DIVIDER TOP/MIDDLE ----
    elif 'y="200" width="480" height="4"' in line:
        line = line.replace('height="4"', 'height="3.6"')

    # ---- TROFAST ZONE ----
    elif 'y="204" width="88" height="370"' in line:
        line = line.replace('y="204"', 'y="203.6"').replace('height="370"', 'height="383.2"')

    # ---- DISPLAY ZONE ----
    elif 'y="204" width="296" height="228"' in line:
        line = line.replace('y="204"', 'y="203.6"').replace('height="228"', 'height="230"')

    # ---- DISPLAY BAY LABELS (2 lines with y=222) ----
    elif 'y="222"' in line and 'LEGO BAY' in line:
        line = line.replace('y="222"', 'y="221.6"')

    # ---- DISPLAY SHELF LABELS (2 lines with y=280) ----
    elif 'y="280"' in line and 'ke go' in line:
        line = line.replace('y="280"', 'y="279.6"')

    # ---- DISPLAY MO LABEL ----
    elif 'y="415"' in line and '150cm' in line:
        line = line.replace('y="415"', 'y="419"')

    # ---- DISPLAY V10 RECT ----
    elif 'y="420" width="244"' in line:
        line = line.replace('y="420"', 'y="421"')

    # ---- DISPLAY V10 TEXT ----
    elif 'y="429"' in line and 'THAY DOI' in line:
        line = line.replace('y="429"', 'y="430"')

    # ---- DISPLAY/VALI DIVIDER ----
    elif 'y="434" width="296" height="4"' in line:
        line = line.replace('y="434"', 'y="433.6"').replace('height="4"', 'height="3.6"')

    # ---- VALI ZONE ----
    elif 'y="438" width="296" height="136"' in line:
        line = line.replace('y="438"', 'y="437.2"').replace('height="136"', 'height="149.6"')

    # ---- VALI DOORS (4 lines) ----
    elif 'y="440"' in line and 'height="132" fill="#ffffff"' in line:
        line = line.replace('y="440"', 'y="439"').replace('height="132"', 'height="146"')

    # ---- VALI HINGE MARKS (3 lines) ----
    elif 'y1="442"' in line and 'y2="570"' in line:
        line = line.replace('y1="442"', 'y1="441"').replace('y2="570"', 'y2="585"')

    # ---- VALI HANDLES (4 lines) ----
    elif 'y="500"' in line and 'fill="#999"' in line:
        line = line.replace('y="500"', 'y="510"')

    # ---- VALI TEXT ----
    elif 'y="485"' in line and 'VALI' in line:
        line = line.replace('y="485"', 'y="508"')
    elif 'y="516"' in line and 'Bi-fold' in line:
        line = line.replace('y="516"', 'y="540"')
    elif 'y="532"' in line and 'vali cabin' in line:
        line = line.replace('y="532"', 'y="556"')
    elif 'y="548"' in line and 'hoac' in line:
        line = line.replace('y="548"', 'y="572"')

    # ---- VALI V10 RECT ----
    elif 'y="556" width="204"' in line:
        line = line.replace('y="556"', 'y="578"')

    # ---- VALI V10 TEXT ----
    elif 'y="565"' in line and 'THAY DOI' in line:
        line = line.replace('y="565"', 'y="587"')

    # ---- CLEANING ZONE ----
    elif 'y="204" width="84" height="370"' in line:
        line = line.replace('y="204"', 'y="203.6"').replace('height="370"', 'height="383.2"')

    # ---- CLEANING DOOR ----
    elif 'height="366"' in line and 'stroke="#bbb"' in line:
        line = line.replace('height="366"', 'height="379.6"')

    # ---- CLEANING LABELS ----
    elif 'y="480"' in line and 'CLEANING' in line:
        line = line.replace('y="480"', 'y="500"')
    elif 'y="493"' in line and 'DYSON' in line:
        line = line.replace('y="493"', 'y="513"')
    elif 'y="508"' in line and 'Vach' in line:
        line = line.replace('y="508"', 'y="528"')
    elif 'y="520"' in line and 'Lung' in line:
        line = line.replace('y="520"', 'y="540"')
    elif 'y="532"' in line and 'Canh' in line:
        line = line.replace('y="532"', 'y="552"')
    elif 'y="546"' in line and 'cheo' in line:
        line = line.replace('y="546"', 'y="566"')

    # ---- RIGHT DIM TICKS ----
    elif 'y1="434" x2="560" y2="434"' in line:
        line = line.replace('y1="434"', 'y1="433.6"').replace('y2="434"', 'y2="437.2"')
    elif 'y1="574" x2="560" y2="574"' in line:
        line = line.replace('y1="574"', 'y1="586.8"').replace('y2="574"', 'y2="590.4"')
    elif 'y1="592" x2="560" y2="592"' in line:
        line = line.replace('y1="592"', 'y1="590.4"').replace('y2="592"', 'y2="606.4"')

    # ---- TOTAL HEIGHT TICK ----
    elif 'y1="610" x2="605" y2="610"' in line:
        line = line.replace('y1="610"', 'y1="606.4"').replace('y2="610"', 'y2="606.4"')

    # ---- RIGHT DIM LINE y2 ----
    elif 'y1="50" y2="610" stroke="#333"' in line:
        line = line.replace('y2="610"', 'y2="606.4"')

    # ---- VERTICAL DIVIDERS ----
    elif 'height="378" fill="#8B7355"' in line:
        line = line.replace('height="378"', 'height="390.4"')

    # ---- RIGHT DIM TEXT ----
    elif 'y="130"' in line and '75cm' in line:
        line = line.replace('y="130"', 'y="131.8"')
    elif 'y="322"' in line and '115cm' in line:
        line = line.replace('y="322"', 'y="397"').replace('115cm', '195cm')
    elif 'y="508"' in line and 'text-anchor="start"' in line and 'font-size="8"' in line:
        line = line.replace('y="508"', 'y="510"').replace('68cm', '74.8cm')
    elif 'y="585"' in line and '8cm' in line:
        line = line.replace('y="585"', 'y="598"')

    # ---- TOTAL TEXT ----
    elif 'y="335"' in line and '280cm' in line:
        line = line.replace('y="335"', 'y="332"')

    # ---- COLUMN WIDTHS ----
    elif 'y="630"' in line:
        line = line.replace('y="630"', 'y="650"')
    elif 'y1="625"' in line:
        line = line.replace('y1="625"', 'y1="645"')
    elif 'y2="635"' in line:
        line = line.replace('y2="635"', 'y2="655"')
    elif 'y="645"' in line and '240cm' in line:
        line = line.replace('y="645"', 'y="665"')
    elif 'y="657"' in line:
        line = line.replace('y="657"', 'y="677"')
    elif 'y1="653"' in line:
        line = line.replace('y1="653"', 'y1="673"')
    elif 'y2="661"' in line:
        line = line.replace('y2="661"', 'y2="681"')
    elif 'y="672"' in line:
        line = line.replace('y="672"', 'y="692"')
    elif 'y="685"' in line:
        line = line.replace('y="685"', 'y="705"')
    elif 'y="698"' in line:
        line = line.replace('y="698"', 'y="718"')

    # ---- LEFT PEGBOARD UPPER ----
    elif 'y="240" width="50" height="70"' in line:
        line = line.replace('y="240"', 'y="260"')
    elif 'cy="255"' in line:
        line = line.replace('cy="255"', 'cy="PEG_A1"')
    elif 'cy="275"' in line:
        line = line.replace('cy="275"', 'cy="PEG_A2"')
    elif 'cy="295"' in line:
        line = line.replace('cy="295"', 'cy="PEG_A3"')
    elif 'y="260" width="16"' in line:
        line = line.replace('y="260"', 'y="280"')
    elif 'cy="290"' in line:
        line = line.replace('cy="290"', 'cy="310"')

    # ---- LEFT PEGBOARD LOWER ----
    elif 'y="420" width="50" height="70"' in line:
        line = line.replace('y="420"', 'y="440"')
    elif 'cy="435"' in line:
        line = line.replace('cy="435"', 'cy="PEG_B1"')
    elif 'cy="455"' in line:
        line = line.replace('cy="455"', 'cy="PEG_B2"')
    elif 'cy="475"' in line:
        line = line.replace('cy="475"', 'cy="PEG_B3"')
    elif 'y="440" width="20"' in line:
        line = line.replace('y="440"', 'y="460"')
    elif 'y="460" width="10"' in line:
        line = line.replace('y="460"', 'y="480"')
    elif 'y="230"' in line and 'CANH' in line:
        line = line.replace('y="230"', 'y="250"')
    elif 'y="340"' in line and 'pegboard' in line:
        line = line.replace('y="340"', 'y="360"')
    elif 'y="350"' in line and '35x35' in line:
        line = line.replace('y="350"', 'y="370"')

    # ---- PLAN VIEW ----
    elif 'y="730"' in line:
        line = line.replace('y="730"', 'y="750"')
    elif 'y="744"' in line:
        line = line.replace('y="744"', 'y="764"')
    elif 'y="880" width="490"' in line:
        line = line.replace('y="880"', 'y="900"')
    elif 'y="898"' in line:
        line = line.replace('y="898"', 'y="918"')
    elif 'y="800" width="390"' in line:
        line = line.replace('y="800"', 'y="820"')
    elif '450,800 540,760 540,880 450,880' in line:
        line = line.replace('450,800', '450,820').replace('540,760', '540,780').replace('540,880', '540,900').replace('450,880', '450,900')
    elif 'y1="800" x2="540" y2="760"' in line:
        line = line.replace('y1="800"', 'y1="820"').replace('y2="760"', 'y2="780"')
    elif 'y="775"' in line:
        line = line.replace('y="775"', 'y="795"')
    elif 'y1="800" x2="150" y2="880"' in line:
        line = line.replace('y1="800"', 'y1="820"').replace('y2="880"', 'y2="900"')
    elif 'y1="800" x2="450" y2="880"' in line:
        line = line.replace('y1="800"', 'y1="820"').replace('y2="880"', 'y2="900"')
    elif 'y1="802" x2="536" y2="876"' in line:
        line = line.replace('y1="802"', 'y1="822"').replace('y2="876"', 'y2="896"')
    elif 'y="840"' in line and 'PEGBOARD' in line:
        line = line.replace('y="840"', 'y="860"')
    elif 'y1="876" x2="530" y2="876"' in line:
        line = line.replace('y1="876"', 'y1="896"').replace('y2="876"', 'y2="896"')
    elif 'y="870"' in line:
        line = line.replace('y="870"', 'y="890"')
    elif 'cy="820"' in line:
        line = line.replace('cy="820"', 'cy="840"')
    elif 'y="815"' in line:
        line = line.replace('y="815"', 'y="835"')
    elif 'y="835"' in line:
        line = line.replace('y="835"', 'y="855"')
    elif 'y="850"' in line:
        line = line.replace('y="850"', 'y="870"')
    elif 'y="825" text-anchor="middle" font-size="5"' in line:
        line = line.replace('y="825"', 'y="845"')
    elif 'y1="800" x2="40" y2="880"' in line:
        line = line.replace('y1="800"', 'y1="820"').replace('y2="880"', 'y2="900"')
    elif 'y1="800" x2="45" y2="800"' in line:
        line = line.replace('y1="800"', 'y1="820"').replace('y2="800"', 'y2="820"')
    elif 'y1="880" x2="45" y2="880"' in line:
        line = line.replace('y1="880"', 'y1="900"').replace('y2="880"', 'y2="900"')
    elif 'y="843"' in line:
        line = line.replace('y="843"', 'y="863"')
    elif 'y1="760" x2="555" y2="880"' in line:
        line = line.replace('y1="760"', 'y1="780"').replace('y2="880"', 'y2="900"')
    elif 'y1="760" x2="560" y2="760"' in line:
        line = line.replace('y1="760"', 'y1="780"').replace('y2="760"', 'y2="780"')
    elif 'y1="880" x2="560" y2="880"' in line:
        line = line.replace('y1="880"', 'y1="900"').replace('y2="880"', 'y2="900"')
    elif 'y="825" text-anchor="middle" font-size="8"' in line:
        line = line.replace('y="825"', 'y="845"')
    elif 'y="905"' in line:
        line = line.replace('y="905"', 'y="925"')
    elif 'y1="901"' in line:
        line = line.replace('y1="901"', 'y1="921"')
    elif 'y2="909"' in line:
        line = line.replace('y2="909"', 'y2="929"')
    elif 'y="917"' in line:
        line = line.replace('y="917"', 'y="937"')
    elif 'y="862"' in line:
        line = line.replace('y="862"', 'y="882"')
    elif 'y="760" width="10"' in line:
        line = line.replace('y="760"', 'y="780"')
    elif 'y="767"' in line:
        line = line.replace('y="767"', 'y="787"')
    elif 'y1="764"' in line:
        line = line.replace('y1="764"', 'y1="784"').replace('y2="764"', 'y2="784"')

    # ---- TROFAST LABELS ----
    elif 'y="385"' in line and '6 nho' in line:
        line = line.replace('y="385"', 'y="400"')
    elif 'y="562"' in line and '3 lon' in line:
        line = line.replace('y="562"', 'y="572"')
    elif 'y="572"' in line and 'TROFAST' in line:
        line = line.replace('y="572"', 'y="582"')

    new_lines.append(line)

    # ========== INSERT DIMENSION ANNOTATIONS ==========

    # After TOP zone last gas strut, insert door dimensions
    if 'gas strut' in line and 'x="458"' in line:
        new_lines.append('  <!-- TOP ZONE DOOR DIMENSIONS -->\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="64" y1="46" x2="64" y2="52"/><line x1="220" y1="46" x2="220" y2="52"/>\n')
        new_lines.append('    <line x1="64" y1="48" x2="220" y2="48"/>\n')
        new_lines.append('    <line x1="222" y1="46" x2="222" y2="52"/><line x1="378" y1="46" x2="378" y2="52"/>\n')
        new_lines.append('    <line x1="222" y1="48" x2="378" y2="48"/>\n')
        new_lines.append('    <line x1="380" y1="46" x2="380" y2="52"/><line x1="536" y1="46" x2="536" y2="52"/>\n')
        new_lines.append('    <line x1="380" y1="48" x2="536" y2="48"/>\n')
        new_lines.append('    <line x1="540" y1="55.6" x2="544" y2="55.6"/><line x1="540" y1="198" x2="544" y2="198"/>\n')
        new_lines.append('    <line x1="542" y1="55.6" x2="542" y2="198"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="142" y="44" text-anchor="middle" font-size="6" fill="#555">78.8cm</text>\n')
        new_lines.append('  <text x="300" y="44" text-anchor="middle" font-size="6" fill="#555">78.8cm</text>\n')
        new_lines.append('  <text x="458" y="44" text-anchor="middle" font-size="6" fill="#555">78.8cm</text>\n')
        new_lines.append('  <text x="546" y="130" text-anchor="start" font-size="6" fill="#555">73.2cm</text>\n')
        new_lines.append('  <text x="62" y="44" text-anchor="start" font-size="5" fill="#999">Top frame 1.8cm</text>\n')

    # After trofast labels, insert left-side dimensions + internal width
    if 'TROFAST 45cm' in line:
        new_lines.append('  <!-- TROFAST LEFT-SIDE DIMS -->\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="56" y1="203.6" x2="56" y2="586.8"/>\n')
        new_lines.append('    <line x1="52" y1="203.6" x2="60" y2="203.6"/><line x1="52" y1="210" x2="60" y2="210"/>\n')
        new_lines.append('    <line x1="52" y1="240" x2="60" y2="240"/><line x1="52" y1="270" x2="60" y2="270"/>\n')
        new_lines.append('    <line x1="52" y1="300" x2="60" y2="300"/>\n')
        new_lines.append('    <line x1="48" y1="330" x2="56" y2="330"/><line x1="48" y1="360" x2="56" y2="360"/>\n')
        new_lines.append('    <line x1="50" y1="330" x2="50" y2="360"/>\n')
        new_lines.append('    <line x1="48" y1="390" x2="56" y2="390"/><line x1="48" y1="436" x2="56" y2="436"/>\n')
        new_lines.append('    <line x1="50" y1="390" x2="50" y2="436"/>\n')
        new_lines.append('    <line x1="48" y1="450" x2="56" y2="450"/><line x1="48" y1="496" x2="56" y2="496"/>\n')
        new_lines.append('    <line x1="50" y1="450" x2="50" y2="496"/>\n')
        new_lines.append('    <line x1="48" y1="510" x2="56" y2="510"/><line x1="48" y1="556" x2="56" y2="556"/>\n')
        new_lines.append('    <line x1="50" y1="510" x2="50" y2="556"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="54" y="208" text-anchor="end" font-size="5" fill="#555">3cm</text>\n')
        new_lines.append('  <text x="54" y="228" text-anchor="end" font-size="5" fill="#555">15cm</text>\n')
        new_lines.append('  <text x="54" y="258" text-anchor="end" font-size="5" fill="#555">15cm</text>\n')
        new_lines.append('  <text x="54" y="288" text-anchor="end" font-size="5" fill="#555">15cm</text>\n')
        new_lines.append('  <text x="46" y="348" text-anchor="end" font-size="5" fill="#c62828">10cm</text>\n')
        new_lines.append('  <text x="46" y="416" text-anchor="end" font-size="5" fill="#c62828">23cm</text>\n')
        new_lines.append('  <text x="46" y="476" text-anchor="end" font-size="5" fill="#c62828">23cm</text>\n')
        new_lines.append('  <text x="46" y="536" text-anchor="end" font-size="5" fill="#c62828">23cm</text>\n')
        new_lines.append('  <text x="106" y="216" text-anchor="middle" font-size="5" fill="#555" font-style="italic">Trong: 43.2cm</text>\n')

    # After Display/Vali divider, insert right-side dims + bay widths + internal width
    if 'y="433.6" width="296" height="3.6" fill="#8B7355"' in line:
        new_lines.append('  <!-- DISPLAY RIGHT-SIDE DIMS -->\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="442" y1="203.6" x2="442" y2="433.6"/>\n')
        new_lines.append('    <line x1="438" y1="203.6" x2="446" y2="203.6"/><line x1="438" y1="246" x2="446" y2="246"/>\n')
        new_lines.append('    <line x1="438" y1="250" x2="446" y2="250"/><line x1="438" y1="292" x2="446" y2="292"/>\n')
        new_lines.append('    <line x1="438" y1="296" x2="446" y2="296"/><line x1="438" y1="338" x2="446" y2="338"/>\n')
        new_lines.append('    <line x1="438" y1="342" x2="446" y2="342"/><line x1="438" y1="384" x2="446" y2="384"/>\n')
        new_lines.append('    <line x1="438" y1="388" x2="446" y2="388"/><line x1="438" y1="433.6" x2="446" y2="433.6"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="436" y="228" text-anchor="end" font-size="5" fill="#555">20.8cm</text>\n')
        new_lines.append('  <text x="436" y="249" text-anchor="end" font-size="5" fill="#c62828">1.8cm</text>\n')
        new_lines.append('  <text x="436" y="274" text-anchor="end" font-size="5" fill="#555">20.8cm</text>\n')
        new_lines.append('  <text x="436" y="295" text-anchor="end" font-size="5" fill="#c62828">1.8cm</text>\n')
        new_lines.append('  <text x="436" y="320" text-anchor="end" font-size="5" fill="#555">20.8cm</text>\n')
        new_lines.append('  <text x="436" y="341" text-anchor="end" font-size="5" fill="#c62828">1.8cm</text>\n')
        new_lines.append('  <text x="436" y="366" text-anchor="end" font-size="5" fill="#555">20.8cm</text>\n')
        new_lines.append('  <text x="436" y="387" text-anchor="end" font-size="5" fill="#c62828">1.8cm</text>\n')
        new_lines.append('  <text x="436" y="414" text-anchor="end" font-size="5" fill="#555">20.8cm</text>\n')
        new_lines.append('  <!-- DISPLAY BAY WIDTHS -->\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="154" y1="199" x2="154" y2="202"/><line x1="300" y1="199" x2="300" y2="202"/>\n')
        new_lines.append('    <line x1="154" y1="200.5" x2="300" y2="200.5"/>\n')
        new_lines.append('    <line x1="304" y1="199" x2="304" y2="202"/><line x1="450" y1="199" x2="450" y2="202"/>\n')
        new_lines.append('    <line x1="304" y1="200.5" x2="450" y2="200.5"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="227" y="197" text-anchor="middle" font-size="5" fill="#555">72.3cm</text>\n')
        new_lines.append('  <text x="377" y="197" text-anchor="middle" font-size="5" fill="#555">72.3cm</text>\n')
        new_lines.append('  <text x="302" y="197" text-anchor="middle" font-size="4" fill="#999">1.8</text>\n')
        new_lines.append('  <text x="302" y="234" text-anchor="middle" font-size="5" fill="#555" font-style="italic">Trong: 146.4cm</text>\n')

    # After VALI v10 text, insert vali dims
    if 'y="587"' in line and 'THAY DOI v10: 4 canh' in line:
        new_lines.append('  <!-- VALI DIMENSIONS -->\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="148" y1="437.2" x2="148" y2="586.8"/>\n')
        new_lines.append('    <line x1="144" y1="437.2" x2="152" y2="437.2"/><line x1="144" y1="586.8" x2="152" y2="586.8"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="142" y="515" text-anchor="end" font-size="6" fill="#555">74.8cm</text>\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="156" y1="590" x2="156" y2="594"/><line x1="229" y1="590" x2="229" y2="594"/>\n')
        new_lines.append('    <line x1="156" y1="592" x2="229" y2="592"/>\n')
        new_lines.append('    <line x1="231" y1="590" x2="231" y2="594"/><line x1="304" y1="590" x2="304" y2="594"/>\n')
        new_lines.append('    <line x1="231" y1="592" x2="304" y2="592"/>\n')
        new_lines.append('    <line x1="306" y1="590" x2="306" y2="594"/><line x1="379" y1="590" x2="379" y2="594"/>\n')
        new_lines.append('    <line x1="306" y1="592" x2="379" y2="592"/>\n')
        new_lines.append('    <line x1="381" y1="590" x2="381" y2="594"/><line x1="448" y1="590" x2="448" y2="594"/>\n')
        new_lines.append('    <line x1="381" y1="592" x2="448" y2="592"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="192" y="602" text-anchor="middle" font-size="5" fill="#555">~37cm</text>\n')
        new_lines.append('  <text x="268" y="602" text-anchor="middle" font-size="5" fill="#555">~37cm</text>\n')
        new_lines.append('  <text x="342" y="602" text-anchor="middle" font-size="5" fill="#555">~37cm</text>\n')
        new_lines.append('  <text x="414" y="602" text-anchor="middle" font-size="5" fill="#555">~37cm</text>\n')
        new_lines.append('  <text x="302" y="612" text-anchor="middle" font-size="5" fill="#c62828">4x ~37cm = 148cm (150cm voi khe ho)</text>\n')

    # After Cleaning last label (cheo), insert cleaning dims
    if 'cheo' in line and 'y="566"' in line:
        new_lines.append('  <!-- CLEANING DIMENSIONS -->\n')
        new_lines.append('  <text x="496" y="216" text-anchor="middle" font-size="5" fill="#555" font-style="italic">Trong: 43.2cm</text>\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="545" y1="208" x2="549" y2="208"/><line x1="545" y1="368" x2="549" y2="368"/>\n')
        new_lines.append('    <line x1="547" y1="208" x2="547" y2="368"/>\n')
        new_lines.append('    <line x1="545" y1="378" x2="549" y2="378"/>\n')
        new_lines.append('    <line x1="547" y1="368" x2="547" y2="378"/>\n')
        new_lines.append('    <line x1="545" y1="498" x2="549" y2="498"/>\n')
        new_lines.append('    <line x1="547" y1="378" x2="547" y2="498"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="551" y="291" text-anchor="start" font-size="5" fill="#555">80cm</text>\n')
        new_lines.append('  <text x="551" y="375" text-anchor="start" font-size="5" fill="#555">5cm</text>\n')
        new_lines.append('  <text x="551" y="441" text-anchor="start" font-size="5" fill="#555">60cm</text>\n')
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="456" y1="250" x2="456" y2="430"/>\n')
        new_lines.append('    <line x1="453" y1="250" x2="459" y2="250"/>\n')
        new_lines.append('    <line x1="453" y1="340" x2="459" y2="340"/>\n')
        new_lines.append('    <line x1="453" y1="430" x2="459" y2="430"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="454" y="298" text-anchor="end" font-size="5" fill="#555">45cm</text>\n')
        new_lines.append('  <text x="454" y="388" text-anchor="end" font-size="5" fill="#555">45cm</text>\n')
        new_lines.append('  <text x="492" y="245" text-anchor="middle" font-size="4" fill="#777">34cm</text>\n')

    # ---- BASE TEXT (adjust position for moved base) ----
    elif 'DE 8cm' in line and 'y="587"' in line:
        line = line.replace('y="587"', 'y="600"')
        new_lines.append(line)
        # Insert base dim + divider annotations after this line
        new_lines.append('  <g stroke="#555" stroke-width="0.5" fill="none">\n')
        new_lines.append('    <line x1="630" y1="590.4" x2="630" y2="606.4"/>\n')
        new_lines.append('    <line x1="626" y1="590.4" x2="634" y2="590.4"/><line x1="626" y1="606.4" x2="634" y2="606.4"/>\n')
        new_lines.append('  </g>\n')
        new_lines.append('  <text x="636" y="600" text-anchor="start" font-size="6" fill="#555">8cm</text>\n')
        new_lines.append('  <!-- DIVIDER THICKNESS -->\n')
        new_lines.append('  <text x="58" y="203" text-anchor="end" font-size="4" fill="#999">1.8cm</text>\n')
        new_lines.append('  <text x="58" y="436" text-anchor="end" font-size="4" fill="#999">1.8cm</text>\n')
        new_lines.append('  <text x="58" y="590" text-anchor="end" font-size="4" fill="#999">1.8cm</text>\n')
        new_lines.append('  <text x="152" y="596" text-anchor="middle" font-size="4" fill="#999">1.8cm</text>\n')
        new_lines.append('  <text x="452" y="596" text-anchor="middle" font-size="4" fill="#999">1.8cm</text>\n')
        new_lines.append('  <text x="300" y="598" text-anchor="middle" font-size="4" fill="#999">Bottom frame 1.8cm</text>\n')
        continue

    # After legend last item (LED strip), add dim legend
    if 'LED strip' in line:
        new_lines.append('  <line x1="430" y1="784" x2="450" y2="784" stroke="#555" stroke-width="0.5"/>\n')
        new_lines.append('  <text x="455" y="787" font-size="6" fill="#333">Kich thuoc</text>\n')
        new_lines.append('  <line x1="495" y1="784" x2="515" y2="784" stroke="#c62828" stroke-width="0.8"/>\n')
        new_lines.append('  <text x="520" y="787" font-size="6" fill="#c62828">Kich thuoc quan trong</text>\n')

# Post-process: replace pegboard placeholders with actual values
final_lines = []
for line in new_lines:
    line = line.replace('cy="PEG_A1"', 'cy="275"')
    line = line.replace('cy="PEG_A2"', 'cy="295"')
    line = line.replace('cy="PEG_A3"', 'cy="315"')
    line = line.replace('cy="PEG_B1"', 'cy="455"')
    line = line.replace('cy="PEG_B2"', 'cy="475"')
    line = line.replace('cy="PEG_B3"', 'cy="495"')
    final_lines.append(line)

# Write result
with open(FILE, 'w') as f:
    f.writelines(final_lines)

print(f"Done! {len(lines)} original lines -> {len(new_lines)} lines")
