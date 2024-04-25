# 以下を「app.py」に書き込み

import os
from google.cloud import texttospeech

import io
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'onseigousei_secret.json'

def synthesize_speech(text, lang='日本語', gender='defalut'):
    gender_type = {
        'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP'
    }

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

st.title('専門基礎1学期パーフェクト アプリ2024')

st.markdown('#### 適する用語プルダウンからを選んでください。')


input_option = st.selectbox(
    '問1　無人であり、遠隔操作または自動操縦で飛行できる、200g以上の重量の機体',
    ('選んでください', 'AI', 'ドローン', '自動運転技術','ビッグデータ',)
)
input_data = None
if input_option == 'ドローン':
    st.write('正解です。音声で確認してください。')
    input_data = '無人であり、遠隔操作または自動操縦で飛行できる、200g以上の重量の機体は、ドローンです。'
    if st.button('音声開始1'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')



input_option = st.selectbox(
    '問2　人間のように知的な振る舞いをするコンピューター',
    ('選んでください','AI', 'ドローン', '自動運転技術','ビッグデータ',)
)
input_data = None
if input_option == 'AI':
    st.write('正解です。音声で確認してください。')
    input_data = '人間のように知的な振る舞いをするコンピューターのことをAIと言います。'
    if st.button('音声開始2'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')



input_option = st.selectbox(
    '問3　人間では全体を把握することが困難な巨大なデータ群のこと',
    ('選んでください','AI', 'ドローン', '自動運転技術','ビッグデータ',)
)
input_data = None
if input_option == 'ビッグデータ':
    st.write('正解です。音声で確認してください。')
    input_data = '人間では全体を把握することが困難な巨大なデータ群のことをビッグデータと言います。'
    if st.button('音声開始3'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問4　ドライバーが行っている、認知、判断、運転操作といった行為を、人間の代わりに機械が行うもの',
    ('選んでください','AI', 'ドローン', '自動運転技術','ビッグデータ',)
)
input_data = None

if input_option == '自動運転技術':
    st.write('正解です。音声で確認してください。')
    input_data = 'ドライバーがおこなっている、認知、判断、運転操作といった行為を、人間の代わりに機械が行うものを自動運転技術と言います。'
    if st.button('音声開始4'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問5　日本の人口は、何年から減少に変化しましたか？',
    ('選んでください','2000年', '2004年', '2008年','2012年','2016年')
)
input_data = None

if input_option == '2008年':
    st.write('正解です。音声で確認してください。')
    input_data = '日本の人口は、2008年から減少に変化しました。'
    if st.button('音声開始5'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問6　2015年の日本の人口は、およそ何人？',
    ('選んでください','1億1千700万人', '1億2千700万人', '1億3千700万人','1億4千700万人')
)
input_data = None

if input_option == '1億2千700万人':
    st.write('正解です。音声で確認してください。')
    input_data = '2015年の日本の人口は、およそ1億2千700万人です。'
    if st.button('音声開始6'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問7　高速で安定した第5世代通信システムのことを何というか？',
    ('選んでください','3G', '3.5G', '4G','5G')

input_data = None

if input_option == '5G':
    st.write('正解です。音声で確認してください。')
    input_data = '高速で安定した第5世代通信システムのことを5Gといいます。'
    if st.button('音声開始7'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問8　事故の発生についての経験則で、1件の重大事故の背後には、\
    重大事故に至らなかった29件の軽微な事故が隠れており、\
    さらにその背後には事故寸前だった300件の異常、\
    いわゆるヒヤリハットが隠れているというものを現す法則を何というか？',
    ('選んでください','ハイブリットの法則', 'ニュートンの法則', 'ハインリッヒの法則','ヒトラーの法則')
)
input_data = None

if input_option == 'ハインリッヒの法則':
    st.write('正解です。音声で確認してください。')
    input_data = 'ハインリッヒの法則とは、事故の発生についての経験則で、1件の重大事故の背後には、\
    重大事故に至らなかった29件の軽微な事故が隠れており、\
    さらにその背後には事故寸前だった300件の異常、\
    いわゆるヒヤリハットが隠れているという法則を言います。'
    if st.button('音声開始8'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問9　製造現場での職場環境改善のための活動である５Sとは、整理、整頓、清掃、しつけともう一つは何？',
    ('選んでください','純愛', '潔白', '正直','清潔')
)
input_data = None

if input_option == '清潔':
    st.write('正解です。音声で確認してください。')
    input_data = '製造現場での職場環境改善のための活動である５Sとは、不要なものを処分する整理、\
    必要なものを使いやすい場所に置く整頓、きれいに掃除して点検を行う清掃、清潔な状態を維持する清潔、\
    4つのSを習慣づけるしつけです。'
    if st.button('音声開始9'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
else :
    st.write('不正解です。見直してください。')
st.write('')


input_option = st.selectbox(
    '問10　2020年の日本の産業別の就業者数割合において、第3次産業はおよそ何％か？',
    ('選んでください','3.2%', '23.4%', '63.8%','73.4%')
)
input_data = None

if input_option == '73.4%':
    st.write('正解です。音声で確認してください。')
    input_data = '2020年の日本の産業別の就業者数割合は、農業、林業、漁業の第１次産業はおよそ3.2％。\
    また、鉱業、採石業、建設業、製造業の第２次産業はおよそ23.4％。\
    そして電気、運輸、情報、サービスの第３次産業はおよそ73.4％です。'
    if st.button('音声開始10'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
        st.write('')
        st.markdown('### お疲れ様でした。')
else :
   st.write('不正解です。見直してください。')

st.write('')

st.write('次の文章の（　　）に適する用語を選びなさい')
input_option = st.selectbox(
    '問11　機械の（　　　）の異常に気づいたら、直ちに機械を停止する',
    ('選んでください','感電', '素手', '運転音','排気', '引火性', '火気')
)
input_data = None

if input_option == '運転音':
    st.write('正解です。')
else :
   st.write('不正解です。見直してください。')


st.write('')


input_option = st.selectbox(
    '問12　（　　）、発火性のある薬品や溶剤、塗料などを使用するときは、火気に気をつける。',
    ('選んでください','感電', '素手', '運転音','排気', '引火性', '火気')
)
input_data = None

if input_option == '引火性':
    st.write('正解です')
else :
   st.write('不正解です。見直してください。')


st.write('')


input_option = st.selectbox(
    '問13　刺激臭のガスを発生する物質を取り扱う場合は、（　　）を十分に行う。',
    ('選んでください','感電', '素手', '運転音','排気', '引火性', '火気')
)
input_data = None

if input_option == '排気':
    st.write('正解です。')
else :
   st.write('不正解です。見直してください。')


st.write('')


input_option = st.selectbox(
    '問14　ぬれた手などで、電源スイッチなどに触れると、（　　）の恐れがある。\
    実習中は、電流が流れているかどうかを常に確認してから機器を取り扱う。',
    ('選んでください','感電', '素手', '運転音','排気', '引火性', '火気')
)
input_data = None

if input_option == '感電':
    st.write('正解です。')
else :
   st.write('不正解です。見直してください。')


st.write('')


input_option = st.selectbox(
    '問15　切りくずを（　　）で払ったりしない。必ず手ぼうきを使用する。',
    ('選んでください','感電', '素手', '運転音','排気', '引火性', '火気')
)
input_data = None

if input_option == '素手':
    st.write('正解です。これまでをの回答を音声で確認してください。')
    input_data = '作業中における安全は、\
    機械の運転音の異常に気付いたら、ただちに機械を停止する。\
　　工具や機械を本来の用途以外に使用しない。\
　　引火性、発火性のある薬品や溶剤、塗料などを使用するときは、火気に気をつける。\
    刺激臭のガスを発生する物質を取り扱う場合は、排気を十分に行う。\
　　使用した廃液や溶剤などは、実習室の流しに流してはいけない。\
    水質汚濁や火災、爆発の原因となるので、決められた回収容器に必ず戻す。\
　　ぬれた手などで、電源スイッチなどに触れると、感電の恐れがある。\
    実習中は、電流が流れているかどうかを常に確認してから機器を取り扱う。\
　　切りくずを素手で払ったりしない。必ず手ぼうきを使用する。'

    if st.button('音声開始15'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang='日本語', gender='defalut')
        st.audio(response.audio_content)
#        comment.write('完了しました')
        st.write('')
        st.markdown('### お疲れ様でした。')
else :
   st.write('不正解です。見直してください。')


st.write('')

st.write('by Teraoka DENSHI')










