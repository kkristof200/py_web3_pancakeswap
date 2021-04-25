# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import Web3, Bep20, Wbnb
from kw3.constants import Constants

# Local
from .reserves_wbnb import ReservesWbnb

from ..core import PancakeswapLiquidityPool

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- class: PancakeswapWbnbLiquidityPool --------------------------------------------- #

class PancakeswapWbnbLiquidityPool(PancakeswapLiquidityPool):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3,
        address: str
    ):
        super().__init__(
            web3=web3,
            address=address
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Custom

    def tokenAddress(self) -> Optional[str]:
        return self.token().address

    def token(self) -> Optional[Bep20]:
        return self.quoteToken() if self._is_base_wbnb() else self.baseToken()

    def wbnbAddress(self) -> Optional[str]:
        return self.wbnb().address

    def wbnb(self) -> Optional[Wbnb]:
        return self.baseToken() if self._is_base_wbnb() else self.quoteToken()

    def priceTokenCumulativeLast(self) -> int:
        return self.quoteTokenPriceCumulativeLast() if self._is_base_wbnb() else self.baseTokenPriceCumulativeLast()

    def priceWbnbCumulativeLast(self) -> int:
        return self.baseTokenPriceCumulativeLast() if self._is_base_wbnb() else self.quoteTokenPriceCumulativeLast()

    def tokenPrice(self) -> Optional[float]:
        '''BNB for 1 Token'''
        return self.quoteTokenPrice() if self._is_base_wbnb() else self.baseTokenPrice()

    def wbnbPrice(self) -> Optional[float]:
        '''Token for 1 BNB'''
        return self.baseTokenPrice() if self._is_base_wbnb() else self.quoteTokenPrice()

    def toToken(
        self,
        wbnbAmount: int
    ) -> Optional[float]:
        '''Token for "wbnbAmount" BNB'''
        return (self.toQuoteToken if self._is_base_wbnb() else self.toBaseToken)(wbnbAmount)

    def toWbnb(
        self,
        tokenAmount: int
    ) -> Optional[float]:
        '''BNB for "tokenAmount" Token'''
        return (self.toBaseToken if self._is_base_wbnb() else self.toQuoteToken)(tokenAmount)

    def getReserves(self) -> Optional[ReservesWbnb]:
        return self._getReserves(
            ReservesWbnb,
            is_base_wbnb=self._is_base_wbnb()
        )

    def tokenHoldings(self) -> Optional[int]:
        reserves = self.getReserves()

        return reserves.reserveToken if reserves else None

    def wbnbHoldings(self) -> Optional[int]:
        reserves = self.getReserves()

        return reserves.reserveWbnb if reserves else None


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    def _is_base_wbnb(self) -> bool:
        if not hasattr(self, '__is_base_wbnb'):
            self.__is_base_wbnb = self.token0().address == Constants.WBNB.ADDRESS

        return self.__is_base_wbnb


# -------------------------------------------------------------------------------------------------------------------------------- #