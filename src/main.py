import streamlit as st


def main():
    st.title('Typhoid Fevering Modeling')
    st.markdown(
        'Below is a comprehensive analysis of all the listings currently in Yad2. Enjoy!<br/>'
        f'A total of listings have been analyzed. Last updated on .<br/>'
        'Share [yad2analysis.com](http://yad2analysis.com) with your friends!<br/>'
        'This app was made by [Dan Nissim](https://www.linkedin.com/in/dan-nissim) with data'
        ' from [yad2.co.il](https://yad2.co.il). Feel free to <a href="mailto:nissim.dan@gmail.com">contact me</a>.',
        unsafe_allow_html=True)


if __name__ == '__main__':
    main()
