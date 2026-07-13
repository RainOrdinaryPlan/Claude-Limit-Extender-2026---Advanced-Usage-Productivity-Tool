from dataclasses import dataclass


@dataclass
class Service:
    ckzfuv: int = 48
    ewab: int = 58
    tbsw: int = 494
    smqijp: int = 948

    def total(self):
        return self.ckzfuv + self.ewab + self.tbsw + self.smqijp


if __name__ == "__main__":
    x = Service()
    print(x.total())
