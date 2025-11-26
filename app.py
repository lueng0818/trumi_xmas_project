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

# --- 自定義 CSS 樣式 ---
# 這裡打造聖誕與高級感的視覺風格 (深紅、金色、奶油色調)
st.markdown("""
    <style>
        /* 全局字體與背景 */
        .stApp {
            background-color: #FDFBF7; /* 溫暖的奶油米色背景 */
            color: #3E2723; /* 深咖啡色文字 */
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        /* 主標題樣式 */
        .main-title {
            font-size: 2.8rem !important;
            font-weight: 700;
            color: #8E2121; /* 聖誕深紅色 */
            text-align: center;
            line-height: 1.3;
            margin-bottom: 1rem;
        }
        
        /* 副標題樣式 */
        .sub-title {
            font-size: 1.3rem !important;
            font-weight: 400;
            color: #5D4037;
            text-align: center;
            margin-bottom: 2.5rem;
        }
        
        /* 強調文字 (金色) */
        .gold-highlight {
            color: #B8860B; /* 金色 */
            font-weight: bold;
        }
        
        /* 章節標題樣式 */
        h2 {
            color: #8E2121 !important;
            border-bottom: 2px solid #D4AF37; /* 金色底線 */
            padding-bottom: 10px;
            margin-top: 3rem !important;
        }
        
        /* CTA 按鈕樣式優化 (Streamlit原生按鈕限制較多，這邊用CSS輔助視覺) */
        .stButton button {
            background-color: #8E2121 !important;
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
           background-color: #A52A2A !important;
           transform: translateY(-2px);
        }
        
        /* 資訊方塊樣式 */
        div[data-testid="stMetricValue"] {
            font-size: 1.4rem !important;
            color: #8E2121 !important;
        }
        
        /* 列表樣式調整 */
        ul {
            list-style-type: none; /* 移除預設圓點 */
            padding-left: 0;
        }
        li {
            margin-bottom: 1.2rem;
            padding-left: 1.5rem;
            text-indent: -1.5rem;
        }
        li:before {
            content: "✨"; /* 使用星星代替圓點 */
            padding-right: 10px;
            color: #B8860B;
        }
    </style>
""", unsafe_allow_html=True)

# --- 變數設定 (請在此替換實際資訊) ---
# 注意：連結現在應該指向您的「預約諮詢系統」（例如 Calendly, Google 表單, 或 Line 官方帳號連結）
CTA_LINK = "https://your-consultation-booking-link.com" # [請替換您的實際諮詢預約連結]

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
    <div style="text-align: center; font-size: 1.1rem; line-height: 1.8; margin: 2rem 0; padding: 1.5rem; background-color: #F8F0E3; border-radius: 15px;">
    妳是否也厭倦了每年聖誕節，尋找一份「有意義」的禮物？<br>
    Tru-Mi 相信，最珍貴的愛，值得最久的時間淬鍊。<br>
    今年聖誕，我們送出的不是冰冷的成品，而是一份<br>
    <strong style="font-size: 1.3rem; color: #8E2121;">「共同創作的永恆承諾」</strong>。
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
    # 這裡使用外部 icon連結
    st.image("https://img.icons8.com/ios/50/8E2121/gift-box.png", width=40)

with col2:
    st.markdown("""
    <ul>
        <li><strong>Jessica 的親筆歡迎信</strong><br>來自妳（珠寶故事收藏家）的問候，賦予禮物情感溫度。</li>
        <li><strong>預約啟動 QR Code</strong><br>導向專屬預約系統，讓收禮人隨時啟動她的旅程，無時間壓力。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios/50/8E2121/qr-code--v1.png", width=40)

st.markdown("---")

# ==========================================
# Section III. 購買前的兩大焦慮與保證 (Handling Objections)
# ==========================================
st.header("III. 購買前的兩大焦慮與保證")
st.write("我們知道，送一份特別的禮物，妳心裡總有一些擔心。Tru-Mi 為妳解決痛點：")

st.markdown("") # 空行間距

col_ob1, col_ob2 = st.columns(2)

with col_ob1:
    with st.container(border=True):
        st.markdown("#### 😟 焦慮 1：怕買錯 / 不合她意")
        st.metric(label="Tru-Mi 的承諾", value="零風險承諾")
        st.markdown("""
        這份禮物是**「讓她 100% 滿意」**的承諾。<br>
        妳送的是「決定權」與「共同設計」，妳不會買錯！
        <br><br>
        <span class="gold-highlight">💡 策略關鍵：送的是體驗，不是物品。</span>
        """, unsafe_allow_html=True)

with col_ob2:
    with st.container(border=True):
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

# --- 改用「諮詢引導」取代「價格顯示」 ---
st.markdown("""
    <div style="text-align: center; padding: 30px 20px; background-color: #FDF3F3; border-radius: 15px; margin-bottom: 30px;">
        <h3 style="margin-top:0; color: #8E2121;">💎 每一份愛，都值得專屬對待</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #5D4037;">
            Tru-Mi 深知，您的故事與預算是獨一無二的。<br>
            因此，我們不設定標準定價。
        </p>
        <p style="font-size: 1.2rem; font-weight: bold; color: #B8860B; margin: 20px 0;">
            誠摯邀請您預約一次與設計師 Jessica 的深度諮詢。
        </p>
        <p style="font-size: 1rem; color: #666;">
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
        <h3 style="color: #8E2121;">👉 立即啟動聖誕故事</h3>
        <p>別讓今年的心意，又變成一份普通的禮物。<br>先聊聊，再決定。</p>
    </div>
""", unsafe_allow_html=True)

# 創建一個置中的按鈕容器
col_cta_spacer1, col_cta, col_cta_spacer2 = st.columns([1, 2, 1])

with col_cta:
    # 使用 st.link_button 直接導向外部連結
    # 按鈕文字已更新為「預約諮詢」
    st.link_button(
        label="🎄 預約「專屬方案諮詢」 (開啟故事旅程)",
        url=CTA_LINK,
        type="primary",
        use_container_width=True
    )

# 頁尾
st.markdown("""
    <div style="text-align: center; margin-top: 5rem; font-size: 0.8rem; color: #999;">
        © 2023-2025 Tru-Mi Jewelry. All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
