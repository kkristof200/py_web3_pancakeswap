# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from kw3.constants import Constants

# Local
from ..core import Reserves

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: ReservesBusd ----------------------------------------------------- #

class ReservesBusd(Reserves):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        reserve0: int,
        reserve1: int,
        blockTimestampLast: int,
        is_base_busd: bool
    ):
        super().__init__(
            reserve0=reserve0,
            reserve1=reserve1,
            blockTimestampLast=blockTimestampLast
        )

        self.__is_base_busd = is_base_busd


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def reserveToken(self) -> int:
        return self.reserve1 if self.__is_base_busd else self.reserve0

    @property
    def reserveBusd(self) -> int:
        return self.reserve0 if self.__is_base_busd else self.reserve1

    @property
    def token_busd_rate(self) -> float:
        return self.token1_token0_rate if self.__is_base_busd else self.token0_token1_rate

    @property
    def busd_token_rate(self) -> float:
        return self.token0_token1_rate if self.__is_base_busd else self.token1_token0_rate


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def tokenPrice(
        self,
        token_decimals: int
    ) -> float:
        '''BNB for 1 Token'''
        token_0_decimals, token_1_decimals = (Constants.BUSD.DECIMALS, token_decimals) if self.__is_base_busd else (token_decimals, Constants.BUSD.DECIMALS)

        return (self.token1Price if self.__is_base_busd else self.token0Price)(
            token_0_decimals=token_0_decimals,
            token_1_decimals=token_1_decimals
        )

    def busdPrice(
        self,
        token_decimals: int
    ) -> float:
        '''Token for 1 BNB'''
        token_0_decimals, token_1_decimals = (token_decimals, Constants.BUSD.DECIMALS) if self.__is_base_busd else (Constants.BUSD.DECIMALS, token_decimals)

        return (self.token0Price if self.__is_base_busd else self.token1Price)(
            token_0_decimals=token_0_decimals,
            token_1_decimals=token_1_decimals
        )


# -------------------------------------------------------------------------------------------------------------------------------- #