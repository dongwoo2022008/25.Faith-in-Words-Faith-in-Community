import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

import matplotlib.font_manager as fm
fm.fontManager.addfont("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
fm.fontManager.addfont("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
plt.rcParams["font.family"] = "Noto Sans CJK JP"
FS_H, FS_B, FS_E = 12.5, 11, 10.5

W, H = 17, 14.6
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W); ax.set_ylim(-0.6, H); ax.axis("off")

def box(x0, y0, x1, y1, header, lines, dashed=False, fill="white", center=False):
    y0 = y1 - (0.36+0.5+0.4*(len(lines)-1)+0.35)
    st = (0, (5, 3)) if dashed else "solid"
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0, boxstyle="round,pad=0.02,rounding_size=0.12",
                                lw=1.3, ec="black", fc=fill, ls=st, zorder=2))
    ax.text((x0+x1)/2, y1-0.36, header, ha="center", va="center", fontsize=FS_H, weight="bold", zorder=3)
    y = y1-0.36-0.5
    for ln in lines:
        if center:
            ax.text((x0+x1)/2, y, ln, ha="center", va="center", fontsize=FS_B, zorder=3)
        else:
            ax.text(x0+0.25, y, ln, ha="left", va="center", fontsize=FS_B, zorder=3)
        y -= 0.4
    return y0

def arrow(x0, y0, x1, y1, label=None, dashed=False, lx=0.15, ly=0):
    st = (0, (5, 3)) if dashed else "solid"
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=16,
                                 lw=1.3, color="black", ls=st, shrinkA=0, shrinkB=0, zorder=1))
    if label:
        ax.text((x0+x1)/2+lx, (y0+y1)/2+ly, label, ha="left", va="center", fontsize=FS_E, style="italic")

grey = "#f2f2f2"

# ---- column A: affiliation (left) ; column B: religious language (right)
ax.text(4.25, H-0.35, "A. 종교기관 소속 (직함)", ha="center", fontsize=14, weight="bold")
ax.text(12.5, H-0.35, "B. 종교 언어 (설명문)", ha="center", fontsize=14, weight="bold")

# --- A ---
GAP=0.55
y=H-0.8
b=box(1.0,0,7.5,y,"1. 규칙 (사전 지정)",
    ["직함에 성직 역할어(pastor, minister, chaplain, rabbi …)",
     "또는 종교조직어(church, parish, diocese …) 포함",
     "단, 병원·학교·보험사·은행 이름의 일부이면 제외"])
arrow(4.25,b,4.25,b-GAP); y=b-GAP
b=box(1.0,0,7.5,y,"2. 건수",
    ["전체 파일 5,014건 → 종결 표본 3,105건 (H1 처리집단)",
     "성직 역할어 2,497건 / 종교조직명만 608건 (교회 직원)"])
arrow(4.25,b,4.25,b-GAP); y=b-GAP
b=box(1.0,0,7.5,y,"3. 검증: 무작위 200건 감사 (부록 표 B2)",
    ["A 성직 역할 146 / B 비성직 교회 직원 48",
     "C 종교 무관 2 (루이지애나 civil parish) / D 분류 불가 4",
     "정밀도 97%. parish 오류 30건 제외 시 OR 0.692 → 0.683"], fill=grey)
arrow(4.25,b,4.25,b-GAP); y=b-GAP
bA=box(1.0,0,7.5,y,"4. 용도",
    ["확인적 검정 H1: 규칙 그대로 (OR 0.69)",
     "성직 vs 교회 직원 비교 → 5.3절 (탐색적)"])

# --- B ---
y=H-0.8
b=box(9.0,0,16.0,y,"1. 사전 (사전 지정)",
    ["제목·본문에 종교 용어(God, church, pray, bless, tithe …)",
     "관용구 제외 (good faith, heaven forbid, Lord & Taylor)",
     "→ 설명문 표본 123,292건 중 681건 (0.55%)"])
arrow(12.5,b,12.5,b-GAP); y=b-GAP
b=box(9.0,0,16.0,y,"2. 코드북 코딩 (LLM, 681건 전부; 부록 B)",
    ["a 관용구 467  (\"Thank you and God bless\")",
     "b 정체성·가치 34  (\"as a Christian I pay my debts\")",
     "c 실천·지출 82  (십일조, 교회 취업, 선교)",
     "x 비종교 98  (사전 오탐)          a+b+c = 583"])
arrow(12.5,b,12.5,b-GAP); y=b-GAP
b=box(9.0,0,16.0,y,"3. 검증 (부록 표 B1)",
    ["다른 계열 LLM 200건 재코딩: κ 0.86 (유형), 0.81 (종교 여부)",
     "사람 코더(저자) 200건: κ 0.72 (유형), 0.55 (종교 여부)",
     "누락 점검: 종교어 가린 분류기 + LLM 판독 → 수십 건"], fill=grey)
arrow(12.5,b,12.5,b-GAP); y=b-GAP
bB=box(9.0,0,16.0,y,"4. 용도",
    ["확인적 검정 H2: 사전 지표 681건 (OR 1.28)",
     "강건성: 확인 지표 583건 (OR 1.34)",
     "플라시보: 오탐 98건 (OR 0.95) → 효과는 단어가 아니라 내용",
     "유형별 분해 (탐색적): a 1.39 / b 1.46 / c 0.99"])

# --- bottom
yb=min(bA,bB)-1.0
box(1.0,0,7.5,yb,"두 지표의 중첩 (설명문 표본)",
    ["소속 372건, 종교 언어 681건, 둘 다 20건",
     "→ 거의 다른 사람들: 두 신호를 독립적으로 비교 가능"], center=True)
box(9.0,0,16.0,yb,"원칙",
    ["확인적 검정은 추정 전에 정한 규칙·사전 그대로",
     "정제 지표·유형 분해는 점검용, 더 나은 척도로 취급하지 않음"], center=True)
arrow(4.25,bA,4.25,yb,dashed=True)
arrow(12.5,bB,12.5,yb,dashed=True)

ax.text(W/2, -0.35, "3.2절 측정 구축 흐름. 회색 상자 = 타당성 검증 (본문에서는 요약만, 세부는 부록 B).",
        ha="center", fontsize=FS_E)

fig.savefig("fig_measurement_ko.png", dpi=200, bbox_inches="tight", facecolor="white")
print("ok")
