from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor

SUP_RE = r"(\^)([\S]+?)(\^)"
SUB_RE = r"(\~)([\S]+?)(\~)"

class MarkdownSubSup(Extension):
    def extendMarkdown(self, md):
        del_proc = SimpleTagInlineProcessor(SUB_RE, 'sub')
        md.inlinePatterns.register(del_proc, 'sub', 65)
        del_proc = SimpleTagInlineProcessor(SUP_RE, 'sup')
        md.inlinePatterns.register(del_proc, 'sup', 65)


def makeExtension(**kwargs):
    return MarkdownSubSup(**kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md')
