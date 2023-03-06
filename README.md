# markdown_sub_sup

Extends the [Python Markdown](https://python-markdown.github.io/).
Adds the possibility to use `^something^` to create `<sup>something</sup>` or `~something~` to create `<sub>something</sub>`

Install through pip:

```bash
pip install markdown_sub_sup
```

To enable the markdown_sub_sup package and use it in your markdown generation just add it like so:

```python
import markdown

result = markdown.markdown(textToRender, extensions=["markdown_sub_sup",])
```
