import streamlit as st
import requests
from api_client import signup, login, get_notes, create_note, delete_note

st.set_page_config(page_title="Personal Note App", page_icon="📝")

# Khởi tạo Session State
if "user" not in st.session_state:
    st.session_state.user = None
if "notes" not in st.session_state:
    st.session_state.notes = []
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
if "show_login" not in st.session_state:
    st.session_state.show_login = True

def load_notes():
    if not st.session_state.user:
        return
    try:
        st.session_state.notes = get_notes(st.session_state.user["idToken"])
    except Exception as e:
        st.error(f"Lỗi tải ghi chú: {e}")

def login_form():
    st.subheader("Đăng nhập")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")
        goto_signup = st.form_submit_button("Chưa có tài khoản? Đăng ký ngay")
        
    if goto_signup:
        st.session_state.show_signup = True
        st.session_state.show_login = False
        st.rerun()
        
    if submitted:
        try:
            user = login(email, password)
            st.session_state.user = user
            load_notes()
            st.success("Đăng nhập thành công")
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng nhập thất bại: Tài khoản hoặc mật khẩu không đúng.")
        except Exception as e:
            st.error(f"Lỗi: {e}")

def signup_form():
    st.subheader("Đăng ký")
    with st.form("signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Tạo tài khoản")
        goto_login = st.form_submit_button("Đã có tài khoản? Đăng nhập")
        
    if goto_login:
        st.session_state.show_signup = False
        st.session_state.show_login = True
        st.rerun()
        
    if submitted:
        try:
            signup(email, password)
            st.success("Tạo tài khoản thành công, hãy đăng nhập")
            st.session_state.show_signup = False
            st.session_state.show_login = True
            st.rerun()
        except requests.HTTPError as e:
            st.error(f"Đăng ký thất bại, email có thể đã tồn tại.")

# Giao diện chính
st.title("📝 Sổ Ghi Chú Cá Nhân")

if st.session_state.user:
    st.success(f"Đang đăng nhập: {st.session_state.user['email']}")
    if st.button("Đăng xuất"):
        st.session_state.user = None
        st.session_state.notes = []
        st.rerun()
        
    st.divider()
    
    # Form tạo ghi chú mới
    st.subheader("Thêm ghi chú mới")
    new_note = st.text_area("Nội dung ghi chú", height=100)
    if st.button("Lưu ghi chú", type="primary"):
        if new_note.strip():
            try:
                create_note(st.session_state.user["idToken"], new_note)
                st.success("Đã lưu!")
                load_notes() # Tải lại danh sách
                st.rerun()
            except Exception as e:
                st.error(f"Lỗi khi lưu: {e}")
        else:
            st.warning("Vui lòng nhập nội dung ghi chú!")
            
    st.divider()
    
    # Hiển thị danh sách ghi chú
    st.subheader("Danh sách ghi chú của bạn")
    if not st.session_state.notes:
        st.info("Bạn chưa có ghi chú nào. Hãy thêm ghi chú đầu tiên ở trên!")
    else:
        for note in st.session_state.notes:
            with st.container(border=True):
                # Chia làm 2 cột: cột 1 rộng 85% chứa text, cột 2 rộng 15% chứa nút xóa
                col1, col2 = st.columns([0.85, 0.15])
                
                with col1:
                    st.caption(f"🕒 {note['timestamp']}")
                    st.write(note['content'])
                    
                with col2:
                    # Nút Xóa cần có key duy nhất (dùng ID của note) để Streamlit không bị lỗi trùng lặp
                    if st.button("🗑️ Xóa", key=f"del_{note['id']}", type="secondary"):
                        try:
                            delete_note(st.session_state.user["idToken"], note["id"])
                            st.success("Đã xóa ghi chú!")
                            load_notes() # Tải lại danh sách sau khi xóa
                            st.rerun()   # Làm mới giao diện
                        except Exception as e:
                            st.error(f"Lỗi khi xóa: {e}")

else:
    if st.session_state.show_signup:
        signup_form()
    else:
        login_form()