import streamlit as st
from deep_translator import GoogleTranslator


with st.container():
    st.markdown("<div style='text-align:center'><img src='https://cdn-icons-png.freepik.com/256/3797/3797971.png?ga=GA1.1.1364760796.1729789431&semt=ais_hybrid' width='150'></div>", unsafe_allow_html=True)
    # st.markdown("<h4 style='text-align:center;color:white-blue;font-family:Comic Sans MS'>MY TRANSLATOR</h4>",unsafe_allow_html=True)
def translate():
    st.markdown(f'<h5>Enter text: </h5>',unsafe_allow_html=True)
    text=st.text_area('',placeholder='Type something....')
    options={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 
             'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 
             'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 
             'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 
             'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN',
               'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 
               'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch':
                 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 
                 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 
                 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 
                 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha',
                   'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 
                   'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 
                   'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 
                   'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 
                   'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri',
                     'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 
                     'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
                       'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 
                       'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai',
                       'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt',
                         'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei',
                           'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne',
                             'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om',
                               'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 
                               'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 
                               'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 
                               'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 
                               'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 
                               'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
                                 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 
                                 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th',
                                   'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 
                                   'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 
                                   'uzbek': 'uz', 'vietnamese': 'vi',
              'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    st.markdown(f'<h5>Language: </h5>',unsafe_allow_html=True)
    lang=st.selectbox('',options)
    if text and lang:
        output=GoogleTranslator(source='auto',target=lang).translate(text)
    if st.button('Translate'):
        st.title(output)
    else:
        st.error('Enter details..')
translate()