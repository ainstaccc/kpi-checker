import streamlit as st
import pandas as pd

# 模擬資料
data = {
    "員工編號": ["21000452", "24000861", "23000795", "23000759", "23000680"],
    "姓名": ["施佩真", "黃耀樟", "傅巧竺", "黃鈺", "謝雅林"],
    "店櫃名稱": ["ALL WEARS台中新時代", "ALL WEARS高雄夢時代", "ALL WEARS台中大遠百", "ALL WEARS新北中和環球", "ALL WEARS台北京站"],
    "考核月份": ["2025/06"] * 5,
    "考核分數": [30, 30, 29, 27, 30],
    "評等": ["A+", "A+", "A+", "A", "A+"],
    "備註": ["", "", "", "", ""]
}
df = pd.DataFrame(data)

# 查詢介面
st.title("📋 月考核查詢平台")
st.markdown("請輸入下列資訊查詢考核成績：")

emp_id = st.text_input("🔢 員工編號（必填）")
emp_name = st.text_input("👤 姓名（選填）")
month = st.selectbox("📅 查詢月份", sorted(df["考核月份"].unique(), reverse=True))

if st.button("🔍 查詢"):
    if not emp_id:
        st.warning("請輸入員工編號")
    else:
        result = df[(df["員工編號"] == emp_id) & (df["考核月份"] == month)]
        if emp_name:
            result = result[result["姓名"] == emp_name]

        if result.empty:
            st.error("查無資料，請確認輸入資訊是否正確")
        else:
            st.success("✅ 查詢成功！以下是考核結果：")
            st.table(result[["員工編號", "姓名", "店櫃名稱", "考核月份", "考核分數", "評等", "備註"]])