import sqlglot
import streamlit as st
from streamlit_ace import st_ace

all_dialects = sorted(d.value for d in iter(sqlglot.Dialects) if d.value)

left, right = st.columns(2)
input_lng = left.selectbox("Input language",  all_dialects)
output_lng = right.selectbox("Output language",  all_dialects)
pretty = st.checkbox("Pretty format")
input_sqls = st_ace(language="sql")

if input_sqls:
    try:
        output_sqls = sqlglot.transpile(input_sqls, read=input_lng, write=output_lng, pretty=pretty)
        for output_sql in output_sqls:
            st.code(output_sql, language="sql")
    except sqlglot.errors.ParseError as e:
        st.write("**Transpilation errors:**")
        st.table(e.errors)