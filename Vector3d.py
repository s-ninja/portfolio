class Vector1d:
    def __init__(self, x):
        self.x = x

    def __sub__(self, other: 'Vector1d') -> 'Vector1d':
        if not isinstance(other, Vector1d):
            raise TypeError('Не поддерживается')
        return Vector1d(self.x - other.x)

    def __add__(self, other: 'Vector1d') -> 'Vector1d':
        if not isinstance(other, Vector1d):
            raise TypeError('Не поддерживается')
        return Vector1d(self.x + other.x)

    def __mul__(self, other: (int, float)) -> 'Vector1d':
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector1d(self.x * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector1d(self.x / other)

    def __str__(self):
        return f'Координата {self.x=}\n'


class Vector2d(Vector1d):
    def __init__(self, x, y):
        super().__init__(x=x)
        self.y = y

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        if not isinstance(other, Vector2d):
            raise TypeError('Не поддерживается')
        return Vector2d(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        if not isinstance(other, Vector2d):
            raise TypeError('Не поддерживается')
        return Vector2d(self.x + other.x, self.y + other.y)

    def __mul__(self, other: (int, float)) -> 'Vector2d':
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector2d(self.x * other, self.y * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector2d(self.x / other, self.y / other)

    def __str__(self):
        return f'{super().__str__()}Координата {self.y=}\n'


class Vector3d(Vector2d):
    def __init__(self, x, y, z):
        super(Vector3d, self).__init__(x=x, y=y)
        self.z = z

    def __sub__(self, other: 'Vector3d') -> 'Vector3d':
        if not isinstance(other, Vector3d):
            raise TypeError('Не поддерживается')
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: 'Vector3d') -> 'Vector3d':
        if not isinstance(other, Vector3d):
            raise TypeError('Не поддерживается')
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other: (int, float)) -> 'Vector3d':
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector3d(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Не поддерживается')
        return Vector3d(self.x / other, self.y / other, self.z / other)

    def __str__(self):
        return f'{super().__str__()}Координата {self.z=}'


a = Vector3d(6, 6, 6)
b = Vector3d(10, 10, 10)
c = Vector3d(84, 84, 84)
res = a - b
print(res)
