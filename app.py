import streamlit as st
from PIL import Image
import os

# --- 頁面設定 ---
st.set_page_config(
    page_title="Tru-Mi 聖誕企劃 | 故事淬鍊邀請函",
    page_icon="🎁",
    layout="centered", # 使用置中布局聚焦內容
    initial_sidebar_state="collapsed"
)

# --- 自定義 CSS 樣式 (配色更新為 Tru-Mi 品牌色) ---
st.markdown("""
    <style>
        /* 全局字體與背景 */
        .stApp {
            background-color: #FDFBF7; /* 品牌米奶油色背景 */
            color: #333333; /* 深炭灰色文字，取代原本的深咖啡色 */
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* 主標題樣式 */
        .main-title {
            font-size: 2.8rem !important;
            font-weight: 700;
            color: #00563F; /* Tru-Mi 深祖母綠 */
            text-align: center;
            line-height: 1.3;
            margin-bottom: 1rem;
        }
        
        /* 副標題樣式 */
        .sub-title {
            font-size: 1.3rem !important;
            font-weight: 400;
            color: #555555; /* 中灰色 */
            text-align: center;
            margin-bottom: 2.5rem;
        }
        
        /* 強調文字 (品牌金) */
        .gold-highlight {
            color: #C99E10; /* Tru-Mi 品牌金 */
            font-weight: bold;
        }
        
        /* 章節標題樣式 */
        h2 {
            color: #00563F !important; /* Tru-Mi 深祖母綠 */
            border-bottom: 2px solid #C99E10; /* 品牌金底線 */
            padding-bottom: 10px;
            margin-top: 3rem !important;
        }
        
        /* CTA 按鈕樣式優化 */
        .stButton button {
            background-color: #00563F !important; /* Tru-Mi 深祖母綠 */
            color: white !important;
            font-size: 1.2rem !important;
            font-weight: bold !important;
            padding: 0.8rem 2rem !important;
            border-radius: 30px !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
        .stButton button:hover {
           background-color: #003A2B !important; /* 按鈕懸停時的深綠色 */
           transform: translateY(-2px);
        }
        
        /* 資訊方塊樣式 (Metric) */
        div[data-testid="stMetricValue"] {
            font-size: 1.4rem !important;
            color: #00563F !important; /* Tru-Mi 深祖母綠 */
        }
        
        /* 列表樣式調整 */
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin-bottom: 1.2rem;
            padding-left: 1.5rem;
            text-indent: -1.5rem;
        }
        li:before {
            content: "✨";
            padding-right: 10px;
            color: #C99E10; /* 品牌金圖示 */
        }

        /* 引言與諮詢區塊背景色微調 */
        .quote-box, .consultation-box {
            background-color: #F2F7F4; /* 極淺的綠色調背景，呼應品牌 */
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            line-height: 1.8;
            margin: 2rem 0;
        }
        .consultation-box h3 {
            color: #00563F; /* 深祖母綠標題 */
        }

    </style>
""", unsafe_allow_html=True)

# --- 變數設定 ---
# 更新 Line@ 連結為新的 ID
CTA_LINK = "https://line.me/R/ti/p/@3303nksbt"

# --- 頁面內容開始 ---

# ==========================================
# Section I. 頂部主標與核心價值 (Hook & Value)
# ==========================================
st.markdown('<div class="main-title">🎯 別再送「商品」了。<br>送一份「永恆的故事」</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">妳的愛情，值得一份不會錯過、也不會被遺忘的禮物。<br>視覺重點：妳精心準備的<span class="gold-highlight">【故事淬鍊邀請函】</span>實體珍藏盒。</div>', unsafe_allow_html=True)

# 置放產品主圖的區域
hero_image_path = "hero_image.jpg" # 請確保目錄下有這張圖片
if os.path.exists(hero_image_path):
    st.image(hero_image_path, use_column_width=True, caption="Tru-Mi 聖誕限定：故事淬鍊邀請函珍藏禮盒")
else:
    # 如果沒有圖片的替代顯示方案
    st.info("（請確認 hero_image.jpg 已放入專案資料夾中）", icon="📸")
    st.markdown("---")


# 引言段落
st.markdown("""
    <div class="quote-box" style="font-size: 1.1rem;">
    妳是否也厭倦了每年聖誕節，尋找一份「有意義」的禮物？<br>
    Tru-Mi 相信，最珍貴的愛，值得最久的時間淬鍊。<br>
    今年聖誕，我們送出的不是冰冷的成品，而是一份<br>
    <strong style="font-size: 1.3rem; color: #00563F;">「共同創作的永恆承諾」</strong>。
    </div>
""", unsafe_allow_html=True)


# ==========================================
# Section II. 禮物內容與儀式感 (Product Reframed)
# ==========================================
st.header("II. 禮物內容與儀式感")
st.subheader("🎁 妳在 12/25 當天送出的是：【故事淬鍊邀請函】")
st.write("這份禮盒，是開啟一段珍貴旅程的實體憑證與專屬儀式：")

st.markdown("") # 空行間距

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <ul>
        <li><strong>獨家珍藏禮盒</strong><br>一個重磅、高質感、可長久珍藏的 keepsake box。</li>
        <li><strong>故事收藏憑證卡</strong><br>妳為摯愛預定一趟 [60-90分鐘] 深度故事諮詢的證明。</li>
    </ul>
    """, unsafe_allow_html=True)
    # 這裡使用外部 icon連結 (顏色已替換為品牌綠)
    st.image("https://img.icons8.com/ios/50/00563F/gift-box.png", width=40)

with col2:
    # 修正：確保 <ul> 標籤正確包覆所有 <li> 項目並在結束時關閉
    st.markdown("""
    <ul>
        <li><strong>Jessica 的親筆歡迎信</strong><br>來自妳（珠寶故事收藏家）的問候，賦予禮物情感溫度。</li>
        <li><strong>預約啟動 QR Code</strong><br>導向專屬預約系統，讓收禮人隨時啟動她的旅程，無時間壓力。</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # --- QR Code 圖片顯示邏輯 ---
    # 這部分程式碼應該在 st.markdown 結束後執行，確保圖片顯示在文字列表下方
    qr_code_path = "qr_code.png" # 請確保目錄下有這張圖片
    if os.path.exists(qr_code_path):
        # 顯示 QR Code，寬度設為 120px 以便掃描
        # 加入一個小的上邊距，讓圖片與文字保持距離
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        st.image(qr_code_path, width=120, caption="掃描加入 Tru-Mi Line@ 預約")
    else:
        # 如果沒有圖片的替代顯示方案
        st.info("（請確認 qr_code.png 已放入專案資料夾中）", icon="📱")


st.markdown("---")

# ==========================================
# Section III. 購買前的兩大焦慮與保證 (Handling Objections)
# ==========================================
st.header("III. 購買前的兩大焦慮與保證")
st.write("我們知道，送一份特別的禮物，妳心裡總有一些擔心。Tru-Mi 為妳解決痛點：")

st.markdown("") # 空行間距

col_ob1, col_ob2 = st.columns(2)

with col_ob1:
    # 移除 st.container(border=True) 以避免舊版 Streamlit 報錯
    with st.container():
        st.markdown("#### 😟 焦慮 1：怕買錯 / 不合她意")
        st.metric(label="Tru-Mi 的承諾", value="零風險承諾")
        st.markdown("""
        這份禮物是**「讓她 100% 滿意」**的承諾。<br>
        妳送的是「決定權」與「共同設計」，妳不會買錯！
        <br><br>
        <span class="gold-highlight">💡 策略關鍵：送的是體驗，不是物品。</span>
        """, unsafe_allow_html=True)

with col_ob2:
    # 移除 st.container(border=True) 以避免舊版 Streamlit 報錯
    with st.container():
        st.markdown("#### 😟 焦慮 2：萬一她很忙 / 怕拖太久")
        st.metric(label="Tru-Mi 的承諾", value="無限期承諾")
        st.markdown("""
        **憑證無使用期限**。<br>
        收禮人可以在她/他最放鬆、最有靈感的時候，隨時向妳兌現這個禮物。
        <br><br>
        <span class="gold-highlight">💡 策略關鍵：給予「時間自由」(Marry 最看重的價值)。</span>
        """, unsafe_allow_html=True)


# ==========================================
# Section V. 預約諮詢與行動呼籲 (Consultation & CTA)
# ==========================================
st.header("V. 預約諮詢與行動呼籲")

# --- 諮詢引導區塊 ---
st.markdown("""
    <div class="consultation-box">
        <h3 style="margin-top:0;">💎 每一份愛，都值得專屬對待</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #555555;">
            Tru-Mi 深知，您的故事與預算是獨一無二的。<br>
            因此，我們不設定標準定價。
        </p>
        <p style="font-size: 1.2rem; font-weight: bold; color: #C99E10; margin: 20px 0;">
            誠摯邀請您預約一次與設計師 Jessica 的深度諮詢。
        </p>
        <p style="font-size: 1rem; color: #666666;">
            讓我們透過對話，了解您的需求，<br>為您量身打造最適合的「故事淬鍊」方案。
        </p>
    </div>
""", unsafe_allow_html=True)

# 期限與重要提醒區塊
col_alert1, col_alert2 = st.columns(2)
with col_alert1:
    st.error("⏰ **聖誕限定：最後收單日**\n\n**2025 年 12 月 25 日**\n\n(為了確保聖誕節前拿到禮盒，請盡早預約諮詢)")

with col_alert2:
    st.warning("⚠️ **重要提醒**\n\n禮盒保證於 12/24 前寄達。\n\n最終首飾將於收禮人確認設計後 **4-12 週**交付。")

st.markdown("") # 空行間距

# 最終 CTA 區塊
st.markdown("""
    <div style="text-align: center; margin-top: 3rem;">
        <h3 style="color: #00563F;">👉 立即啟動聖誕故事</h3>
        <p>別讓今年的心意，又變成一份普通的禮物。<br>先聊聊，再決定。</p>
    </div>
""", unsafe_allow_html=True)

# 創建一個置中的按鈕容器
col_cta_spacer1, col_cta, col_cta_spacer2 = st.columns([1, 2, 1])

with col_cta:
    # 使用 st.link_button 直接導向外部連結
    # 連結已更新為新的 Line@ ID
    st.link_button(
        label="🎄 預約「專屬方案諮詢」 (開啟故事旅程)",
        url=CTA_LINK,
        type="primary",
        use_container_width=True
    )

# 頁尾
st.markdown("""
    <div style="text-align: center; margin-top: 5rem; font-size: 0.8rem; color: #999999;">
        © 2023-2025 Tru-Mi Jewelry. All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
