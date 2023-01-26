# メモ書き

## 統計

- 栗原の入門統計学から作った統計ノートで作った
- 今後は東京大学出版会　統計学入門 からピックアップして作っていくか？その方が詳しいので。

## docsフォルダにRenderしたいとき

_quarto.yamlに下記の通り設定する

[Render to docs](https://quarto.org/docs/publishing/github-pages.html#render-to-docs)

## Combining R and Python with {reticulate} and Quarto

https://www.r-bloggers.com/2023/01/combining-r-and-python-with-reticulate-and-quarto/

## A Quarto tip a day

投稿の仕方の参考になりそう。

https://mine-cetinkaya-rundel.github.io/quarto-tip-a-day/

## How to write mathematics

[Markdownに数式を挿入する方法](https://b1san-blog.com/post/vscode/vscode-md-math/)

[LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

## htmlとmarkdownの両方に出力する方法

```
library(rmarkdown)
rmarkdown::render("statistics_01.Rmd",output_format = "html_document")
rmarkdown::render("statistics_01.Rmd",output_format = "md_document")
```
