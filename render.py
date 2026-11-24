"""Render the 1024x1024 broadsheet for Tuesday 24 November 2026.

Deterministic: fixed fonts, fixed geometry, no clocks, no randomness —
two runs write the same bytes.
"""
from PIL import Image, ImageDraw, ImageFont

import data

W = H = 1024
CREAM = (247, 241, 227)
PAPER = (252, 248, 238)
INK = (26, 23, 16)
RED = (179, 35, 27)
BLUE = (30, 64, 120)
GREY = (96, 90, 78)
RULE = (26, 23, 16)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, font_path, size, width, min_size=9):
    while size > min_size:
        f = F(font_path, size)
        if draw.textlength(text, font=f) <= width:
            return f
        size -= 1
    return F(font_path, min_size)


def block(draw, x, y, text, font, width, leading, fill=INK, max_lines=None):
    lines = wrap(draw, text, font, width)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def masthead(d):
    d.line([24, 14, W - 24, 14], fill=RULE, width=3)
    f = fit(d, data.TITLE, SERIF, 64, W - 48)
    tw = d.textlength(data.TITLE, font=f)
    d.text(((W - tw) / 2, 20), data.TITLE, font=f, fill=INK)
    sub = f"{data.DAY}  \u00b7  {data.SUBTITLE}"
    f2 = fit(d, sub, SANS_B, 21, W - 48)
    tw = d.textlength(sub, font=f2)
    d.text(((W - tw) / 2, 88), sub, font=f2, fill=RED)
    d.line([24, 116, W - 24, 116], fill=RULE, width=3)


def ticker(d):
    d.polygon([(0, 128), (W, 118), (W, 152), (0, 162)], fill=RED)
    f = fit(d, data.TICKER, SANS_B, 15, W - 30)
    # follow the band's slant: it falls 10px across the width
    d.text((14, 130), data.TICKER, font=f, fill=(255, 250, 240))


def stat_band(d, y=168):
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    col_w = (W - 48) // 6
    for i, (fig, label, dt) in enumerate(data.STATS):
        x = 24 + i * col_w
        if i:
            d.line([x - 8, y + 8, x - 8, y + 58], fill=GREY, width=1)
        ff = fit(d, fig, SERIF, 29, col_w - 14)
        d.text((x, y + 4), fig, font=ff, fill=RED)
        block(d, x, y + 38, label, F(SANS_B, 9.5), col_w - 14, 11.5,
              max_lines=2)
    d.line([24, y + 66, W - 24, y + 66], fill=RULE, width=2)
    return y + 74


CERT_MARK = {"R": "\u25cf", "C": "\u25d0", "D": "\u25d2"}


def icon_chip(d, x, y, s):
    d.rounded_rectangle([x, y, x + s, y + s], 8, outline=INK, width=4)
    d.rounded_rectangle([x + s * .3, y + s * .3, x + s * .7, y + s * .7], 4,
                        outline=RED, width=4)
    for i in range(4):
        t = x + s * (.18 + .21 * i)
        d.line([t, y - 8, t, y], fill=INK, width=4)
        d.line([t, y + s, t, y + s + 8], fill=INK, width=4)
        t2 = y + s * (.18 + .21 * i)
        d.line([x - 8, t2, x, t2], fill=INK, width=4)
        d.line([x + s, t2, x + s + 8, t2], fill=INK, width=4)


def icon_ship(d, x, y, s):
    d.polygon([(x, y + s * .55), (x + s, y + s * .55), (x + s * .85, y + s * .8),
               (x + s * .15, y + s * .8)], fill=INK)
    d.rectangle([x + s * .55, y + s * .3, x + s * .8, y + s * .55], fill=RED)
    d.line([x + s * .25, y + s * .55, x + s * .25, y + s * .2], fill=INK, width=4)
    cx, cy = x + s * .3, y + s * .08
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)
    for dx, dy in [(-16, -8), (16, -8), (-16, 8), (16, 8)]:
        d.line([cx, cy, cx + dx, cy + dy], fill=INK, width=3)
        d.ellipse([cx + dx - 4, cy + dy - 4, cx + dx + 4, cy + dy + 4],
                  outline=INK, width=2)
    for i in range(3):
        d.arc([x + i * s * .3, y + s * .82, x + (i + 1) * s * .3, y + s],
              0, 180, fill=BLUE, width=3)


def icon_globe(d, x, y, s):
    d.ellipse([x, y, x + s, y + s], outline=BLUE, width=4)
    d.ellipse([x + s * .32, y, x + s * .68, y + s], outline=BLUE, width=3)
    d.line([x, y + s * .5, x + s, y + s * .5], fill=BLUE, width=3)
    d.arc([x, y + s * .18, x + s, y + s * .55], 0, 180, fill=BLUE, width=3)
    d.arc([x, y + s * .45, x + s, y + s * .82], 180, 360, fill=BLUE, width=3)
    tx = x + s * .78
    d.rounded_rectangle([tx, y + s * .1, tx + s * .1, y + s * .75], 5,
                        outline=RED, width=3)
    d.ellipse([tx - s * .05, y + s * .68, tx + s * .15, y + s * .88], fill=RED)


ICONS = {"chip": icon_chip, "ship": icon_ship, "globe": icon_globe}


def leads(d, y):
    col_w = (W - 48 - 16) // 3
    for i, (icon, kick, head, body, dt, cert) in enumerate(data.LEADS):
        x = 24 + i * (col_w + 8)
        d.rectangle([x, y, x + col_w, y + 196], fill=PAPER, outline=RULE,
                    width=2)
        ICONS[icon](d, x + 14, y + 12, 50)
        block(d, x + 78, y + 14, kick, F(SANS_B, 11.5), col_w - 90, 14,
              fill=RED, max_lines=2)
        d.text((x + 78, y + 44), f"{CERT_MARK[cert]} {dt}",
               font=F(SANS_B, 11.5), fill=GREY)
        yy = block(d, x + 12, y + 72, head, F(SERIF, 16.5), col_w - 24, 20,
                   max_lines=3)
        block(d, x + 12, max(yy + 2, y + 130), body, F(SANS, 12),
              col_w - 24, 15.5, max_lines=4)
    return y + 204


def cards(d, y):
    col_w = (W - 48 - 4 * 8) // 5
    row_h = 84
    for idx, (no, region, head, dt, cert) in enumerate(data.CARDS):
        r, c = divmod(idx, 5)
        x = 24 + c * (col_w + 8)
        yy = y + r * (row_h + 8)
        d.rectangle([x, yy, x + col_w, yy + row_h], outline=RULE, width=1)
        d.text((x + 7, yy + 5), f"{no:02d}", font=F(SERIF, 15), fill=RED)
        d.text((x + 36, yy + 6), region, font=F(SANS_B, 9), fill=BLUE)
        d.text((x + 36, yy + 18), f"{CERT_MARK[cert]} {dt}",
               font=F(SANS_B, 9), fill=GREY)
        block(d, x + 7, yy + 32, head, F(SANS, 10), col_w - 14, 12.5,
              max_lines=4)
    return y + 2 * row_h + 8


def timeline(d, y):
    d.rectangle([24, y, W - 24, y + 50], fill=INK)
    d.text((36, y + 4), "THE ROAD TO TUESDAY \u2014 HOW THE DAY WAS MADE",
           font=F(SERIF, 12.5), fill=(255, 250, 240))
    col_w = (W - 72) // 3
    for i, (when, text) in enumerate(data.TIMELINE):
        r, c = divmod(i, 3)
        x = 36 + c * col_w
        yy = y + 22 + r * 13
        d.text((x, yy), when, font=F(SANS_B, 9), fill=(240, 160, 140))
        wlen = d.textlength(when + " ", font=F(SANS_B, 9))
        f = fit(d, text, SANS, 9, col_w - wlen - 6, min_size=8)
        d.text((x + wlen, yy), text, font=f, fill=(255, 250, 240))
    return y + 58


# Land spans per latitude row. Grid: 100 cols (lon -180..180, 3.6 deg/col),
# 36 rows (lat 80..-60, ~3.9 deg/row). Each row lists (first, last) land cols.
LAND = [
    [(16, 30), (33, 41), (58, 97)], [(14, 32), (34, 42), (57, 98)],
    [(0, 12), (14, 34), (36, 41), (55, 99)], [(1, 13), (15, 35), (54, 99)],
    [(2, 12), (16, 34), (44, 45), (56, 99)], [(3, 11), (17, 34), (54, 99)],
    [(18, 33), (53, 97)], [(19, 32), (52, 95)], [(18, 32), (51, 93)],
    [(18, 31), (50, 90), (91, 93)], [(18, 31), (47, 88), (90, 92)],
    [(18, 30), (46, 86)], [(18, 29), (45, 85)], [(19, 27), (44, 84)],
    [(19, 26), (43, 83)], [(20, 26), (43, 83)], [(21, 26), (42, 86)],
    [(29, 35), (42, 62), (80, 90)], [(29, 37), (43, 61), (79, 92)],
    [(29, 39), (44, 59), (80, 94)], [(30, 39), (44, 57), (81, 90)],
    [(30, 37), (45, 56), (78, 88)], [(30, 36), (45, 55), (79, 86)],
    [(30, 35), (46, 55), (57, 58), (81, 89)],
    [(31, 34), (46, 54), (57, 58), (79, 91)],
    [(31, 33), (46, 53), (57, 58), (78, 92)], [(31, 33), (47, 52), (79, 91)],
    [(31, 32), (47, 51), (80, 89)], [(31, 32), (47, 50), (81, 92), (96, 98)],
    [(31, 31), (83, 91), (96, 98)], [(31, 31), (95, 97)], [(30, 31), (94, 96)],
    [(30, 30)], [(30, 30)], [], [],
]


def pin_map(d, x0, y0, x1, y1):
    rows, cols = len(LAND), 100
    cw = (x1 - x0) / cols
    ch = (y1 - y0) / rows
    for r, spans in enumerate(LAND):
        for a, b in spans:
            for c in range(a, b + 1):
                cx, cy = x0 + c * cw, y0 + r * ch
                d.ellipse([cx, cy, cx + 2.4, cy + 2.4], fill=(178, 168, 148))
    offsets = {"Warsaw": (-46, -7), "Kyiv": (6, -14), "Gaza": (-32, 9),
               "Lisbon": (-38, -5), "Geneva": (-44, -13), "Turin": (-34, 10),
               "Antalya": (-20, -15), "Delhi": (-40, 7), "Juba": (6, 13),
               "Nairobi": (6, 9), "Bayelsa": (-48, 3)}
    for label, lon, lat in data.PINS:
        px = x0 + (lon + 180) / 360 * (x1 - x0)
        py = y0 + (80 - lat) / 140 * (y1 - y0)
        d.ellipse([px - 3.4, py - 3.4, px + 3.4, py + 3.4], fill=RED,
                  outline=INK, width=1)
        dx, dy = offsets.get(label, (5, -5))
        d.text((px + dx, py + dy), label, font=F(SANS_B, 8.5), fill=INK)


def bottom_row(d, y):
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    d.text((24, y + 6), "WHERE IT HAPPENED \u2014 THE DAY ON THE MAP",
           font=F(SERIF, 13), fill=INK)
    pin_map(d, 24, y + 26, 640, y + 134)
    bx = 660
    d.rectangle([bx, y + 26, W - 24, y + 134], outline=RED, width=3)
    d.text((bx + 10, y + 31), "DATE CHECK", font=F(SERIF, 14), fill=RED)
    yy = y + 53
    for line in data.DATE_CHECK:
        d.text((bx + 10, yy), "\u2713 " + line, font=F(SANS_B, 9.5), fill=INK)
        yy += 11.5
    yy += 4
    for mark, text in data.LEGEND:
        d.text((bx + 10, yy), f"{mark} {text}", font=F(SANS, 9.5), fill=INK)
        yy += 11.5
    return y + 142


def also_strip(d, y):
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    d.text((24, y + 4), "ALSO ON THE WIRE \u2014 MONDAY INTO TUESDAY",
           font=F(SERIF, 13), fill=RED)
    col_w = (W - 48 - 2 * 12) // 3
    per = (len(data.ALSO) + 2) // 3
    size = 10.5
    while size > 8.5:
        f = F(SANS, size)
        worst = 0
        for c in range(3):
            n = 0
            for item in data.ALSO[c * per:(c + 1) * per]:
                n += len(wrap(d, "\u00b7 " + item, f, col_w - 6))
            worst = max(worst, n)
        if worst * (size + 1.5) <= H - (y + 26) - 4:
            break
        size -= 0.5
    f = F(SANS, size)
    for c in range(3):
        x = 24 + c * (col_w + 12)
        yy = y + 26
        for item in data.ALSO[c * per:(c + 1) * per]:
            yy = block(d, x, yy, "\u00b7 " + item, f, col_w - 6, size + 1.5,
                       max_lines=3)
    return H


def render(path):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    masthead(d)
    ticker(d)
    y = stat_band(d, 168)
    y = leads(d, y + 6)
    y = cards(d, y + 8)
    y = timeline(d, y + 8)
    y = bottom_row(d, y + 8)
    also_strip(d, y + 6)
    img.save(path, "PNG")
    return path
