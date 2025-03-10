# 📄 ファイル変換スクリプト (File Converter Script)

## 📖 概要
- このPythonスクリプトは、MarkdownファイルをHTMLに変換するツールです。
- コマンドラインから簡単にMarkdownをHTML形式に変換できます。

## 🚀 使い方
このスクリプトは以下の形式で使用します。

```
python file_converter.py markdown <input_file> <output_file>
```

### MarkdownをHTMLに変換する
example.md の内容をHTMLに変換し、example.html に出力します。
```
python file_converter.py markdown example.md example.html
```

## 🛠 コードの説明
### 1. validate_args(args, expected_args)
コマンドの引数が正しいかチェック。
指定したMarkdownファイルが存在するか検証。

### 2. convert_to_markdown(input_path, output_path)
input_path のMarkdownをHTMLに変換し、output_path に保存。

### 3. main()
コマンドを解析し、markdown コマンドなら変換処理を実行。


