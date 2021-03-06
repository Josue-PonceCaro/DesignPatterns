class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)

        lines.append(f'{i}<{self.name}>') # OPEN

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}') # text

        for e in self.elements:
            lines.append(e.__str(indent + 1)) # NEW ELEMENT

        lines.append(f'{i}</{self.name}>') # CLOSE
        
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    # To create a fathe inside an other father
    def add_big_child(self, name):
        newElement = HtmlElement.create(name)
        self.__root.elements.append(newElement)
        return newElement
        
    def __str(self, ind):
        return self.__root.__str(ind)
    
    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)
    
# ordinary non-fluent builder
# builder = HtmlBuilder('ul')
builder = HtmlElement.create('div')
# builder = builderx.add_big_child('lu')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# # fluent builder
# builder.clear()
# builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
# print('Fluent builder:')
# print(builder)

# # if you want to build a simple HTML paragraph using a list
# hello = 'hello'
# parts = ['<p>', hello, '</p>']
# print(''.join(parts))

# # now I want an HTML list with 2 words in it
# words = ['hello', 'world']
# parts = ['<ul>']
# for w in words:
#     parts.append(f'  <li>{w}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))