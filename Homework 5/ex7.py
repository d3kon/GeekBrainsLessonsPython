# -- coding: cp1251 --

# �������� ���������, ������������ ��� �����������, ��� ��� ���������
# ����������� ����� ����������� ���������: 1+2+...+n = n(n+1)/2,
# ��� n - ����� ����������� �����.
# ������:
# ��� n = 5
# 1+2+3+4+5 = 5(5+1)/2
# ����� �������� ����������� �-��� ������ ��� ����� ����� ���������!
# ��������� ����� ������� � ������ ������.
# ������ ����� ��������� � ����������� �-��� ���� �� ������!
# ������ ����� ��������. � ������� ������ ��������� �����.


class Rec():

    @classmethod
    def rec(cls, num, result):
        if num == 0:
            return result
        else:
            return cls.rec(num - 1, result + num)


if __name__ == '__main__':
    print(Rec.rec(5, 0))