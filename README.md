# Hololive Tool

## 介紹
這是一個關於Hololive的小工具

### 名稱：Holo小工具
<div align=center>
	<img src="img/icon.png" >
</div>
<div align=center>
	<img src="img/0.png" >
</div>

### 功能：
下圖是主選單
<div align=center>
	<img src="img/1.jpg" width="300" height="480">
</div>

1. 可以以人氣成員進行查詢
2. 可以以所有成員進行查詢
3. 可以查詢實況中成員
4. 可以隨機發送Hololive的成員圖片

+ 首先按下人氣成員按鈕，會秀出10張人氣成員的圖片，按下圖片以看取成員介紹
<div align=center>
	<img src="img/2.jpg" width="300" height="480">
	<img src="img/3.jpg" width="300" height="480">
	<img src="img/4.jpg" width="300" height="480">
</div>

+ 秀完介紹後跳出再次詢問框
<div align=center>
	<img src="img/5.jpg" width="300" height="480">
</div>

+ 按下成員查詢，送出個成員基本名字訊息，輸入括號內英文名以看成員資訊
<div align=center>
	<img src="img/6.jpg" width="300" height="480">
	<img src="img/7.jpg" width="300" height="480">
	<img src="img/8.jpg" width="300" height="480">
	<img src="img/9.jpg" width="300" height="480">
</div>

+ 按下實況中，送出實況中影片訊息
<div align=center>
	<img src="img/10.jpg" width="300" height="480">
	<img src="img/11.jpg" width="300" height="480">
	<img src="img/12.jpg" width="300" height="480">
	<img src="img/13.jpg" width="300" height="480">
	<img src="img/14.jpg" width="300" height="480">
</div>

+ 按下抽卡進入抽卡模式
<div align=center>
	<img src="img/15.jpg" width="300" height="480">
	<img src="img/16.jpg" width="300" height="480">
	<img src="img/17.jpg" width="300" height="480">
	<img src="img/18.jpg" width="300" height="480">
</div>

### FSM
<div align=center>
	<img src="fsm.png">
</div>

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.

## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
