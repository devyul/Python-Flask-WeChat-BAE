# coding=utf-8
from flask import Flask, g, request

app = Flask(__name__)
app.debug = True  #debug 模式


from wechat_sdk import WechatConf
conf = WechatConf(
    token='yultoken',
    appid='wxbe7dffcbb8fb9416',
    appsecret='da9312248f4878506141be5e6a7ecd97',
    encrypt_mode='compatible',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    # encoding_aes_key='your_encoding_aes_key'  # 如果传入此值则必须保证同时传入 token, appid
)

from wechat_sdk import WechatBasic
wechat = WechatBasic(conf=conf)


@app.route('/')
def hello():
    return "Hello, world! -Python Flask\n "

#JSON test
@app.route('/getBannerList')
def json_test():
    return "{\"isSuccess\":true,\"errorMsg\":\"\",\"timeStamp\":\"001463035302000\",\"nonce\":\"BWDBMCDQMV\",\"sign\":\"8EC6B53199DC93E75B119CF1A48F31B3496CA306\",\"data\":{\"msg\":\"\",\"inkey\":[{\"newsId\":1,\"bTitle\":\"安全生产培训须知1\",\"newsImgUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\",\"newsUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\"},{\"newsId\":1,\"bTitle\":\"消防知识你要明白\",\"newsImgUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\",\"newsUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\"},{\"newsId\":1,\"bTitle\":\"安3333知1\",\"newsImgUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\",\"newsUrl\":\"http://img02.hc360.com/it/201601/201601111652346312.jpg\"}]}}"

#微信token验证
@app.route('/wx')
def hello_ping():

    if wechat.check_signature(request.args.get('signature'), request.args.get('timestamp'),request.args.get('nonce') ):
        # print request.args.get('signature')
        return request.args.get('echostr')
        print "success"
    else:

        return "Wrong\n"


#------如果是本地环境
# if __name__ == '__main__':
# ##app.run()

# -------如果是BAE环境
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)