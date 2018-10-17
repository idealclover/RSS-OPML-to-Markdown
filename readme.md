# RSS-OPML-to-Markdown

> 🎁 Please take my RSS list!

RSS-OPML-to-Markdown 可以将从平台导出的 OPML 文件转化为易读的 Markdown 表格的形式，便于分享与展示

目前已在 [inoreader](https://www.inoreader.com) 与 [tiny tiny RSS](https://tt-rss.org/) 上进行测试

## Demo

转换前 [OPML](/sample.xml) -> 转换后 [Markdown](/sample.md)

##How to Use

本项目基于 Python3 构建，依赖包 [listparser](https://pypi.org/project/listparser/) 与 [tabulate](https://pypi.org/project/tabulate/)

1. 下载本python包 [链接](https://github.com/idealclover/RSS-OPML-to-Markdown/archive/master.zip)
2. 下载依赖

```
pip install listparser, tabulate
```

3. 进入项目目录

```
python rss-opml-to-markdown.py {OPML文件的位置与名称} {期望输出markdown文件的位置与名称}
```

> 注：后一参数为空则输出结果到控制台

## Planned Features

- [ ] 表格源代码美化

- [ ] 更多选项支持

## Contribute

如果有任何想法或需求，可以在 [issue](https://github.com/idealclover/RSS-OPML-to-Markdown/issues) 中告诉我们，同时欢迎各种 pull requests

## Open-source Licenses

This project is under MIT license, feel free to use it under the license.