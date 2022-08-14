# clip2html
Windows及びLinux向け クリップボード同期センター

## 起動方法
1. `pip3 install -r requirements.txt`などしてモジュールをインストールします。
Linuxの場合、xclipをインストールします。

ディストリビューション|コマンド
---|---
Ubuntu/Debian|`sudo apt install -y xclip` または [こちら](apt:xclip)
Fedora|`sudo dnf install -y xclip`
RedHat/CentOS|`sudo yum install -y xclip`
ArchLinux|`sudo pacman -S xclip`

2. `temp.setting.json`を参考にして、`setting.json`を作成します。
3. `python3 main.py`などして、`main.py`を実行します。
4. `setting.json`で指定したアドレスにアクセスすることでクリップボードを管理できます。

## エンドポイント一覧
- `/post`(Method: POST)
送信された値をサーバーでクリップボードに保存します。
```json
{
    "content":"クリップボードに保存したい内容"
}
```
上記のようなJSONを送信してください。

- `/get`(Method: GET)
クリップボードの内容を取得します。

## 使用例
例えばiOSでは、`ショートカット`アプリの`HTTPの内容を取得`を使うことで、大変便利に使えると思います。
ショートカットを共有シートに表示すれば、共有のところからクリップボードに送れます。
これは便利だぁ...（小並感）

## 最後に
Linuxの方は試していませんが多分動くだろうなっていう希望的観測なので、動かなかったら直してからPRしてくれたらうれしいですうぅう...
