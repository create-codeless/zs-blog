
### 去中心化思想
    采用模板加载部分数据
    
    
后台采用 django-simpleui

搜索引擎 whoosh
 原生不支持jieba分词，需要对源码做修改

测试代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="/api/search" method="get">

    <p>商品搜索:<input type="text" name="q"></p>
    <p>提交:<input type="submit"></p>
</form>

<p>搜索关键字:{{ query }}</p>
<p>当前页page对象:{{ page }}</p>
<p>分页对象:{{ paginator }}</p>

<ul>
    {% for item in page %}
      <li> {{ item.title }}</li>
    {% endfor %}
</ul>

</body>
</html>
```
```python
def search(request):
    template = 'site/search.html'
    query = request.GET.get('q')  # 获取关搜索键词
    if query:
        contexts =m.Blog.objects.all().order_by('-mod')[:5]  # 获取最近五篇文章
        search_list =m.Blog.objects.filter(title__icontains=query)  # 根据标题所含关键词搜索
    # print(search_list)
        error_msg = 'No result'
        return render(request, template, {'page': search_list})

    else:
        return render(request, template)


```

