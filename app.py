import streamlit as st
import requests
import json

st.title("アンケート")
st.write("以下の項目に答えてください")

with st.form(key="questionnaire"):
    st.header("基本情報")
    name = st.text_input("名前", max_chars=20)
    age = st.number_input("年齢", min_value=0, max_value=120, step=1)
    residence1 = st.text_input("生誕から12歳までの主だった居住地（県レベルまで）")
    residence2 = st.text_input("12歳から現在までの主だった居住地（県レベルまで）")

    st.divider()
    
    st.header("味")
    
    st.subheader("うま味")
    umamiA = st.slider("うま味 A", 0, 100)
    umamiB = st.slider("うま味 B", 0, 100)

    st.subheader("甘味")
    sweetA = st.slider("甘味 A", 0, 100)
    sweetB = st.slider("甘味 B", 0, 100)

    st.subheader("苦味")
    bitterA = st.slider("苦味 A", 0, 100)
    bitterB = st.slider("苦味 B", 0, 100)

    st.subheader("酸味")
    sourA = st.slider("酸味 A", 0, 100)
    sourB = st.slider("酸味 B", 0, 100)

    st.subheader("塩味")
    saltyA = st.slider("塩味 A", 0, 100)
    saltyB = st.slider("塩味 B", 0, 100)

    st.subheader("渋味")
    astringencyA = st.slider("渋味 A", 0, 100)
    astringencyB = st.slider("渋味 B", 0, 100)

    st.divider()

    st.header("食感")

    st.subheader("シャキシャキさ")
    shakishakiA = st.slider("シャキシャキさ A", 0, 100)
    shakishakiB = st.slider("シャキシャキさ B", 0, 100)

    st.subheader("フワフワさ")
    fuwafuwaA = st.slider("フワフワさ A", 0, 100)
    fuwafuwaB = st.slider("フワフワさ B", 0, 100)

    st.subheader("果皮の硬さ")
    peelfirmnessA = st.slider("果皮の硬さ A", 0, 100)
    peelfirmnessB = st.slider("果皮の硬さ B", 0, 100)

    st.subheader("果肉の硬さ")
    pulpfirmnessA = st.slider("果肉の硬さ A", 0, 100)
    pulpfirmnessB = st.slider("果肉の硬さ B", 0, 100)

    st.divider()

    st.header("食後アンケート")

    allergy = st.text_area("1. 食物アレルギーはありますか。")
    howtoeat = st.text_area("2. 普段どのような方法で食しますか。")
    brand = st.text_area("3. ブランドがあることをしっていますか。知っていればそのブランドをお書きください。")
    comment = st.text_area("4. 自由に感想などをお書きください。")

    data = {
        "name": name,
        "age": age,
        "residence1": residence1,
        "residence2": residence2,
        "umamiA": umamiA,
        "umamiB": umamiB,
        "sweetA": sweetA,
        "sweetB": sweetB,
        "bitterA": bitterA,
        "bitterB": bitterB,
        "sourA": sourA,
        "sourB": sourB,
        "saltyA": saltyA,
        "saltyB": saltyB,
        "astringencyA": astringencyA,
        "astringencyB": astringencyB,
        "shakishakiA": shakishakiA,
        "shakishakiB": shakishakiB,
        "fuwafuwaA": fuwafuwaA,
        "fuwafuwaB": fuwafuwaB,
        "peelfirmnessA": peelfirmnessA,
        "peelfirmnessB": peelfirmnessB,
        "pulpfirmnessA": pulpfirmnessA,
        "pulpfirmnessB": pulpfirmnessB,
        "allergy": allergy,
        "howtoeat": howtoeat,
        "brand": brand,
        "comment": comment,
    }

    submit_button = st.form_submit_button(label="送信")

if submit_button:
    url = "http://127.0.0.1:8000/submit"
    res = requests.post(
        url,
        data=json.dumps(data)
    )
    if res.status_code == 200:
        st.success("送信完了")
        st.json(res.json())
    else:
        st.error("送信失敗")