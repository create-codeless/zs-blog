$(function () {
  // 新闻列表功能
  let $newsLi = $(".menu .sub li");
  let iPage = 1;  //默认第1页
  let iTotalPage = 1; //默认总页数为1
  let bIsLoadData = true;   // 是否正在向后台加载数据
   let sCurrentTagId = 0; //默认分类标签为0

  // 加载新闻列表信息
  fn_load_content();

    $newsLi.click(function () {
    // 获取绑定在当前选中分类上的data-id属性值
    let sClickTagId = $(this).children('a').attr('data-id');
        console.log(window.location.href)
        console.log(window.location.host) // http:// + window.location.host + '/'
     if(window.location.href !=  'http://' + window.location.host + '/'){
          window.location.href = 'http://' + window.location.host + '/'
     }

        let titles = $(this).children('a').text();
        console.log(titles);
         $(".banbox").remove();  // 删除标签
         $(".headline").remove();  // 删除标签
         $(".zhuanti").remove();  // 删除标签
         $(".ad").css('display','none');  // 删除标签
         $(".news-list").html("");
         let data = `
          <div class="whitebg lanmu"><img src="https://tbweb.iimzt.com/thumbs/2019/03/178121_200.jpg" alt="图片丢失">
        <h1>${titles}</h1>
        <p>公开公正内容分享平台.如果本站有侵犯您的权益;请联系我.</p>
    </div>
         `
        $('.lanmu').remove();
         $('.lbox').prepend(data);

    if (sClickTagId !== sCurrentTagId) {
            sCurrentTagId = sClickTagId;  // 记录当前分类id
            // 重置分页参数
            iPage = 1;
            iTotalPage = 1;
            fn_load_content()
        }
  });


  //页面滚动加载相关
  $(window).scroll(function () {
    // 浏览器窗口高度
    let showHeight = $(window).height();

    // 整个网页的高度
    let pageHeight = $(document).height();

    // 页面可以滚动的距离
    let canScrollHeight = pageHeight - showHeight;

    // 页面滚动了多少,这个是随着页面滚动实时变化的
    let nowScroll = $(document).scrollTop();

    if ((canScrollHeight - nowScroll) < 100) {
      // 判断页数，去更新新闻数据
      if (!bIsLoadData) {
        bIsLoadData = true;
        // 如果当前页数据如果小于总页数，那么才去加载数据
        if (iPage < iTotalPage) {
          iPage += 1;
          $(".btn-more").remove();  // 删除标签
          // 去加载数据
          fn_load_content()
        } else {
          alert('已全部加载，没有更多内容！');
          $(".btn-more").remove();  // 删除标签
          $(".news-list").append($('<a href="javascript:void(0);" class="btn-more">已全部加载，没有更多内容！</a>'))

        }
      }
    }
  });

  // 定义向后端获取新闻列表数据的请求
  function fn_load_content() {
    // 创建请求参数
    let sDataParams = {
        "tag_id": sCurrentTagId,
      "page": iPage
    };

    // 创建ajax请求
    $.ajax({
      // 请求地址
      url: "/api/",  // url尾部需要添加/
      // 请求方式
      type: "GET",
      data: sDataParams,
      // 响应数据的格式（后端返回给前端的格式）
      dataType: "json",
    })

      .done(function (res) {
        if (res['status'] === 0) {
          iTotalPage = res.data.total_pages;  // 后端传过来的总页数
          // if (iPage === 1) {
          //   $(".news-list").html("")
          // }
        // // 需要修改 href  接收后台传来的id号 响应详情页  /news/${one_news.id}/
          res.data.news.forEach(function (one_news) {
               let content = `
          <li>
          <h3 class="blogtitle"><a href="/api/${one_news.id}/" target="_blank">${one_news.title}</a></h3>
          <span class="blogpic imgscale"><i><a href="/">原创模板</a></i><a href="/api/${one_news.id}/" title=""><img src="${one_news.cover}" alt=""></a></span>
          <p class="blogtext">${one_news.digest}</p>
          <p class="bloginfo"><i class="avatar"><img src="images/avatar.jpg"></i><span>${one_news.author.username}</span><span>${one_news.mod}</span><span>【<a href="/">原创模板</a>】</span></p>
          <a href="/api/${one_news.id}/" class="viewmore">阅读更多</a> 
          </li>
        `;

            $(".news-list").append(content)
          });

          $(".news-list").append($('<a href="javascript:void(0);" class="btn-more">滚动加载更多</a>'));
          // 数据加载完毕，设置正在加载数据的变量为false，表示当前没有在加载数据
          bIsLoadData = false;

        } else {
          // 登录失败，打印错误信息
          console.log('服务器错误')
        }
      })
      .fail(function () {
        console.log('服务器超时，请重试！');
      });
  }




});