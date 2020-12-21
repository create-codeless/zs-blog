/*
* author: jeeyshe@gmail.com
* date: 2019-04-09 00:34
* description: 埋藏在控制台的彩蛋
* */

/*控制台彩蛋*/
var str = [
    "%c路漫漫其修远兮；",
    "%c吾将上下而求索",
    "%c欢迎关注本站，可以联系QQ:919841483",
];

var site_name = [
    "%c                               _       _ _                  _                            ",
    "%c                              | |     (_|_)                (_)                           ",
    "%c __      ____      ____      _| |_   _ _ _  __ _ _ __ __  ___ _ __    ___ ___  _ __ ___  ",
    "%c \\ \\ /\\ / /\\ \\ /\\ / /\\ \\ /\\ / / | | | | | |/ _` | \'_ \\\\ \\/ / | \'_ \\  / __/ _ \\| \'_ ` _ \\ ",
    "%c  \\ V  V /  \\ V  V /  \\ V  V /| | |_| | | | (_| | | | |>  <| | | | || (_| (_) | | | | | |",
    "%c   \\_/\\_/    \\_/\\_/    \\_/\\_(_)_|\\__,_| |_|\\__,_|_| |_/_/\\_\\_|_| |_(_)___\\___/|_| |_| |_|",
    "%c                                     _/ |                                                ",
    "%c                                    |__/                                                 "
];

//重复n个字符
function repeat(str, n) {
    return new Array(n + 1).join(str);
}

//任意页面加载动画//加载层-风格2
layer.load(1);
//页面加载完后关闭加载动画
setTimeout(function () {
    layer.closeAll('loading');
}, 1000);

function doing() {
    layer.msg('<h1>功能暂未开放</h1>请留意微信公众号，功能开放后会第一时间通知呦', {
        time: 3000, //3s后自动关闭
    });
}

$(document).ready(function () {
    console.clear();
    console.log("%c《青春》---lanyu", "color: yellow;");
    for (var index = 0; index < str.length; index++) {
        console.log('\r\n');
        console.log(str[index], "color: green;");
    }
    console.log('\r\n');
    console.log("%c2020-11-11 05:20 http://www.ccmsy.com", "color: red;");

    // for (i = 0; i < site_name.length; i++) {
    //    console.log(site_name[i], "color: blue;");
    //}
    console.log("%c~既然都发现这个彩蛋了，收藏一下本站呗^o^", "color: red;");

});

