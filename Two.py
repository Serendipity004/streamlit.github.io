import pandas as pd
import streamlit as st

#添加标题
st.title('长三角PM2.5监测数据')

#读取csv数据以dataframe显示
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,encoding="utf8")

#创建expander容器
with st.expander("显示原始数据"):
    st.dataframe(df)
    
#以地图显示
df1 = pd.read_csv(url_data,usecols=["经度","纬度"],encoding="utf8")
df1["lon"] = df1["经度"]
df1["lat"] = df1["纬度"]
#st.map(df1)

#创建表单
with st.form("my_form"):
    st.title("基于属性表达式查询记录")

#两个selectbox
#第一个“选择一个字段”
    names1 = list(["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"])
    name1 = st.selectbox('选择一个字段',names1)
    
#第二个“选择一个关系”
    names2 = list(['>','<'])
    name2 = st.selectbox('选择一个字段',names2)
    
#一个Text_input
    txt = st.text_input('输入一个值',value="",type="default")#type为缺省
    
#一个表单提交按钮form_submit_button
    submit_button = st.form_submit_button('提交')

    if submit_button:
        column_name = df.columns[df.columns.str.contains(name1)][0]
        if name2 == "<":
            condition = df[column_name] < float(txt)
        elif name2 == ">":
            condition = df[column_name] > float(txt)
        else:
            raise ValueError("Invalid relational operator")
        filtered_df = df[condition]
        st.header("共有{}条记录".format(df.shape[0]))
        st.dataframe(filtered_df)
        
        df1 = filtered_df[['经度', '纬度']]  # 选择经度和纬度列
        df1["lon"] = df1["经度"]
        df1["lat"] = df1["纬度"]
        st.map(df1)
