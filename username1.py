class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            print(len(name))
            raise ValueError(f'{name}は文字数のルール違反です')

        self.name = name

    def screen_name(self):
        return self.name.upper()

hibiki = UserName(name='hibiki')

# print(hibiki)
# print(type(hibiki))
print(hibiki.name)

print(hibiki.screen_name())

# UserNameクラスのインスタンス化
# sho = UserName(name = 'sho')
# print(sho.name)
