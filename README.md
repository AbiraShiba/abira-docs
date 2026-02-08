# 自前で環境を作る場合

## 前提

GitHubアカウント

Git（ローカルにインストール済み）

Python 3.11 以上

uv インストール済み

は前提とします。

## Gitの設定

gitをクローンします
```sh
git clone https://XXXXXXXXXXX
cd docs-site
```

## uv による環境設定

プロジェクトを作成
```sh
uv init
uv venv
```

開発依存としてモジュールをダウンロード
```sh
uv add --dev sphinx myst-parser furo sphinx-autobuild
```

# 使用方法

リアルタイムで確認する場合は以下のコマンドを使用して（デフォルト8000ポートで起動）
```sh
uv run sphinx-autobuild docs docs/_build/html
```

# tips

現在の構成をメモしたい場合に便利な ls コマンド
```sh
ls -R docs | head -n 50
```
