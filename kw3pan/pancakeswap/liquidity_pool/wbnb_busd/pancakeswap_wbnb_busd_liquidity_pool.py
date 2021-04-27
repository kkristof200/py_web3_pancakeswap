# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import Web3, Busd, Wbnb

# Local
from .reserves_wbnb_busd import ReservesWbnbBusd

from ..core.pancakeswap_liquidity_pool import PancakeswapLiquidityPool

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------- class: PancakeswapWbnbBusdLiquidityPool ------------------------------------------- #

class PancakeswapWbnbBusdLiquidityPool(PancakeswapLiquidityPool):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address=Constants.ADDRESS_LIQUIDITY_POOL_WBNB_BUSD
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Custom

    def wbnbAddress(self) -> Optional[str]:
        return self.token0Address()

    def busdAddress(self) -> Optional[str]:
        return self.token1Address()

    def wbnb(self) -> Optional[Wbnb]:
        return self.token0()

    def busd(self) -> Optional[Busd]:
        return self.token1()

    def getReserves(self) -> Optional[ReservesWbnbBusd]:
        return self._getReserves(ReservesWbnbBusd)

    def priceWbnbCumulativeLast(self) -> int:
        return self.price0CumulativeLast()

    def priceBusdCumulativeLast(self) -> int:
        return self.price1CumulativeLast()

    def wbnbPrice(self) -> Optional[float]:
        '''BUSD for 1 BNB'''
        return self.token0Price()

    def busdPrice(self) -> Optional[float]:
        '''BNB for 1 BUSD'''
        return self.token1Price()

    def toWbnb(
        self,
        busdAmount: int
    ) -> Optional[float]:
        '''BNB for "busdAmount" Busd'''
        return self.toToken0(busdAmount)

    def toBusd(
        self,
        wbnbAmount: int
    ) -> Optional[float]:
        '''Busd for "wbnbAmount" BNB'''
        return self.toToken1(wbnbAmount)


# -------------------------------------------------------------------------------------------------------------------------------- #