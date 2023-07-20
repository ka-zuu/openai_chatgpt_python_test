# OpenAI APIにプロンプトを送信して、結果を取得する。

from dotenv import load_dotenv
import os

import openai
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 会話履歴の初期化
conversation = [
    {"role": "system", "content": "あなたは家庭用のチャットツールに参加します。日常の会話や質問に受け答えをしてください。落ち着きのある丁寧なキャラクターを演じてください。語尾が「プリ」で終わるようにしてください。「だプリ」「だプリね」「するプリ」「プリ？」のような感じです。適度な改行を入れるようにしてください"},
]


def chat_with_gpt3(message, max_tokens=2048):
    # ユーザーの入力を会話履歴に追加
    conversation.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo",
        model="gpt-4",
        messages=conversation[-10:],
        max_tokens=max_tokens,
        temperature=0.8,
    )

    # 返答の内容を取得
    ai_message = response.choices[0].message["content"]

    # AIの返答を会話履歴に追加
    conversation.append({"role": "assistant", "content": ai_message})

    return ai_message


while True:
    message = input("You: ")
    response = chat_with_gpt3(message)
    print("AI: ", response)
