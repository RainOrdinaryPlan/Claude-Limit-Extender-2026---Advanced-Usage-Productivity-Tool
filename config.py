from dataclasses import dataclass


@dataclass
class Config:
    auvybv: int = 531
    ynsjqwd: int = 915
    rhhtjoi: int = 151
    aqdawg: int = 124

    def total(self):
        return self.auvybv + self.ynsjqwd + self.rhhtjoi + self.aqdawg


if __name__ == "__main__":
    x = Config()
    print(x.total())
