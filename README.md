# watsonx-orchestrate-sample

このリポジトリは、IBM watsonx Orchestrate を活用したサンプルコードを提供します。  
文章要約エージェントや Gmail 送信ツールなど、Orchestrate の機能を組み合わせた実装例を含んでいます。

詳細な解説は以下の記事をご覧ください：  
👉 [Qiita: watsonx Orchestrate サンプル解説](https://qiita.com/y-oakbe/items/b5eff207dc4ca70189a0)

## ディレクトリ構成

```
/
├── agent
│   └── sentence_summary_agent.yaml  # 文章要約エージェントの定義
├── tool
│   └── send_gmail.py                # Gmail送信ツール
└── README.md
```

## 内容紹介

- **agent/sentence_summary_agent.yaml**  
  watsonx Orchestrate のエージェント定義ファイルです。文章を要約する機能を持っています。

- **tool/send_gmail.py**  
  Python を使って Gmail を送信するツールです。Orchestrate のワークフロー内で利用可能です。
