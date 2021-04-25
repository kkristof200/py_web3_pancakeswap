# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from jsoncodable import JSONCodable

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: Reserves ------------------------------------------------------- #

class Reserves(JSONCodable):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        reserve0: int,
        reserve1: int,
        blockTimestampLast: int
    ):
        self.reserve0 = reserve0
        self.reserve1 = reserve1
        self.blockTimestampLast = blockTimestampLast


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def token0_token1_rate(self) -> float:
        return self.reserve0 / self.reserve1

    @property
    def token1_token0_rate(self) -> float:
        return self.reserve1 / self.reserve0


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def token0Price(
        self,
        token_0_decimals: int,
        token_1_decimals: int
    ) -> float:
        return self.token1_token0_rate * pow(10, token_0_decimals - token_1_decimals)

    def token1Price(
        self,
        token_0_decimals: int,
        token_1_decimals: int
    ) -> float:
        return self.token0_token1_rate * pow(10, token_1_decimals - token_0_decimals)


# -------------------------------------------------------------------------------------------------------------------------------- #