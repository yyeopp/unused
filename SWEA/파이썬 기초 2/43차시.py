# members = [
#     {"name": "홍길동", "age": 20},
#     {"name": "이순신", "age": 45},
#     {"name": "강감찬", "age": 35}
# ]    # 하나의 딕셔너리에 한명의 정보, 그걸 모아서 리스트로 구성
# for member in members:
#     print(member["name"])
#     print(member["age"])

# def create(name, age):  # 정보를 입력받아 딕셔너리로 저장하는 함수
#     return {"name":name, "age":age}
# def output(person):
#     return "{0}\t{1}".format(person["name"], person["age"])
# members = [
#     create("홍길동", 20),
#     create("이순신", 45),
#     create("강감찬", 35)
# ]
# for member in members:
#     print(output(member))    # 아까랑 같은 결과물인데, 함수가 활용된



# class Person:   # 클래스 생성
#     pass   # 일단 세부사항 없으니까 pass로 넘어감
# member = Person()   # member라는 객체 생성   # Person()은 객체를 생성하기 위해 호출하는 생성자 메서드
# if isinstance(member, Person):   # 해당함수는 첫번째 인자의 '객체'가
#     print("맞습니다")       # 두번째 인자의 '클래스'의 '인스턴스'인지 검사








# class Person:   # __init__은 매직메서드로 "속성"을 설정해주는 메서드. 함수의 일종이라 생각하면 편함
#     def __init__(self, name, age):    # 첫 매개변수는 항상 self고 그 외에 name과 age 변수를 선언해준 상태
#         self.name = name        # name 속성에 name 변수를 ,age 속성에 age 변수를 선언
#         self.age = age
#         print("객체 생성")
#     def __del__(self):   # 객체 제거하는 기능
#         print("객체 제거")
# member = Person("홍길동", 20)   # member를 Person 클래스의 인스턴스로 설정하게 됨
# a= 2   #아무의미 없는 코드입니다 #member 객체 속 name 필드와 age 필드에 각각 값이 저장됨


# print(member.name)          # member는 Person이라는 class에 속하고, 이 때 name이라는 속성을 가지기 때문에 이를 프린팅하는 것.
# print(member.age)
# print(dir(member))
# class dict:
#     key = 'd'
#     key2 = 'f'
#     def get(self, key):
#         print(self.key)
# data = {1:"d", 2:"f", 3:"g"}
# print(data.get(2)
# "ffff".split().sort().   # 여기까지 자습용
# input().split()

'''
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)   # wallet에 10000을 입력
maria.pay(3000)      # 3000의 amount를 pay하는 방식. wallet이 비공개 속성이므로 클래스 안에서 선언된 메서드를 통해서만 간접적으로 통제될 수 있다.
'''



'''
class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음


james = Person()
# james.__greeting()  # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음
james.hello()         # 이렇게 하면 호출이 가능함. hello라는 공개 메서드를 Person 안에 만들면서 greeting 비공개 메서드를 호출해놨기 때문
'''

'''
class Person:
    bag = []                 # 클래스의 공통 속성으로 bag을 선언.
    def put_bag(self, stuff):      # put_bag이라는 메서드를 도입
        self.bag.append(stuff)      # bag은 list 형식에 해당하므로, .append()함수로 목록에 추가 가능
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)        # 두 결과가 동일한데, bag에다가 james가 넣든 maria가 넣든 bag이라는 속성을 두 인스턴스가 공유하기 때문
print(maria.bag)
'''

'''
class Person:
    def __init__(self):             # 이렇게 만들면 달라짐
        self.bag = []               # bag이라는 list가 Person 클래스에 입력되는 인스턴스의 속성값이 되는 것.
    def put_bag(self, stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)        # 책
print(maria.bag)        # 열쇠
'''


'''
class Calc:
    @staticmethod          # '정적메서드'를 지칭하는 데코레이터. 메서드에 추가기능을 넣을 때 사용.
    def add(a, b):          # 데코레이터를 통해 self를 매개변수로 추가하지 않아도 됨.
        print(a + b)
    @staticmethod
    def mul(a, b):
        print(a * b)
Calc.add(10, 20)  # 클래스에서 바로 메서드 호출         # 인스턴스가 따로 없어도 된다는 뜻.
Calc.mul(10, 20)  # 클래스에서 바로 메서드 호출         # 앞에서는 result = calc(); result.add(10,20) 이런 식이였음
'''

'''
class Person:
    count = 0       # 클래스 속성을 선언
    def __init__(self):
        Person.count += 1        # 인스턴스가 만들어질 때 '클래스 속성'인 count에 1을 더함
    @classmethod        # 클래스메서드를 사용하겠다는 데코레이터
    def print_count(cls):     # 첫번째 매개변수 cls가 필수임.
        print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성(아까 위에서 만든 count)에 접근
james = Person()
maria = Person()           # 인스턴스 두 개 생성.
Person.print_count()  # 2명 생성되었습니다.
'''

'''
class Person:
    def greeting(self):         # greeting 메서드를 가지는 클래스 Person
        print('안녕하세요.')
class Student(Person):          # study 메서드를 가지는 클래스 Student
    def study(self):            # Person 클래스를 상속받는다는 특징 보유
        print('공부하기')
james = Student()           # james는 Student 클래스의 인스턴스 = Person 클래스에도 해당.
james.greeting()  # 안녕하세요.: '기반 클래스' Person의 메서드 호출
james.study()  # 공부하기: '파생 클래스' Student에 추가한 study 메서드
'''
'''
class Person:
    pass
class Student(Person):
    pass
print(issubclass(Student, Person))         # issubclass(a,b)는 a가 b의 subclass인지 확인하는 함수. T/F 결과
'''