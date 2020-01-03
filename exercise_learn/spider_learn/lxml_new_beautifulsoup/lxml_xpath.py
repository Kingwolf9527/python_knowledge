# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 11:55

from lxml import html

test = '''
<!DOCTYPE html>

<html lang="zh-cmn-Hans">

    <head>

        <meta charset="utf-8" />

        <title>网易免费邮箱 - 中国第一大电子邮件服务商</title>

        <meta name="description" content="网易免费邮箱--中国第一大电子邮件服务商，提供以@163.com、@126.com和@yeah.net为后缀的免费邮箱。16年邮箱运营经验，系统快速稳定，垃圾邮件拦截率超过98%，邮箱容量自动翻倍，支持高达2G超大附件，提供免费网盘及手机邮箱服务。">

        <meta name="keywords" content="邮件，邮箱，电子邮件，电子邮箱，网易邮箱，163邮箱，126邮箱，yeah邮箱，免费邮箱，mail，email，网盘">

        <link rel="dns-prefetch" href="//mimg.127.net" />

        <link rel="dns-prefetch" href="//mail.163.com"/>

        <link rel="dns-prefetch" href="//mail.126.com"/>

        <link rel="dns-prefetch" href="//mail.yeah.net" />

        <link rel="shortcut icon" href="//email.163.com/favicon.ico" />

        <script>var aTag = ["aside","figcaption","figure","footer","header","hgroup","nav","section"],i = 0;for(i in aTag){document.createElement(aTag[i]);}</script>

    <link href="//mimg.127.net/act/2017/171019-email-index/pc/css/style.0dc308e9.css" rel="stylesheet"></head>

    <body>

<script>

// polyfill

(function(){if(!Object.defineProperty||!(function(){try{Object.defineProperty({},"x",{});return true}catch(b){return false}}())){var a=Object.defineProperty;Object.defineProperty=function(d,f,c){if(a){try{return a(d,f,c)}catch(b){}}if(d!==Object(d)){throw TypeError("Object.defineProperty called on non-object")}if(Object.prototype.__defineGetter__&&("get" in c)){Object.prototype.__defineGetter__.call(d,f,c.get)}if(Object.prototype.__defineSetter__&&("set" in c)){Object.prototype.__defineSetter__.call(d,f,c.set)}if("value" in c){d[f]=c.value}return d}}}());if(!Array.indexOf){Array.prototype.indexOf=function(b){for(var a=0;a<this.length;a++){if(this[a]==b){return a}}return -1}}if(!Object.keys){Object.keys=(function(){var c=Object.prototype.hasOwnProperty,d=!({toString:null}).propertyIsEnumerable("toString"),b=["toString","toLocaleString","valueOf","hasOwnProperty","isPrototypeOf","propertyIsEnumerable","constructor"],a=b.length;return function(g){if(typeof g!=="object"&&typeof g!=="function"||g===null){throw new TypeError("Object.keys called on non-object")}var e=[];for(var h in g){if(c.call(g,h)){e.push(h)}}if(d){for(var f=0;f<a;f++){if(c.call(g,b[f])){e.push(b[f])}}}return e}})()}if(!Array.prototype.forEach){Array.prototype.forEach=function(b){var a=this.length;if(typeof b!="function"){throw new TypeError()}var d=arguments[1];for(var c=0;c<a;c++){if(c in this){b.call(d,this[c],c,this)}}}}if(!Array.prototype.filter){Array.prototype.filter=function(c){if(this===void 0||this===null){throw new TypeError()}var f=Object(this);var a=f.length>>>0;if(typeof c!=="function"){throw new TypeError()}var e=[];var b=arguments.length>=2?arguments[1]:void 0;for(var d=0;d<a;d++){if(d in f){var g=f[d];if(c.call(b,g,d,f)){e.push(g)}}}return e}};

</script>

<script type="text/javascript" src="https://ursdoccdn.nosdn.127.net/webzj_cdn101/message_170510.js"></script>

<script type="text/javascript" src="//mimg.127.net/act/2017/171019-email-index/vendor/ads.v2.js"></script>

<!--[if lte IE 7]>

    <div class="overlay"></div>

    <div class="overlay-tips">

        <p>您的浏览器版本过旧无法正常登录邮箱，<br />建议您使用版本更高的IE浏览器或其他浏览器登录。<br /><a href="https://www.microsoft.com/zh-cn/download/internet-explorer.aspx" target="_blank">Internet Explorer 下载</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.google.cn/chrome/browser/desktop/index.html" target="_blank">chrome</a></p>

    </div>

<![endif]-->

    <header class="header">

        <div class="inner">

            <h1>

                <a href="http://www.163.com/" target="_blank">

                    <img src="//mimg.127.net/index/email/img/2012/ntes_logo.png" alt="网易NetEase" width="87" height="27" />

                </a>

            </h1>

            <p class="ext">

                <a class="link" href="http://vipmail.163.com/?from=email" title="收费邮" target="_blank">收费邮</a>

                <a class="link" href="http://qiye.163.com/login/" title="企业邮箱" target="_blank">企业邮箱</a>

                <a class="link" href="http://hw.mail.163.com/" title="国外用户登录" target="_blank">国外用户登录</a>

                <a class="link" href="http://18.mail.163.com/login.do?from=mail" target="_blank" style="position:relative;">学生用户登录

                    <b class="ico ico-new" style="position:absolute;top:-11px;right:2px;"></b>

                </a>

                <a class="link" href="http://mail.163.com/client/dl.html?from=mail13" target="_blank">手机客户端</a>

                <a class="link" href="http://help.mail.163.com" title="" target="_blank">帮助</a>

                <a target="_blank" href="http://help.mail.163.com/newfeedback.do?m=add">登录反馈</a>

        </div>

    </header>





    <section class="main" id="main">

        <h2 class="h2" title="中国第一大电子邮件服务商">中国第一大电子邮件服务商</h2>

        <b class="ico-arr"></b>

        <ul class="nav" id="nav">

            <li class="item item-163" data-target="163">

                <b class="logo logo-163" title="网易163免费邮"></b>

            </li>

            <li class="item item-126" data-target="126">

                <b class="logo logo-126" title="网易126免费邮"></b>

            </li>

            <li class="item item-yeah" data-target="yeah">

                <b class="logo logo-yeah" title="网易yeah免费邮"></b>

            </li>

            <li class="item item-mobile" data-target="mobile">

                <b class="logo logo-mobile" title="网易手机号码邮箱"></b>

            </li>

        </ul>

        <div class="panel" id="panel">





            <div class="extra fn-txtc">

                <div class="free">

                    <label class="ssl" for="sslAble"><input id="sslAble" type="checkbox" />SSL安全登录</label>



                    邮箱版本：

                    <a href="javascript:void(0)" class="fn-selC" id="styleSelect">

                        <span id="styleCurrect">默认版本</span>

                        <b class="ico arr fn-arrC"></b>

                    </a>

                    <div class="styleMenu fn-txtOption" id="styleOptions" style="display:none"></div>

                </div>

                <div class="mobile">

                    还没有网易手机号码邮箱？ 

                    <a class="fn-extLinkC" href="http://reg.email.163.com/unireg/call.do?cmd=register.entrance&amp;flow=mobile&amp;from=email_mobile" target="_blank" tabindex="9">免费激活</a>

                </div>

            </div>

            <div class="ads" id="ads"></div>

            <div class="errTips" id="errTips" style="display:none"></div>

        </div>

    </section>





    <footer class="footer">

        <!-- 推广 -->

        <div class="expansion">

            <ul class="extText" id="extText"></ul>

        </div>

        <!-- 关于 -->

        <div class="copyright">

            <a href="http://www.163.com/" target="_blank">网易首页</a>

            <a href="http://mail.163.com/html/mail_intro" target="_blank">关于网易免费邮</a>

            <a href="https://3c.163.com/?from=pdengluyetoutu1" target="_blank">网易智造</a>

            <a href="http://qian.163.com" target="_blank">网易•有钱</a>

            <a href="http://you.163.com/" target="_blank">网易严选</a>

            <a href="http://pin.mail.163.com?utm_source=maillogin&utm_medium=email" target="_blank">网易一起拼</a>

            <a href="http://corp.163.com/gb/legal/legal.html" target="_blank">隐私政策</a>

            <span class="sptln">|</span>网易公司版权所有 &copy; 1997-

            <script type="text/javascript" src="//mimg.127.net/copyright/year.js"></script>

            <span>

                （数据来源：艾媒邮箱报告）

            </span>

        </div>



    </footer>



    <form id="login" name="login" method="post" style=" width: 0; height: 0;"></form>    

    <iframe class="httploginframe" src="about:blank" id="frameforlogin" name="frameforlogin" style="display:none;overflow:hidden;border:0">登录iframe</iframe>

    

    	

    <script type="text/javascript" src="//mimg.127.net/act/2017/171019-email-index/pc/js/index.3f2a6efb.js"></script></body>

</html>
'''

def parse_text():

    #得到的是一个element对象,具体的用法是这个：html.etree.HTML()
    htmlElement = html.etree.HTML(test)
    print(type(htmlElement))
    #结果是：<class 'lxml.etree._Element'>

    #element对象的数据类型为bytes类型，要转为Unicode的字符串
    str_html = html.etree.tostring(htmlElement,encoding='utf-8').decode('utf-8')

    print(str_html)

def parse_file():

    # #读取文件，得到的也是一个element对象,具体的用法是这个：html.etree.parse()，去解析文件，但是这样会存在的问题的，因为它默认的解析器是xml的，但是我们解析的是HTML，但是HTML不一定规范，这样就会出现问题
    # html_elemnet = html.etree.parse('mail.html')
    # # element对象的数据类型为bytes类型，要转为Unicode的字符串
    # str_html = html.etree.tostring(html_elemnet, encoding='utf-8').decode('utf-8')
    # print(str_html)
    # #容易产生这样的报错：lxml.etree.XMLSyntaxError: Opening and ending tag mismatch

    #因此需要调用HTML的解析器，而不是xml的解释器，这样再读取文件，才能给确保不会出现标签规范的问题
    parser = html.etree.HTMLParser(encoding='utf-8')
    html_elemnet = html.etree.parse('mail.html',parser=parser)
    # element对象的数据类型为bytes类型，要转为Unicode的字符串
    str_html = html.etree.tostring(html_elemnet, encoding='utf-8').decode('utf-8')
    print(str_html)

if __name__ == '__main__':

    parse_file()