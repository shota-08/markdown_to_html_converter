import sys
import os
import markdown

def validate_args(args, expected_args):
    """引数の数とファイルの存在を検証"""
    if len(args) != expected_args:
        print(f"Error: {args[1]} コマンドには {expected_args - 1} つの引数が必要です。")
        sys.exit(1)
    if not os.path.exists(args[2]):
        print(f"Error: {args[2]} ファイルが見つかりません。")
        sys.exit(1)

def convert_to_markdown(input_path, output_path):
    """input_pathのファイル内容をhtmlに書き換え、output_pathに出力する"""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()
        html = markdown.markdown(content)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Error: コマンドが指定されていません。")
        print("Usage: file_converter.py markdown <input_path> <output_path>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "markdown":
        validate_args(sys.argv, 4)
        convert_to_markdown(sys.argv[2], sys.argv[3])
    else:
        print(f"Error: {command} というコマンドは存在しません。")
        sys.exit(1)

if __name__ == "__main__":
    main()