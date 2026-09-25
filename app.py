import streamlit as st
from password_analyzer import analyze_password, generate_password
from database import init_db, hash_password, password_was_used

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered",
)

init_db()

st.title("🔐 Password Strength Analyzer")
st.write("Check password length, entropy, complexity, and common-password usage.")

tab1, tab2 = st.tabs(["Password Checker", "Password Generator"])

with tab1:
    password = st.text_input(
        "Enter password",
        type="password",
        placeholder="Enter your password..."
    )

    if password:
        result = analyze_password(password)

        st.subheader("Password Analysis")

        col1, col2, col3 = st.columns(3)
        col1.metric("Length", result["length"])
        col2.metric("Entropy", f"{result['entropy']:.2f} bits")
        col3.metric("Score", f"{result['score']}/100")

        if result["verdict"] == "Weak":
            st.error(f"Verdict: {result['verdict']}")
        elif result["verdict"] == "Moderate":
            st.warning(f"Verdict: {result['verdict']}")
        elif result["verdict"] == "Strong":
            st.info(f"Verdict: {result['verdict']}")
        else:
            st.success(f"Verdict: {result['verdict']}")

        st.progress(result["score"] / 100)

        st.subheader("Checks")
        checks = {
            "Lowercase letter": any(c.islower() for c in password),
            "Uppercase letter": any(c.isupper() for c in password),
            "Number": any(c.isdigit() for c in password),
            "Special character": any(c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in password),
            "At least 8 characters": len(password) >= 8,
            "Not a common password": not result["is_common"],
        }

        for name, passed in checks.items():
            st.write(("✅ " if passed else "❌ ") + name)

        if result["suggestions"]:
            st.subheader("Suggestions")
            for suggestion in result["suggestions"]:
                st.warning(suggestion)

        if password_was_used(password):
            st.error("This password was found in this application's local password history.")
        else:
            st.success("This password was not found in the local password history.")

        if st.button("Add password to demo history"):
            hash_password(password)
            st.success("Only the bcrypt hash was stored; the plaintext password was not stored.")

with tab2:
    st.subheader("Generate a Strong Password")
    length = st.slider("Password length", 12, 40, 20)

    if st.button("Generate Password"):
        st.session_state["generated_password"] = generate_password(length)

    if "generated_password" in st.session_state:
        st.code(st.session_state["generated_password"])
        st.caption("Store generated passwords in a password manager.")

st.divider()
st.caption("Tutorial-inspired implementation + automated pytest testing")
