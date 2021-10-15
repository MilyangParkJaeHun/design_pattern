from abc import ABC, abstractmethod
from typing import List

"""
Strategy 의 인터페이스를 규정하는 Abstract 클래스
"""
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

"""
실제 전략이 구현되는 Concrete 클래스
"""
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

"""
Client 가 사용할 인터페이스 정의
"""
class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    """
    런타임에서도 전략을 수정할 수 있게 하기 위한 setter 함수
    """
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    """
    Context 는 다양한 버전의 알고리즘을 소유하기 보단,
    Strategy 객체에게 작업을 위임한다.
    """
    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()