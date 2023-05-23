# Python FLASKでウェブアプリを作る。（原題：Python and Flask Bootcamp: Create Websites using Flask!）

https://www.udemy.com/share/106pIg3@gVtFNucfZYKdqt7Ic-NVROJVk8Ls4I-eAT99nJ5_zjQR7BlJt3D-VkIrxkr6Ea8fUQ==/

Joseさんの講座でPythonとFlaskを使ってウェブアプリを作成します。

Flaskについては[公式サイト](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/)を確認してください。

## Pythonの環境構築

私はpyenvとvirtualenvを組み合わせて使っていますが、各自使っているPythonの環境で結構です。

```sh
brew install pyenv
brew install pyenv-virtualenv
```

pyenvで最新バージョンのPythonをインストールします。
pyenv install -lでインストールできるPythonのリストが表示されます。
私は現時点の最新である3.11.3をインストールしました。

```sh
# インストールできるPythonのリストを確認
pyenv install -l

# pythonをインストールする。
pyenv install 3.11.3

# インストールしたPythonのバージョンを確認
pyenv versions

# virtualenvを生成
pyenv virtualenv 3.11.3 flask_examples
```

プロジェクトのRootディレクトリーを生成して使いたいPythonを指定します。

```sh
mkdir flask_examples
cd flask_examples
pyenv local
```

これでこのプロジェクトに入ると自動でPython 3.11.3の仮装環境が用意されました。

## プロジェクトの生成及びスタート

```sh
cd flask_examples
pip install -r requirements.txt
```

migrationsフォルダの生成などmigrationの下準備

```sh
flask db init
```

Databaseマイグレーションファイルを生成します。
migrateを実行する前にmodelが用意されていること。
メッセージの入力は必須ではないが、gitみたいにマイグレーションの履歴を確認するためにメッセージも入力します。

```sh
flask db migrate -m "Create puppies table"
```

Databaseマイグレーションを行います。

```sh
flask db upgrade
```

Databaseマイグレーション履歴を確認します。

```sh
flask db history
```

seedデータを入力します。

```sh
flask seed run
```

## サーバーの確認

講座では各セクション毎に別途のプロジェクトを生成して進んでいましたが、blueprintで一つのプロジェクトにまとめています。
講座が古いので、ライブラリーのバージョンもできるだけ最新のものを使いました。
flask-seederというライブラリーを設置して使っていますが、講座では紹介されておりません。
またdotenvというライブラリーを設置して環境変数をまとめて保存してgitのバージョン管理対象外にしました。

サーバーを起動する前に.envファイルを作成します。

```sh:.env
FLASK_APP=apps.app:create_app('local')
FLASK_DEBUG=1
FLASK_RUN_PORT=8000

# database
USERNAME=root
PASSWORD=
HOSTNAME=localhost
DATABASE=flask_example

# oauth
OAUTHLIB_INSECURE_TRANSPORT='1'
OAUTHLIB_RELAX_TOKEN_SCOPE='1'
OAUTH_GOOGLE_CLIENT_ID='<google_client_id>'
OAUTH_GOOGLE_CLIENT_SECRET='<google_client_secret>'

# stripe
STRIPE_PUBLISHABLE_KEY='<stripe_publishable_key>'
STRIPE_SECRET_KEY='<stripe_secret_key>'
```

flaskで使っているポート番号はデフォルトで5000ですが、最新のmacですとmacのアプリで5000ポートを使うケースがあるので、8000に変更しました。
googleとstipeについて個人アカウントで発行したキーが必要になります。

```sh
flask run
```

http://127.0.0.1:8000/
