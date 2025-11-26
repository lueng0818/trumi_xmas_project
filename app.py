import streamlit as st
import pandas as pd
import random

# ────────────── Page Config & CSS ──────────────
st.set_page_config(page_title="Tilandky 爆文煉金系統", layout="wide", page_icon="🏭")

# 定義品牌色 (維持一致性)
COLOR_PRIMARY = "#073B4C"
COLOR_SECONDARY = "#118AB2"
COLOR_BG = "#F1F5F9"

st.markdown(
    f"""<style>
    .stApp {{
        background-color: {COLOR_BG};
        font-family: 'Noto Sans TC', sans-serif;
    }}
    
    /* Header Style */
    .header-box {{
        background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_SECONDARY} 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    
    /* Process Cards */
    .process-card {{
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {COLOR_SECONDARY};
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }}
    
    /* Output Box */
    .output-box {{
        background-color: #fff;
        border: 2px dashed {COLOR_PRIMARY};
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
    }}
    
    h3 {{ color: {COLOR_PRIMARY}; }}
    </style>""",
    unsafe_allow_html=True,
)

# ────────────── Data: T.R.U.S.T. Logic ──────────────

# 濾鏡思維庫
reframing_lenses = {
    "工程師邏輯 (Debug)": {
        "desc": "將情緒問題轉化為「系統 Bug」或「流程錯誤」。",
        "keywords": ["SOP", "Debug", "底層代碼", "系統當機", "迴圈", "效能優化", "專案管理"],
        "example": "老公不洗碗 → 家務專案的權責劃分不清 (Permission Denied)。"
    },
    "資安顧問視角 (Security)": {
        "desc": "將心理界線轉化為「防火牆」或「病毒防護」。",
        "keywords": ["防火牆", "病毒入侵", "安全憑證", "漏洞", "權限設定", "攻擊防禦"],
        "example": "被婆婆情緒勒索 → 妳的能量防火牆 (Firewall) 出現漏洞。"
    },
    "男性視角 (Translation)": {
        "desc": "翻譯男人的腦袋，用男性的理性同理女性的感性。",
        "keywords": ["單執行緒", "CPU過熱", "待機模式", "邏輯運算", "狩獵本能"],
        "example": "老公發呆聽不到 → 他的 CPU 過熱，正在強制降溫，不是不愛妳。"
    }
}

# 內容分類庫
trust_categories = {
    "T - 共鳴型 (Truth)": {"goal": "導流、漲粉", "hook": "天啊！這就是在說我！"},
    "R - 觀點型 (Reframe)": {"goal": "建立權威", "hook": "原來這不是我的錯，是系統問題！"},
    "U - 關係型 (Union)": {"goal": "增加黏著度", "hook": "我想和他一起變好。"},
    "S - 乾貨型 (Strategy)": {"goal": "收藏、轉發", "hook": "這招太實用了，先存起來！"},
    "T - 見證型 (Transformation)": {"goal": "轉化成交", "hook": "如果她可以，我也想要這種改變。"}
}

# 標題公式庫
title_formulas = {
    "A. 工程師理性分析": [
        "工程師觀察：為什麼 80% 的{痛點}，都是因為「{工程名詞}」錯誤？",
        "別再{痛點}了！用工程師的「{工程名詞}」思維，三步驟解決。",
        "家庭系統崩潰？因為妳忽略了這個關鍵的「{工程名詞}」。"
    ],
    "B. 資安顧問警示": [
        "資安警告：妳的「{資安名詞}」過期了嗎？3個徵兆檢測{痛點}。",
        "別讓情緒病毒入侵！資安顧問教妳建立最強「{資安名詞}」。",
        "停止自我攻擊！妳正在遭遇內在的「{資安名詞}」危機。"
    ],
    "C. 男性溫柔反差": [
        "作為男人我說實話：其實老公{行為}，是因為{男性機制}。",
        "給老婆的說明書：當男人{行為}時，其實他在想什麼？",
        "不需要通靈！用男人的邏輯，秒懂為什麼他總是{痛點}。"
    ]
}

# ────────────── Sidebar ──────────────
st.sidebar.header("⚙️ 系統設定")
st.sidebar.info("歡迎回到 Tilandky 內容工廠。請依照 SOP 產出您的爆文。")
if st.sidebar.button("清除重來"):
    st.rerun()

# ────────────── Main Interface ──────────────

# Header
st.markdown(
    """
    <div class="header-box">
        <h1>🏭 T.R.U.S.T. 爆文生產流水線</h1>
        <p>Input: 真實痛點 ➡ Process: 工程師濾鏡 ➡ Output: 高價值內容</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Stage 1: Source the Truth
st.subheader("1️⃣ 第一階段：礦場挖掘 (Source)")
st.markdown('<div class="process-card">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    raw_pain = st.text_input("輸入客戶痛點 (Input)", placeholder="例如：老公回家只會滑手機，都不幫忙...")
    st.caption("🔍 檢核點：這個問題是否讓她們「睡不著覺」？是否有強烈的帶入感？")
with col2:
    pain_keyword = st.text_input("提煉 1 個關鍵字", placeholder="例如：偽單親")
st.markdown('</div>', unsafe_allow_html=True)

if raw_pain and pain_keyword:
    
    # Stage 2: The Engineer's Reframe
    st.subheader("2️⃣ 第二階段：濾鏡加工 (Reframe)")
    st.markdown('<div class="process-card">', unsafe_allow_html=True)
    
    lens_type = st.radio("選擇您的加工濾鏡：", list(reframing_lenses.keys()), horizontal=True)
    selected_lens = reframing_lenses[lens_type]
    
    st.info(f"💡 **濾鏡思維**：{selected_lens['desc']}\n\n📝 **參考詞彙**：{', '.join(selected_lens['keywords'])}")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.write(f"**❌ 一般視角 (抱怨)：** {raw_pain}")
    with col_r2:
        reframe_idea = st.text_area(f"**✅ Tilandky 視角 ({lens_type})：**", placeholder=f"例如：這不是態度問題，這是{selected_lens['keywords'][0]}設定錯誤...")
    
    st.markdown('</div>', unsafe_allow_html=True)

    if reframe_idea:
        
        # Stage 3: Categorize
        st.subheader("3️⃣ 第三階段：內容定位 (Categorize)")
        st.markdown('<div class="process-card">', unsafe_allow_html=True)
        
        category = st.selectbox("選擇這篇貼文的戰略目的：", list(trust_categories.keys()))
        cat_details = trust_categories[category]
        st.success(f"🎯 **目標**：{cat_details['goal']} | 🎣 **鉤子**：{cat_details['hook']}")
        
        st.markdown('</div>', unsafe_allow_html=True)

        # Stage 4: Viral Titles
        st.subheader("4️⃣ 第四階段：標題工程 (Viral Titles)")
        st.markdown('<div class="process-card">', unsafe_allow_html=True)
        
        # 自動生成標題建議
        st.write("🤖 **系統自動運算的標題建議：**")
        
        # 準備填入變數
        tech_term = selected_lens['keywords'][0] # 取第一個關鍵字當預設
        
        generated_titles = []
        
        if "工程師" in lens_type:
            formulas = title_formulas["A. 工程師理性分析"]
            for f in formulas:
                generated_titles.append(f.replace("{痛點}", pain_keyword).replace("{工程名詞}", tech_term))
        elif "資安" in lens_type:
            formulas = title_formulas["B. 資安顧問警示"]
            for f in formulas:
                generated_titles.append(f.replace("{痛點}", pain_keyword).replace("{資安名詞}", tech_term))
        else: # 男性視角
            formulas = title_formulas["C. 男性溫柔反差"]
            for f in formulas:
                generated_titles.append(f.replace("{行為}", pain_keyword).replace("{男性機制}", tech_term).replace("{痛點}", pain_keyword))
        
        # 顯示生成的標題
        final_title = st.radio("請選擇一個標題 (或作為靈感)：", generated_titles)
        
        st.markdown('</div>', unsafe_allow_html=True)

        # Stage 5: Final Output & Monetization
        st.divider()
        st.subheader("🚀 最終產出：爆文草稿")
        
        cta_text = """
        ---
        我是 Tilandky，用工程師邏輯陪妳聊出內在力量。
        如果妳也卡在這個「系統 Bug」裡出不來...
        
        👉 **點擊主頁連結，預約 20 分鐘「前導邏輯診斷」**
        讓我幫妳找出那個卡住妳的程式碼，重啟妳的人生系統。
        """
        
        st.markdown(
            f"""
            <div class="output-box">
                <h3>{final_title}</h3>
                <p><strong>(圖片建議：{pain_keyword} 的情境圖 + 工程師風格文字壓字)</strong></p>
                <br>
                <p>{raw_pain}</p>
                <p>很多媽媽問我怎麼辦？</p>
                <p>其實，如果我們用<strong>「{lens_type}」</strong>來看，這根本不是妳的問題...</p>
                <p><strong>{reframe_idea}</strong></p>
                <br>
                <p>(在此處展開您的 {category.split(' - ')[1]} 內容...)</p>
                <br>
                {cta_text.replace(chr(10), '<br>')}
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.caption("💡 提示：請將上方內容複製到 Notion 或 Instagram 發布工具中。")