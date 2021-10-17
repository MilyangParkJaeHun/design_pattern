"""
클라이언트가 사용하는 인터페이스를 정의하는 클래스
"""
class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."

"""
클라이언트가 사용하는 인터페이스와 호환되지 않는 인터페이스를 가진 클래스
"""
class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

"""
Aapter 는 Adaptee 의 인터페이스를 composition 을 통해 Target 의 인터페이스와 호환되게 만들어준다.
"""
class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

def client_code(target: Target) -> None:
    print(target.request(), end="")

if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)