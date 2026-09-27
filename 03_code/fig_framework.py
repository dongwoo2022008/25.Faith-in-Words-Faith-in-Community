import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "Liberation Serif"

FS_H = 14.0
FS_B = 12.5
FS_E = 12.0

HEAD = 0.48      # header centre below top edge
GAP = 0.62       # header to first body line
STEP = 0.46      # body line step
BOT = 0.34       # bottom padding

W, H = 16.5, 12.0
fig, ax = plt.subplots(figsize=(W, H + 1.1))
ax.set_xlim(0, W); ax.set_ylim(-1.1, H); ax.axis("off")


def height(n):
    return HEAD + GAP + (n - 1) * STEP + BOT


def box(x0, x1, ytop, header, lines, dashed=False, center=False):
    y0 = ytop - height(len(lines))
    st = (0, (5, 3)) if dashed else "solid"
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, ytop - y0,
                                boxstyle="square,pad=0", linewidth=1.3,
                                edgecolor="black", facecolor="white",
                                linestyle=st, zorder=2))
    ax.text((x0 + x1) / 2, ytop - HEAD, header, ha="center", va="center",
            fontsize=FS_H, fontweight="bold", zorder=3)
    y = ytop - HEAD - GAP
    for ln in lines:
        if center:
            ax.text((x0 + x1) / 2, y, ln, ha="center", va="center",
                    fontsize=FS_B, zorder=3)
        else:
            ax.text(x0 + 0.32, y, ln, ha="left", va="center",
                    fontsize=FS_B, zorder=3)
        y -= STEP
    return y0


def arrow(x0, y0, x1, y1, dashed=False):
    st = (0, (5, 3)) if dashed else "solid"
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=17, linewidth=1.3,
                                 color="black", linestyle=st,
                                 shrinkA=0, shrinkB=0, zorder=1))


def line(x0, y0, x1, y1, dashed=False):
    st = (0, (5, 3)) if dashed else "solid"
    ax.plot([x0, x1], [y0, y1], color="black", linewidth=1.3,
            linestyle=st, zorder=1, solid_capstyle="butt")


L0, L1 = 3.4, 8.6
R0, R1 = 9.4, 14.6
LC, RC = (L0 + L1) / 2, (R0 + R1) / 2
MID = 9.0

# --- top -------------------------------------------------------------
top_bottom = box(5.5, 12.5, 11.60, "Borrower credit file",
                 ["LendingClub, 1.34 million terminated loans, 2007–2018"],
                 center=True)

SPLIT = 10.00
line(MID, top_bottom, MID, SPLIT)
line(LC, SPLIT, MID, SPLIT)
line(MID, SPLIT, RC, SPLIT, dashed=True)
arrow(LC, SPLIT, LC, 9.40)
arrow(RC, SPLIT, RC, 9.40, dashed=True)
ax.text(LC + 0.20, 9.72, "observable, verifiable", ha="left", va="center",
        fontsize=FS_E, style="italic")
ax.text(RC + 0.20, 9.72, "costless, unverifiable", ha="left", va="center",
        fontsize=FS_E, style="italic")

# --- signals ---------------------------------------------------------
sig_b = box(L0, L1, 9.40, "Institutional affiliation (n = 3,105)",
            ["Job title: pastor, minister, chaplain,",
             "church secretary, church administrator"])
box(R0, R1, 9.40, "Self-authored religious language (n = 681)",
    ["Loan description: “God bless”,",
     "“as a Christian I pay my debts”"], dashed=True)

arrow(LC, sig_b, LC, 7.05)
arrow(RC, sig_b, RC, 7.05, dashed=True)

# --- mechanisms ------------------------------------------------------
mech_b = box(L0, L1, 7.05, "Community as collateral",
             ["Default is observed by the congregation;",
              "the reputational cost of default rises",
              "with community density",
              "(Besley and Coate, 1995; Karlan et al., 2009)"])
box(R0, R1, 7.05, "Low-cost, unverifiable signal",
    ["Costless to write; selection into invoking",
     "faith and substitution for verifiable facts",
     "(Crawford and Sobel, 1982;",
     "Farrell and Rabin, 1996)"], dashed=True)

RES_TOP = 2.75
arrow(LC, mech_b, LC, RES_TOP)
arrow(RC, mech_b, RC, RES_TOP, dashed=True)
ax.text(LC + 0.25, 3.10, "H1: odds ratio < 1", ha="left", va="center",
        fontsize=FS_E, style="italic", fontweight="bold")
ax.text(RC + 0.25, 3.10, "H2: odds ratio > 1", ha="left", va="center",
        fontsize=FS_E, style="italic", fontweight="bold")

# --- moderator -------------------------------------------------------
box(0.10, 3.05, 4.34, "Local congregation density",
    ["2010 U.S. Religion Census"], center=True)
MOD_Y = 3.62
arrow(3.05, MOD_Y, LC - 0.09, MOD_Y)
MOD_X = (3.05 + LC) / 2
ax.text(MOD_X, MOD_Y + 0.44, "moderates H1",
        ha="center", va="bottom", fontsize=FS_E, style="italic")
ax.text(MOD_X, MOD_Y + 0.16, "(interaction OR 0.84)",
        ha="center", va="bottom", fontsize=FS_E, style="italic")

# --- results ---------------------------------------------------------
box(L0, L1, RES_TOP, "Default odds ratio 0.69 (−4.8 pp)",
    ["Same for clergy and church staff;",
     "larger where congregations are denser;",
     "unresponsive to local unemployment"])
box(R0, R1, RES_TOP, "Default odds ratio 1.28 (+3.2 pp)",
    ["Direction stable; imprecise once the full",
     "text is conditioned on; no interaction",
     "with local religiosity"], dashed=True)

# --- pricing footer ---------------------------------------------------
line(0.10, -0.30, W - 0.10, -0.30)
ax.text(W / 2, -0.72,
        "Neither signal is reflected in the platform’s grade-based pricing "
        "(−64 bp and +28 bp per year of unpriced default).",
        ha="center", va="center", fontsize=FS_B)

fig.savefig("fig1_channels.png", dpi=600, bbox_inches="tight",
            facecolor="white")
fig.savefig("figures/Figure1_channels.png", dpi=600, bbox_inches="tight",
            facecolor="white")
fig.savefig("figures/Figure1_channels.pdf", bbox_inches="tight",
            facecolor="white")
print("ok")
