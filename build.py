"""Rebuild the two static pages with Python 3. No third-party packages required."""
from html import escape
from pathlib import Path

DIST = Path(__file__).resolve().parent / "dist"
SCHOLAR = "https://scholar.google.com/citations?user=c-I0GMYAAAAJ&hl=en"
EMAIL = "jizhou_han@stu.xjtu.edu.cn"
CVPR = "https://openaccess.thecvf.com/content/CVPR2026/html/Han_Learning_Like_Humans_Analogical_Concept_Learning_for_Generalized_Category_Discovery_CVPR_2026_paper.html"
ORAL = "https://cvpr.thecvf.com/virtual/2026/oral/40316"
GOAL = "https://arxiv.org/abs/2602.19872"
NEURIPS = "https://proceedings.neurips.cc/paper_files/paper/2025/hash/be36e50757bf9cd280aa74f89a7d1c23-Abstract-Conference.html"
MSTTA = "https://doi.org/10.1109/TCSVT.2026.3676383"
FROZEN_SPACE = "https://doi.org/10.1109/TCSVT.2026.3716498"
RADA = "https://aclanthology.org/2026.findings-emnlp.192/"
FIRST_AUTHOR_PAPERS = [
    ("CVPR", "2026", "conference", "Learning Like Humans: Analogical Concept Learning for Generalized Category Discovery",
     "Jizhou Han, Chenhao Ding, Yuhang He, Qiang Wang, Shaokun Wang, SongLin Dong, Yihong Gong", "analogical", CVPR),
    ("AAAI", "2026", "conference", "GOAL: Geometrically Optimal Alignment for Continual Generalized Category Discovery",
     "Jizhou Han, Chenhao Ding, SongLin Dong, Yuhang He, Shaokun Wang, Qiang Wang, Yihong Gong", "goal", GOAL),
    ("IEEE TCSVT", "2026", "journal", "Unleashing the Potential of All Test Samples: Mean-Shift Guided Test-Time Adaptation",
     "Jizhou Han, Chenhao Ding, Songlin Dong, Xinyuan Gao, Qiang Wang, Yuhang He, Yihong Gong", "mean-shift", MSTTA),
    ("IEEE TCSVT", "2026", "journal", "Learn by Reasoning: Analogical Weight Generation for Few-Shot Class-Incremental Learning",
     "Jizhou Han, Chenhao Ding, Yuhang He, Songlin Dong, Qiang Wang, Xinyuan Gao, Yihong Gong", "reasoning", "https://doi.org/10.1109/TCSVT.2025.3637903"),
    ("NeurIPS", "2025", "conference", "Consistent Supervised-Unsupervised Alignment for Generalized Category Discovery",
     "Jizhou Han, Shaokun Wang, Yuhang He, Chenhao Ding, Qiang Wang, Xinyuan Gao, SongLin Dong, Yihong Gong", "nc-gcd", NEURIPS),
    ("IEEE Sensors Journal", "2023", "journal", "Extrinsic Calibration of a Binocular Camera and LiDAR Based on Neural Networks",
     "Jizhou Han, Zhenhai Zhang, Zhoubo Wang, Jingyu Li, Xiaodong Guo, Xiao Kang", "calibration", "https://doi.org/10.1109/JSEN.2023.3325329"),
]
COLLABORATIVE_PAPERS = [
    ("Findings of EMNLP", "2026", "conference", "Sustaining Cross-Modal Dependency for Generalizable Vision-Language Model Tuning",
     "Chenhao Ding, Jizhou Han, SongLin Dong, Xinyuan Gao, Qiang Wang, Lixin Xiu, Wei Ke, Yihong Gong, Hideki Nakayama", "rada", RADA),
    ("IEEE TCSVT", "2026", "journal", "Reorienting the Frozen Space: Training-Free Test-Time Adaptation by Geometric Transformation",
     "Chenhao Ding, Jizhou Han, Songlin Dong, Xiang Song, Xinyuan Gao, Qiang Wang, Yuhang He, Zhiheng Ma, Yihong Gong", "frozen-space", FROZEN_SPACE),
]
ICONS = {
    "arrow": '<path d="M5 15 15 5M6 5h9v9"/>',
    "mail": '<rect x="2" y="4" width="16" height="12" rx="2"/><path d="m3 5 7 5 7-5"/>',
    "pin": '<path d="M16 8c0 5-6 10-6 10S4 13 4 8a6 6 0 0 1 12 0Z"/><circle cx="10" cy="8" r="2"/>',
    "globe": '<circle cx="10" cy="10" r="8"/><ellipse cx="10" cy="10" rx="3.5" ry="8"/><path d="M2 10h16"/>',
}


def icon(name):
    return f'<svg class="icon" aria-hidden="true" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'


def link(url, label, cls=""):
    return f'<a class="{cls}" href="{escape(url, quote=True)}">{label}</a>'


def render(chinese):
    def tr(en, zh):
        return zh if chinese else en

    figure_descriptions = {
        "analogical": tr("Human analogical learning and the Analogical Textual Concept Generator", "人类类比学习与类比文本概念生成器"),
        "goal": tr("Classifier geometry as new categories are discovered across learning sessions", "持续发现新类别时，不同分类器原型的几何结构"),
        "mean-shift": tr("Test samples and the feature cache before and after mean-shift adaptation", "均值漂移自适应前后的测试样本与特征缓存"),
        "reasoning": tr("An analogy for recognizing pandas and the corresponding class-weight generator", "以识别熊猫为例的人类类比过程及相应的新类权重生成器"),
        "nc-gcd": tr("Fixed class prototypes, the NC-GCD framework and performance comparisons", "固定类别原型、NC-GCD 框架及其性能对比"),
        "calibration": tr("Stereo images of a checkerboard calibration target, from the author’s presentation", "作者报告中的双目相机棋盘格标定图像"),
        "rada": tr("RADA retrieves multimodal memories to generate adaptive tokens for frozen CLIP encoders", "RADA 从多模态记忆库检索信息，为冻结的 CLIP 编码器生成自适应词元"),
        "frozen-space": tr("A dynamic sample cache and a change of basis for CLIP test-time adaptation", "用于 CLIP 测试时自适应的动态样本缓存和基变换"),
    }

    def paper_row(paper):
        venue, year, kind, title, authors, figure, url = paper
        badge = f'<span class="oral">{tr("Oral", "口头报告")}</span>' if url == CVPR else ""
        caption = figure_descriptions.get(figure, title)
        preview = f'<div class="paper-figure"><a class="thumb" href="{url}" aria-label="{escape(title)}"><img src="assets/{figure}.webp" loading="lazy" alt="{escape(caption)}"></a></div>' if figure else ""
        byline = authors.replace("Jizhou Han", "<strong>Jizhou Han</strong>")
        paper_label = "arXiv" if url == GOAL else tr("Paper", "论文")
        actions = link(url, paper_label + icon("arrow"))
        return f'<li class="paper" data-kind="{kind}">{preview}<div class="paper-info"><div class="meta"><span>{venue} {year}</span>{badge}</div><h4 lang="en">{link(url, title)}</h4><p class="authors" lang="en">{byline}</p><div class="paper-links">{actions}</div></div></li>'

    def paper_group(title, papers, group_id):
        entries = "".join(paper_row(paper) for paper in papers)
        return f'<section class="paper-group" aria-labelledby="{group_id}"><h3 id="{group_id}">{title}</h3><ol class="papers">{entries}</ol></section>'

    honors = [
        ("2026", tr("National Scholarship", "国家奖学金")),
        ("2026", tr("Bambu Lab Scholarship", "拓竹奖学金")),
        ("2023", tr("Beijing Outstanding Graduate", "北京市优秀毕业生")),
        ("2022", tr("Jiefang Linghang Scholarship, FAW Jiefang Automotive Company", "一汽解放领航奖学金")),
        ("2022", tr("Beijing Institute of Technology Robotics Scholarship", "北京理工大学机器人奖学金")),
    ]
    honors_html = "".join(f'<li><time>{year}</time><span>{title}</span></li>' for year,title in honors)

    news = [
        ("11", "Nov", tr("Reorienting the Frozen Space appeared in the November issue of IEEE TCSVT.", "合作论文 Reorienting the Frozen Space 刊于 IEEE TCSVT 11 月刊。"), FROZEN_SPACE),
        ("10", "Oct", tr("Our work on cross-modal dependency in vision-language model tuning appeared in Findings of EMNLP 2026.", "我们关于视觉语言模型微调中跨模态依赖的研究发表于 EMNLP 2026 Findings。"), RADA),
        ("08", "Aug", tr("Our paper on mean-shift guided test-time adaptation appeared in IEEE TCSVT.", "关于均值漂移引导测试时自适应的论文刊于 IEEE TCSVT。"), MSTTA),
        ("06", "Jun", tr("I presented Learning Like Humans as an oral at CVPR 2026 in Denver.", "在丹佛举行的 CVPR 2026 上，我作了 Learning Like Humans 口头报告。"), ORAL),
        ("03", "Mar", tr("GOAL appeared in the AAAI-26 proceedings.", "GOAL 收录于 AAAI-26 会议论文集。"), GOAL),
    ]
    news_html = "".join(f'<li><time datetime="2026-{m}">{tr(month+" 2026","2026 年 "+str(int(m))+" 月")}</time><p>{link(url,line)}</p></li>' for m,month,line,url in news)
    education = [
        (tr("2023 – present", "2023 – 至今"),tr("Ph.D. in Artificial Intelligence", "博士 · 人工智能"),tr("Xi’an Jiaotong University", "西安交通大学")),
        ("2020 – 2023",tr("Master’s in Mechatronic Systems and Sensors", "硕士 · 机电系统与传感器"),tr("Beijing Institute of Technology", "北京理工大学")),
        ("2016 – 2020",tr("Bachelor’s in Mechatronics Engineering", "本科 · 机械电子工程"),tr("Beijing Institute of Technology", "北京理工大学")),
    ]
    edu = "".join(f'<li><time>{period}</time><h3>{degree}</h3><p>{uni}</p></li>' for period,degree,uni in education)
    filters = "".join(f'<button type="button" data-filter="{kind}" aria-pressed="{str(kind=="all").lower()}">{label}</button>' for kind,label in [
        ("all",tr("All","全部")),("conference",tr("Conferences","会议")),("journal",tr("Journals","期刊"))])
    about, publications, background = tr("About","简介"), tr("Publications","论文"), tr("Background","学术经历")
    return f'''<!doctype html>
<html lang="{tr("en","zh-CN")}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tr("Jizhou Han | Academic Homepage","韩季洲 | 学术主页")}</title>
<meta name="description" content="{tr("Jizhou Han studies generalized category discovery and continual learning at Xi’an Jiaotong University. Selected papers, research updates and academic background.","韩季洲，西安交通大学人工智能博士研究生。研究方向为广义类别发现、持续学习和类比推理。")}">
<link rel="alternate" hreflang="en" href="index.html"><link rel="alternate" hreflang="zh-CN" href="zh.html"><link rel="stylesheet" href="styles.css"><script defer src="site.js"></script></head>
<body><a class="skip" href="#about">{tr("Skip to profile","跳到个人简介")}</a>
<header><div class="shell header-inner"><a class="brand" href="#about">Jizhou Han</a>
<nav aria-label="{tr("Main navigation","主导航")}">{link("#about",about)}{link("#publications",publications)}{link("#background",background)}<a class="language" hreflang="{tr("zh-CN","en")}" href="{tr("zh.html","index.html")}">{icon("globe")}{tr("中文","EN")}</a></nav></div></header>
<main class="shell"><section class="hero" id="about"><div class="intro"><p class="eyebrow"><span class="rule"></span>{tr("Computer vision & machine learning","计算机视觉与机器学习")}</p>
<h1>{tr("Jizhou Han","韩季洲")} <span lang="{tr("zh-CN","en")}">{tr("韩季洲","Jizhou Han")}</span></h1>
<p class="position">{tr("Ph.D. student in Artificial Intelligence","人工智能博士研究生")}</p>
<p class="affiliation">{tr("Xi’an Jiaotong University","西安交通大学")}</p>
<p class="bio">{tr("I study how visual models can discover new categories while remembering the ones they already know. My work at the Institute of Artificial Intelligence and Robotics, advised by Prof. Yihong Gong, draws on continual learning and human analogical reasoning.","我在西安交通大学人工智能与机器人研究所攻读博士学位，导师为龚怡宏教授。我的研究关注视觉模型如何在识别已知类别的同时发现新类别，并探索持续学习和人类类比推理如何帮助模型保留和运用已有知识。")}</p>
<div class="profile-links">{link("mailto:"+EMAIL,icon("mail")+tr("Email","邮箱"),"primary")}{link(SCHOLAR,"Google Scholar")}{link("https://dblp.org/pid/339/5410.html","DBLP")}</div></div>
<figure class="portrait"><div class="photo-mat"><img width="1913" height="1280" src="assets/jizhou-han.jpg?v=20261118" alt="{tr("Jizhou Han beside a cat mural","韩季洲与猫咪壁画")}"></div>
<figcaption>{icon("pin")}{tr("Xi’an, China","中国 · 西安")}</figcaption></figure></section>
<div class="content-grid"><section class="pubs" id="publications"><h2>{tr("Selected publications","代表论文")}</h2>
<div class="pub-tools"><div class="filters" role="group" aria-label="{tr("Filter by publication type","按论文类型筛选")}">{filters}</div>
{link(SCHOLAR,tr("Full list on Google Scholar","完整列表 · Google Scholar")+icon("arrow"),"full-list")}</div>
{paper_group(tr("First-author papers","第一作者论文"), FIRST_AUTHOR_PAPERS, "first-author")}
{paper_group(tr("Selected second-author papers","第二作者代表论文"), COLLABORATIVE_PAPERS, "collaborative")}</section>
<aside><section class="updates" id="news"><h2>{tr("Recent news","学术动态")}</h2><ol class="timeline">{news_html}</ol></section>
<section class="topics"><h2>{tr("Research interests","研究方向")}</h2><ul><li>{tr("Generalized category discovery","广义类别发现")}</li><li>{tr("Continual learning","持续学习")}</li><li>{tr("Analogical reasoning","类比推理")}</li><li>{tr("Test-time adaptation","测试时自适应")}</li></ul></section></aside></div>
<section class="background" id="background"><h2>{tr("Academic background","学术经历")}</h2><div class="bg-grid"><section><h3 class="eyebrow">{tr("Education","教育经历")}</h3><ol class="history">{edu}</ol></section>
<div><section><h3 class="eyebrow">{tr("Academic service","学术服务")}</h3>
<p><b>{tr("Conference reviewer","会议审稿")}</b><br>CVPR, ECCV, AAAI, ACM MM, ICLR</p>
<p><b>{tr("Teaching assistant","研究生课程助教")}</b><br>{tr("Statistical Methods and Machine Learning for Computer Vision, Xi’an Jiaotong University.","西安交通大学《计算机视觉的统计方法与机器学习》。")}</p></section>
<section class="honors" id="honors"><h3 class="eyebrow">{tr("Honors & scholarships","荣誉与奖学金")}</h3><ul>{honors_html}</ul></section></div></div></section></main>
<footer><div class="shell"><span>© 2026 Jizhou Han · 韩季洲</span>{link("mailto:"+EMAIL,EMAIL)}</div></footer></body></html>'''


if __name__ == "__main__":
    for chinese, filename in [(False, "index.html"), (True, "zh.html")]:
        (DIST / filename).write_text(render(chinese), encoding="utf-8")
